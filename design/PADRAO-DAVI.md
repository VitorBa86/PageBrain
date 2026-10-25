# PageBrain · Padrão Davi: como a casa constrói landing pages

**Propósito:** o que se repete em todas as páginas da casa (Davi / Zarion / O Rei da Landing): estrutura, design system, tipografia, botões, espaçamentos, animações, imagens, responsividade, código, scripts, tracking e otimizações. **É o documento mais importante do acervo.**
**Quando usar:** antes de desenhar ou montar qualquer página nova, e como critério de desempate quando duas referências discordarem (o padrão da casa vence).
**Relacionados:** [MEDIDAS-REAIS.md](MEDIDAS-REAIS.md), [ANTI-SLOP.md](ANTI-SLOP.md), [design-system-davi.html](design-system-davi.html), [CATALOGO.md](../paginas/nossas/CATALOGO.md), [copy/metodo-de-copy.md](<../copy/metodo-de-copy.md>), [codigos/GUIA-CODIGOS.md](<../codigos/GUIA-CODIGOS.md>), [elementor/padroes-recorrentes.md](<../elementor/padroes-recorrentes.md>), [elementor/regras-html-convertivel.md](<../elementor/regras-html-convertivel.md>)

## Base de evidência

- **37 páginas publicadas** (pasta `paginas/nossas`), medidas no Chrome headless a 1440px e 390px (estilos computados reais): ver `ficha.json` de cada uma.
- **25 JSONs de página inteira** do Elementor (`elementor`, 2.678 elementos) e **37 JSONs de seção**.
- **CSS customizado** isolado pelos marcadores `/* Start custom CSS */` do Elementor Pro em cada página.
- Os números entre parênteses dizem em quantas páginas o padrão aparece. Onde é leitura minha e não medição, está marcado `(inferido)`.

## 1. Plataforma e construção

