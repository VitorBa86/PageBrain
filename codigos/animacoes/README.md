# animacoes

**Propósito:** Animações de entrada, de texto e com GSAP.  
**Quando usar:** ao montar uma página e precisar desse tipo de efeito ou componente.  
**Relacionados:** [GUIA-CODIGOS.md](../GUIA-CODIGOS.md), [preview.html](../preview.html), [snippets.json](../snippets.json)

| Snippet | O que faz | Onde colar | Uso nas páginas da casa |
|---|---|---|---|
| [animacao-scroll-reveal.html](animacao-scroll-reveal.html) | Elementos aparecem deslizando e com fade quando entram na tela. É o efeito padrão de todas as páginas da casa. | CSS: CSS personalizado da página. Script: widget HTML no fim da página. | 34 |
| [animacao-scroll-reveal-blur.css](animacao-scroll-reveal-blur.css) | Mesma animação de entrada, mas o elemento começa desfocado (blur 10px) e fica nítido ao entrar. | CSS personalizado da página | 12 |
| [texto-gradiente-animado.css](texto-gradiente-animado.css) | Palavras com gradiente de cor que corre em loop. Usado para destacar a palavra-chave da headline. | CSS personalizado (página ou widget) | 1 |
| [texto-palavras-girando.html](texto-palavras-girando.html) | Frase fixa seguida de uma palavra que troca sozinha (rolando para cima) em loop. | Widget HTML | 0 |
| [texto-destaque-iphone.css](texto-destaque-iphone.css) | Palavra dentro de uma caixinha translúcida com bordas laterais, texto em gradiente e dois pontinhos nos cantos. | CSS personalizado | 1 |
| [gsap-texto-palavras-no-scroll.html](gsap-texto-palavras-no-scroll.html) | Cada palavra do título desce e aparece em sequência conforme a pessoa rola a página. | Widget HTML no fim da página | 2 |
| [gsap-tela-abrindo-3d.html](gsap-tela-abrindo-3d.html) | O container começa deitado (rotateX -90) e vai "abrindo" em 3D enquanto a pessoa rola. Ótimo para mockup de tela. | Widget HTML no fim da página | 1 |
| [linha-que-cresce-ao-aparecer.html](linha-que-cresce-ao-aparecer.html) | Uma linha fina cresce da esquerda para a direita (no celular, de cima para baixo) quando o bloco entra na tela. Usado para ligar etapas. | Widget HTML (CSS pode ir no CSS da página) | 1 |
| [elementos-flutuando.css](elementos-flutuando.css) | Dois elementos (ícones, imagens, selos) sobem e descem suavemente em loop, com ritmos diferentes. | CSS personalizado da página | 1 |

Cada arquivo começa com um comentário padronizado: o que faz, como usar, onde colar, dependências, origem e em quais páginas da casa ele aparece.
