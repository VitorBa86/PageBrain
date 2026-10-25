# Como usar: PÁGINA PSI [LUANA CAROLINA · CASAIS]

**Propósito:** página de referência aprovada pelo usuário em 24/10/2026. É o exemplo vivo das regras fixas do PageBrain (sem menu, logo acima da headline, títulos em até 3 linhas, ícones da skill better-icons, hero com foto de fundo e fade no desktop e no mobile).
**Quando usar:** em **toda** página nova, como referência de hero, de tamanho de título e de ícones, qualquer que seja o nicho. Para o resto do layout, ela também serve de molde em psicologia, terapia e saúde com visual creme e café.
**Relacionados:** [extraido/index.html](extraido/index.html) (abrir no navegador), [raio-x/raio-x.md](raio-x/raio-x.md), [copy.md](copy.md), [ficha.json](ficha.json), [SKILL.md](../../../SKILL.md), [hero-foto-de-fundo-fade.html](<../../../codigos/fundos-e-texturas/hero-foto-de-fundo-fade.html>)

- **Origem:** página de teste do PageBrain, feita com o PageBrain e ajustada com o usuário até a aprovação. Publicada na Vercel como teste.
- **Dados:** **fictícios** (WhatsApp 5500000000000, CRP 00/000000, e-mail, Instagram). Nunca copie esses dados.
- **Nicho:** Psicologia (terapia de casal) · **Tipo de página:** captação · **Relevância:** 5/5 como referência de padrão

## O que esta página fixou (vale para toda página do PageBrain)

| Regra | Como está feito aqui |
|---|---|
| **Sem menu** | Não há `<nav>` nem link no topo. Menu só entra se o usuário pedir. |
| **Logo acima da headline** | Logo (52px de altura no desktop, 28px no mobile) logo acima do rótulo e do H1, dentro da coluna de texto da hero. |
| **Títulos em até 3 linhas** | H1 46px desktop / 29px mobile; H2 até 48px desktop / 26px mobile. Nenhum título passa de 3 linhas na coluna dele (4 só em frase longa). Teto absoluto: 55px. |
| **Ícones da skill better-icons** | Os 6 cards de "para quem é" usam lucide (`messages-square`, `heart-crack`, `house-heart`, `flame`, `signpost`, `gem`), traço 1,6, dentro de círculo creme com cor vinho. Pegos com `scripts/icone.sh`. |
| **Hero com foto de fundo e fade** | Desktop: foto 16:9 em cover, pessoa à direita, fade creme da esquerda até 58%. Mobile: recorte quase quadrado da mesma foto, centralizado no corpo, largura total no topo; rosto e tronco nítidos acima da logo; conteúdo começa em 44svh; o botão aparece sem rolar (termina em 635px numa tela de 390x664). Snippet: [hero-foto-de-fundo-fade.html](<../../../codigos/fundos-e-texturas/hero-foto-de-fundo-fade.html>). |

## Estrutura de seções (na ordem)

1. **hero** (foto de fundo + fade): logo, rótulo, H1 com 2 palavras em cor, sub, botão, 3 selos informativos abaixo do botão.
2. **dor**: H2 centralizado com final em cor, parágrafo, seta, caixa de impacto com frase grande.
3. **para quem é** (fundo creme): 6 cards em 2 colunas com borda esquerda caramelo, ícone em círculo, número e texto.
4. **como funciona** (fundo café escuro): 5 passos em cards escuros com número grande, palavra fantasma ao fundo.
5. **diferenciais**: foto à esquerda + lista de 4 itens com ícone em card com borda vinho.
6. **frase de destaque** + faixa de texto correndo (marquee).
7. **sobre**: texto à esquerda, foto à direita, citação com borda, botão; galeria de 3 fotos abaixo.
8. **FAQ** em `<details>` com botão "+" que gira.
9. **CTA final** (fundo café) com logo clara e botão de WhatsApp.
10. **rodapé** curto + botão flutuante de WhatsApp.

## Design em números

- **Fundos:** `#FBF7F1` (papel), `#F4ECE2` (creme), `#3A2A22` (café escuro), `#2C1F19` (rodapé)
- **Textos:** `#3A2A22` (títulos), `#6F5D51` (corpo)
- **Destaques:** `#7A2320` (vinho, palavras do H1 e ícones), `#9E6644` (caramelo, rótulos e palavras dos H2), `#C49A78` (tan, números)
- **Fonte:** Inter em tudo. Títulos 600, corpo 400. Destaque de palavra **só por cor** (sem itálico, sem serifa).
- **Escala desktop:** H1 46 · H2 48 · frase de impacto 36 · título de card 18 a 20 · corpo 17 a 18 · rótulo 12 (caixa alta, espaçado)
- **Escala mobile:** H1 29 · H2 26 · sobre 30 · corpo 14,5 a 16 · rótulo 11
- **Botão:** gradiente caramelo `linear-gradient(120deg,#87533A,#B98663 45%,#D2AE8D 55%,#9E6644)`, 13px/600 caixa alta, padding 20px 34px, raio 4px, seta solta à direita, largura total no mobile
- **Cards:** fundo papel, borda esquerda 2px caramelo, raio 0 6px 6px 0, sombra `0 18px 40px -30px rgba(58,42,34,.45)`, sobe 4px no hover
- **Largura do conteúdo:** 1160px · **padding de seção:** 110px desktop, 84px mobile

## O que vale copiar

- A hero inteira (snippet pronto) e a regra de recorte separado para o mobile.
- Ícone em círculo claro que inverte a cor no hover do card.
- Ritmo de fundos: papel, creme, café escuro, papel, gradiente, creme, café.
- Rótulo pequeno em caixa alta acima de cada H2.

## O que NÃO copiar

- **Selo circular com texto girando** (seções diferenciais e sobre): está na [ANTI-SLOP.md](../../../design/ANTI-SLOP.md) como proibido. Ficou nesta página de teste, mas não leve para páginas novas.
- **A pessoa da foto de fundo da hero** foi gerada por IA (Nano Banana Pro) e não é a psicóloga das outras fotos. Em página real, a hero usa a foto do cliente ou uma composição feita **com a foto do cliente como referência** (imagens-ia/README.md).
- Dados fictícios (WhatsApp, CRP, e-mail, Instagram).
- Botão em caixa alta: aqui foi escolha do teste. Em captação a casa usa frase normal na maioria das páginas (MEDIDAS-REAIS.md).
