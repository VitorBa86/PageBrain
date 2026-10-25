#!/usr/bin/env python3
"""
elementor-para-preview.py
Gera um HTML de PRÉ-VISUALIZAÇÃO aproximada a partir de um JSON do Elementor (página ou seção), e opcionalmente um PNG.
Serve para ver como é uma seção/página sem ter WordPress. Não é fiel a 100%: widgets de addons, animações,
carrosseis e CSS custom com 'selector' são aproximados ou ignorados.

Uso:
  python3 elementor-para-preview.py entrada.json saida.html [--png saida.png] [--largura 1440]
Dependências para PNG: playwright + Google Chrome.
"""
import json, sys, html, re, argparse, pathlib, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _navegador import chrome  # noqa: E402

ap = argparse.ArgumentParser()
ap.add_argument('entrada'); ap.add_argument('saida')
ap.add_argument('--png'); ap.add_argument('--largura', type=int, default=1440)
ap.add_argument('--chrome', default=None, help='caminho do Chrome (padrão: acha sozinho, ver _navegador.py)')
a = ap.parse_args()

d = json.load(open(a.entrada))
root = d.get('content') or d.get('elements') or []
fonts = set()
esc = lambda s: html.escape(str(s), quote=True)

def unit(v, default='px'):
    if isinstance(v, dict):
        s = v.get('size')
        if s in (None, ''): return None
        return f"{s}{v.get('unit') or default}"
    return None

def box(v):
    if not isinstance(v, dict): return None
    u = v.get('unit', 'px')
    vals = [v.get(k, '0') or '0' for k in ('top', 'right', 'bottom', 'left')]
    return ' '.join(f'{x}{u}' for x in vals)

def bg(s, p=''):
    t = s.get(p + 'background_background')
    css = []
    if t == 'gradient':
        ang = unit(s.get(p + 'background_gradient_angle'), 'deg') or '180deg'
        a1 = s.get(p + 'background_color', '#fff'); a2 = s.get(p + 'background_color_b', '#000')
        st1 = unit(s.get(p + 'background_color_stop'), '%') or '0%'; st2 = unit(s.get(p + 'background_color_b_stop'), '%') or '100%'
        if s.get(p + 'background_gradient_type') == 'radial':
            css.append(f'background:radial-gradient({a1} {st1}, {a2} {st2})')
        else:
            css.append(f'background:linear-gradient({ang}, {a1} {st1}, {a2} {st2})')
    elif t in ('classic', None):
        if s.get(p + 'background_color'): css.append(f"background-color:{s[p + 'background_color']}")
        img = s.get(p + 'background_image')
        if isinstance(img, dict) and img.get('url'):
            css.append(f"background-image:url(&quot;{img['url']}&quot;);background-size:{s.get(p + 'background_size', 'cover') if s.get(p + 'background_size') not in (None, 'initial') else 'cover'};background-position:{s.get(p + 'background_position', 'center center').replace('_', ' ')};background-repeat:no-repeat")
    return ';'.join(css)

def typo(s, p=''):
    css = []
    f = s.get(p + 'typography_font_family')
    if f: css.append(f"font-family:'{f}',sans-serif"); fonts.add(f)
    for k, c in (('typography_font_size', 'font-size'), ('typography_line_height', 'line-height'), ('typography_letter_spacing', 'letter-spacing')):
        v = unit(s.get(p + k))
        if v: css.append(f'{c}:{v}')
    if s.get(p + 'typography_font_weight'): css.append(f"font-weight:{s[p + 'typography_font_weight']}")
    if s.get(p + 'typography_text_transform'): css.append(f"text-transform:{s[p + 'typography_text_transform']}")
    if s.get(p + 'typography_font_style'): css.append(f"font-style:{s[p + 'typography_font_style']}")
    return ';'.join(css)

