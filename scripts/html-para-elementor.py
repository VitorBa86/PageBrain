#!/usr/bin/env python3
"""
html-para-elementor.py
Converte uma página HTML (escrita seguindo regras-html-convertivel.md) em JSON do Elementor
(formato de exportação v0.4, containers flexbox), no padrão das páginas da casa.

Como funciona
  1. Abre o HTML no Chrome headless (Playwright) em 1440px e em 390px.
  2. Percorre o DOM e lê os ESTILOS COMPUTADOS de cada elemento (não importa onde o CSS está).
  3. Mapeia: <section> e blocos com filhos -> container; h1..h6 -> heading; p -> text-editor;
     a.btn/button -> button; img -> image; ul/ol -> icon-list; details -> toggle; iframe -> video/google_maps;
     [data-el="html"], svg soltos, canvas, form e o que não tiver equivalente -> widget html.
  4. Diferenças entre desktop e mobile viram configurações *_mobile (fonte do mobile em vw, como a casa usa).
  5. Classes CSS e id viram css_classes (container) ou _css_classes (widget) e _element_id (mantém scroll-bottom etc.).
  6. O <style> da página vai para page_settings.custom_css e os <script> viram um widget html no fim.

Uso
  python3 html-para-elementor.py pagina.html saida.json [--titulo "Nome"] [--clipboard] [--sem-css] [--chrome CAMINHO]

  --clipboard  gera o formato "colar de outro site" ({"type":"elementor","elements":[...]}).
  --sem-css    não copia o <style> da página para page_settings.custom_css.

Dependências
  pip install playwright   (e um Chrome instalado; por padrão usa o Google Chrome do macOS)

Limitações principais: ver ../mapa-html-para-elementor.md (seção "Limitações do conversor").
"""
import sys, json, re, random, pathlib, argparse, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _navegador import chrome  # noqa: E402

ap = argparse.ArgumentParser()
ap.add_argument('entrada'); ap.add_argument('saida')
ap.add_argument('--titulo', default=None)
ap.add_argument('--clipboard', action='store_true')
ap.add_argument('--sem-css', action='store_true')
ap.add_argument('--chrome', default=None, help='caminho do Chrome (padrão: acha sozinho, ver _navegador.py)')
ap.add_argument('--offline', action='store_true', help='bloqueia requisições externas ao renderizar')
args = ap.parse_args()