| Item | Padrão | Evidência |
|---|---|---|
| CMS | WordPress + **Elementor Pro** | 37/37 |
| Layout | **Containers flexbox** (Elementor v0.4). Nunca section/column. | 100% dos 62 JSONs |
| Domínio | `lp.oreidalanding.com.br/<slug-do-cliente>/` (24 páginas) ou domínio do cliente | `captura.json` |
| Addons | Happy Addons (25), JetEngine em sites com catálogo (2) | bibliotecas detectadas |
| Globais do kit | **Não usa** cores nem fontes globais. Tudo é definido em cada widget. O kit (`post-5.css`) continua com o padrão do Elementor (#6EC1E4, Roboto). | 0 `__globals__` nos 25 JSONs |
| Widget de texto | **`heading` para quase tudo**: 687 headings contra 182 text-editors. Parágrafos também viram heading. | JSONs |
| Tag do título | Quase sempre **h2**, inclusive no hero. 29 de 37 páginas não têm `<h1>`. | HTML publicado |

**Regra para páginas novas:** manter containers flexbox e o widget heading, mas usar **um `<h1>` no hero** e `p` (text-editor) nos parágrafos longos. A ausência de h1 é um problema de SEO, não um padrão a copiar (inferido).

## 2. Estrutura de página

> **Regras fixas do PageBrain (24/10/2026), por cima de tudo abaixo:** página **sem menu** (só se o usuário pedir), **logo na hero acima da headline**, títulos em **até 3 linhas** (4 se a frase for longa, teto 55px), **ícones da skill better-icons** e **hero com foto de fundo e fade**. Referência viva: [psi-luana-carolina-casais](../paginas/nossas/psi-luana-carolina-casais/como-usar.md). Detalhes no [SKILL.md](../SKILL.md).

Ordem e frequência detalhadas em [estrutura-de-pagina.md](<../copy/estrutura-de-pagina.md>). Em resumo:

- **Captação:** hero, (barra de números ou faixa), dor/para quem é, serviços, sobre, como funciona, prova social, FAQ, CTA final, localização, rodapé. Média de **8 a 9 seções**, página entre **4.000 e 10.000px** de altura no desktop.
- **Vendas:** hero, faixa, dor, solução, para quem é, conteúdo, bônus, prova, oferta, garantia, sobre, FAQ. Média de 10 a 11 seções.
- **CTA em toda dobra**, sempre o mesmo texto ou uma variação muito próxima.
- **Botão flutuante de WhatsApp** (Lottie fixo ou ícone no header HTML).
- **Rodapé curto:** "Todos os direitos reservados © ANO" + "Termos de uso Ι Política de Privacidade" (aparece em 18 páginas). Em páginas mais novas, rodapé completo em widget HTML (Vega, Inter Frios, Maria Rita, Rosangela, Santa Boemia).

## 3. Grid e espaçamento

| Token | Valor padrão | Evidência |
|---|---|---|
| Largura do conteúdo | **1140px** (26 de 37 páginas medidas); 1240px é a segunda opção | estilos computados + `boxed_width` nos JSONs (1240 em 28 containers, 1140 em 23) |
| Container de topo | `content_width: boxed` (225 de 231) | JSONs |
| Padding vertical das seções | **80px topo / 80px base** (65 containers); 50/50 (36); hero e faixas com 0 | JSONs |
| Altura do hero | **min-height 800px** no desktop (24 heros); 700 e 750 também aparecem. Mediana medida: 800px | JSONs + medição |
| Gap padrão | **20px** (87 containers e 36 de 37 páginas), depois 30, 24, 10 e 16px | JSONs + medição |
| Espaço entre widgets | 20px (padrão do Elementor mantido) | kit |
| Direção | coluna (694) e linha (262); `row-reverse` para alternar foto e texto (10) | JSONs |

Layout típico de dobra: **duas colunas (texto + imagem)** no desktop, empilhadas no mobile; grids de cards em 3 colunas (2x3 ou 3x2) ou 4 colunas.

## 4. Cores

Não há uma paleta única: **cada cliente recebe uma paleta própria**. O que se repete é a **estrutura** da paleta:

1. **Uma cor de marca escura** para seções de impacto, hero e cards (navy, verde-escuro, petróleo, roxo, bordô, preto). 17 de 37 páginas têm o fundo dominante escuro.
2. **Um neutro claro quente** para as seções de leitura (off-white, creme, bege: `#FAF8F5`, `#F5F0E1`, `#FFF5E8`, `#F2F2F2`).
3. **Um acento** para CTA e palavras destacadas (dourado, laranja, amarelo, verde WhatsApp, lilás).
4. **Alternância de fundo** entre seções (claro, escuro, claro) para marcar o ritmo. Ver a faixa "Estrutura e ritmo de cores" em cada `style-guide.html`.
5. **Gradientes** em 21 dos 37 botões principais e em faixas e heros (`linear-gradient` de duas tonalidades da mesma cor).

Paletas por nicho observadas (inferido a partir das 37):

| Nicho | Paletas usadas |
|---|---|
| Advocacia | navy + dourado (Calgarotto, Luisa), verde-escuro (Barros), preto + vermelho (Souza Santos), azul-violeta + dourado (Gustavo) |
| Psicologia | bege e taupe (Andressa), creme e café (Julia), off-white e petróleo (Renan), roxo e lavanda (Rosangela), creme e terracota (Vivian), petróleo e bege (Maria Rita) |
| Saúde | roxo uva e rosé (Cecília), grafite e creme (Luciano), navy e branco (Pedro) |
| Odonto | bege e dourado (Invisalign), rosa (Rubiane) |
| Imobiliário | verde-escuro + laranja (Vega), navy + mostarda (Vitta), bege + dourado (The Palace), preto e branco (MB2) |
| Vendas | **fundo preto** com um acento quente (laranja, bronze, vermelho) ou azul royal; 6 de 6 escuras |

## 5. Tipografia

| Item | Padrão | Evidência |
|---|---|---|
| Fonte de texto | **Inter** (principal em 15 páginas, presente em 16; 566 usos nos JSONs), depois Poppins (7) e Sora (12 páginas, 220 usos) | medição + JSONs |
| Fonte de título com personalidade | **serifa** para psi, saúde, alto padrão (Fraunces, Playfair Display, Georgia, Gelasio, Roboto Serif, Antic Didone, Crimson Text); **condensada** para eventos e vendas agressivas (Anton, Oswald) | fichas |
| Pares mais comuns | Inter + serifa (Renan, Pedro, Vega), Poppins sozinha, Sora + Inter | fichas |
| Linhas por título | **Regra fixa:** todo H1 e H2 cabe em **até 3 linhas** na largura da coluna, no desktop e no mobile; 4 só se a frase passar de 70 caracteres. Teto de 55px. Conferir com `scripts/checar_pagina.py` | regra do usuário, 24/10/2026 |
| Escala desktop | hero **40px** de mediana (33 a 45); H2 de seção **36 a 42px** (30 a 46); título de card 20 a 22px; corpo **16 a 18px**. Medido por papel em 21/10/2026, ver [MEDIDAS-REAIS.md](MEDIDAS-REAIS.md) | `medir_papeis.py` |
| Escala mobile | hero **27px** (25 a 29); H2 de seção **25px** (22 a 28); corpo 16px | `medir_papeis.py` |
| Destaque de palavra | span ou strong dentro do título com **cor de acento, itálico ou marca-texto** (25 páginas). Variações: marca-texto amarelo (Santa Boemia), itálico serifado (Renan, Rosangela, Carol), cor (Vega, Inter Frios, Luiz Gustavo), gradiente animado (Harmony) | HTML |
| Rótulo acima do H2 | texto pequeno em caixa alta e espaçado ("SERVIÇOS", "COMO FUNCIONA") nas páginas mais novas | fichas |

## 6. Botões

| Item | Padrão |
|---|---|
| Texto | Verbo + ação, em geral sem caixa alta (30 de 37); páginas de vendas em CAIXA ALTA |
| Tamanho | **16 a 20px, peso 500** (o mais comum é 18px/500); altura de ~58px |
| Padding | entre **18px 30px e 20px 50px** |
| Raio | duas famílias: **pequeno (4 a 14px)** em advocacia, B2B e vendas; **pílula (40px a 999px)** em psi, saúde e imobiliário |
| Fundo | **gradiente** da cor de marca ou do acento (21 de 37); botão verde de WhatsApp quando a paleta permite |
| Ícone | ícone de WhatsApp ou seta **solto** à direita (nunca dentro de um quadradinho) (23 páginas com ícone no botão; o tamanho do SVG é ajustado com [botao-icone-tamanho.css](<../codigos/utilitarios-css/botao-icone-tamanho.css>)) |
| Efeitos | brilho passando ([botao-brilho-passando.css](<../codigos/botoes/botao-brilho-passando.css>)), borda de luz girando ([botao-borda-girando-conic.css](<../codigos/botoes/botao-borda-girando-conic.css>)), hover com leve subida |
| Link | `https://wa.me/55DDDNUMERO?text=` + mensagem codificada (19 páginas) |

## 7. Cards, bordas e sombras

- **Raios mais usados:** 8px (19 páginas), 12px (18), 6px (10), 22px (7) e pílula 999px (5).
- **Sombras:** suaves e difusas, com opacidade de 0,06 a 0,28 e blur de 10 a 46px. Exemplo típico: `rgba(31,78,95,0.06) 0 12px 40px` (Renan) ou `rgba(0,0,0,0.12) 8px 10px 46px` (sombra deslocada para a direita e para baixo, comum na casa).
- **Card padrão:** fundo branco ou cor de marca, raio de 8 a 14px, padding de 24 a 32px, ícone em quadrado colorido no topo, título curto e texto de 2 linhas.
- **Card premium:** borda de 1px em degradê ([card-borda-degrade.css](<../codigos/cards-e-bordas/card-borda-degrade.css>), 5 páginas), vidro fosco (11 páginas), faixa luminosa no topo.
- **Grid de cards dentro de um container claro arredondado** que sobe sobre o hero (Goncont, Cecília). Recurso recorrente nas páginas mais novas (inferido).

## 8. Animações e movimento

| Recurso | Uso |
|---|---|
| **Scroll reveal da casa** (`scroll-bottom`, `scroll-left`, `scroll-right`, `scroll-top` + script) | **37 de 37 páginas**; `scroll-bottom` em 477 elementos dos JSONs. Variação com blur em 12 páginas. [animacao-scroll-reveal.html](<../codigos/animacoes/animacao-scroll-reveal.html>) |
| Animações de entrada do Elementor | quase não usa (fadeIn em 36 elementos de 2.678) |
| Scroll suave Lenis | 26 páginas (script incluído por plugin ou widget) |
| Faixa infinita (marquee) | 5 páginas com o padrão icon-list + script, mais as faixas de checks |
| Carrossel linear contínuo | 7 páginas |
| GSAP | 2 páginas (Vivian, Maria Rita) para efeitos avançados |
| Hover | escala 1,05 em cards (6 páginas), brilho em botões |

## 9. Imagens

- **Padrão do PageBrain desde 24/10/2026: hero com foto de fundo e fade.** No desktop, a foto ocupa a hero inteira com a pessoa à direita e um fade da cor de fundo cobrindo a esquerda, onde ficam logo, rótulo, título, texto e botão. No mobile, entra um recorte da mesma foto centralizado na pessoa, no topo, com o corpo nítido acima da logo, o fade começando logo acima da logo e o botão visível sem rolar. Código: [hero-foto-de-fundo-fade.html](<../codigos/fundos-e-texturas/hero-foto-de-fundo-fade.html>). Referência: [psi-luana-carolina-casais](../paginas/nossas/psi-luana-carolina-casais/como-usar.md).
- Nas páginas antigas da casa, o dominante era **foto real do profissional recortada (PNG sem fundo)** no hero, à direita, sobre fundo de cor ou foto escurecida (advocacia, saúde e psi). Use só se o usuário pedir.
- **Ícones:** sempre da skill better-icons (`scripts/icone.sh`, coleção lucide), SVG inline, mesmo estilo na página toda. Nunca emoji, nunca desenhado à mão.
- Fotos em **WebP**, com tamanhos responsivos do WordPress (`-300x`, `-768x`, `-1024x`).
- **Fundo do hero** com foto + overlay da cor da marca, ou cor sólida com formas decorativas.
- **Mockups** (notebook, celular, tablet) em páginas de vendas e de produto digital.
- Prints reais como prova: Google Reviews (widget Trustindex), conversas de WhatsApp, painéis de resultados, notícia do G1.
- Logos e selos circulares ("Desde 2006", "TOP3 Brasil", monograma) sobre a foto.

## 10. Responsividade

- Ajustes **mobile-first por widget**: 4.593 configurações `_mobile` contra 1.138 `_tablet` nos JSONs. O tablet quase sempre herda.
- Breakpoints do Elementor: **1024px** (tablet) e **767px** (mobile). Nos CSS custom aparecem também `max-width: 800px` e `900px`.
- No mobile: colunas empilham, imagem do hero vai para baixo ou para o fundo, título cai para 26 a 35px, botões ficam em largura total (inferido pelos prints mobile do style guide).
- `html, body { overflow-x: hidden; }` em todas as páginas para evitar rolagem lateral causada por decorações.

## 11. Código que entra em toda página

Ver [codigos/GUIA-CODIGOS.md](<../codigos/GUIA-CODIGOS.md>). O kit mínimo:

1. **CSS base** no CSS personalizado da página: `::selection` discreto, `overflow-x: hidden`, `p:last-of-type { margin-bottom: 0 }`, barra de rolagem personalizada (33 páginas). [css-base-toda-pagina.css](<../codigos/utilitarios-css/css-base-toda-pagina.css>)
2. **Scroll reveal** (CSS + script em widget HTML no fim da página).
3. **`position: absolute` em decorações** via CSS personalizado do widget (27 páginas).
4. **Tamanho do ícone do botão** (12 páginas) e **raio do FAQ** (10 páginas).
5. Widgets HTML **autocontidos** e com **prefixo de classe** (`sb-`, `ifm-`, `rb-`, `vega-`) para menus, rodapés, gráficos e timelines, com um comentário no topo explicando como colar e o que trocar.

Mediana de **12 blocos de CSS custom por página** (média 18, de 0 a 117). Classes custom mais usadas nos JSONs: `scroll-bottom`, `scroll-right`, `scroll-left`, `botao`, `gradient-border`, `borda-animada`, `bot`, `card1`, `card-pulse`, `carrossel`.

## 12. Tracking e pixels

| Tag | Páginas |
|---|---|
| Google Analytics 4 | 35 |
| **Meta Pixel** (também via plugin Pixel Cat com Conversions API) | 27 |
| **Google Ads** (AW-) | 26 |
| Google Tag Manager | 3 (domínios próprios de cliente) |

Snippets em [codigos/tracking-e-pixels/](<../codigos/tracking-e-pixels/README.md>).

## 13. Otimizações observadas

- Fotos em WebP com `srcset` do WordPress.
- Lazy load de backgrounds de container (`e-lazyloaded`, nativo do Elementor) em 35 páginas.
- WP Rocket / WP Meteor (scripts com `nowprocket`, `data-wpmeteor`, scripts em base64) em algumas páginas, o que mostra cache e adiamento de JS.
- Fontes carregadas localmente pelo Elementor (Google Fonts locais).
- Pontos fracos a evitar: ausência de h1, jQuery e várias bibliotecas carregadas em toda página, vídeos e placeholders esquecidos (Lorem Ipsum em 3 páginas).

## 14. Checklist do padrão (para a página nova)

- [ ] Página reproduz um molde da casa seção por seção (raio-x do molde aberto) e passa no [ANTI-SLOP.md](ANTI-SLOP.md).
- [ ] Containers flexbox, conteúdo boxed em 1140 ou 1240px, seções com padding 80/80 (ou 50/50).
- [ ] Sem menu (a não ser que o usuário peça); logo na hero acima do H1.
- [ ] Hero com foto de fundo e fade (snippet `hero-foto-de-fundo-fade.html`), H1 com palavra destacada, sub, CTA; no celular, corpo da pessoa acima da logo e botão visível sem rolar.
- [ ] Todo H1 e H2 em até 3 linhas (4 se longo), nenhum acima de 55px.
- [ ] Ícones da skill better-icons (`icone.sh`), SVG inline.
- [ ] `python3 scripts/checar_pagina.py pagina.html` sem ERRO.
- [ ] Paleta: 1 cor de marca escura + 1 neutro claro quente + 1 acento; fundos alternando entre seções.
- [ ] Inter (ou Poppins/Sora) no texto; serifa ou condensada nos títulos quando o nicho pedir; tamanhos do molde ou de [MEDIDAS-REAIS.md](MEDIDAS-REAIS.md).
- [ ] Botões de 18px/500 com gradiente da marca, padding de ~18px 40px, raio coerente com o nicho.
- [ ] Cards com raio de 8 a 14px, sombra suave, ícone no topo.
- [ ] Classe `scroll-bottom` (ou left/right) nos blocos + script do scroll reveal.
- [ ] CSS base da casa no CSS da página.
- [ ] CTA de WhatsApp com mensagem em toda dobra e botão flutuante.
- [ ] Meta Pixel + Google Ads + GA4.
- [ ] Ajustes de mobile em todos os títulos, paddings e colunas.
- [ ] Nenhum Lorem Ipsum ou placeholder publicado.
