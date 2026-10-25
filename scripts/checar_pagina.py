"""PageBrain · Checagem das regras fixas numa página gerada.

Confere, no Chrome, as regras fixas do PageBrain (24/10/2026) (ver SKILL.md, "Regras fixas do PageBrain"):

  1. Títulos (h1 e h2) com no máximo 3 linhas; 4 só quando a frase é longa (mais de 70 caracteres).
     Nunca mais de 4. Nenhum título acima de 55px.
  2. Sem menu de navegação (a não ser que o usuário tenha pedido: use --com-menu).
  3. Logo na hero, acima do H1 (a não ser que o usuário tenha pedido outro lugar: use --logo-livre).
  4. No celular (390x664), o primeiro botão da hero aparece sem rolar.
  5. Sem rolagem horizontal em 1440px e 390px.
  6. Ícones em SVG inline (vindos do icone.sh / better-icons), nada de emoji como ícone.

Uso:
  python3 checar_pagina.py caminho/index.html [--com-menu] [--logo-livre] [--prints pasta]

Sai com código 1 se houver ERRO. AVISO não bloqueia, mas precisa de motivo.
Requisitos: Python 3.9+ e playwright (usa o Google Chrome instalado ou o Chromium do Playwright).
"""
import asyncio
import os
import sys

from playwright.async_api import async_playwright

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _navegador import chrome  # noqa: E402

# Mostra tudo que o scroll reveal esconde (classes da casa e da página de referência).
CSS_REVELAR = """*{animation-play-state:paused!important;transition:none!important}
.scroll-bottom,.scroll-left,.scroll-right,.scroll-top,.rv,[class*=reveal]{opacity:1!important;transform:none!important;filter:none!important;visibility:visible!important}"""

JS = r"""() => {
  const vis = e => { const r = e.getBoundingClientRect(), c = getComputedStyle(e);
    return r.width > 0 && r.height > 0 && c.display !== 'none' && c.visibility !== 'hidden'; };
  const top = e => e.getBoundingClientRect().top + scrollY;
  const titulos = [...document.querySelectorAll('h1, h2')].filter(vis).map(e => {
    const c = getComputedStyle(e), fs = parseFloat(c.fontSize);
    let lh = parseFloat(c.lineHeight); if (isNaN(lh)) lh = fs * 1.2;
    const texto = e.innerText.replace(/\s+/g, ' ').trim();
    return { tag: e.tagName.toLowerCase(), texto, chars: texto.length, fs: Math.round(fs),
             linhas: Math.round(e.getBoundingClientRect().height / lh) };
  });
  const h1 = document.querySelector('h1');
  const hero = h1 ? (h1.closest('header, section') || document.body) : null;
  // menu: nav (fora do rodapé) ou bloco no topo com 3+ links internos
  const navs = [...document.querySelectorAll('nav')].filter(n => vis(n) && !n.closest('footer'));
  const linksTopo = [...document.querySelectorAll('a[href^="#"]')].filter(a => vis(a) && top(a) < 160 && !a.classList.contains('btn'));
  const temMenu = navs.length > 0 || linksTopo.length >= 3;
  // logo: img/svg com "logo" no src, alt, classe ou id, dentro da hero e acima do h1
  const logos = hero ? [...hero.querySelectorAll('img, svg')].filter(e => vis(e) &&
      /logo|marca/i.test([e.getAttribute('src'), e.getAttribute('alt'), e.getAttribute('class'), e.id].join(' '))) : [];
  const logoAcima = !!(h1 && logos.some(l => l.getBoundingClientRect().bottom <= h1.getBoundingClientRect().top + 2));
  // primeiro botão da hero
  const btn = hero ? [...hero.querySelectorAll('a, button')].find(a => vis(a) &&
      (/btn|botao|button|cta/i.test(a.className) || /wa\.me|whatsapp/i.test(a.getAttribute('href') || ''))) : null;
  const btnBase = btn ? Math.round(btn.getBoundingClientRect().bottom + scrollY) : null;
  // ícones: emoji usado como ícone em cards, títulos e listas
  // ™ ® © também são Extended_Pictographic, mas são texto de marca, não ícone: saem da checagem
  const emoji = /\p{Extended_Pictographic}/u;
  const semMarcas = t => (t || '').replace(/[™®©]️?/g, '');
  const comEmoji = [...document.querySelectorAll('h2, h3, h4, li, [class*=card] span, [class*=icon], [class*=ic]')]
      .filter(e => vis(e) && emoji.test(semMarcas(e.innerText))).map(e => (e.innerText || '').trim().slice(0, 40));
  const svgs = document.querySelectorAll('svg').length;
  return { titulos, temMenu, nNavs: navs.length, nLinksTopo: linksTopo.length, nLogos: logos.length, logoAcima,
           btnTexto: btn ? btn.innerText.trim().slice(0, 40) : null, btnBase,
           larguraDoc: document.documentElement.scrollWidth, larguraTela: innerWidth,
           comEmoji: [...new Set(comEmoji)].slice(0, 6), svgs };
}"""


