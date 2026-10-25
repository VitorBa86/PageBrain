---
name: pagebrain
description: PageBrain, o cérebro criador de landing pages no padrão O Rei da Landing (Davi / Zarion). Cria a página do zero com copy, design, código HTML e, quando pedido, o JSON do Elementor, reproduzindo uma página real da casa como molde para não sair com "cara de IA". Use sempre que pedirem uma LP, landing page, página de captação, página de vendas, página para advogado, psicólogo, médico, dentista, imobiliária, negócio local ou infoproduto, revisão de uma página dessas, prompts de imagem para a página, ou a conversão de uma página HTML para Elementor.
---

# PageBrain · Criar landing page no padrão da casa

**Propósito:** instruções passo a passo para criar uma landing page completa no padrão da casa (O Rei da Landing), usando o acervo desta skill: 40 páginas reais medidas seção por seção, método de copy, snippets, imagens e conversão para Elementor.
**Quando usar:** em qualquer pedido de página nova, revisão de página ou conversão para Elementor.
**Relacionados:** [docs/LEIA-PRIMEIRO.md](docs/LEIA-PRIMEIRO.md), [design/PADRAO-DAVI.md](design/PADRAO-DAVI.md), [design/MEDIDAS-REAIS.md](design/MEDIDAS-REAIS.md), [design/ANTI-SLOP.md](design/ANTI-SLOP.md), [imagens-ia/README.md](imagens-ia/README.md), [docs/glossario.md](docs/glossario.md)

Todos os caminhos abaixo são relativos à pasta desta skill. Rode os scripts a partir dela (`python3 scripts/...`).

## Mapa da skill

| Pasta | O que tem | Quando abrir |
|---|---|---|
| `copy/` | Método de copy, tom de voz e regras por nicho, estrutura de página, fórmulas, banco de headlines e CTAs, checklist, briefing, 37 copys reais transcritas e os guias originais em `fontes/` | Passos 1 e 2 |
| `paginas/nossas/` | **40 páginas da casa**. Cada uma: `como-usar.md`, `ficha.json`, `raio-x/` (o molde medido seção por seção, com prints), `extraido/index.html` (a página salva, abre offline), `print.jpg` e `style-guide.html`. Índice em `CATALOGO.md` | Passos 3 a 5 |
| `paginas/gerais/` | 32 sites de referência de terceiros: `como-usar.md`, `ficha.json`, `style-guide.html`, `print.jpg`. Só ideia de componente e efeito | Passo 4, quando faltar algo na casa |
| `design/` | `PADRAO-DAVI.md` (o padrão da casa), `MEDIDAS-REAIS.md` (tamanhos reais), `ANTI-SLOP.md` (o que não fazer), `design-system-davi.html` | Passo 5 |
| `codigos/` | 68 snippets em 15 categorias (`GUIA-CODIGOS.md`, `preview.html`), incluindo a hero padrão `fundos-e-texturas/hero-foto-de-fundo-fade.html` | Passo 6 |
| `imagens-ia/` | Slots de imagem, estilos de prompt por nicho e geração com IA | Passos 5 e 6b |
| `elementor/` | 25 JSONs de página da casa, 37 seções prontas (`secoes/`), esqueletos, regras de HTML convertível e documentação do formato | Passo 7 |
| `scripts/` | `raio_x_molde.py`, `checar_pagina.py`, `icone.sh`, conversor e validador do Elementor, `shot.py`, `verificar_skill.py` (ver `scripts/README.md`) | Passos 3, 5, 7 e 8 |

**Requisitos:** Python 3.9+ com `pip install -r requirements.txt` e um navegador para o Playwright (Google Chrome instalado ou `python3 -m playwright install chromium`); Node.js (para o `npx` do `icone.sh`). Geração de imagem é opcional (conector do Magnific/Freepik).

## Regras inegociáveis

