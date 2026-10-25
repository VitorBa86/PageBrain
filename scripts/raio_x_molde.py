"""PageBrain · Raio-x de molde.

Fatia uma página (da casa ou gerada) em seções e mede, seção por seção, o que a IA
precisa copiar para a página nova ficar "irmã" da original: fundo, padding, altura,
cada estilo de texto (tamanho, peso, fonte, cor, line-height, caixa), botões, cards
e o tamanho exato de cada imagem (que vira o slot da página nova).

Uso:
  python3 raio_x_molde.py <arquivo.html | slug de paginas/nossas> [pasta_saida]

Exemplos:
  python3 raio_x_molde.py vendas-mentoria-bancario-jessica
  python3 raio_x_molde.py ../../minha-pagina/index.html /tmp/raio-x-gerada

Saída (padrão: <pasta do site>/raio-x/): raio-x.md, raio-x.json, secao-NN.jpg e pagina-mobile.jpg.
Requisitos: Python 3.9+, playwright e Pillow (usa o Google Chrome instalado ou o Chromium do Playwright).
"""
import asyncio
import json
import os
import sys
from io import BytesIO

from PIL import Image
from playwright.async_api import async_playwright

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _navegador import chrome  # noqa: E402
AQUI = os.path.dirname(os.path.abspath(__file__))
NOSSAS = os.path.normpath(os.path.join(AQUI, '..', 'paginas', 'nossas'))
DESIGN = os.path.normpath(os.path.join(AQUI, '..', 'design'))

# Força tudo visível: o scroll reveal da casa deixa blocos com opacity 0 até rolar.
CSS_REVELAR = """*{animation-play-state:paused!important;transition:none!important}
.scroll-bottom,.scroll-left,.scroll-right,.scroll-top,[class*=reveal],.elementor-invisible{opacity:1!important;transform:none!important;filter:none!important;visibility:visible!important}"""