async def medir(browser, url, w, h, prints, nome):
    pg = await browser.new_page(viewport={'width': w, 'height': h})
    await pg.goto(url, wait_until='load')
    await pg.add_style_tag(content=CSS_REVELAR)
    await pg.wait_for_timeout(600)
    dados = await pg.evaluate(JS)
    if prints:
        await pg.screenshot(path=os.path.join(prints, f'{nome}-primeira-tela.png'))
    await pg.close()
    return dados


async def main():
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    if not args:
        print(__doc__); sys.exit(2)
    com_menu = '--com-menu' in sys.argv
    logo_livre = '--logo-livre' in sys.argv
    prints = None
    if '--prints' in sys.argv:
        prints = sys.argv[sys.argv.index('--prints') + 1]
        args = [a for a in args if a != prints]
        os.makedirs(prints, exist_ok=True)
    url = 'file://' + os.path.abspath(args[0])

    async with async_playwright() as p:
        browser = await p.chromium.launch(executable_path=chrome())
        desk = await medir(browser, url, 1440, 900, prints, 'desktop')
        mob = await medir(browser, url, 390, 664, prints, 'mobile')
        await browser.close()

    erros, avisos = [], []
    for tela, d in (('1440px', desk), ('390px', mob)):
        for t in d['titulos']:
            rot = f'{t["tag"]} "{t["texto"][:60]}" ({tela}, {t["fs"]}px, {t["linhas"]} linhas)'
            if t['fs'] > 55:
                erros.append(f'Título acima de 55px: {rot}')
            if t['linhas'] > 4:
                erros.append(f'Título com mais de 4 linhas: {rot}. Diminua a fonte ou alargue a coluna.')
            elif t['linhas'] == 4 and t['chars'] <= 70:
                avisos.append(f'Título curto quebrando em 4 linhas: {rot}. Deveria caber em 3.')
        if d['larguraDoc'] > d['larguraTela'] + 1:
            erros.append(f'Rolagem horizontal em {tela}: documento com {d["larguraDoc"]}px.')

    if desk['temMenu'] and not com_menu:
        erros.append(f'Página com menu ({desk["nNavs"]} nav, {desk["nLinksTopo"]} links no topo). '
                     'Só entra menu se o usuário pedir (rode com --com-menu se ele pediu).')
    if not logo_livre:
        if desk['nLogos'] == 0:
            erros.append('Hero sem logo (img/svg com "logo" no src, alt ou classe).')
        elif not desk['logoAcima']:
            erros.append('A logo da hero não está acima do H1.')
    if mob['btnBase'] is None:
        erros.append('Não achei o botão da hero (classe btn/botao/cta ou link de WhatsApp).')
    elif mob['btnBase'] > 664:
        erros.append(f'No celular (390x664) o botão "{mob["btnTexto"]}" termina em {mob["btnBase"]}px: '
                     'precisa aparecer sem rolar.')
    if desk['comEmoji']:
        erros.append('Emoji usado como ícone: ' + ' | '.join(desk['comEmoji']) + '. Use ./icone.sh (better-icons).')

    print(f'Página: {args[0]}')
    print(f'Títulos medidos: {len(desk["titulos"])} · SVGs inline: {desk["svgs"]} · '
          f'botão da hero no celular termina em {mob["btnBase"]}px de 664')
    for e in erros:
        print('ERRO  ', e)
    for a in avisos:
        print('AVISO ', a)
    if not erros and not avisos:
        print('OK: todas as regras fixas passaram.')
    sys.exit(1 if erros else 0)


if __name__ == '__main__':
    asyncio.run(main())