1. **Nenhum travessão (— ou –) em nenhum texto da página.** Use ponto, vírgula, dois-pontos ou parênteses.
2. **Nada inventado.** Dado que o cliente não deu vai como `[CONFIRMAR COM CLIENTE]`.
3. **Conselho de classe:** OAB, CFP, CFO, CFM e CRECI limitam a copy (sem promessa de resultado, sem depoimento em advocacia e psicologia, sem preço em advocacia e odonto). Ver `copy/tom-de-voz.md`.
4. **Molde da casa:** toda página nova reproduz uma página de `paginas/nossas` seção por seção (passo 3). Nada de componente que não exista em alguma página da casa.
5. **Prioridade de referência:** `paginas/nossas` vence `paginas/gerais` em qualquer conflito. As gerais continuam valendo como ideia de layout, componente e efeito.
6. **Um objetivo por página** e CTA para o WhatsApp (captação) ou checkout (vendas) em toda dobra.

## Regras fixas do PageBrain

Valem para **toda** página, por cima do molde. Só mudam se o usuário pedir outra coisa naquela página. A página que mostra todas funcionando é a referência de padrão [psi-luana-carolina-casais](paginas/nossas/psi-luana-carolina-casais/como-usar.md): abra o `extraido/index.html` e o `raio-x/` dela junto com o molde.

1. **Sem menu.** Não crie navbar, header com links nem menu hambúrguer, mesmo que o molde tenha. Menu (snippets de `codigos/menus-e-headers/`) só entra quando o usuário pedir.
2. **Logo acima da headline.** A logo fica na hero, dentro da coluna de texto, logo acima do rótulo e do H1 (52px de altura no desktop, 28 a 32px no mobile). Em outro lugar só se o usuário pedir.
3. **Títulos em até 3 linhas.** Escolha o tamanho do H1 e de cada H2 para que ele quebre em **no máximo 3 linhas** na largura da coluna dele, no desktop e no mobile. Frase longa (mais de 70 caracteres) pode ir a **4 linhas**, nunca mais. Título nunca fica enorme: teto de **55px**, padrão de 40 a 48px no desktop e 26 a 30px no mobile. Se não couber, diminua a fonte ou alargue a coluna, não encurte a copy sem avisar.
4. **Ícones sempre da skill better-icons.** Todo ícone da página (cards, listas, selos, passos, rodapé) vem de `scripts/icone.sh` (CLI do better-icons, coleção lucide por padrão), colado como SVG inline. Nunca desenhe ícone à mão, nunca use emoji como ícone.
5. **Hero com foto de fundo e fade**, no padrão da referência: foto em tela cheia no desktop com fade da cor de fundo à esquerda (onde fica o texto) e, no mobile, um recorte da mesma foto centralizado na pessoa, no topo, com o corpo nítido acima da logo e o botão visível sem rolar. Código pronto: `codigos/fundos-e-texturas/hero-foto-de-fundo-fade.html`.

Confira as cinco com `python3 scripts/checar_pagina.py pagina.html` (passo 8).

## Fluxo

### 1. Briefing

- Abra `copy/template-briefing.md` e responda (ou pergunte) os blocos A a H.
- Feche com o resumo de 6 linhas (tipo de página, ação e mensagem do WhatsApp, promessa do anúncio, público e dor, prova disponível, pendências).
- Identifique o **nicho** e o **tipo de página** (captação, lançamento imobiliário, vendas, aplicação, institucional).

### 2. Escrever a copy

1. Leia `copy/metodo-de-copy.md` e `copy/tom-de-voz.md` (inclusive a tabela do nicho).
2. Defina a estrutura com `copy/estrutura-de-pagina.md`: 6 dobras na captação, até 8 no lançamento imobiliário, sequência própria em vendas e aplicação.
3. Escreva cada bloco com as fórmulas de `copy/formulas-e-modelos.md`. Busque inspiração no nicho em `copy/banco-de-headlines-e-ctas.md` e nas transcrições de `copy/copys-reais/` (pegue as páginas do mesmo nicho).
4. Entregue no formato `## DOBRA N: NOME` com os campos (Kicker, H1, Subheadline, CTA, Microcopy, Selo...), mais a mensagem pré-configurada do WhatsApp de cada CTA.
5. Rode `copy/checklist-de-copy.md`, incluindo os comandos `grep` de travessão e palavras proibidas.

### 3. Escolher o molde (obrigatório)

**A página nova é irmã de uma página da casa.** Antes de pensar em layout, escolha **um molde**: a página da casa que será reproduzida seção por seção. É isso que impede o resultado "cara de IA" (ver `design/ANTI-SLOP.md`).

