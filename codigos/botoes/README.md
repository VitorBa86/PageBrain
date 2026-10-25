# botoes

**Propósito:** Botões de CTA com efeitos (glow, brilho, 3D, borda girando).  
**Quando usar:** ao montar uma página e precisar desse tipo de efeito ou componente.  
**Relacionados:** [GUIA-CODIGOS.md](../GUIA-CODIGOS.md), [preview.html](../preview.html), [snippets.json](../snippets.json)

| Snippet | O que faz | Onde colar | Uso nas páginas da casa |
|---|---|---|---|
| [botao-glow-roxo-pontilhado.html](botao-glow-roxo-pontilhado.html) + [botao-glow-roxo-pontilhado.elementor.json](botao-glow-roxo-pontilhado.elementor.json) | Botão pílula escuro que acende em roxo com gradiente radial e borda de pontinhos animada. | Widget HTML do Elementor (ou JSON colado) | 0 |
| [botao-blob-gradiente-escuro.html](botao-blob-gradiente-escuro.html) + [botao-blob-gradiente-escuro.elementor.json](botao-blob-gradiente-escuro.elementor.json) | Botão escuro com gradiente radial metálico e uma mancha (blob) azul neon no canto. | Widget HTML do Elementor (ou JSON colado) | 0 |
| [botao-gradiente-azul-deslizante.css](botao-gradiente-azul-deslizante.css) | Botão com gradiente azul claro/escuro, sombra interna e o gradiente desliza ao passar o mouse. | CSS personalizado da página (ou do widget) | 0 |
| [botao-3d-perspectiva.css](botao-3d-perspectiva.css) | Botão azul inclinado em perspectiva que "afunda" no hover e no clique. | CSS personalizado do widget Botão | 0 |
| [botao-brilho-passando.css](botao-brilho-passando.css) | Uma faixa branca inclinada atravessa o botão em loop a cada 3s. Chama atenção para o CTA sem mudar a cor do botão. | CSS personalizado do widget Botão | 3 |
| [botao-shiny-borda-conica.css](botao-shiny-borda-conica.css) | Botão preto pílula com borda de luz que gira (conic-gradient), pontinhos internos e brilho que respira no hover. | CSS personalizado da página | 0 |
| [botao-borda-girando-conic.css](botao-borda-girando-conic.css) | Botão pílula azul com uma luz que percorre a borda continuamente; no hover acelera e sobe 2px. | CSS personalizado da página | 2 |

## Observações

- **botao-shiny-borda-conica**: O original terminava com regras de demonstração para html e body (display:grid, fundo #02040c) que quebram o layout da página. Elas foram removidas aqui.

Cada arquivo começa com um comentário padronizado: o que faz, como usar, onde colar, dependências, origem e em quais páginas da casa ele aparece.