JS = r"""() => {
  const root = document.querySelector('div.elementor[data-elementor-type="wp-page"]')
            || document.querySelector('main') || document.body;
  let secs = [...root.children].filter(e => !['SCRIPT','STYLE','LINK','NOSCRIPT'].includes(e.tagName));
  if (secs.length < 3) secs = [...document.querySelectorAll('body section, body > header, body > footer')];
  const vis = e => { const r = e.getBoundingClientRect(); const cs = getComputedStyle(e);
    return r.width > 0 && r.height > 0 && cs.visibility !== 'hidden' && cs.display !== 'none'; };
  const px = v => Math.round(parseFloat(v) || 0);
  const lhEm = cs => { const l = parseFloat(cs.lineHeight), f = parseFloat(cs.fontSize);
    return isNaN(l) ? 'normal' : (l / f).toFixed(2) + 'em'; };
  const curto = v => v.replace(/url\(["']?[^"')]*\/([^\/"')?]+)[^)]*\)/g, 'url($1)');
  const bgOf = cs => cs.backgroundImage !== 'none' ? curto(cs.backgroundImage).slice(0, 140) + (/url/.test(cs.backgroundImage) ? ' sobre ' + cs.backgroundColor : '') : cs.backgroundColor;
  const out = [];
  secs.forEach((s, i) => {
    if (!vis(s)) return;
    const r = s.getBoundingClientRect(), cs = getComputedStyle(s);
    const inner = s.querySelector(':scope > .e-con-inner');
    const textos = {}, botoes = {}, imgs = [], cards = {};
    [s, s.querySelector(':scope > .e-con-inner')].forEach(f => { if (!f) return;
      const u = getComputedStyle(f).backgroundImage.match(/url\(["']?([^"')]+)/); if (!u) return;
      const fb = f.getBoundingClientRect();
      imgs.push({ tipo: 'fundo da seção', arquivo: u[1].split('/').pop().split('?')[0].slice(0, 60), largura: Math.round(fb.width), altura: Math.round(fb.height),
        proporcao: (fb.width / fb.height).toFixed(2), x: 0, y_na_secao: 0, raio: '0px', encaixe: getComputedStyle(f).backgroundSize, alt: '' }); });
    s.querySelectorAll('*').forEach(e => {
      if (!vis(e) || ['SCRIPT','STYLE','SVG','PATH','svg','path'].includes(e.tagName)) return;
      const c = getComputedStyle(e), b = e.getBoundingClientRect();
      const own = [...e.childNodes].filter(n => n.nodeType === 3).map(n => n.textContent.trim()).join(' ').trim();
      if (own.length >= 2) {
        const k = [px(c.fontSize), c.fontWeight, c.fontFamily.split(',')[0].replace(/["']/g, ''), c.color, c.textTransform, lhEm(c), c.letterSpacing, c.fontStyle].join('|');
        if (!textos[k]) textos[k] = { tamanho: px(c.fontSize), peso: c.fontWeight, fonte: c.fontFamily.split(',')[0].replace(/["']/g, ''),
          cor: c.color, caixa: c.textTransform, lh: lhEm(c), espacamento: c.letterSpacing, italico: c.fontStyle === 'italic',
          tag: e.tagName.toLowerCase(), exemplo: own.slice(0, 70), chars: 0, largura_max: 0 };
        textos[k].chars += own.length; textos[k].largura_max = Math.max(textos[k].largura_max, Math.round(b.width));
      }
      if ((e.tagName === 'A' || e.tagName === 'BUTTON') && e.innerText.trim().length > 3 && e.innerText.trim().length < 70 &&
          (c.backgroundImage !== 'none' || !/rgba\(0, 0, 0, 0\)|transparent/.test(c.backgroundColor) || px(c.borderTopWidth) > 0)) {
        const k = [c.fontSize, c.fontWeight, c.padding, c.borderRadius, bgOf(c)].join('|');
        if (!botoes[k]) botoes[k] = { texto: e.innerText.trim().slice(0, 50), tamanho: px(c.fontSize), peso: c.fontWeight,
          fonte: c.fontFamily.split(',')[0].replace(/["']/g, ''), caixa: c.textTransform, padding: c.padding, raio: c.borderRadius,
          fundo: bgOf(c), cor: c.color, borda: px(c.borderTopWidth) ? c.borderTopWidth + ' ' + c.borderTopColor : '',
          sombra: c.boxShadow !== 'none' ? c.boxShadow.slice(0, 90) : '', altura: Math.round(b.height), largura: Math.round(b.width),
          tem_icone: !!e.querySelector('svg,i,img'), qtde: 0 };
        botoes[k].qtde++;
      }
      const bgUrl = c.backgroundImage.match(/url\(["']?([^"')]+)/);
      if ((e.tagName === 'IMG' && b.width >= 60 && b.height >= 60) || (bgUrl && b.width >= 150 && b.height >= 100 && e !== s)) {
        const src = e.tagName === 'IMG' ? (e.currentSrc || e.src) : bgUrl[1];
        imgs.push({ tipo: e.tagName === 'IMG' ? 'img' : 'fundo', arquivo: src.split('/').pop().split('?')[0].slice(0, 60),
          largura: Math.round(b.width), altura: Math.round(b.height), proporcao: (b.width / b.height).toFixed(2),
          x: Math.round(b.left), y_na_secao: Math.round(b.top - r.top), raio: c.borderRadius, encaixe: c.objectFit || c.backgroundSize,
          alt: e.getAttribute('alt') || '' });
      }
      const rad = px(c.borderTopLeftRadius);
      if (rad > 0 && b.width >= 150 && b.width <= 760 && b.height >= 80 && e.innerText.trim().length > 10 &&
          (!/rgba\(0, 0, 0, 0\)/.test(c.backgroundColor) || c.backgroundImage !== 'none' || px(c.borderTopWidth) > 0 || c.boxShadow !== 'none') &&
          !['A', 'BUTTON'].includes(e.tagName)) {
        const k = [c.borderRadius, bgOf(c), c.borderTopWidth, c.boxShadow, c.padding].join('|');
        if (!cards[k]) cards[k] = { raio: c.borderRadius, fundo: bgOf(c), borda: px(c.borderTopWidth) ? c.borderTopWidth + ' ' + c.borderTopColor : '',
          sombra: c.boxShadow !== 'none' ? c.boxShadow.slice(0, 90) : '', padding: c.padding, largura: Math.round(b.width), altura: Math.round(b.height), qtde: 0 };
        cards[k].qtde++;
      }
    });
    const ic = inner ? getComputedStyle(inner) : null;
    out.push({ indice: i, topo: Math.round(r.top + scrollY), altura: Math.round(r.height), largura: Math.round(r.width),
      fundo: bgOf(cs), padding: cs.padding, padding_interno: ic ? ic.padding : '', largura_conteudo: inner ? Math.round(inner.getBoundingClientRect().width) : null,
      direcao: cs.flexDirection, gap: cs.gap,
      textos: Object.values(textos).sort((a, b) => b.tamanho - a.tamanho || b.chars - a.chars).slice(0, 12),
      botoes: Object.values(botoes).slice(0, 3), imagens: imgs.slice(0, 14),
      cards: Object.values(cards).sort((a, b) => b.qtde - a.qtde).slice(0, 3) });
  });
  return { secoes: out, altura: document.body.scrollHeight };
}"""