1. **Se o briefing cita uma página da casa** (link `lp.oreidalanding.com.br/...`), ela é o molde. Procure a URL nos `ficha.json` de `paginas/nossas`. Se ela ainda não estiver no acervo, capture a página (zip da extensão de captura), extraia e rode o raio-x direto no `index.html` capturado.
2. **Se não cita**, filtre `paginas/nossas/CATALOGO.md` por nicho e tipo de página e escolha a mais parecida com o estilo pedido. Na dúvida entre duas, mostre os `print.jpg` das duas e pergunte.
3. Referência **externa** do cliente (site de terceiros) serve só para ideia de componente ou efeito; o molde continua sendo da casa.
4. Abra o raio-x do molde: `paginas/nossas/<slug>/raio-x/raio-x.md` + as imagens `secao-NN.jpg` + `pagina-mobile.jpg`. Se a pasta não existir, gere: `python3 scripts/raio_x_molde.py <slug>`.
5. Abra também o raio-x da referência de padrão `psi-luana-carolina-casais`. A hero, a posição da logo, o tamanho dos títulos e os ícones vêm dela, não do molde (regras fixas). Se o molde tem menu, ele sai.
6. **Página de vendas ou infoproduto com visual escuro:** a referência aprovada é [vendas-luana-carolina-metodo-lua](paginas/nossas/vendas-luana-carolina-metodo-lua/como-usar.md). O `como-usar.md` dela tem a tabela "copy → molde" pronta para venda de formação (problema, protocolo, depoimentos, módulos, bônus, resultados, autoridade, 2 planos, certificado, FAQ). Use-a junto com o molde `vendas-odonto-luiz-gustavo-melo`. Para o estilo laranja sobre preto com objetos 3D, o molde é [vendas-mentoria-bancario-jessica-v2](paginas/nossas/vendas-mentoria-bancario-jessica-v2/como-usar.md).

### 4. Mapear copy para as seções do molde

- Monte uma tabela: **dobra da copy → seção do molde que ela vai usar** (ex.: "Para quem é" → seção 03 da Jéssica, cards 661x120). A ordem de fundos segue a do molde.
- Dobra da copy sem equivalente no molde: pegue a seção do mesmo tipo em **outra página da casa** (`elementor/secoes/catalogo-secoes.md` e `elementor/secoes/<tipo>/README.md`) e rode o raio-x dela. Nunca invente um componente.
- Copiar do molde, sem mudar: **tamanhos e pesos de texto, line-height, botão (tamanho, padding, raio, caixa, altura), rótulo acima do título, raio e padding dos cards, paddings das seções, largura do conteúdo, número de colunas, posição de foto e texto, comportamento no mobile.**
- Trocar: copy, paleta (as cores do cliente nos mesmos papéis das cores do molde), imagens e ícones.
- Sem molde possível (caso raro): use `design/MEDIDAS-REAIS.md` e `design/PADRAO-DAVI.md`.
- Para montar direto no Elementor, considere partir do JSON da página molde (`elementor/indice.md`) ou de um esqueleto (`elementor/templates/`).

### 5. Montar o HTML

Siga **ao mesmo tempo** o raio-x do molde, `elementor/regras-html-convertivel.md` e `design/ANTI-SLOP.md`. Parta de `elementor/templates/exemplo-pagina-convertivel.html`.

Tokens padrão quando o molde não define (medidos nas páginas da casa, ver `design/MEDIDAS-REAIS.md`):

| Token | Valor |
|---|---|
| Largura do conteúdo | 1140px (ou 1240px) |
| Padding vertical da seção | 80px (50px no mobile) |
| Hero | `min-height: min(100vh, 860px)`, foto de fundo com fade (snippet `hero-foto-de-fundo-fade.html`), logo acima do H1, sem menu, botão visível sem rolar no celular |
| Gap | 20px |
| H1 do hero | 40 a 46px desktop, 27 a 29px mobile, peso 600; **até 3 linhas** (4 se a frase passar de 70 caracteres); teto 55px |
| H2 de seção | 36 a 48px desktop, 25 a 26px mobile; **até 3 linhas** na largura da coluna (4 se longo); teto 55px |
| Título de card | 20 a 22px, peso 600, frase normal (nunca caixa alta pesada) |
| Corpo | 16 a 18px desktop, 16px mobile, peso 300 ou 400, line-height 1,5em |
| Botão | 18px/500, ~58px de altura, padding ~20px 40px, ícone solto (nunca em quadradinho), caixa alta só em vendas |
| Card | raio de 8 a 14px, sombra suave, ícone no topo |
| Breakpoints | 1024px e 767px |

