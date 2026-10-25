# Anatomia do JSON do Elementor

**Propósito:** explicar, campo a campo, a estrutura dos JSONs de exportação do Elementor usados pela casa, para que uma IA consiga ler, editar e gerar esses arquivos.
**Quando usar:** antes de editar um JSON à mão, de gerar um JSON a partir de HTML ou de depurar uma importação que falhou.
**Relacionados:** [padroes-recorrentes.md](padroes-recorrentes.md), [mapa-html-para-elementor.md](mapa-html-para-elementor.md), [indice.md](indice.md), [templates/](templates/), [scripts/validar-json-elementor.py](../scripts/validar-json-elementor.py)

## Resposta curta: containers ou section/column?

**Só containers (flexbox).** Os 25 JSONs de página e os 37 de seção estão no formato `version: "0.4"` e todos os elementos de layout têm `elType: "container"`. Nenhum usa `section` ou `column`. Gere sempre containers.

## Dois formatos de arquivo

### 1. Exportação de template (os arquivos desta pasta)

```json
{
  "content": [ ...containers de topo... ],
  "page_settings": { "custom_css": "..." },
  "version": "0.4",
  "title": "Renan Psi JSON",
  "type": "page"
}
```

| Chave | O que é |
|---|---|
| `content` | Lista dos **containers de topo**, na ordem da página. Cada um é uma seção/dobra. |
| `page_settings` | Configurações da página. Em 22 dos 25 arquivos tem `custom_css` com o CSS base da casa. Às vezes `background_background` e `background_color` (fundo da página). Pode vir como lista vazia `[]`. |
| `version` | `"0.4"` em todos. |
| `title` | Nome do template no Elementor (ex.: "VEGA E COSTA JSON"). |
| `type` | `"page"` nas páginas inteiras e `"container"` nos JSONs de seção. |

Importação: Elementor > Templates > Importar templates, ou no editor, pasta de templates > Importar.

### 2. Formato "colar de outro site" (área de transferência)

```json
{ "type": "elementor", "siteurl": "https://lp.oreidalanding.com.br/wp-json/", "elements": [ ... ] }
```

É o formato dos snippets `botao1.md`, `faixaanimada.md` e `fundoanimado.md` de `codigos`. Para usar: copie o JSON, clique com o botão direito no editor do Elementor e escolha **Colar de outro site**. Os `elements` têm a mesma estrutura de `content`.

## O elemento (container ou widget)

```json
{
  "id": "5447a09d",
  "elType": "container",
  "isInner": false,
  "settings": { ... },
  "elements": [ ...filhos... ]
}
```

| Chave | Regras |
|---|---|
| `id` | Hexadecimal de 7 ou 8 caracteres (2.347 com 8, 317 com 7, 14 com 6). Precisa ser **único** no documento. Ao gerar, use `'%07x' % random`. |
| `elType` | `"container"` ou `"widget"`. |
| `widgetType` | Só em widgets: `heading`, `text-editor`, `button`, `image`, `icon-box`, `icon-list`, `html`, `icon`, `divider`, `video`, `image-carousel`, `toggle`, `spacer`, `google_maps` etc. (lista completa com contagem em [padroes-recorrentes.md](padroes-recorrentes.md)). |
| `isInner` | `false` no topo; `true` em containers dentro de containers. Widgets usam `false`. |
| `settings` | Só as configurações **diferentes do padrão** do Elementor. Campo ausente = valor padrão. |
| `elements` | Filhos. Widgets têm lista vazia. |

## Settings de container

Exemplo real (hero do psi-renan):

```json
"settings": {
  "flex_direction": "column",
  "boxed_width": {"unit": "px", "size": 1140, "sizes": []},
  "padding": {"unit": "px", "top": "120", "right": "0", "bottom": "96", "left": "0", "isLinked": false},
  "padding_tablet": {"unit": "px", "top": "79", "right": "24", "bottom": "63", "left": "24", "isLinked": false},
  "padding_mobile": {"unit": "%", "top": "79", "right": "4", "bottom": "10", "left": "4", "isLinked": false},
  "background_background": "classic",
  "background_color": "#FAF8F5",
  "background_image": {"url": ".../pt01.webp", "id": 35541, "size": "", "alt": "", "source": "library"},
  "background_image_mobile": {"url": ".../PT01-MB.webp", "id": 35558, ...},
  "background_position": "top center",
  "min_height": {"unit": "px", "size": 800, "sizes": []},
  "min_height_mobile": {"unit": "px", "size": 0, "sizes": []},
  "flex_justify_content": "center",
  "_element_id": "inicio"
}
```

| Chave | Valores |
|---|---|
| `content_width` | `"boxed"` (padrão, com `boxed_width`) ou `"full"`. Containers internos quase sempre `"full"` (661 de 735). |
| `boxed_width` | `{"unit":"px","size":1140}`; aparece 1240, 1140, 1180, 1220. |
| `flex_direction` | `column` (padrão), `row`, `row-reverse`, `column-reverse`. Variantes `_tablet` e `_mobile`. |
| `flex_justify_content`, `flex_align_items` | `flex-start`, `center`, `flex-end`, `space-between`... |
| `flex_gap` | `{"column":"20","row":"20","isLinked":true,"unit":"px","size":20}` |
| `flex_wrap` | `wrap` / `nowrap` |
| `width` | Largura do container interno (`{"unit":"%","size":50}`), com `width_mobile`. |
| `min_height` | Altura mínima (hero: 800px). |
| `padding`, `margin` | Objeto de 4 lados com `unit`, `isLinked`. |
| `background_background` | `classic` (cor/imagem), `gradient`, `video`. Com gradiente: `background_color`, `background_color_b`, `background_gradient_angle`, `background_color_stop`. |
| `background_overlay_*` | Camada sobre a imagem de fundo (cor e opacidade). |
| `border_border`, `border_width`, `border_color`, `border_radius` | Borda e raio. |
| `box_shadow_box_shadow_type` + `box_shadow_box_shadow` | Sombra (`{"horizontal":0,"vertical":12,"blur":40,"spread":0,"color":"rgba(...)"}`). |
| `_element_id` | Âncora (`#inicio`, `#servicos`) usada pelos menus. |
| `_css_classes` | Classes extras de widget (`scroll-bottom`, `card1`...). Em container a chave é `css_classes`, sem o sublinhado. |
| `custom_css` | CSS personalizado do elemento (Elementor Pro). A palavra `selector` aponta para o próprio elemento. |