async def medir(pg, url, largura):
    await pg.set_viewport_size({'width': largura, 'height': 900})
    await pg.goto(url, wait_until='domcontentloaded', timeout=45000)
    await pg.wait_for_timeout(1500)
    await pg.evaluate("""async () => { for (let y = 0; y < document.body.scrollHeight; y += 500) {
        window.scrollTo(0, y); await new Promise(r => setTimeout(r, 70)); } window.scrollTo(0, 0); }""")
    await pg.add_style_tag(content=CSS_REVELAR)
    await pg.wait_for_timeout(900)
    return await pg.evaluate(JS)


def linha_texto(t):
    extra = []
    if t['caixa'] != 'none':
        extra.append(t['caixa'])
    if t['italico']:
        extra.append('itálico')
    if t['espacamento'] not in ('normal', '0px'):
        extra.append('ls ' + t['espacamento'])
    return f"| {t['tamanho']}px | {t['peso']} | {t['fonte']} | {t['lh']} | {t['cor']} | {' '.join(extra)} | {t['tag']} | {t['exemplo']} |"


def gerar_md(nome, d, m, rel='../..'):
    L = [f'# Raio-x de molde: {nome}', '',
         '**Propósito:** medidas exatas, seção por seção, para reproduzir esta página como molde (trocar copy, cores e imagens, manter tamanhos, pesos, componentes e ritmo).',
         '**Quando usar:** no passo 4 da SKILL (modo molde). Abra junto as imagens `secao-NN.jpg` desta pasta.',
         f'**Relacionados:** [MEDIDAS-REAIS.md](<{rel}/MEDIDAS-REAIS.md>), [ANTI-SLOP.md](<{rel}/ANTI-SLOP.md>)', '',
         f"Altura total: {d['altura']}px no desktop (1440) e {m['altura']}px no mobile (390). Mobile inteiro em `pagina-mobile.jpg`.", '']
    mob = {s['indice']: s for s in m['secoes']}
    for n, s in enumerate(d['secoes'], 1):
        L += [f"## Seção {n:02d} · `secao-{n:02d}.jpg`", '',
              f"- Altura {s['altura']}px · fundo `{s['fundo']}`",
              f"- Padding `{s['padding']}`" + (f" · interno `{s['padding_interno']}`" if s['padding_interno'] else '') +
              (f" · conteúdo {s['largura_conteudo']}px" if s['largura_conteudo'] else '') + f" · direção {s['direcao']} · gap {s['gap']}"]
        sm = mob.get(s['indice'])
        if sm:
            L.append(f"- Mobile: altura {sm['altura']}px · padding `{sm['padding']}`" + (f" · interno `{sm['padding_interno']}`" if sm['padding_interno'] else ''))
        if s['textos']:
            L += ['', '| Tamanho | Peso | Fonte | Line-height | Cor | Extra | Tag | Exemplo |', '|---|---|---|---|---|---|---|---|']
            L += [linha_texto(t) for t in s['textos']]
            if sm and sm['textos']:
                L += ['', 'Mobile (tamanho → exemplo): ' + ' · '.join(f"{t['tamanho']}px/{t['peso']} \"{t['exemplo'][:28]}\"" for t in sm['textos'][:6])]
        for b in s['botoes']:
            L.append(f"- **Botão** \"{b['texto']}\": {b['tamanho']}px/{b['peso']} {b['fonte']}, caixa {b['caixa']}, padding `{b['padding']}`, raio `{b['raio']}`, "
                     f"altura {b['altura']}px, largura {b['largura']}px, fundo `{b['fundo']}`, texto `{b['cor']}`" +
                     (f", borda `{b['borda']}`" if b['borda'] else '') + (f", sombra `{b['sombra']}`" if b['sombra'] else '') +
                     (', com ícone' if b['tem_icone'] else ', sem ícone'))
        for c in s['cards']:
            L.append(f"- **Card** (x{c['qtde']}): {c['largura']}x{c['altura']}px, raio `{c['raio']}`, fundo `{c['fundo']}`, padding `{c['padding']}`" +
                     (f", borda `{c['borda']}`" if c['borda'] else '') + (f", sombra `{c['sombra']}`" if c['sombra'] else ''))
        if s['imagens']:
            L += ['', '| Slot | Tipo | Tamanho na tela | Proporção | Raio | Encaixe | Arquivo original |', '|---|---|---|---|---|---|---|']
            for k, im in enumerate(s['imagens'], 1):
                L.append(f"| S{n:02d}-{k} | {im['tipo']} | {im['largura']}x{im['altura']} | {im['proporcao']} | {im['raio']} | {im['encaixe']} | {im['arquivo']} |")
        L.append('')
    return '\n'.join(L)