Estrutura do arquivo: uma `<section>` por dobra com `<div class="wrap">`, só flexbox, um `<h1>`, `<p>` para texto, `<a class="btn">` para CTA, `<details>` para FAQ, todo o CSS num `<style>`, mobile num único `@media (max-width: 767px)`, scripts no fim.

**Hero:** parta de `codigos/fundos-e-texturas/hero-foto-de-fundo-fade.html`. Dois slots de fundo: `IMG-01` (foto 16:9, pessoa à direita, lado esquerdo limpo) e `IMG-01-mobile` (recorte quase quadrado da IMG-01, centralizado no corpo, feito com o comando `ffmpeg` do snippet). Ajuste de foto: veja os comentários do snippet.

**Tamanho dos títulos:** para cada H1 e H2, estime as linhas antes de fixar a fonte: em Inter 600, cabem cerca de `largura da coluna ÷ (0,52 × fonte)` caracteres por linha. Ex.: coluna de 560px com 46px cabe ~23 caracteres por linha, então uma headline de 65 caracteres fica em 3 linhas. Confirme depois no `checar_pagina.py`.

**Ícones:** busque e pegue com `scripts/icone.sh` (ex.: `scripts/icone.sh buscar "coração"` e `scripts/icone.sh pegar lucide:heart-crack`). Cole o SVG inline dentro de um `<span>` com a cor no `color` (o SVG usa `currentColor`). Mesmo estilo e espessura em toda a página (lucide, traço 1,6). Padrão de card da referência: círculo de 48px na cor clara, ícone de 22px na cor de destaque, invertendo no hover.

**Imagens:** toda imagem entra como slot (`imagens-ia/README.md`): `<img class="pb-slot" src="imagens/IMG-NN.webp" width height alt data-slot data-prompt>`, com largura e altura da tabela "Slot" do raio-x do molde, e o script de `imagens-ia/slot-de-imagem.html`. Crie `imagens/imagens.json` ao lado da página com todos os slots (formato em `imagens-ia/imagens-modelo.json`). Foto e print do cliente nunca são inventados nem desenhados em HTML.

### 6. Inserir os snippets da casa

Abra `codigos/GUIA-CODIGOS.md` (e `codigos/preview.html` para ver funcionando). Obrigatórios em toda página:

1. `codigos/utilitarios-css/css-base-toda-pagina.css` no início do `<style>`;
2. `codigos/animacoes/animacao-scroll-reveal.html` (classes `scroll-bottom`, `scroll-left`, `scroll-right` nos blocos + script no fim);
3. link de WhatsApp com mensagem (`codigos/whatsapp-e-flutuantes/link-whatsapp-com-mensagem.html`) e botão flutuante;
4. Meta Pixel e Google Ads (`codigos/tracking-e-pixels/`) com IDs do cliente ou placeholders;
5. `codigos/fundos-e-texturas/hero-foto-de-fundo-fade.html` na hero (regra fixa 5).

Opcionais **só se o molde usa**: faixa infinita, brilho no botão, borda de luz girando, card com borda degradê, linha do tempo, carrossel de avaliações do Google e rodapé pronto. **Menu só se o usuário pedir**, mesmo que o molde tenha. Componentes complexos entram como bloco com `data-el="html"` e CSS com prefixo próprio.

### 6b. Gerar as imagens

1. Para cada slot de origem "gerar", monte o prompt com `imagens-ia/estilos-de-prompt.md` (tipo de imagem + assunto da seção + estilo do nicho + paleta + regras fixas) e grave em `imagens.json` e no `data-prompt`.
2. Se o conector do Magnific estiver disponível: simule o custo total (`simulate_cost`), **mostre a lista e o custo e espere o OK do usuário**, gere na proporção do slot (Seedream 5 Pro por padrão; foto do cliente como referência quando o slot for composição com o expert), baixe, converta para WebP como `imagens/IMG-NN.webp` e atualize o status.
3. Sem conector ou sem OK: entregue a página com os slots e os prompts (botão "Copiar prompt" em cada caixa) para o usuário gerar onde preferir e soltar os arquivos em `imagens/`.

