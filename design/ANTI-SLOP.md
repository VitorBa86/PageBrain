# PageBrain · Anti-slop: o que denuncia página feita por IA

**Propósito:** lista do que a IA tende a inventar e que **não existe nas páginas da casa**. Tudo aqui saiu do teste real de 19/10/2026 (página da Andressa, Método Renda Bancária), comparado com a referência que o cliente mandou ([construcao2](../paginas/nossas/vendas-mentoria-bancario-jessica-v2/como-usar.md)) e com as 37 páginas medidas.
**Quando usar:** no passo 5 da SKILL (antes de codar) e no checklist final. Se um item daqui aparecer na página, troque pelo que a coluna "Na casa" manda.
**Relacionados:** [MEDIDAS-REAIS.md](MEDIDAS-REAIS.md), [PADRAO-DAVI.md](PADRAO-DAVI.md), [SKILL.md](../SKILL.md)

## A regra que resolve quase tudo

**A página nova é irmã de uma página da casa, não uma criação nova.** Escolha um molde (SKILL, passo 4), abra o `raio-x/` dele e reproduza seção por seção: mesmos componentes, mesmos tamanhos, mesmo botão, mesmo ritmo. Muda a copy, a paleta e as imagens. Se um elemento não existe no molde nem em outra página da casa, ele não entra.

## Proibido (com o que usar no lugar)

| A IA fez | Por que é slop | Na casa |
|---|---|---|
| Interface falsa desenhada em HTML: celular com "9:41", painel "Comissão do mês R$ 4.860 +23%", gráfico de barras "Contratos no mês +18%", "Comissão recebida R$ 1.270,74" | Número inventado (quebra a regra "nada inventado") e cara de template de SaaS | **Imagem real** num slot: print, mockup gerado a partir de print real, ou foto. Se não houver, slot vazio com o prompt |
| Chips flutuando em volta da foto ("Comissão · por contrato fechado", "Direto de casa · no seu horário") | Enfeite genérico de template | Foto limpa; no máximo os elementos 3D da própria arte do cliente, que vêm **dentro da imagem** |
| Botão com ícone de seta dentro de quadradinho branco | Veio da landing do PageBrain (estilo Frontpack), não das páginas de cliente | Botão só com texto, ou texto + ícone solto à direita. 18 a 20px/500, ~58px de altura, raio do molde |
| Título de card em CAIXA ALTA, 24px, peso 800 | Nenhuma página da casa faz isso | Frase normal, 20 a 22px, peso 600 |
| Títulos grandes (H1 44px, H2 36 a 38px) num nicho em que o molde usa 27 a 34px | Ignora o tamanho real da casa | Tamanhos do `raio-x.md` do molde; sem molde, [MEDIDAS-REAIS.md](MEDIDAS-REAIS.md) |
| Rótulo acima do título em 15px, frase normal | O rótulo da casa é outro | Pílula com borda fina, texto em caixa alta 16 a 20px, peso 300 a 500 (copiar do molde) |
| Molduras geométricas em volta das seções (linhas em hexágono), palco com chão em perspectiva, grade de pontos no fundo | Decoração que nenhuma página de cliente usa | Fundo sólido, gradiente da cor da marca, ou **foto de fundo** gerada para a seção (slot de fundo) |
| Selo circular girando com texto, etiquetas "Liberado" com cadeado em cada módulo, faixa "Módulo N" em diagonal | Excesso de enfeite por bloco | Accordion simples ou abas, como no molde (Jéssica: abas "MÓDULO 01" em botões) |
| Seção inteira em branco no meio de página escura sem motivo | Quebra o ritmo da referência | Ritmo de fundos do molde, na mesma ordem |
| Placeholder de depoimento desenhado (ícone de celular + "[CONFIRMAR COM CLIENTE]" em 5 cards) | Fica com cara de rascunho | Slot de imagem com a proporção real do print (ex.: 280x498, 0,56) e o nome do arquivo esperado |
| Card de "dúvida" com Instagram ao lado do FAQ, contadores, selos de "100% seguro" inventados | Conteúdo que o cliente não deu | Só o que está na copy. Falta algo: `[CONFIRMAR COM CLIENTE]` no texto, não um componente novo |
| Menu no topo (navbar, links de âncora, hambúrguer) sem o usuário pedir | Regra fixa do PageBrain (24/10/2026): página do PageBrain não tem menu | Sem menu. Logo na hero, acima do rótulo e do H1. Menu só se o usuário pedir |
| Logo num header separado, no canto, ou fora da hero | Regra fixa do PageBrain | Logo dentro da coluna de texto da hero, logo acima do rótulo e da headline |
| Título quebrando em 5, 6 linhas (fonte grande demais para a coluna, principalmente no celular) | Regra fixa do PageBrain: até 3 linhas, 4 se a frase for longa | Diminuir a fonte (26 a 30px no mobile) ou alargar a coluna. Conferir com `checar_pagina.py` |
| Ícone desenhado à mão em SVG, emoji como ícone, ícones de estilos misturados | Regra fixa do PageBrain: ícones sempre da skill better-icons | `scripts/icone.sh` (lucide, traço 1,6), SVG inline com `currentColor` |
| Foto do expert em moldura (arco, círculo) solta à direita da hero, com selo "+8 anos" por cima | Não é mais o padrão de hero | Hero com foto de fundo e fade (`hero-foto-de-fundo-fade.html`) |
| Fonte, peso e cor variando entre seções | A casa usa uma família e uma escala por página | Uma família (a do molde ou a do briefing), escala fixa do molde |
| Brilhos, glow e sombra coloridos em todo botão e card ao mesmo tempo | Excesso | Um efeito por página no máximo (brilho passando no botão **ou** borda degradê nos cards), como nos snippets da casa |

## Teste rápido antes de entregar

1. Ponha o print do molde e o da página nova lado a lado (`secao-NN.jpg` do molde contra o screenshot da nova). Parecem do mesmo designer?
2. Rode o raio-x na página nova (`python3 scripts/raio_x_molde.py caminho/index.html /tmp/rx`) e compare tamanhos de título, corpo e botão com os do molde. Diferença acima de 4px num título exige justificativa.
3. Procure no HTML: `9:41`, `+23%`, `R$` fora da oferta, `Liberado`, `chip`, `badge-float`, `@keyframes spin`, `<nav`. Cada ocorrência precisa de motivo.
4. Conte os componentes que **não existem** no molde. O ideal é zero; mais de dois, refaça a seção.
5. Rode `python3 scripts/checar_pagina.py pagina.html`: menu, logo acima do H1, linhas de cada título, botão do celular sem rolar e emoji como ícone.