def common(s):
    css = []
    if box(s.get('_padding')): css.append(f"padding:{box(s['_padding'])}")
    if box(s.get('_margin')): css.append(f"margin:{box(s['_margin'])}")
    if s.get('_element_width') == 'initial' and unit(s.get('_element_custom_width'), '%'): css.append(f"width:{unit(s['_element_custom_width'], '%')}")
    if s.get('_position') == 'absolute': css.append('position:absolute;opacity:.85')
    b = bg(s, '_')
    if b: css.append(b)
    if box(s.get('_border_radius')): css.append(f"border-radius:{box(s['_border_radius'])}")
    return ';'.join(css)

def icon(sel, color='#888', size='28px'):
    if not isinstance(sel, dict): return ''
    v = sel.get('value')
    if isinstance(v, dict) and v.get('url'): return f"<img src='{esc(v['url'])}' style='width:{size};height:{size};object-fit:contain'>"
    if isinstance(v, str) and v: return f"<i class='{esc(v)}' style='color:{color};font-size:{size}'></i>"
    return ''

def widget(x):
    s = x.get('settings') if isinstance(x.get('settings'), dict) else {}
    t = x.get('widgetType'); cs = common(s); cls = esc(s.get('_css_classes', ''))
    al = s.get('align') or s.get('text_align') or ''
    if t == 'heading':
        tag = s.get('header_size', 'h2'); tag = tag if tag in ('h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'div', 'p', 'span') else 'div'
        return f"<{tag} class='w {cls}' style='margin:0;color:{s.get('title_color', '#222')};text-align:{al or 'left'};{typo(s)};{cs}'>{s.get('title', '')}</{tag}>"
    if t == 'text-editor':
        return f"<div class='w te {cls}' style='color:{s.get('text_color', '#444')};text-align:{al or 'left'};{typo(s)};{cs}'>{s.get('editor', '')}</div>"
    if t == 'button':
        b = bg(s) or f"background:{s.get('background_color', '#333')}"
        st = f"display:inline-flex;gap:8px;align-items:center;text-decoration:none;color:{s.get('button_text_color', '#fff')};{b};padding:{box(s.get('text_padding')) or '14px 28px'};border-radius:{box(s.get('border_radius')) or '4px'};{typo(s)}"
        if s.get('border_border'): st += f";border:{(s.get('border_width') or {}).get('top', '1')}px {s['border_border']} {s.get('border_color', '#000')}"
        just = {'center': 'center', 'right': 'flex-end', 'justify': 'stretch'}.get(al, 'flex-start')
        return f"<div class='w {cls}' style='display:flex;justify-content:{just};{cs}'><a style='{st}'>{esc(s.get('text', 'Botão'))} {icon(s.get('selected_icon'), s.get('button_text_color', '#fff'), '1em')}</a></div>"
    if t == 'image':
        img = s.get('image') or {}
        w = unit(s.get('width'), '%') or '100%'
        return f"<div class='w {cls}' style='text-align:{al or 'center'};{cs}'><img src='{esc(img.get('url', ''))}' style='width:{w};max-width:100%;border-radius:{box(s.get('image_border_radius')) or '0'}'></div>"
    if t == 'icon':
        return f"<div class='w {cls}' style='text-align:{al or 'center'};{cs}'>{icon(s.get('selected_icon'), s.get('primary_color', '#555'), unit(s.get('size')) or '40px')}</div>"
    if t == 'icon-box':
        return (f"<div class='w {cls}' style='text-align:{s.get('text_align', 'left')};{cs}'>{icon(s.get('selected_icon'), s.get('primary_color', '#555'), unit(s.get('icon_size')) or '36px')}"
                f"<div style='color:{s.get('title_color', '#222')};{typo(s, 'title_')};margin:8px 0 4px;font-weight:600'>{s.get('title_text', '')}</div>"
                f"<div style='color:{s.get('description_color', '#555')};{typo(s, 'description_')}'>{s.get('description_text', '')}</div></div>")
    if t == 'image-box':
        img = s.get('image') or {}
        return (f"<div class='w {cls}' style='text-align:{s.get('text_align', 'left')};{cs}'><img src='{esc(img.get('url', ''))}' style='width:{unit(s.get('image_size'), '%') or '100%'};border-radius:8px'>"
                f"<div style='color:{s.get('title_color', '#222')};{typo(s, 'title_')};margin:8px 0 4px;font-weight:600'>{s.get('title_text', '')}</div>"
                f"<div style='color:{s.get('description_color', '#555')};{typo(s, 'description_')}'>{s.get('description_text', '')}</div></div>")
    if t == 'social-icons':
        its = s.get('social_icon_list') or []
        return f"<div class='w' style='display:flex;gap:10px;{cs}'>" + ''.join(f"<span style='width:36px;height:36px;border-radius:50%;background:{s.get('icon_primary_color', '#333')};display:grid;place-items:center'>{icon(i.get('social_icon'), s.get('icon_secondary_color', '#fff'), '16px')}</span>" for i in its) + "</div>"
    if t == 'icon-list':
        items = s.get('icon_list') or []
        inline = s.get('view') == 'inline'
        lis = ''.join(f"<li style='display:flex;gap:8px;align-items:center;{'margin-right:24px' if inline else 'margin:4px 0'}'>{icon(it.get('selected_icon'), s.get('icon_color', '#555'), unit(s.get('icon_size')) or '14px')}<span>{esc(it.get('text', ''))}</span></li>" for it in items)
        return f"<ul class='w {cls}' style='list-style:none;margin:0;padding:0;display:{'flex' if inline else 'block'};flex-wrap:{'nowrap' if inline else 'wrap'};overflow:hidden;color:{s.get('text_color', '#444')};{typo(s, 'icon_')};{cs}'>{lis}</ul>"
    if t == 'toggle' or t == 'accordion':
        tabs = s.get('tabs') or []
        return f"<div class='w {cls}' style='{cs}'>" + ''.join(f"<details style='border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:6px 0;background:{s.get('title_background', '#fff')}'><summary style='{typo(s, 'title_')};color:{s.get('title_color', '#222')}'>{esc(tb.get('tab_title', ''))}</summary>{tb.get('tab_content', '')}</details>" for tb in tabs) + "</div>"
    if t == 'divider':
        return f"<hr class='w' style='border:0;border-top:{unit(s.get('weight')) or '1px'} solid {s.get('color', '#ccc')};width:{unit(s.get('width'), '%') or '100%'};{cs}'>"
    if t == 'spacer':
        return f"<div style='height:{unit(s.get('space')) or '30px'}'></div>"
    if t == 'html':
        return f"<div class='w {cls}' style='{cs}'>{s.get('html', '')}</div>"
    if t == 'google_maps':
        return f"<iframe class='w' src='https://maps.google.com/maps?q={esc(s.get('address', ''))}&output=embed' style='width:100%;height:{unit(s.get('height')) or '300px'};border:0'></iframe>"
    if t == 'video':
        return f"<div class='w' style='aspect-ratio:16/9;background:#111;color:#fff;display:flex;align-items:center;justify-content:center;border-radius:8px;{cs}'>▶ vídeo</div>"
    if t == 'image-carousel':
        imgs = s.get('carousel') or []
        return f"<div class='w' style='display:flex;gap:10px;overflow:hidden;{cs}'>" + ''.join(f"<img src='{esc(i.get('url', ''))}' style='height:220px;border-radius:8px'>" for i in imgs[:6]) + "</div>"
    label = esc(t or '?')
    return f"<div class='w' style='border:1px dashed #aaa;padding:16px;color:#888;font:12px monospace;{cs}'>[widget {label}]</div>"

def container(x, top):
    s = x.get('settings') if isinstance(x.get('settings'), dict) else {}
    dirn = s.get('flex_direction') or 'column'
    css = [f'display:flex;flex-direction:{dirn};position:relative']
    gap = s.get('flex_gap')
    if isinstance(gap, dict): css.append(f"gap:{gap.get('row') or gap.get('size') or 20}{gap.get('unit', 'px')} {gap.get('column') or gap.get('size') or 20}{gap.get('unit', 'px')}")
    else: css.append('gap:20px')
    if s.get('flex_justify_content'): css.append(f"justify-content:{s['flex_justify_content']}")
    if s.get('flex_align_items'): css.append(f"align-items:{s['flex_align_items']}")
    if s.get('flex_wrap'): css.append(f"flex-wrap:{s['flex_wrap']}")
    css.append(f"padding:{box(s.get('padding')) or ('10px' if not top else '10px')}")
    if box(s.get('margin')): css.append(f"margin:{box(s['margin'])}")
    if unit(s.get('min_height')): css.append(f"min-height:{unit(s['min_height'])}")
    if not top:
        w = unit(s.get('width'), '%')
        css.append(f"width:{w}" if w else ('flex:1 1 0' if any(dirn.startswith(r) for r in ('row',)) else 'width:100%'))
    b = bg(s)
    if b: css.append(b)
    if box(s.get('border_radius')): css.append(f"border-radius:{box(s['border_radius'])}")
    if s.get('border_border'): css.append(f"border:{(s.get('border_width') or {}).get('top', '1')}px {s['border_border']} {s.get('border_color', '#000')}")
    sh = s.get('box_shadow_box_shadow')
    if isinstance(sh, dict): css.append(f"box-shadow:{sh.get('horizontal', 0)}px {sh.get('vertical', 0)}px {sh.get('blur', 10)}px {sh.get('spread', 0)}px {sh.get('color', 'rgba(0,0,0,.2)')}")
    ov = s.get('background_overlay_color')
    over = f"<div style='position:absolute;inset:0;background:{ov};opacity:{(s.get('background_overlay_opacity') or {}).get('size', .5)};border-radius:inherit;pointer-events:none'></div>" if ov else ''
    inner = ''.join(render(c, False) for c in x.get('elements', []))
    if top and s.get('content_width', 'boxed') == 'boxed':
        bw = unit(s.get('boxed_width')) or '1140px'
        inn = ';'.join(c for c in css if c.startswith(('display', 'gap', 'justify', 'align', 'flex-wrap')))
        outer = ';'.join(c for c in css if not c.startswith(('gap', 'justify', 'align', 'flex-wrap'))).replace(f'flex-direction:{dirn}', 'flex-direction:column;align-items:center')
        return f"<section class='{esc(s.get('_css_classes', ''))}' style='{outer}'>{over}<div style='{inn};width:100%;max-width:{bw};position:relative'>{inner}</div></section>"
    tag = 'section' if top else 'div'
    return f"<{tag} class='{esc(s.get('_css_classes', ''))}' style='{';'.join(css)}'>{over}{inner}</{tag}>"

def render(x, top):
    return container(x, top) if x.get('elType') in ('container', 'section', 'column') else widget(x)

body = ''.join(render(x, True) for x in root)
ps = d.get('page_settings') if isinstance(d.get('page_settings'), dict) else {}
pcss = (ps.get('custom_css') or '')
fl = '&'.join('family=' + f.replace(' ', '+') + ':ital,wght@0,300;0,400;0,500;0,600;0,700;0,800;1,400' for f in sorted(fonts) if f and f != 'googlefonts')
page = f"""<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Preview · {esc(d.get('title', pathlib.Path(a.entrada).stem))}</title>
{f'<link rel="stylesheet" href="https://fonts.googleapis.com/css2?{fl}&display=swap">' if fl else ''}
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css">
<style>body{{margin:0;font-family:Inter,system-ui,sans-serif;background:#fff}} .w{{max-width:100%}} .te p{{margin:0 0 .6em}} img{{max-width:100%}}
.scroll-left,.scroll-right,.scroll-top,.scroll-bottom{{opacity:1!important;transform:none!important;filter:none!important}}
{pcss}</style></head><body>{body}</body></html>"""
open(a.saida, 'w').write(page)
if a.png:
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path=a.chrome or chrome(), headless=True)
        pg = b.new_page(viewport={'width': a.largura, 'height': 300})
        pg.goto(pathlib.Path(a.saida).resolve().as_uri(), wait_until='networkidle', timeout=60000)
        pg.wait_for_timeout(800)
        pg.screenshot(path=a.png, full_page=True); b.close()
print('ok', a.saida, a.png or '')