### 7. Converter para JSON do Elementor (quando pedido)

```bash
python3 scripts/html-para-elementor.py caminho/pagina.html caminho/pagina.json --titulo "Cliente X"
python3 scripts/validar-json-elementor.py caminho/pagina.json
python3 scripts/elementor-para-preview.py caminho/pagina.json caminho/preview.html --png caminho/preview.png
```

- O validador precisa terminar com **0 erros**. Avisos de chave fora do vocabulário devem ser revistos.
- Confira o preview e compare com o HTML.
- Avise o usuário das limitações (`elementor/mapa-html-para-elementor.md`): imagens precisam ir para a biblioteca do WordPress, efeitos de hover e animação dependem do CSS em `page_settings`, widgets HTML precisam ser revisados.
- Se a página for montada à mão no Elementor, use `elementor/anatomia-json-elementor.md` e as seções de `elementor/secoes/`.

### 8. Checklist final de qualidade

**Copy**
- [ ] `grep -nE "—|–"` sem resultado em todo o HTML e na copy.
- [ ] Nenhuma palavra proibida; no máximo uma exclamação (nenhuma em psi).
- [ ] H1 com até 12 palavras, continuando o anúncio; cidade na hero e no rodapé.
- [ ] Dados não confirmados marcados; nada que o conselho proíbe.

**Regras fixas do PageBrain** (rodar `python3 scripts/checar_pagina.py pagina.html`, que precisa terminar sem ERRO)
- [ ] Sem menu (a não ser que o usuário tenha pedido; nesse caso rode com `--com-menu`).
- [ ] Logo na hero, acima do rótulo e do H1.
- [ ] Nenhum H1 ou H2 com mais de 3 linhas em 1440px e 390px (4 só em frase longa); nenhum acima de 55px.
- [ ] Todos os ícones vindos do `icone.sh` (better-icons), SVG inline, mesmo estilo; nenhum emoji.
- [ ] Hero com foto de fundo e fade; no celular, corpo da pessoa acima da logo e botão visível sem rolar (390x664).

**Design e código**
- [ ] Molde escolhido e citado no resumo; cada seção mapeada para uma seção do molde ou de outra página da casa.
- [ ] Raio-x da página nova (`python3 scripts/raio_x_molde.py pagina.html /tmp/rx`) comparado com o do molde: títulos, corpo e botão a no máximo 4px de diferença.
- [ ] Nada da `design/ANTI-SLOP.md` (interface falsa, número inventado, chips flutuando, ícone em quadradinho no botão, card em caixa alta pesada).
- [ ] Todas as imagens em slots `imagens/IMG-NN` com tamanho do molde; `imagens.json` completo.
- [ ] Paleta com marca escura + neutro + acento; fundos na ordem do molde.
- [ ] Hero até 860px de altura, foto de fundo (real do cliente ou composição feita com a foto dele) e CTA visível sem rolar.
- [ ] CTA em toda dobra; botão flutuante de WhatsApp.
- [ ] CSS base + scroll reveal + pixels presentes.
- [ ] Testado em 1440px e 390px, sem rolagem horizontal, títulos legíveis no mobile.
- [ ] Um `<h1>` só; imagens com `alt`.
- [ ] Nenhum Lorem Ipsum, placeholder de vídeo ou link `#` publicado.

**Elementor (se aplicável)**
- [ ] JSON validado com 0 erros e preview conferido.
- [ ] Fonte do mobile em vw, paddings e direções de mobile presentes.

## Armadilhas já resolvidas

Cada item abaixo custou uma rodada de correção numa página real. Confira antes de entregar.

