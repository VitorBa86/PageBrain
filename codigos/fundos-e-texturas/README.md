# fundos-e-texturas

**Propósito:** Fundos animados, texturas e linhas decorativas.  
**Quando usar:** ao montar uma página e precisar desse tipo de efeito ou componente.  
**Relacionados:** [GUIA-CODIGOS.md](../GUIA-CODIGOS.md), [preview.html](../preview.html), [snippets.json](../snippets.json)

| Snippet | O que faz | Onde colar | Uso nas páginas da casa |
|---|---|---|---|
| [hero-foto-de-fundo-fade.html](hero-foto-de-fundo-fade.html) | **Hero padrão do PageBrain.** Foto de fundo com fade no desktop e recorte próprio no mobile, logo acima do H1, sem menu, botão visível sem rolar. | Container da hero (ou widget HTML) | 1 (referência psi-luana-carolina-casais) |
| [fundo-gradiente-animado.html](fundo-gradiente-animado.html) + [fundo-gradiente-animado.elementor.json](fundo-gradiente-animado.elementor.json) | Fundo escuro com manchas de cor que se movem e textura de ruído, com um card de vidro por cima. | Widget HTML | 0 |
| [textura-quadriculada.css](textura-quadriculada.css) | Grade de linhas finas sobre fundo preto que some de cima para baixo, com uma luz branca desfocada no topo. | CSS personalizado do container da seção | 1 |
| [linhas-verticais-animadas.html](linhas-verticais-animadas.html) | Duas linhas finas fixas nas laterais da tela com um feixe de luz que desce em loop. Fundo de página escura premium. | Widget HTML + CSS personalizado da página | 1 |

## Observações

- **fundo-gradiente-animado**: Não foi encontrado em nenhuma página publicada. O CSS aplica overflow:hidden no body, o que trava a rolagem; ajuste antes de usar em página real.

Cada arquivo começa com um comentário padronizado: o que faz, como usar, onde colar, dependências, origem e em quais páginas da casa ele aparece.
