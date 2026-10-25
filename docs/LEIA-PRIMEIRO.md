# PageBrain · Leia primeiro

**Propósito:** porta de entrada do acervo. Explica o que é, a hierarquia de prioridade, a ordem de leitura e onde está cada coisa.
**Quando usar:** é o primeiro arquivo que qualquer IA (ou pessoa) deve ler antes de usar o acervo. O fluxo de trabalho completo está no [SKILL.md](../SKILL.md).
**Relacionados:** [SKILL.md](../SKILL.md), [README.md](../README.md), [glossario.md](glossario.md), [CHANGELOG.md](../CHANGELOG.md)

## O que é o PageBrain

**PageBrain** é o cérebro criador de páginas da casa (Davi Barros Batista · Zarion · O Rei da Landing): a base de conhecimento para criar landing pages **exatamente como a casa cria**, com a mesma copy, o mesmo design, o mesmo jeito de construir no Elementor e com a possibilidade de entregar o JSON do Elementor.

Foi montado a partir de:

- **40 páginas da casa** (38 publicadas e 2 referências de padrão aprovadas), medidas no navegador seção por seção, transcritas e documentadas uma a uma;
- **32 sites de referência** de terceiros;
- **2 guias de copy** do Davi;
- **25 JSONs de página** e **37 seções** do Elementor;
- **68 snippets** de código usados nas páginas.

## Hierarquia de prioridade

1. **Regras do Davi** (guia de copy, principalmente: nenhum travessão, nada inventado, conselho de classe) e as **regras fixas do PageBrain** ([SKILL.md](../SKILL.md): sem menu, logo acima da headline, títulos em até 3 linhas, ícones da skill better-icons, hero com foto de fundo e fade). Vencem tudo, inclusive o molde, a não ser que o usuário peça outra coisa na página.
2. **`paginas/nossas` e o [PADRAO-DAVI.md](../design/PADRAO-DAVI.md)**. Em conflito com qualquer referência externa, o padrão da casa vence.
3. **`paginas/gerais`**: referências válidas para ideias de layout, componentes e efeitos, sempre adaptadas ao padrão da casa.
4. O que foi inferido (marcado como `(inferido)` nos documentos) vem por último.

Dentro de `paginas/nossas`, algumas páginas antigas desrespeitam o guia de copy (travessões, depoimentos em advocacia, Lorem Ipsum esquecido). Cada `como-usar.md` tem a seção "O que NÃO copiar".

## Ordem de leitura recomendada

1. Este arquivo.
2. [SKILL.md](../SKILL.md): o fluxo completo de criação, passo a passo.
3. [design/ANTI-SLOP.md](../design/ANTI-SLOP.md) e [design/MEDIDAS-REAIS.md](../design/MEDIDAS-REAIS.md): o que não fazer e os tamanhos reais.
4. A referência de padrão [psi-luana-carolina-casais](../paginas/nossas/psi-luana-carolina-casais/como-usar.md) (abrir `extraido/index.html` no navegador, no desktop e no celular): é como toda página nova deve ficar na hero, nos títulos e nos ícones.
5. Para **página de vendas escura** (curso, formação, mentoria): a referência [vendas-luana-carolina-metodo-lua](../paginas/nossas/vendas-luana-carolina-metodo-lua/como-usar.md), com o mapa copy → molde pronto. Leia também a seção "Armadilhas já resolvidas" do [SKILL.md](../SKILL.md).
6. [design/PADRAO-DAVI.md](../design/PADRAO-DAVI.md) e [design-system-davi.html](../design/design-system-davi.html) (abrir no navegador).
7. [copy/README.md](../copy/README.md) e os documentos que ele indica (método, tom de voz, estrutura, fórmulas, checklist).
8. [imagens-ia/README.md](../imagens-ia/README.md): slots de imagem e geração com IA.
9. [codigos/GUIA-CODIGOS.md](../codigos/GUIA-CODIGOS.md) e [preview.html](../codigos/preview.html).
10. [elementor/README.md](../elementor/README.md) (anatomia, regras de HTML convertível, conversor) e [elementor/secoes/catalogo-secoes.md](../elementor/secoes/catalogo-secoes.md).
11. Os catálogos de páginas: [nossas](../paginas/nossas/CATALOGO.md) e [gerais](../paginas/gerais/CATALOGO.md).
12. [glossario.md](glossario.md) sempre que um termo não estiver claro.

## Fluxo para criar uma página nova (resumo da SKILL)

```
1. Briefing ............ copy/template-briefing.md
2. Copy ................ metodo-de-copy + tom-de-voz + formulas + checklist-de-copy
3. Molde ............... 1 página de paginas/nossas + raio-x/ dela (scripts/raio_x_molde.py)
4. Mapa copy → seções .. cada dobra numa seção do molde (ou de outra página da casa)
5. HTML ................ raio-x do molde + referência psi-luana-carolina-casais + regras-html-convertivel + ANTI-SLOP + slots de imagem
                         (sem menu, logo acima do H1, títulos em até 3 linhas, ícones via scripts/icone.sh)
6. Snippets ............ codigos/GUIA-CODIGOS (CSS base, scroll reveal, WhatsApp, pixels, hero-foto-de-fundo-fade)
6b. Imagens ............ imagens-ia/estilos-de-prompt + Magnific (com OK do custo) ou prompts nos slots
7. Elementor ........... scripts/html-para-elementor.py + scripts/validar-json-elementor.py
8. Checklist final ..... SKILL.md, seção 8 + python3 scripts/checar_pagina.py pagina.html (sem ERRO)
```

## Como cada pasta está organizada

| Pasta | Conteúdo principal |
|---|---|
| [copy](../copy/README.md) | Método de copy, tom, fórmulas, banco de headlines e CTAs, checklist, briefing, 37 copys reais transcritas, guias originais em `fontes/`. |
| [paginas/nossas](../paginas/nossas/CATALOGO.md) | 40 páginas da casa: cada uma com `como-usar.md`, `ficha.json`, `raio-x/` (medidas e print de cada seção, para usar como molde), `extraido/` (a página salva), `print.jpg` e `style-guide.html`. |
| [paginas/gerais](../paginas/gerais/CATALOGO.md) | 32 sites de referência: `como-usar.md`, `ficha.json`, `style-guide.html`, `print.jpg` e as imagens do style guide em `ref/`. |
| [design](../design/PADRAO-DAVI.md) | PADRAO-DAVI, MEDIDAS-REAIS, ANTI-SLOP, design system e os dados brutos das medidas. |
| [codigos](../codigos/GUIA-CODIGOS.md) | 68 snippets em 15 categorias, preview ao vivo. |
| [imagens-ia](../imagens-ia/README.md) | Slots de imagem, estilos de prompt por nicho e geração com IA. |
| [elementor](../elementor/README.md) | 25 JSONs de página, 37 seções por tipo, índice, previews, anatomia, padrões, mapa HTML→Elementor, regras e esqueletos. |
| [scripts](../scripts/README.md) | Raio-x de molde, checagem das regras fixas, ícones, conversor e validador do Elementor, screenshot e verificação da skill. |
| `docs/` (esta pasta) | Este arquivo e o glossário. |

## Convenções

- Pastas de site com o nome `nicho-nome` (`adv-`, `psi-`, `saude-`, `odonto-`, `imob-`, `negocio-`, `servico-`, `info-`, `vendas-`). O nome original de cada uma está em `ficha.json` (`pasta_original`).
- Todo `.md` começa com Propósito, Quando usar e Relacionados.
- Nomes de pasta e de arquivo sem espaço nem acento, para funcionar igual em macOS, Windows, Linux e GitHub.