# ---------------------------------------------------------------- coleta (JS no navegador)
COLLECT = r"""
() => {
  document.querySelectorAll('body *').forEach((e, i) => e.setAttribute('data-h2e', i + 1));
  const SKIP = new Set(['SCRIPT','STYLE','NOSCRIPT','TEMPLATE','LINK','META','BR']);
  const vis = el => { const s = getComputedStyle(el); const r = el.getBoundingClientRect(); return s.display !== 'none' && s.visibility !== 'hidden' && (r.width > 0 || r.height > 0); };
  const pick = (s, keys) => { const o = {}; for (const k of keys) o[k] = s.getPropertyValue(k); return o; };
  const CK = ['display','flex-direction','flex-wrap','justify-content','align-items','gap','row-gap','column-gap','padding-top','padding-right','padding-bottom','padding-left',
    'margin-top','margin-right','margin-bottom','margin-left','background-color','background-image','background-size','background-position','background-repeat',
    'border-top-width','border-top-style','border-top-color','border-top-left-radius','border-top-right-radius','border-bottom-right-radius','border-bottom-left-radius',
    'box-shadow','min-height','max-width','width','height','position','text-align','overflow','opacity'];
  const TK = ['font-family','font-size','font-weight','line-height','letter-spacing','text-transform','font-style','color','text-align','text-decoration-line'];
  function walk(el, depth) {
    if (SKIP.has(el.tagName)) return null;
    if (!vis(el)) return null;
    const n = +el.getAttribute('data-h2e');
    const s = getComputedStyle(el); const r = el.getBoundingClientRect();
    const kids = [];
    for (const c of el.children) { const k = walk(c, depth + 1); if (k) kids.push(k); }
    let directText = 0; for (const t of el.childNodes) if (t.nodeType === 3 && t.textContent.trim()) directText += t.textContent.trim().length;
    return { id: n, tag: el.tagName.toLowerCase(), cls: el.getAttribute('class') || '', elid: el.id || '', attrs: Object.fromEntries([...el.attributes].map(a => [a.name, a.value])),
      w: Math.round(r.width), h: Math.round(r.height), parentW: el.parentElement ? Math.round(el.parentElement.getBoundingClientRect().width) : 0,
      box: pick(s, CK), typo: pick(s, TK), directText, html: el.innerHTML.replace(/ data-h2e="\d+"/g, ''), outer: el.outerHTML.length < 200000 ? el.outerHTML.replace(/ data-h2e="\d+"/g, '') : '', text: (el.innerText || '').trim(),
      src: el.currentSrc || el.getAttribute('src') || '', kids };
  }
  const body = document.body;
  const roots = []; for (const c of body.children) { const k = walk(c, 0); if (k) roots.push(k); }
  const styles = [...document.querySelectorAll('style')].map(s => s.textContent).join('\n');
  const scripts = [...document.querySelectorAll('body script')].map(s => s.outerHTML).join('\n');
  const links = [...document.querySelectorAll('link[rel="stylesheet"]')].map(l => l.href);
  return { roots, styles, scripts, links, title: document.title, vw: window.innerWidth };
}
"""
MOBILE = r"""
() => { const out = {}; const TK=['font-size','line-height','letter-spacing','padding-top','padding-right','padding-bottom','padding-left','flex-direction','gap','text-align','display','min-height','width','margin-top','margin-bottom'];
  document.querySelectorAll('[data-h2e]').forEach(el => { const s = getComputedStyle(el); const o = {}; for (const k of TK) o[k] = s.getPropertyValue(k); o['_hidden'] = (s.display === 'none'); out[el.getAttribute('data-h2e')] = o; }); return out; }
"""

from playwright.sync_api import sync_playwright
src = pathlib.Path(args.entrada).resolve()
with sync_playwright() as p:
    b = p.chromium.launch(executable_path=args.chrome or chrome(), headless=True)
    def open_at(w, mob=False):
        ctx = b.new_context(viewport={'width': w, 'height': 900}, is_mobile=mob)
        pg = ctx.new_page()
        if args.offline: pg.route(re.compile(r'^https?://'), lambda r: r.abort())
        pg.goto(src.as_uri(), wait_until='load', timeout=60000); pg.wait_for_timeout(800)
        # força estado final de animações de entrada da casa
        pg.evaluate("document.querySelectorAll('.scroll-left,.scroll-right,.scroll-top,.scroll-bottom').forEach(e=>e.classList.add('ativo'))")
        return ctx, pg
    ctx, pg = open_at(1440)
    data = pg.evaluate(COLLECT)
    ids_html = pg.content()
    ctx.close()
    # mobile: reabre e marca os mesmos elementos na mesma ordem
    ctx, pg = open_at(390, True)
    pg.evaluate("document.querySelectorAll('body *').forEach((e, i) => e.setAttribute('data-h2e', i + 1))")  # mesma numeração do desktop
    mob = pg.evaluate(MOBILE)
    ctx.close(); b.close()

# ---------------------------------------------------------------- helpers
def nid():
    return '%07x' % random.randrange(16 ** 7)

def px(v):
    try: return float(str(v).replace('px', ''))
    except: return None

def num(v):
    f = px(v)
    if f is None: return None
    return int(f) if abs(f - int(f)) < 0.01 else round(f, 2)

def rgb2hex(c):
    m = re.match(r'rgba?\(([\d.]+),\s*([\d.]+),\s*([\d.]+)(?:,\s*([\d.]+))?\)', c or '')
    if not m: return None
    r, g, bb = (int(float(x)) for x in m.groups()[:3]); a = float(m.group(4)) if m.group(4) else 1
    if a == 0: return None
    return '#%02X%02X%02X' % (r, g, bb) if a >= 0.99 else '#%02X%02X%02X%02X' % (r, g, bb, int(a * 255))

