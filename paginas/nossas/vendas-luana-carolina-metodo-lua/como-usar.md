# Como usar: PÁGINA VENDAS [LUANA CAROLINA · MÉTODO L.U.A.]

**Propósito:** página de vendas escura aprovada pelo usuário em 25/10/2026. É a referência de padrão para **páginas de vendas e infoproduto** (formação, curso, mentoria) com visual escuro e premium, do mesmo jeito que a [psi-luana-carolina-casais](../psi-luana-carolina-casais/como-usar.md) é a referência para captação clara.
**Quando usar:** como molde de página de vendas de formação ou curso para profissionais (saúde, estética, odonto, beleza), e como exemplo de hero escura com foto de fundo. Continua valendo junto com a psi-luana-carolina-casais para as regras fixas.
**Relacionados:** [extraido/index.html](extraido/index.html) (abrir no navegador), [raio-x/raio-x.md](raio-x/raio-x.md), [copy.md](copy.md), [ficha.json](ficha.json), [SKILL.md](../../../SKILL.md), [hero-foto-de-fundo-fade.html](<../../../codigos/fundos-e-texturas/hero-foto-de-fundo-fade.html>)

- **Origem:** página de teste do PageBrain, feita com o PageBrain em 24 e 25/10/2026 e ajustada com o usuário até a aprovação.
- **Molde usado:** [vendas-odonto-luiz-gustavo-melo](../vendas-odonto-luiz-gustavo-melo/como-usar.md) (venda de formação para dentistas).
- **Dados:** **fictícios** (marca Método L.U.A., preços, "+200 profissionais", links de checkout, WhatsApp 55DDDNUMERO, pixels). A expert é real (fotos da pasta `FOTOS LUANA`), o produto não.
- **Nicho:** saúde e estética (infoproduto) · **Tipo de página:** vendas · **Relevância:** 5/5

## Como ela foi feita (o fluxo que deu certo)

1. Copy: transcrição de uma página de referência e reescrita completa para o produto novo (`copy.md`). A copy não foi copiada, só a estrutura.
2. Imagem da hero: Magnific, Seedream 5 Pro, com 2 fotos reais da expert como referência (100 créditos). O prompt está em [imagens-ia/estilos-de-prompt.md](../../../imagens-ia/estilos-de-prompt.md), estilo "Beleza escura com glow violeta".
3. Hero montada primeiro no Paper (artboards "Hero v3" e "Hero v4" do arquivo LUANA) e depois passada para HTML.
4. Resto da página no molde `vendas-odonto-luiz-gustavo-melo`, seção por seção (tabela abaixo).
5. `checar_pagina.py` sem ERRO + prints de 1440 e 390 conferidos seção por seção.

## Mapa copy → molde (reutilizável em qualquer venda de formação)

| Dobra | Componente | De onde veio |
|---|---|---|
| Hero | foto de fundo + fade escuro, logo SVG, rótulo, H1, sub, botão, 3 selos, 2 cards de vidro | referência de padrão + REFERENCIA1 do cliente |
| Faixa | faixa infinita com os pilares do método (lilás no topo, dourada antes do FAQ) | snippet `faixa-animada-infinita` |
| Problema | texto + 4 cards com X à esquerda; foto de antes e depois + citação da expert à direita | seção 04 do molde (texto + imagem) |
| Protocolo | H2 + texto centralizados + slot de vídeo 1000x562 | seção centralizada do molde |
| Depoimentos | 6 slots de print 280x498 (3 por linha) | regra de slot do `imagens-ia/README.md` |
| Módulos | 8 cards 560px em 2 colunas, número em círculo + "Módulo 0N" + título | seção 02 do molde (8 cards) |
| O que você leva | texto + botão à esquerda, 3 cards com ícone, texto e etiqueta à direita | seção 04 do molde |
| Bônus | 3 cards com imagem 413x395 em cima e texto embaixo | seção 07 do molde |
| Resultados | 3 slots 360x440 de antes e depois | regra de slot |
| Autoridade | card grande com texto, 4 credenciais e botão à esquerda, foto 382x546 à direita | seção 03 do molde |
| Oferta | 2 planos (479px, raio 32) lado a lado, itens com check e X, preço 73px | seção 08 do molde |
| Certificado | texto + imagem 560x400 | seção 04 do molde |
| FAQ | `<details>` com chevron que gira | seção 09 do molde |
| Rodapé | logo SVG + 3 linhas | seção 10 do molde |

## O que vale copiar

- **Hero escura** (variante escura do snippet `hero-foto-de-fundo-fade.html`): foto com glow violeta, fade escuro e cards de vidro (`backdrop-filter: blur(14px)`).
- **Mobile da hero:** recorte **aberto** da foto (pessoa menor, com fundo em volta) e posições em `vw` ligadas à proporção do recorte, em vez de `svh`. O texto começa sobre o fim da foto, com o fade por baixo.
- **Logo de texto em SVG inline** (`<svg class="hf-logo" role="img" aria-label="Logo ..."><text>...`): usa as fontes da página e passa no `checar_pagina.py`.
- **Botão pílula dourado** com seta em círculo branco; versão violeta para o plano mais barato.
- **Cards com gradiente escuro** `linear-gradient(189deg,#1E1630,#120E1C)` + borda lavanda a 18%.
- **Plano mais barato** com os itens que faltam riscados e com X (mostra o que o plano completo dá a mais).

## O que NÃO copiar

- Os **dados fictícios**: preços, "+200", links, WhatsApp, IDs de pixel, @ do Instagram.
- O **TM em `<sup>`**: foi para o `checar_pagina.py` não confundir ™ com emoji. O checador já foi corrigido (aceita ™ ® ©), então numa página nova pode usar o símbolo direto.
- O WhatsApp flutuante cobre a seta do botão da hero no celular (390x664). Numa página nova, suba o flutuante ou mostre só depois de rolar.
