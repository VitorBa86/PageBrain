# Regras para HTML convertível em Elementor

**Propósito:** como escrever o HTML de uma página nova para que ela seja fácil (e automática) de converter em JSON do Elementor no padrão da casa.
**Quando usar:** sempre que uma IA for gerar a página em HTML antes de ir para o Elementor. É o passo 5 da [SKILL](../SKILL.md).
**Relacionados:** [mapa-html-para-elementor.md](mapa-html-para-elementor.md), [templates/exemplo-pagina-convertivel.html](templates/exemplo-pagina-convertivel.html), [scripts/html-para-elementor.py](../scripts/html-para-elementor.py), [PADRAO-DAVI.md](<../design/PADRAO-DAVI.md>)

Modelo completo que segue todas as regras: [templates/exemplo-pagina-convertivel.html](templates/exemplo-pagina-convertivel.html). Ele converte em 63 elementos sem erro e sem aviso.

## 1. Estrutura de seções

1. **Uma `<section>` por dobra**, filha direta do `<body>`. Nada de `<main>` ou `<div>` envolvendo a página inteira (o conversor tolera um nível, mas não conte com isso).
2. Dentro de cada seção, **um único wrapper** com a largura do conteúdo: `<div class="wrap">` com `max-width: 1140px` (ou 1240px). Ele vira o `boxed_width` do container de topo.
3. Seção de largura total (hero com foto até a borda, faixas): sem wrapper com max-width.
4. Dê **`id` às seções** que o menu vai linkar (`id="servicos"`). Vira `_element_id`.
5. Header e rodapé: `<header>` e `<footer>` também são containers de topo. Menu com hambúrguer e rodapés complexos vão como widget HTML (regra 7). **Por regra fixa do PageBrain (24/10/2026), a página não tem menu** a não ser que ele peça: a logo fica dentro da hero, acima do H1. Ícones entram como SVG inline vindo de `scripts/icone.sh` (o conversor transforma em widget HTML).

## 2. Layout só com flexbox

1. Todo bloco que agrupa outros é um `<div>` com `display: flex` e `flex-direction` explícito. `display: block` vira coluna.
2. **Evite CSS Grid.** Se precisar de grade de cards, use `display:flex; flex-wrap:wrap` e `flex: 1 1 300px` nos cards.
3. Use **`gap`** para espaçar irmãos, não margens. Padrão da casa: 20px.
4. Duas colunas: um `<div class="linha">` (row) com dois `<div class="col">`. No mobile, mude só o `flex-direction` para `column` num `@media (max-width: 767px)`.
5. Não use `position: absolute` para layout. Para decorações soltas, marque o elemento com `data-el="html"` ou deixe para posicionar no Elementor.
6. Evite aninhar mais de 3 ou 4 níveis de `div` dentro da seção. Cada `div` vira um container.

## 3. Um elemento, um widget

| Quero | Escreva |
|---|---|
| Título | `<h1>` (só um, no hero), `<h2>` por seção, `<h3>` em cards |
| Palavra destacada no título | `<em>`, `<b>` ou `<span class="...">` **dentro** do `<h2>` |
| Parágrafo | `<p>` (um por bloco de texto) |
| Rótulo acima do título | `<p class="rotulo">` |
| Botão | `<a class="btn" href="https://wa.me/...">Texto</a>` (classes `btn`, `button`, `botao` ou `cta`, ou `data-el="button"`) |
| Imagem | `<img src alt>` com `width: 100%` dentro de uma coluna |
| Lista com check | `<ul><li>texto</li></ul>` (só texto dentro do `li`) |
| FAQ | `<details><summary>Pergunta</summary><p>Resposta</p></details>` em sequência |
| Vídeo | `<iframe src="https://www.youtube.com/embed/...">` |
| Mapa | `<iframe src="https://www.google.com/maps?q=...">` |
| Linha divisória | `<hr>` |