def dims(box, prefix):
    t, r_, b_, l = (num(box[f'{prefix}-{k}']) for k in ('top', 'right', 'bottom', 'left'))
    if not any([t, r_, b_, l]): return None
    return {'unit': 'px', 'top': str(t or 0), 'right': str(r_ or 0), 'bottom': str(b_ or 0), 'left': str(l or 0), 'isLinked': len({t, r_, b_, l}) == 1}

def mdims(m, prefix):
    t, r_, b_, l = (num(m.get(f'{prefix}-{k}')) for k in ('top', 'right', 'bottom', 'left'))
    return {'unit': 'px', 'top': str(t or 0), 'right': str(r_ or 0), 'bottom': str(b_ or 0), 'left': str(l or 0), 'isLinked': len({t, r_, b_, l}) == 1}

def radius(box):
    v = [num(box[k]) for k in ('border-top-left-radius', 'border-top-right-radius', 'border-bottom-right-radius', 'border-bottom-left-radius')]
    if not any(v): return None
    return {'unit': 'px', 'top': str(v[0] or 0), 'right': str(v[1] or 0), 'bottom': str(v[2] or 0), 'left': str(v[3] or 0), 'isLinked': len(set(v)) == 1}

def shadow(s):
    if not s or s == 'none' or ',' in s.split(')')[-1]: return None
    m = re.match(r'(rgba?\([^)]*\))\s+(-?[\d.]+)px\s+(-?[\d.]+)px\s+([\d.]+)px(?:\s+(-?[\d.]+)px)?(\s+inset)?', s)
    if not m: return None
    return {'horizontal': num(m.group(2)), 'vertical': num(m.group(3)), 'blur': num(m.group(4)), 'spread': num(m.group(5) or 0), 'color': m.group(1)}

ALIGN = {'flex-start': 'flex-start', 'start': 'flex-start', 'normal': None, 'center': 'center', 'flex-end': 'flex-end', 'end': 'flex-end', 'space-between': 'space-between', 'space-around': 'space-around', 'space-evenly': 'space-evenly', 'stretch': 'stretch', 'baseline': None, 'left': 'flex-start', 'right': 'flex-end'}

def gradient(bgimg):
    m = re.match(r'linear-gradient\((?:(-?[\d.]+)deg,\s*)?(rgba?\([^)]*\))(?:\s+([\d.]+)%)?,\s*(rgba?\([^)]*\))(?:\s+([\d.]+)%)?\)$', bgimg.strip())
    if not m: return None
    return {'background_background': 'gradient', 'background_color': rgb2hex(m.group(2)), 'background_color_stop': {'unit': '%', 'size': num(m.group(3) or 0), 'sizes': []},
            'background_color_b': rgb2hex(m.group(4)), 'background_color_b_stop': {'unit': '%', 'size': num(m.group(5) or 100), 'sizes': []},
            'background_gradient_angle': {'unit': 'deg', 'size': num(m.group(1) or 180), 'sizes': []}}

def background(box, prefix=''):
    st = {}
    bgimg = box['background-image']
    if bgimg and bgimg != 'none':
        g = gradient(bgimg)
        if g:
            st.update({prefix + k: v for k, v in g.items()})
        else:
            u = re.search(r'url\(["\']?([^"\')]+)', bgimg)
            if u:
                st[prefix + 'background_background'] = 'classic'
                st[prefix + 'background_image'] = {'url': u.group(1), 'id': '', 'size': '', 'source': 'url'}
                st[prefix + 'background_size'] = 'cover' if 'cover' in box['background-size'] else 'initial'
                st[prefix + 'background_position'] = 'center center'
                st[prefix + 'background_repeat'] = 'no-repeat'
            if rgb2hex(box['background-color']): st[prefix + 'background_color'] = rgb2hex(box['background-color'])
    elif rgb2hex(box['background-color']):
        st[prefix + 'background_background'] = 'classic'; st[prefix + 'background_color'] = rgb2hex(box['background-color'])
    return st

def classes(node):
    c = ' '.join(x for x in node['cls'].split() if x != 'ativo')  # 'ativo' é estado do scroll reveal, não classe de origem
    return c

