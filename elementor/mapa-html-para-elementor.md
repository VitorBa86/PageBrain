# Mapa HTML para Elementor

**Propósito:** tabela de equivalência entre elementos e propriedades HTML/CSS e os widgets e settings do Elementor (containers flexbox), incluindo o que não tem equivalente direto e como resolver.
**Quando usar:** ao montar no Elementor uma página escrita em HTML, ao escrever HTML que vai ser convertido ou ao manter o [conversor](../scripts/html-para-elementor.py).
**Relacionados:** [regras-html-convertivel.md](regras-html-convertivel.md), [anatomia-json-elementor.md](anatomia-json-elementor.md), [scripts/html-para-elementor.py](../scripts/html-para-elementor.py), [codigos](<../codigos/GUIA-CODIGOS.md>)

## Estrutura

| HTML | Elementor | Observação |
|---|---|---|
| `<section>` / `<header>` / `<footer>` de topo | container de topo (`isInner: false`) | uma seção = uma dobra |
| `<div class="wrap" style="max-width:1140px">` dentro da seção | `content_width: boxed` + `boxed_width: 1140` no container de topo | o wrapper some: os filhos sobem para o container de topo |
| seção sem wrapper com max-width | `content_width: full` | |
| `<div>` com filhos de bloco | container interno (`isInner: true`, `content_width: full`) | |
| `display:flex; flex-direction:row` | `flex_direction: row` | |
| `display:flex; flex-direction:column` ou `display:block` | `flex_direction: column` | |
| `display:grid` | container `row` + `flex_wrap: wrap` + largura % nos filhos | grid de verdade não existe no container clássico; ver limitações |
| `gap: 20px` | `flex_gap {column, row, size: 20}` | |
| `justify-content` / `align-items` | `flex_justify_content` / `flex_align_items` | |
| `flex-wrap: wrap` | `flex_wrap: wrap` | |
| `width: 50%` (filho de linha) | `width {unit:'%', size:50}` + `width_mobile 100%` | |
| `min-height: 800px` | `min_height {px 800}` | |
| `id="servicos"` | `_element_id: servicos` | âncora de menu |
| `class="card scroll-bottom"` | `css_classes` (container) ou `_css_classes` (widget): `"card scroll-bottom"` | mantém animações e CSS custom |

## Caixa (box model e fundo)

| CSS | Setting |
|---|---|
| `padding` | `padding {unit px, top, right, bottom, left, isLinked}` |
| `margin` | `margin {...}` (container) / `_margin` (widget) |
| `background-color` | `background_background: classic` + `background_color` |
| `background-image: url()` | `background_background: classic` + `background_image {url}` + `background_size`, `background_position`, `background_repeat` |
| `background-image: linear-gradient(a, b)` | `background_background: gradient` + `background_color`, `background_color_b`, `background_gradient_angle`, `background_color_stop`, `background_color_b_stop` |
| foto + camada de cor por cima | `background_image` + `background_overlay_background` + `background_overlay_color` (+ opacidade) |
| `border: 1px solid #ccc` | `border_border: solid`, `border_width`, `border_color` |
| `border-radius` | `border_radius {top, right, bottom, left}` (container) / `image_border_radius` (imagem) |
| `box-shadow` | `box_shadow_box_shadow_type: yes` + `box_shadow_box_shadow {horizontal, vertical, blur, spread, color}` |
| `@media (max-width: 767px)` | mesma chave com sufixo `_mobile` |
| `@media (max-width: 1024px)` | sufixo `_tablet` |
| `display: none` no mobile | `hide_mobile: hidden-mobile` |

## Texto

| HTML | Widget | Settings principais |
|---|---|---|
| `<h1>`..`<h6>` | `heading` | `title` (HTML inline permitido), `header_size: h1..h6`, `title_color`, `typography_*`, `align` |
| título com palavra destacada (`<em>`, `<span style>`, `<b>`) | `heading` com o HTML inline no `title` | é assim que a casa faz o destaque |
| `<p>`, `<div>` só com texto | `text-editor` | `editor: "<p>...</p>"`, `text_color`, `typography_*`, `paragraph_spacing: 0` |
| rótulo pequeno acima do H2 | `heading` com `header_size: div` (padrão da casa) ou `text-editor` | |
| `font-family` | `typography_font_family` (+ `typography_typography: custom`) | |
| `font-size: 44px` / no mobile `28px` | `typography_font_size {px 44}` / `typography_font_size_mobile {vw 7.2}` | casa usa vw no mobile: `vw = px / 390 * 100` |
| `line-height: 1.15` | `typography_line_height {em 1.15}` | |
| `letter-spacing`, `text-transform`, `font-style: italic`, `font-weight` | `typography_letter_spacing`, `typography_text_transform`, `typography_font_style`, `typography_font_weight` | |
| `text-align: center` | `align: center` (+ `align_mobile`) | |

