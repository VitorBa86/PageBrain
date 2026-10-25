# cards-e-bordas

**Propósito:** Acabamentos de card: bordas degradê, faixas, ribbons, vidro, hover.  
**Quando usar:** ao montar uma página e precisar desse tipo de efeito ou componente.  
**Relacionados:** [GUIA-CODIGOS.md](../GUIA-CODIGOS.md), [preview.html](../preview.html), [snippets.json](../snippets.json)

| Snippet | O que faz | Onde colar | Uso nas páginas da casa |
|---|---|---|---|
| [card-borda-degrade.css](card-borda-degrade.css) | Card translúcido com borda de 1px que vai de branco a transparente. Visual "glass" para fundos escuros. | CSS personalizado do container | 5 |
| [card-3d-parallax.css](card-3d-parallax.css) | Prepara o card para efeito 3D (transform-style preserve-3d) e mostra uma sombra radial no hover. | CSS personalizado | 0 |
| [faixa-glow-topo-card.css](faixa-glow-topo-card.css) | Uma barra colorida de 5px com brilho (glow) centralizada no topo do card ou seção. | CSS personalizado da página | 1 |
| [linha-glow-canto-card.css](linha-glow-canto-card.css) | Tracinho de 50px com glow no topo esquerdo do card, detalhe de acabamento. | CSS personalizado da página | 0 |
| [ribbon-mais-vendido.css](ribbon-mais-vendido.css) | Fita diagonal no canto do card de oferta com o texto definido na variável --text. | CSS personalizado da página | 0 |
| [cards-expansiveis-hover.html](cards-expansiveis-hover.html) | Cards de tema (ex.: ansiedade, depressão) que mostram uma lista escondida ao passar o mouse; no celular abrem com toque. | Widget HTML | 1 |
| [vidro-fosco.css](vidro-fosco.css) | Desfoca o que está atrás do container. Usado em cards e menus sobre foto ou vídeo. | CSS personalizado do container | 11 |
| [hover-escala.css](hover-escala.css) | O container aumenta 5% ao passar o mouse. | CSS personalizado do container | 6 |

## Observações

- **card-3d-parallax**: O original só tem CSS. A inclinação seguindo o mouse precisaria de um JavaScript que não está no acervo, então hoje o efeito visível é apenas a sombra no hover. Para borda brilhando, use card-borda-degrade.

Cada arquivo começa com um comentário padronizado: o que faz, como usar, onde colar, dependências, origem e em quais páginas da casa ele aparece.