def common(node, st, container=False):
    c = classes(node)
    # no Elementor, container guarda a classe em css_classes; widget, em _css_classes (igual aos JSONs da casa)
    if c: st['css_classes' if container else '_css_classes'] = c
    if node['elid']: st['_element_id'] = node['elid']
    return st

def fam(f):
    return f.split(',')[0].strip().strip('"\'')

def typo(node, prefix, m=None):
    t = node['typo']; st = {f'{prefix}typography_typography': 'custom'}
    st[f'{prefix}typography_font_family'] = fam(t['font-family'])
    fs = num(t['font-size']); st[f'{prefix}typography_font_size'] = {'unit': 'px', 'size': fs, 'sizes': []}
    st[f'{prefix}typography_font_weight'] = t['font-weight']
    lh = px(t['line-height'])
    if lh and fs: st[f'{prefix}typography_line_height'] = {'unit': 'em', 'size': round(lh / fs, 2), 'sizes': []}
    ls = px(t['letter-spacing'])
    if ls: st[f'{prefix}typography_letter_spacing'] = {'unit': 'px', 'size': ls, 'sizes': []}
    if t['text-transform'] not in ('none', ''): st[f'{prefix}typography_text_transform'] = t['text-transform']
    if t['font-style'] == 'italic': st[f'{prefix}typography_font_style'] = 'italic'
    if m:
        mfs = px(m.get('font-size'))
        if mfs and mfs != fs: st[f'{prefix}typography_font_size_mobile'] = {'unit': 'vw', 'size': round(mfs / 390 * 100, 1), 'sizes': []}
        mlh = px(m.get('line-height'))
        if mlh and mfs: st[f'{prefix}typography_line_height_mobile'] = {'unit': 'em', 'size': round(mlh / mfs, 2), 'sizes': []}
    return st

def text_align(node, key, m=None):
    st = {}
    a = node['typo']['text-align']
    if a in ('center', 'right', 'justify'): st[key] = a
    if m and m.get('text-align') and m['text-align'] != a and m['text-align'] in ('center', 'left', 'right', 'justify', 'start'):
        st[key + '_mobile'] = 'left' if m['text-align'] == 'start' else m['text-align']
    return st

def widget(wtype, st):
    return {'id': nid(), 'settings': st, 'elements': [], 'isInner': False, 'widgetType': wtype, 'elType': 'widget'}

def html_widget(node, raw=None):
    return widget('html', common(node, {'html': raw if raw is not None else node['outer']}))

INLINE = {'span', 'strong', 'b', 'em', 'i', 'a', 'br', 'small', 'mark', 'u', 'sup', 'sub', 'code'}
def is_textual(node):
    return all(k['tag'] in INLINE for k in node['kids'])

def mk_heading(node, m):
    st = {'title': node['html'].strip(), 'header_size': node['tag'] if node['tag'] in ('h1', 'h2', 'h3', 'h4', 'h5', 'h6') else 'div'}
    c = rgb2hex(node['typo']['color'])
    if c: st['title_color'] = c
    st.update(typo(node, '', m)); st.update(text_align(node, 'align', m))
    return widget('heading', common(node, st))

def mk_text(node, m):
    inner = node['html'].strip()
    st = {'editor': inner if node['tag'] in ('div', 'span') else f'<{node["tag"]}>{inner}</{node["tag"]}>' if node['tag'] != 'p' else f'<p>{inner}</p>'}
    c = rgb2hex(node['typo']['color'])
    if c: st['text_color'] = c
    st.update(typo(node, '', m)); st.update(text_align(node, 'align', m))
    st['paragraph_spacing'] = {'unit': 'px', 'size': 0, 'sizes': []}
    return widget('text-editor', common(node, st))