## Settings de widget (os mais usados)

| Widget | Conteúdo | Estilo |
|---|---|---|
| `heading` | `title` (aceita HTML inline: `<b>`, `<span style>`, `<em>`), `header_size` (`h1`..`h6`, `div`, `p`, `span`; ausente = h2), `link` | `title_color`, `typography_*`, `align` |
| `text-editor` | `editor` (HTML com `<p>`) | `text_color`, `typography_*`, `paragraph_spacing` |
| `button` | `text`, `link {url,is_external,nofollow}`, `selected_icon {value,library}`, `icon_align`, `icon_indent` | `background_color` (ou gradiente com `background_background: gradient`), `button_text_color`, `border_radius`, `text_padding`, `typography_*`, `button_hover_color`, `button_background_hover_color`, `button_hover_border_color`, `hover_animation` (a casa usa `grow` em 109 botões) |
| `image` | `image {url,id,alt,source}`, `image_size`, `link_to` | `width`, `image_border_radius`, `align` |
| `icon-box` | `selected_icon`, `title_text`, `description_text`, `position` | `primary_color`, `title_typography_*`, `description_typography_*` |
| `icon-list` | `icon_list: [{text, selected_icon, _id, link}]`, `view` (`inline` para faixa) | `icon_color`, `text_color`, `icon_size`, `icon_typography_*` |
| `toggle` | `tabs: [{tab_title, tab_content, _id}]` | `title_background`, `tab_active_color`, `border_*` |
| `html` | `html` (HTML+CSS+JS livre) | `custom_css` |
| `video` | `youtube_url` ou `hosted_url`, `video_type` | `aspect_ratio` |
| `google_maps` | `address`, `zoom` | `height` |
| `image-carousel` | `carousel: [{id,url}]`, `slides_to_show`, `autoplay_speed` | `custom_css` com `transition-timing-function: linear` para carrossel contínuo |

### Tipografia

Todas as chaves de tipografia têm um prefixo (vazio, `title_`, `icon_`, `description_`...) e seguem o mesmo molde:

```json
"typography_typography": "custom",
"typography_font_family": "Inter",
"typography_font_family_type": "googlefonts",
"typography_font_size": {"unit": "px", "size": 17, "sizes": []},
"typography_font_size_tablet": {"unit": "px", "size": 16, "sizes": []},
"typography_font_size_mobile": {"unit": "vw", "size": 3.6, "sizes": []},
"typography_font_weight": "400",
"typography_line_height": {"unit": "em", "size": 1.7, "sizes": []},
"typography_letter_spacing": {"unit": "px", "size": 0.16, "sizes": []},
"typography_text_transform": "uppercase",
"typography_font_style": "italic"
```

Sem `typography_typography: "custom"` o Elementor ignora as demais chaves de tipografia.

## Responsividade

- Qualquer setting pode ter variantes com sufixo **`_tablet`** (até 1024px) e **`_mobile`** (até 767px). Também existem `_widescreen` e `_laptop`, raros.
- Nos JSONs da casa: **4.593 ajustes `_mobile` e 1.138 `_tablet`**.
- Ocultar por dispositivo: `hide_desktop: "hidden-desktop"` (32 vezes), `hide_mobile: "hidden-mobile"` (29), `hide_tablet`. A casa usa isso para ter versões diferentes de um bloco no desktop e no mobile.
- Imagem de fundo diferente no mobile: `background_image_mobile`.

## Globais (cores e fontes do kit)

Quando um setting usa uma cor ou fonte global do kit, aparece `"__globals__": {"title_color": "globals/colors?id=primary"}`. **Os JSONs da casa não usam globais** (0 ocorrências): tudo é valor fixo em cada widget. Ao gerar JSON, use valores fixos também, assim o template funciona em qualquer site.

## Chaves de addons (ruído)

- `ha_cmc_text: "Happy Addons"` aparece em **todos os 2.678 elementos** (Happy Addons grava isso). É inofensiva e pode ser removida.
- `eae_*` (Elementor Addon Elements) em 966 elementos, como `gradient_color_list` e `eae_slider_delay`. Também inofensivas quando o plugin não está instalado.
- Os [templates/](templates/) já vêm sem essas chaves.

## Checklist para gerar ou editar um JSON

1. Topo com `content`, `page_settings`, `version: "0.4"`, `title`, `type: "page"`.
2. Só `container` e `widget`. Containers de topo com `isInner: false`; filhos com `isInner: true`.
3. IDs únicos de 7 ou 8 hexadecimais.
4. `typography_typography: "custom"` sempre que houver chave de tipografia.
5. Medidas como objeto `{"unit","size","sizes":[]}`; padding/margin/raio como objeto de 4 lados em string.
6. Ajustes `_mobile` nos títulos (em `vw`), paddings e direção das linhas.
7. Rodar `python3 scripts/validar-json-elementor.py arquivo.json`, que compara com o vocabulário real da casa.