Não misture texto solto com blocos no mesmo `div` (ex.: `<div>texto <div>bloco</div></div>`). Texto sempre dentro de `<p>` ou heading.

## 4. Onde colocar o CSS

1. **Todo o CSS num único `<style>` no `<head>`.** O conversor lê os estilos computados, então pode usar classes e variáveis CSS à vontade.
2. Comece o `<style>` com o [CSS base da casa](<../codigos/utilitarios-css/css-base-toda-pagina.css>). Ele vai inteiro para `page_settings.custom_css`.
3. Mobile **em um único `@media (max-width: 767px)`**. Tablet em `@media (max-width: 1024px)`, se precisar.
4. Use `px` para tamanhos no desktop; o conversor transforma a fonte do mobile em `vw`, como a casa faz.
5. Gradientes de duas cores (`linear-gradient(180deg, #a 0%, #b 100%)`) viram setting; gradientes com 3 ou mais cores ficam só no CSS.
6. Hover, `@keyframes`, `::before/::after` continuam funcionando porque o CSS e as classes são preservados, mas não viram settings editáveis no painel.

## 5. Classes que a casa usa

- `scroll-bottom`, `scroll-left`, `scroll-right`, `scroll-top` nos blocos que entram animados (+ script do [scroll reveal](<../codigos/animacoes/animacao-scroll-reveal.html>) no fim do `<body>`).
- `carrossel` na lista que vira faixa infinita.
- `bot`, `botao` em botões com efeito especial.
- As classes vão para `css_classes` (container) ou `_css_classes` (widget) e os snippets continuam funcionando no Elementor.

## 6. Onde colocar o JS

1. Scripts **no fim do `<body>`**. O conversor junta todos num widget HTML no último container (`scripts-da-pagina`).
2. Bibliotecas externas (GSAP, Lenis, Swiper) por `<script src>` também no fim.
3. Nada de JS que gere o layout (o conversor lê o DOM depois de carregar, mas o Elementor não vai rodar esse JS no editor).

## 7. Blocos que devem virar widget HTML

Marque com `data-el="html"` o bloco inteiro quando ele for um componente complexo: menu com drawer, rodapé com várias colunas e ícones, timeline, gráfico, formulário customizado, contador, carrossel próprio, mapa estilizado. Escreva esses blocos **autocontidos** (CSS com prefixo próprio, como `.rb-`, `.ifm-`, `.sb-`), no padrão dos snippets de `codigos`.

`<svg>`, `<canvas>`, `<form>`, `<table>`, `<video>` e `<blockquote>` já viram HTML automaticamente. `data-el="ignore"` faz o conversor pular o elemento.

## 8. Imagens e links

- Imagens com URL absoluta (ou relativa ao arquivo). Depois de importar, troque pelas da biblioteca do WordPress.
- Links de CTA sempre no formato `https://wa.me/55DDDNUMERO?text=...` (mensagem codificada).
- `target="_blank"` em links externos vira `is_external`.

## 9. Converter e validar

```bash
# a partir da raiz da skill (pasta pagebrain/)
python3 scripts/html-para-elementor.py minha-pagina.html minha-pagina.json --titulo "Cliente X"
python3 scripts/validar-json-elementor.py minha-pagina.json
```

Use `--clipboard` para gerar o formato "colar de outro site" e `--offline` para não baixar nada da internet durante a leitura.

## Checklist

- [ ] Uma `<section>` por dobra, filha do `<body>`, com `<div class="wrap">` de max-width.
- [ ] Só flexbox, com `gap`. Sem grid.
- [ ] Um `<h1>`; títulos de seção em `<h2>`; textos em `<p>`.
- [ ] Botões como `<a class="btn">` com link de WhatsApp.
- [ ] CSS num só `<style>`, mobile num só `@media (max-width: 767px)`.
- [ ] Componentes complexos com `data-el="html"` e CSS com prefixo.
- [ ] Scripts no fim do `<body>`.
- [ ] Validador sem erros.