def mk_button(node, m):
    a = node['attrs']; b = node['box']
    st = {'text': re.sub(r'\s+', ' ', node['text']).strip(), 'link': {'url': a.get('href', '#'), 'is_external': 'on' if a.get('target') == '_blank' else '', 'nofollow': ''}}
    st.update(typo(node, '', m))
    c = rgb2hex(node['typo']['color'])
    if c: st['button_text_color'] = c
    g = gradient(b['background-image']) if b['background-image'] != 'none' else None
    if g: st.update(g)
    elif rgb2hex(b['background-color']): st['background_color'] = rgb2hex(b['background-color'])
    rd = radius(b); pd = dims(b, 'padding')
    if rd: st['border_radius'] = rd
    if pd: st['text_padding'] = pd
    if m and pd: st['text_padding_mobile'] = mdims(m, 'padding')
    bw = num(b['border-top-width'])
    if bw and b['border-top-style'] != 'none':
        st['border_border'] = b['border-top-style']; st['border_width'] = {'unit': 'px', 'top': str(bw), 'right': str(bw), 'bottom': str(bw), 'left': str(bw), 'isLinked': True}; st['border_color'] = rgb2hex(b['border-top-color'])
    sh = shadow(b['box-shadow'])
    if sh: st['button_box_shadow_box_shadow_type'] = 'yes'; st['button_box_shadow_box_shadow'] = sh
    if '<svg' in node['html'] or '<i ' in node['html']:
        st['selected_icon'] = {'value': 'fab fa-whatsapp' if 'wa.me' in a.get('href', '') or 'whatsapp' in a.get('href', '') else 'fas fa-arrow-right', 'library': 'fa-brands' if 'wa.me' in a.get('href', '') else 'fa-solid'}
        st['icon_align'] = 'right'; st['icon_indent'] = {'unit': 'px', 'size': 10, 'sizes': []}
    return widget('button', common(node, st))

def mk_image(node, m):
    st = {'image': {'url': node['src'], 'id': '', 'size': '', 'alt': node['attrs'].get('alt', ''), 'source': 'url'}, 'image_size': 'full'}
    if node['parentW'] and node['w'] < node['parentW'] * 0.98:
        st['width'] = {'unit': '%', 'size': round(100 * node['w'] / node['parentW']), 'sizes': []}
    rd = radius(node['box'])
    if rd: st['image_border_radius'] = rd
    return widget('image', common(node, st))

def mk_list(node, m):
    items = []
    for li in node['kids']:
        if li['tag'] != 'li': continue
        items.append({'text': re.sub(r'\s+', ' ', li['text']).strip(), 'selected_icon': {'value': 'fas fa-check', 'library': 'fa-solid'}, '_id': nid()})
    st = {'icon_list': items}
    if node['kids']:
        li = node['kids'][0]; st.update(typo(li, 'icon_', mob.get(str(li['id']))))
        c = rgb2hex(li['typo']['color'])
        if c: st['text_color'] = c; st['icon_color'] = c
    return widget('icon-list', common(node, st))

def mk_toggle(nodes):
    tabs = []
    for d in nodes:
        summ = next((k for k in d['kids'] if k['tag'] == 'summary'), None)
        body = ''.join(k['outer'] for k in d['kids'] if k['tag'] != 'summary')
        tabs.append({'tab_title': re.sub(r'\s+', ' ', summ['text'] if summ else '').strip(), 'tab_content': body, '_id': nid()})
    return widget('toggle', {'tabs': tabs})

def mk_iframe(node):
    s = node['src']
    if 'youtube' in s or 'youtu.be' in s or 'vimeo' in s:
        return widget('video', common(node, {'youtube_url': s, 'video_type': 'vimeo' if 'vimeo' in s else 'youtube'}))
    if 'google.com/maps' in s:
        q = re.search(r'[?&]q=([^&]+)', s)
        return widget('google_maps', common(node, {'address': q.group(1) if q else s, 'height': {'unit': 'px', 'size': node['h'], 'sizes': []}}))
    return html_widget(node)

