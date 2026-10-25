# Padrões recorrentes nos JSONs da casa

**Propósito:** configurações do Elementor que se repetem nos 25 JSONs de página (2.678 elementos), medidas por script: larguras, paddings, gaps, fontes, cores, breakpoints, classes e CSS customizado.
**Quando usar:** ao montar uma página no Elementor ou ao gerar JSON, para usar os mesmos valores que a casa usa.
**Relacionados:** [anatomia-json-elementor.md](anatomia-json-elementor.md), [PADRAO-DAVI.md](<../design/PADRAO-DAVI.md>), [regras-html-convertivel.md](regras-html-convertivel.md), [indice.json](indice.json)

Os números são contagens de elementos (não de páginas), salvo indicação. "x" significa quantas vezes o valor aparece.

## Layout

| Item | Padrão | Contagem |
|---|---|---|
| Formato | containers flexbox, `version 0.4` | 100% |
| Container de topo | `boxed` | 225 de 231 |
| Container interno | `content_width: full` | 661 de 735 |
| `boxed_width` | 1240px (28x), 1140px (23x), 1180 (8x), 1220 (6x) | |
| Padding da seção (topo/base) | **80/80px** (65x), 50/50 (36x), 0/0 (29x, heros e faixas) | 231 seções |
| Altura mínima do hero | **800px** (24x), 700 (12x), 750 (5x) | |
| `flex_gap` | **20px** (87x), 30 (42x), 24 (41x), 10 (40x), 16 (21x) | |
| Direção | coluna 694x, linha 262x, `row-reverse` 10x (alternar foto e texto) | |
| Raio de container | **12px** (93x), 8px (61x), 9px, 999px (pílula), 6, 10, 16, 22px | |

## Tipografia

| Item | Padrão |
|---|---|
| Famílias | **Inter** (566 usos), Poppins (283), Sora (220), Karla, Montserrat, Fraunces, DM Sans, Georgia, Anton, Playfair Display |
| Unidade no desktop | **px** (1.445 de 1.445) |
| Unidade no mobile | **vw** (995 de 1.030). É a assinatura da casa: o título encolhe proporcionalmente à tela. |
| Título de seção no mobile | 4 a 7,2vw (em 390px: 16 a 28px). Hero: 5,2 a 7,2vw |
| Texto corrido no desktop | **17px** (89x), 15 e 16px |
| Texto corrido no mobile | **3,5 a 4,4vw** (em 390px: 14 a 17px) |
| Altura de linha do título | **1.4em** (283x) e 1.3em (236x) |
| Peso do título | 400 (185x), 500 (161x), 300 (149x), 600 (130x). Títulos finos (300) são comuns. |
| Tag do título | **h2 por padrão** (o campo nem aparece), `div` em 125 headings usados como texto, h3 em 29, **h1 só em 5** |
| Destaque dentro do título | `<b>`, `<strong>` ou `<span style="color:...">` no próprio `title` |

## Botões

| Item | Padrão |
|---|---|
| Padding | 18px 42px (13x), 18px 38px (12x), 15px 30px (12x), 24px 52px (9x) |
| Raio | 12px (18x), 6px (18x), 8px (14x), 42px (12x), pílula de 100 a 999px (cerca de 45x) |
| Fundo | cor sólida (113x) ou **gradiente** (30x) |
| Hover | `hover_animation: grow` (**109 botões**), mais cor de hover |
| Ícone | `selected_icon` com WhatsApp (fa-brands) ou SVG enviado, à direita |

## Cores mais usadas nos settings

`#FFFFFF` (971x), `#000000` (234x) e depois as cores de marca de cada cliente: `#29476D` (Maria Rita), `#3F3638`, `#4B3325` (The Palace), `#940C0C` (Goncont), `#4B0F55` (Cecília), `#2A2540` (Rosangela), `#4A4A4A` (texto do Renan), `#001D4C` (Pedro), `#F5811E` (Scripts), `#B78241` (Mentoria Jéssica).

**Sem cores globais:** 0 usos de `__globals__`. Cada widget tem a cor fixa.

## Breakpoints e responsividade

- Breakpoints do Elementor: **tablet até 1024px, mobile até 767px**.
- **4.593 settings `_mobile` contra 1.138 `_tablet`**: o ajuste é feito no mobile; o tablet costuma herdar.
- Mais ajustados no mobile: tamanho de fonte (em vw), altura de linha, padding, `flex_direction` (linha vira coluna), largura dos containers internos (100%), alinhamento.
- `hide_desktop` / `hide_mobile` (32 e 29 elementos) para ter blocos exclusivos de cada dispositivo (por exemplo, foto do hero diferente no mobile).
- `background_image_mobile` para trocar a imagem de fundo do hero no celular.

## Classes CSS customizadas

| Classe | Usos | Função |
|---|---|---|
| `scroll-bottom` | **477** | animação de entrada (sobe) |
| `scroll-right` / `scroll-left` | 72 / 70 | animação de entrada lateral |
| `botao` | 23 | estilo de botão definido no CSS da página |
| `gradient-border`, `borda-animada` | 10 / 10 | card com borda degradê ou animada |
| `bot` | 9 | botão com borda de luz girando |
| `card1`, `card-pulse` | 8 / 6 | variações de card |
| `container-botao`, `container-html` | 6 / 6 | wrappers |
| `textoAnimado` | 5 | texto palavra por palavra (GSAP) |
| `carrossel` | 5 | faixa infinita (icon-list) |
| `hover-list` | 5 | cards que abrem no hover |

## CSS personalizado (Elementor Pro)

- **296 elementos** com `custom_css`. Por tipo: button 78, container 71, heading 68, html 42, icon-list 22, image 16, text-editor 10, image-carousel 9, toggle 6.
- **22 de 25 páginas** têm o CSS base da casa em `page_settings.custom_css` (seleção, `overflow-x: hidden`, `p:last-of-type`, scrollbar).
- Usos típicos no widget: `selector{ position: absolute; }` em decorações, tamanho do SVG do botão, brilho passando, borda degradê com `mask-composite`, carrossel linear. Todos estão em [codigos](<../codigos/GUIA-CODIGOS.md>).

## Widgets mais usados

heading 687 · text-editor 182 · icon-box 149 · button 143 · image 132 · icon-list 114 · html 59 · icon 56 · divider 37 · video 33 · image-carousel 25 · toggle 20 · spacer 15 · google_maps 7.

Leitura: a casa monta quase tudo com **heading + text-editor + icon-box + button + image + icon-list** dentro de containers. Widgets HTML (59) entram para o que o Elementor não faz bem: menus, rodapés, timelines, gráficos, scripts.

## Ruído de addons

`ha_cmc_text` em todos os elementos (Happy Addons) e chaves `eae_*` em 966. Não afetam a importação. Os [templates/](templates/) vêm limpos.