**CSS e layout**
- **Botão colado na subheadline:** o CSS base tem `p:last-of-type{margin-bottom:0}`, que vence uma classe sozinha. Margem do último `<p>` vai em seletor composto (`.hf-texto .hf-sub`) ou como `margin-top` no botão. O snippet da hero já vem corrigido.
- **Grade que estoura ou some no celular:** dentro de `.wrap` com `align-items:center`, o bloco filho (grade de cards, planos, prints) encolhe para o conteúdo e transborda. Dê `width:100%` a todo container de cards. E card com `flex:1 1 0` some (altura 0) quando a linha vira coluna no mobile: troque para `flex:none` no breakpoint.
- **Texto quebrado em flex:** em `summary`, `li` e rótulos com `display:flex`, um `<sup>`, `<strong>` ou `<em>` vira item separado e se afasta do texto. Envolva o texto num `<span>`.
- **Logo de texto:** o `checar_pagina.py` só reconhece logo em `img` ou `svg`. Sem arquivo de logo, faça um `<svg class="hf-logo" role="img" aria-label="Logo ..."><text>...</text></svg>` usando as fontes da página.

**Imagens**
- **WebP:** se o `ffmpeg` não tiver `libwebp` (comum no Homebrew), converta com `cwebp -q 82 entrada.jpg -o saida.webp`.
- **Arquivos parecidos:** antes de usar uma foto do cliente, monte uma folha de contato com rótulos (ffmpeg `xstack`) e confira qual arquivo é qual. Nomes como `channels4_profile.jpg` e `foto_01.jpg` enganam: um retrato errado já foi parar na seção "Sua mentora".
- **Expert "mais afastada" no celular:** faça um recorte mais aberto da IMG-01 e posicione em `vw` (ver o snippet da hero, variante escura).
- **Magnific pelo conector:** foto local entra com `creations_request_upload`, depois `curl -X PUT --data-binary @foto.jpg -H "Content-Type: image/jpeg" "<proxyUploadUrl>"` e por fim `creations_finalize_upload`. Rode `simulate_cost` antes de gerar.

**Ferramentas**
- **Python isolado:** `python3 -I` não enxerga pacotes instalados no usuário (Playwright). Use `-I` só para ler arquivos de terceiros. Prints e checagens rodam sem `-I`.
- **Paper (editor de design):** `backgroundImage` com `paper-asset://` num caminho com acento não renderiza; use `<img>` com `position:absolute`. Uma `div` vazia some ao ser criada: crie o container já com o primeiro filho. Para gerar imagem no próprio Paper, `google-nano-banana-2-1` com `reference_nodes` funcionou; `nano-banana-pro-edit` deu erro.
- **Ícones:** o `icone.sh` tira o preenchimento de `circle`, `rect` e `ellipse` e avisa quando um `<rect>` vem sem `width`/`height` (`lucide:lock`, `lucide:clipboard-list`). Complete à mão.
- **™ ® ©:** o `checar_pagina.py` os aceita. Pode usar o símbolo direto no texto.

**Mobile**
- O WhatsApp flutuante (60px, canto inferior direito) cobre a seta do botão da hero em 390x664. Suba o flutuante ou faça ele aparecer só depois de rolar.

## Quando o usuário aprovar uma página

Cada página aprovada vira referência, para a próxima precisar de menos correção:

1. Crie `paginas/nossas/<nicho-nome>/` com `extraido/` (a página final e as imagens), `copy.md`, `ficha.json` (mesmo formato das outras), `como-usar.md` (com o mapa "copy → molde" e o que não copiar) e `print.jpg`.
2. Gere o raio-x: `python3 scripts/raio_x_molde.py <nicho-nome>`.
3. Inclua a página em `paginas/nossas/CATALOGO.md` e `paginas/nossas/catalogo.json`.
4. Corrija o snippet ou script que causou retrabalho e registre a armadilha na seção acima.
5. Rode `python3 scripts/verificar_skill.py` (links, JSONs, travessões).

## Entregáveis esperados

1. Copy completa no formato de dobras + mensagens de WhatsApp + lista de `[CONFIRMAR COM CLIENTE]`.
2. `pagina.html` autocontido (abre no navegador).
3. (Se pedido) `pagina.json` validado + preview.
4. `imagens/` com as imagens geradas (ou os slots vazios) e `imagens/imagens.json`.
5. Resumo curto: molde usado, tabela dobra → seção do molde, outras referências, snippets incluídos, imagens geradas e custo em créditos, pendências.