# ---------------------------------------------------------------- conversão recursiva
WIDGET_TAGS = {'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'img', 'ul', 'ol', 'iframe', 'button', 'details', 'svg', 'canvas', 'form', 'video', 'table', 'picture', 'blockquote', 'figure', 'hr'}

def is_button(node):
    c = node['cls'].lower()
    return node['tag'] == 'button' or (node['tag'] == 'a' and (re.search(r'\b(btn|button|botao|cta)\b', c) or node['attrs'].get('data-el') == 'button'))

def convert(node, depth):
    """devolve lista de elementos Elementor"""
    m = mob.get(str(node['id']), {})
    de = node['attrs'].get('data-el')
    if de == 'html' or node['tag'] in ('svg', 'canvas', 'form', 'table', 'video', 'blockquote'):
        return [html_widget(node)]
    if de == 'ignore': return []
    if node['tag'] in ('h1', 'h2', 'h3', 'h4', 'h5', 'h6') or de == 'heading':
        return [mk_heading(node, m)]
    if is_button(node): return [mk_button(node, m)]
    if node['tag'] == 'img': return [mk_image(node, m)]
    if node['tag'] == 'picture':
        img = next((k for k in node['kids'] if k['tag'] == 'img'), None)
        return [mk_image(img, m)] if img else []
    if node['tag'] in ('ul', 'ol') and all(k['tag'] == 'li' and is_textual(k) for k in node['kids']):
        return [mk_list(node, m)]
    if node['tag'] == 'iframe': return [mk_iframe(node)]
    if node['tag'] == 'hr': return [widget('divider', common(node, {}))]
    if node['tag'] == 'p' or (node['tag'] in ('div', 'span', 'li', 'small', 'label') and node['directText'] and is_textual(node)) or de == 'text':
        return [mk_text(node, m)]
    if node['tag'] == 'a' and is_textual(node):
        return [mk_text(node, m)]
    if not node['kids']:
        bg = background(node['box'])
        if bg or node['h'] > 0:
            if bg or rgb2hex(node['box']['border-top-color']) and num(node['box']['border-top-width']):
                return [html_widget(node)]  # elemento decorativo vazio
        return []
    # container
    kids = []
    i = 0; ks = node['kids']
    while i < len(ks):
        k = ks[i]
        if k['tag'] == 'details':
            group = []
            while i < len(ks) and ks[i]['tag'] == 'details': group.append(ks[i]); i += 1
            kids.append(mk_toggle(group)); continue
        kids.extend(convert(k, depth + 1)); i += 1
    return [mk_container(node, kids, depth, m)]

def mk_container(node, kids, depth, m):
    b = node['box']; st = {}
    flex = b['display'] in ('flex', 'inline-flex')
    grid = b['display'] in ('grid', 'inline-grid')
    st['flex_direction'] = (b['flex-direction'] if flex else ('row' if grid else 'column'))
    if grid or (flex and b['flex-wrap'] == 'wrap'): st['flex_wrap'] = 'wrap'
    if flex or grid:
        jc = ALIGN.get(b['justify-content']); ai = ALIGN.get(b['align-items'])
        if jc: st['flex_justify_content'] = jc
        if ai and ai != 'stretch': st['flex_align_items'] = ai
    g = num(b['column-gap']) if st['flex_direction'].startswith('row') else num(b['row-gap'])
    st['flex_gap'] = {'column': str(num(b['column-gap']) or 0), 'row': str(num(b['row-gap']) or 0), 'isLinked': num(b['column-gap']) == num(b['row-gap']), 'unit': 'px', 'size': g or 0}
    pd = dims(b, 'padding')
    if pd: st['padding'] = pd
    if m and any(m.get(f'padding-{k}') != b[f'padding-{k}'] for k in ('top', 'right', 'bottom', 'left')): st['padding_mobile'] = mdims(m, 'padding')
    if m and flex and m.get('flex-direction') and m['flex-direction'] != b['flex-direction']: st['flex_direction_mobile'] = m['flex-direction']
    if m and grid and m.get('display') == 'grid': st['flex_direction_mobile'] = 'column'
    mh = num(b['min-height'])
    if mh: st['min_height'] = {'unit': 'px', 'size': mh, 'sizes': []}
    st.update(background(b))
    rd = radius(b)
    if rd: st['border_radius'] = rd
    bw = num(b['border-top-width'])
    if bw and b['border-top-style'] != 'none':
        st['border_border'] = b['border-top-style']; st['border_width'] = {'unit': 'px', 'top': str(bw), 'right': str(bw), 'bottom': str(bw), 'left': str(bw), 'isLinked': True}; st['border_color'] = rgb2hex(b['border-top-color'])
    sh = shadow(b['box-shadow'])
    if sh: st['box_shadow_box_shadow_type'] = 'yes'; st['box_shadow_box_shadow'] = sh
    if depth == 0:
        # seção de topo: procura um wrapper com max-width para virar boxed_width
        mw = None
        for k in node['kids']:
            v = num(k['box']['max-width'])
            if v and v < 2000: mw = v; break
        if mw:
            st['content_width'] = 'boxed'; st['boxed_width'] = {'unit': 'px', 'size': mw, 'sizes': []}
            # achata o wrapper: os filhos dele sobem
            if len(kids) == 1 and kids[0]['elType'] == 'container':
                w = kids[0]; kids = w['elements']
                for key in ('flex_direction', 'flex_gap', 'flex_justify_content', 'flex_align_items', 'flex_wrap', 'flex_direction_mobile'):
                    if key in w['settings']: st[key] = w['settings'][key]
        else:
            st['content_width'] = 'full'
    else:
        st['content_width'] = 'full'
        if node['parentW'] and node['w'] < node['parentW'] * 0.97 and node['parentW'] > 0:
            st['width'] = {'unit': '%', 'size': round(100 * node['w'] / node['parentW'], 1), 'sizes': []}
            if m and num(m.get('width')) and num(m.get('width')) > 300: st['width_mobile'] = {'unit': '%', 'size': 100, 'sizes': []}
    common(node, st, container=True)
    for k in kids:
        if k['elType'] == 'container': k['isInner'] = True
    return {'id': nid(), 'settings': st, 'elements': kids, 'isInner': depth > 0, 'elType': 'container'}

# raízes: se o body tiver um único wrapper (main/div) sem estilo, desce um nível
roots = data['roots']
while len(roots) == 1 and roots[0]['tag'] in ('main', 'div') and not background(roots[0]['box']) and not any(k['tag'] in WIDGET_TAGS for k in roots[0]['kids'][:0]):
    roots = roots[0]['kids']
content = []
for r in roots:
    if r['tag'] in ('header', 'nav', 'footer', 'section', 'div', 'main', 'article', 'aside'):
        content.extend(convert(r, 0))
    else:
        el = convert(r, 1)
        content.append({'id': nid(), 'settings': {'flex_direction': 'column', 'content_width': 'boxed'}, 'elements': el, 'isInner': False, 'elType': 'container'})
if data['scripts'].strip():
    content.append({'id': nid(), 'settings': {'flex_direction': 'column', 'content_width': 'full', 'css_classes': 'scripts-da-pagina'}, 'elements': [widget('html', {'html': data['scripts']})], 'isInner': False, 'elType': 'container'})

page_settings = {}
if not args.sem_css and data['styles'].strip():
    page_settings['custom_css'] = data['styles']
fonts = [l for l in data['links'] if 'fonts.googleapis' in l]
title = args.titulo or data['title'] or src.stem
if args.clipboard:
    out = {'type': 'elementor', 'siteurl': '', 'elements': content}
else:
    out = {'content': content, 'page_settings': page_settings, 'version': '0.4', 'title': title, 'type': 'page'}
json.dump(out, open(args.saida, 'w'), ensure_ascii=False, indent=1)

# relatório
cnt = {}
def walk(n):
    for x in n:
        k = x.get('widgetType') or x['elType']; cnt[k] = cnt.get(k, 0) + 1; walk(x.get('elements', []))
walk(content)
print(f'OK: {args.saida}')
print('  seções de topo:', len(content), '| elementos:', sum(cnt.values()))
print('  por tipo:', ', '.join(f'{k} {v}' for k, v in sorted(cnt.items(), key=lambda x: -x[1])))
if fonts: print('  atenção: a página usa Google Fonts por <link>; no Elementor selecione as mesmas famílias (o JSON já traz typography_font_family).')