## Interação e mídia

| HTML | Widget | Observação |
|---|---|---|
| `<a class="btn" href>` / `<button>` | `button` | `text`, `link {url, is_external}`, `background_color` ou gradiente, `button_text_color`, `text_padding`, `border_radius`, `typography_*`, `selected_icon` + `icon_align` |
| `<a>` de texto | `text-editor` com `<a>` dentro | |
| `<img>` | `image` | `image {url, alt}`, `width %`, `image_border_radius` |
| `<ul><li>` simples | `icon-list` | `icon_list: [{text, selected_icon}]`; ícone padrão `fas fa-check` |
| `<ul>` em linha (faixa) | `icon-list` com `view: inline` + snippet de faixa infinita | |
| ícone + título + texto (card) | `icon-box` ou container com `icon` + `heading` + `text-editor` | a casa usa os dois |
| `<details><summary>` em sequência | `toggle` | `tabs: [{tab_title, tab_content}]` |
| `<iframe>` YouTube/Vimeo | `video` | `youtube_url` / `vimeo_url`, `video_type` |
| `<iframe>` Google Maps | `google_maps` | `address`, `height` |
| `<hr>` | `divider` | |
| galeria de imagens em carrossel | `image-carousel` | `carousel: [{url}]`; carrossel contínuo com o snippet de CSS linear |
| espaço vazio | `spacer` | prefira padding/gap |

## O que NÃO tem equivalente direto (e a solução)

| Caso | Solução |
|---|---|
| `<svg>` inline, `<canvas>`, gráficos | widget `html` com o código inteiro |
| `<form>` customizado | widget `html` (formulário próprio, ou envio para WhatsApp) **ou** widget `form` do Elementor Pro montado à mão |
| `<script>` | widget `html` no fim da página (o conversor junta todos os scripts num container final) |
| `@keyframes`, `:hover` complexo, pseudo-elementos `::before/::after` | CSS personalizado da página (`page_settings.custom_css`) ou `custom_css` do elemento com `selector` |
| CSS Grid com áreas (`grid-template-areas`) | reorganizar em linhas e colunas flex; se não der, widget `html` |
| `position: absolute` / `sticky` | `_position: absolute` do Elementor ou `custom_css: selector{position:absolute}` (padrão da casa, 27 páginas) |
| menu com hambúrguer e drawer | widget `html` autocontido ([snippets de menu](<../codigos/menus-e-headers/README.md>)) |
| marquee, timeline com scroll, cartas voando | widget `html` com snippet da biblioteca |
| `<table>` | widget `html` ou reestruturar em containers |
| `<blockquote>` / depoimento | container com `heading` + `text-editor`, ou widget `testimonial` |
| fontes por `<link>` do Google Fonts | selecionar a mesma família no widget (o Elementor carrega sozinho) |
| variáveis CSS (`var(--marca)`) | o conversor lê o valor computado e grava a cor fixa |

## Limitações do conversor (`scripts/html-para-elementor.py`)

Testado em 3 entradas (detalhes no [README](README.md#teste-do-conversor)):

1. **Funciona bem** com HTML limpo que segue [regras-html-convertivel.md](regras-html-convertivel.md): a página de exemplo vira 63 elementos, sem erro e sem nenhuma chave fora do vocabulário da casa.
2. **Não serve para reconverter HTML gerado pelo Elementor** (como os `extraido/index.html`): os wrappers internos viram centenas de containers (807 contra 182 do JSON original do psi-renan). Para páginas da casa use o JSON original.
3. Páginas externas sem as regras convertem, mas com excesso de containers e muitos widgets `html`.
4. Não gera `icon-box`, `image-carousel`, `form` nem `nested-tabs`: monta com containers ou widget `html`.
5. Ícones do botão viram ícone do Font Awesome (WhatsApp ou seta), não o SVG original.
6. Hover, animações e pseudo-elementos não viram settings: continuam valendo pelo CSS copiado para `page_settings.custom_css` e pelas classes preservadas.
7. Imagens ficam com a URL original (`source: url`). Depois de importar, troque pelas imagens da biblioteca de mídia do WordPress.
8. Grid CSS vira linha com quebra; confira as larguras.
9. Sombras múltiplas e gradientes com mais de duas cores não são convertidos (ficam só no CSS).