async def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    alvo = sys.argv[1]
    if os.path.isfile(alvo):
        html, nome = os.path.abspath(alvo), os.path.basename(os.path.dirname(os.path.abspath(alvo)))
        saida = sys.argv[2] if len(sys.argv) > 2 else os.path.join(os.path.dirname(html), 'raio-x')
    else:
        html = os.path.join(NOSSAS, alvo, 'extraido', 'index.html')
        nome = alvo
        saida = sys.argv[2] if len(sys.argv) > 2 else os.path.join(NOSSAS, alvo, 'raio-x')
    os.makedirs(saida, exist_ok=True)
    url = 'file://' + html
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path=chrome())
        pg = await b.new_page()
        d = await medir(pg, url, 1440)
        shot = Image.open(BytesIO(await pg.screenshot(full_page=True))).convert('RGB')
        for n, s in enumerate(d['secoes'], 1):
            if s['altura'] < 10:
                continue
            corte = shot.crop((0, s['topo'], shot.width, min(shot.height, s['topo'] + s['altura'])))
            corte = corte.resize((900, max(1, int(corte.height * 900 / corte.width))))
            corte.save(os.path.join(saida, f'secao-{n:02d}.jpg'), quality=72)
        m = await medir(pg, url, 390)
        mob = Image.open(BytesIO(await pg.screenshot(full_page=True))).convert('RGB')
        mob.thumbnail((390, 20000))
        mob.save(os.path.join(saida, 'pagina-mobile.jpg'), quality=65)
        await b.close()
    json.dump({'pagina': nome, 'desktop': d, 'mobile': m}, open(os.path.join(saida, 'raio-x.json'), 'w'), ensure_ascii=False, indent=1)
    # Travessão vindo de página antiga fica marcado, para a IA não copiar (regra da casa).
    md = gerar_md(nome, d, m, os.path.relpath(DESIGN, saida)).replace('\u2014', '[travessão]').replace('\u2013', '[travessão]')
    open(os.path.join(saida, 'raio-x.md'), 'w').write(md)
    print(f"{nome}: {len(d['secoes'])} seções -> {saida}")


asyncio.run(main())
