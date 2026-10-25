# PageBrain · Guia de códigos úteis

**Propósito:** catálogo de todos os snippets de código usados nas landing pages da casa (O Rei da Landing).  
**Quando usar:** ao montar ou converter uma página, para reaproveitar código testado em vez de escrever do zero.  
**Relacionados:** [preview.html](preview.html) (ver funcionando), [snippets.json](snippets.json) (índice de máquina), [PADRAO-DAVI.md](<../design/PADRAO-DAVI.md>)

## Como esta pasta foi montada

- **68 snippets** em 15 categorias (o 68º, `hero-foto-de-fundo-fade`, veio da referência de padrão `psi-luana-carolina-casais` em 24/10/2026).
- 22 vieram da coleção original de códigos da casa (Notion). Os demais foram **extraídos das 37 páginas publicadas da casa** (widgets HTML e CSS personalizado marcados pelo Elementor). Cada arquivo diz de onde veio.
- A coluna "Uso" conta em quantas das 37 páginas da casa o código aparece. Ela mostra o que é padrão de verdade e o que é exceção.
- Arquivos `.elementor.json` são para colar direto no Elementor: botão direito no editor > **Colar de outro site**.
- Onde o código fala em `selector`, ele deve ir no **CSS personalizado do próprio widget/container** (o Elementor troca `selector` pelo elemento).

## Os 6 que entram em toda página

1. [utilitarios-css/css-base-toda-pagina.css](utilitarios-css/css-base-toda-pagina.css): CSS base no CSS da página.
2. [animacoes/animacao-scroll-reveal.html](animacoes/animacao-scroll-reveal.html): classes `scroll-*` e script no rodapé (ou a variação com blur).
3. [whatsapp-e-flutuantes/link-whatsapp-com-mensagem.html](whatsapp-e-flutuantes/link-whatsapp-com-mensagem.html): link de todos os CTAs.
4. [tracking-e-pixels/meta-pixel.html](tracking-e-pixels/meta-pixel.html) e [tracking-e-pixels/google-ads-gtag.html](tracking-e-pixels/google-ads-gtag.html).
5. [utilitarios-css/elemento-posicao-absoluta.css](utilitarios-css/elemento-posicao-absoluta.css) e [utilitarios-css/botao-icone-tamanho.css](utilitarios-css/botao-icone-tamanho.css), quando houver decoração solta ou ícone no botão.
6. [fundos-e-texturas/hero-foto-de-fundo-fade.html](fundos-e-texturas/hero-foto-de-fundo-fade.html): hero padrão do PageBrain (foto de fundo com fade no desktop, recorte próprio no mobile, logo acima do H1, sem menu). Regra fixa do PageBrain de 24/10/2026.

**Ícones:** não há snippet de ícone. Todo ícone vem da skill better-icons pelo script [`scripts/icone.sh`](<../scripts/icone.sh>) (`scripts/icone.sh buscar "termo"` e `scripts/icone.sh pegar lucide:nome`), colado como SVG inline.

**Menus** (`menus-e-headers/`): só entram quando o usuário pedir menu. Por padrão a página não tem menu.


## Tabela completa

| Snippet | Categoria | Descrição curta | Arquivo | Uso |
|---|---|---|---|---|
| Botão com faixa de brilho passando | botoes | Uma faixa branca inclinada atravessa o botão em loop a cada 3s. Chama atenção para o CTA sem mudar a cor do botão. | [botoes/botao-brilho-passando.css](botoes/botao-brilho-passando.css) | 3 |
| Botão com borda de luz girando (conic) | botoes | Botão pílula azul com uma luz que percorre a borda continuamente; no hover acelera e sobe 2px. | [botoes/botao-borda-girando-conic.css](botoes/botao-borda-girando-conic.css) | 2 |
| Botão glow roxo com borda pontilhada | botoes | Botão pílula escuro que acende em roxo com gradiente radial e borda de pontinhos animada. | [botoes/botao-glow-roxo-pontilhado.html](botoes/botao-glow-roxo-pontilhado.html) | 0 |
| Botão escuro com blob azul | botoes | Botão escuro com gradiente radial metálico e uma mancha (blob) azul neon no canto. | [botoes/botao-blob-gradiente-escuro.html](botoes/botao-blob-gradiente-escuro.html) | 0 |
| Botão gradiente azul que desliza no hover | botoes | Botão com gradiente azul claro/escuro, sombra interna e o gradiente desliza ao passar o mouse. | [botoes/botao-gradiente-azul-deslizante.css](botoes/botao-gradiente-azul-deslizante.css) | 0 |
| Botão 3D inclinado | botoes | Botão azul inclinado em perspectiva que "afunda" no hover e no clique. | [botoes/botao-3d-perspectiva.css](botoes/botao-3d-perspectiva.css) | 0 |
| Botão shiny com borda cônica girando | botoes | Botão preto pílula com borda de luz que gira (conic-gradient), pontinhos internos e brilho que respira no hover. | [botoes/botao-shiny-borda-conica.css](botoes/botao-shiny-borda-conica.css) | 0 |
| Animação de entrada no scroll (scroll-left/right/top/bottom) | animacoes | Elementos aparecem deslizando e com fade quando entram na tela. É o efeito padrão de todas as páginas da casa. | [animacoes/animacao-scroll-reveal.html](animacoes/animacao-scroll-reveal.html) | 34 |
| Animação de entrada no scroll com blur | animacoes | Mesma animação de entrada, mas o elemento começa desfocado (blur 10px) e fica nítido ao entrar. | [animacoes/animacao-scroll-reveal-blur.css](animacoes/animacao-scroll-reveal-blur.css) | 12 |
| Texto que aparece palavra por palavra no scroll (GSAP) | animacoes | Cada palavra do título desce e aparece em sequência conforme a pessoa rola a página. | [animacoes/gsap-texto-palavras-no-scroll.html](animacoes/gsap-texto-palavras-no-scroll.html) | 2 |
| Texto com gradiente animado (destaque / brilho) | animacoes | Palavras com gradiente de cor que corre em loop. Usado para destacar a palavra-chave da headline. | [animacoes/texto-gradiente-animado.css](animacoes/texto-gradiente-animado.css) | 1 |
| Texto destaque estilo iPhone | animacoes | Palavra dentro de uma caixinha translúcida com bordas laterais, texto em gradiente e dois pontinhos nos cantos. | [animacoes/texto-destaque-iphone.css](animacoes/texto-destaque-iphone.css) | 1 |
| Imagem que abre como tela de notebook (GSAP) | animacoes | O container começa deitado (rotateX -90) e vai "abrindo" em 3D enquanto a pessoa rola. Ótimo para mockup de tela. | [animacoes/gsap-tela-abrindo-3d.html](animacoes/gsap-tela-abrindo-3d.html) | 1 |
| Linha que cresce quando aparece na tela | animacoes | Uma linha fina cresce da esquerda para a direita (no celular, de cima para baixo) quando o bloco entra na tela. Usado para ligar etapas. | [animacoes/linha-que-cresce-ao-aparecer.html](animacoes/linha-que-cresce-ao-aparecer.html) | 1 |
| Elementos decorativos flutuando | animacoes | Dois elementos (ícones, imagens, selos) sobem e descem suavemente em loop, com ritmos diferentes. | [animacoes/elementos-flutuando.css](animacoes/elementos-flutuando.css) | 1 |
| Texto com palavras girando | animacoes | Frase fixa seguida de uma palavra que troca sozinha (rolando para cima) em loop. | [animacoes/texto-palavras-girando.html](animacoes/texto-palavras-girando.html) | 0 |
| Barra de progresso com número animado | contadores-e-progresso | Barra que enche até X% e número que conta de 0 até X quando a seção aparece. Usada para "andamento da obra". | [contadores-e-progresso/barra-progresso-animada.html](contadores-e-progresso/barra-progresso-animada.html) | 1 |
| Scroll suave (Lenis) | efeitos-de-scroll | Deixa a rolagem da página suave e com inércia, sensação de site premium. | [efeitos-de-scroll/lenis-scroll-suave.html](efeitos-de-scroll/lenis-scroll-suave.html) | 3 |
| Menu some ao rolar (GSAP) | efeitos-de-scroll | O menu fixo sobe e desaparece quando a pessoa passa de 60% da página, e volta ao rolar para cima. | [efeitos-de-scroll/gsap-menu-some-no-scroll.html](efeitos-de-scroll/gsap-menu-some-no-scroll.html) | 1 |
| Vidro fosco (backdrop blur) | cards-e-bordas | Desfoca o que está atrás do container. Usado em cards e menus sobre foto ou vídeo. | [cards-e-bordas/vidro-fosco.css](cards-e-bordas/vidro-fosco.css) | 11 |
| Card que cresce no hover | cards-e-bordas | O container aumenta 5% ao passar o mouse. | [cards-e-bordas/hover-escala.css](cards-e-bordas/hover-escala.css) | 6 |
| Card de vidro com borda degradê | cards-e-bordas | Card translúcido com borda de 1px que vai de branco a transparente. Visual "glass" para fundos escuros. | [cards-e-bordas/card-borda-degrade.css](cards-e-bordas/card-borda-degrade.css) | 5 |
| Faixa luminosa no topo do card | cards-e-bordas | Uma barra colorida de 5px com brilho (glow) centralizada no topo do card ou seção. | [cards-e-bordas/faixa-glow-topo-card.css](cards-e-bordas/faixa-glow-topo-card.css) | 1 |
| Cards que abrem a lista no hover (clique no celular) | cards-e-bordas | Cards de tema (ex.: ansiedade, depressão) que mostram uma lista escondida ao passar o mouse; no celular abrem com toque. | [cards-e-bordas/cards-expansiveis-hover.html](cards-e-bordas/cards-expansiveis-hover.html) | 1 |
| Card 3D parallax | cards-e-bordas | Prepara o card para efeito 3D (transform-style preserve-3d) e mostra uma sombra radial no hover. | [cards-e-bordas/card-3d-parallax.css](cards-e-bordas/card-3d-parallax.css) | 0 |
| Linha curta luminosa no canto do card | cards-e-bordas | Tracinho de 50px com glow no topo esquerdo do card, detalhe de acabamento. | [cards-e-bordas/linha-glow-canto-card.css](cards-e-bordas/linha-glow-canto-card.css) | 0 |
| Faixa diagonal "MAIS VENDIDO" no card de preço | cards-e-bordas | Fita diagonal no canto do card de oferta com o texto definido na variável --text. | [cards-e-bordas/ribbon-mais-vendido.css](cards-e-bordas/ribbon-mais-vendido.css) | 0 |
| Largura fixa das imagens do carrossel | faixas-e-carrosseis | Força a largura da imagem dentro de cada slide do Carrossel de Imagens. | [faixas-e-carrosseis/carrossel-imagem-largura.css](faixas-e-carrosseis/carrossel-imagem-largura.css) | 8 |
| Carrossel de imagens/logos em movimento contínuo | faixas-e-carrosseis | Faz o Carrossel de Imagens do Elementor andar sem pausa e sem aceleração (efeito esteira). Configure autoplay com velocidade alta (ex.: 5000ms) e intervalo 0. | [faixas-e-carrosseis/carrossel-linear-continuo.css](faixas-e-carrosseis/carrossel-linear-continuo.css) | 7 |
| Faixa (marquee) infinita com lista de ícones | faixas-e-carrosseis | Faixa horizontal que corre sem parar com frases separadas por ícone. Usada logo abaixo do hero ou entre seções. | [faixas-e-carrosseis/faixa-animada-infinita.html](faixas-e-carrosseis/faixa-animada-infinita.html) | 5 |
| Galeria que vira carrossel automático no celular | faixas-e-carrosseis | No celular, transforma um container de imagens em faixa horizontal que rola sozinha (pausa ao tocar). No desktop não faz nada. | [faixas-e-carrosseis/carrossel-mobile-autoscroll.html](faixas-e-carrosseis/carrossel-mobile-autoscroll.html) | 1 |
| Carrossel de avaliações do Google | faixas-e-carrosseis | Bloco com nota geral à esquerda e cards de avaliações rolando à direita, no visual do Google. | [faixas-e-carrosseis/carrossel-avaliacoes-google.html](faixas-e-carrosseis/carrossel-avaliacoes-google.html) | 1 |
| Carrossel com fade nas laterais | faixas-e-carrosseis | Escurece as bordas esquerda e direita do carrossel, dando efeito de que as imagens somem nas pontas. | [faixas-e-carrosseis/carrossel-fade-lateral.css](faixas-e-carrosseis/carrossel-fade-lateral.css) | 0 |
| Hero com foto de fundo e fade (padrão PageBrain) | fundos-e-texturas | Foto em tela cheia com fade da cor de fundo à esquerda no desktop; no celular, recorte centralizado na pessoa no topo, corpo acima da logo e botão visível sem rolar. Sem menu, logo acima do H1. | [fundos-e-texturas/hero-foto-de-fundo-fade.html](fundos-e-texturas/hero-foto-de-fundo-fade.html) | 1 |
| Textura quadriculada com luz no topo | fundos-e-texturas | Grade de linhas finas sobre fundo preto que some de cima para baixo, com uma luz branca desfocada no topo. | [fundos-e-texturas/textura-quadriculada.css](fundos-e-texturas/textura-quadriculada.css) | 1 |
| Linhas verticais com luz descendo | fundos-e-texturas | Duas linhas finas fixas nas laterais da tela com um feixe de luz que desce em loop. Fundo de página escura premium. | [fundos-e-texturas/linhas-verticais-animadas.html](fundos-e-texturas/linhas-verticais-animadas.html) | 1 |
| Fundo com gradientes animados e ruído | fundos-e-texturas | Fundo escuro com manchas de cor que se movem e textura de ruído, com um card de vidro por cima. | [fundos-e-texturas/fundo-gradiente-animado.html](fundos-e-texturas/fundo-gradiente-animado.html) | 0 |
| Menu mobile em tela cheia (script) | menus-e-headers | Abre um container de menu por cima da página, trava a rolagem e fecha ao clicar no X ou em um link. | [menus-e-headers/menu-mobile-tela-cheia.html](menus-e-headers/menu-mobile-tela-cheia.html) | 1 |
| Menu pílula flutuante (Inter Frios) | menus-e-headers | Menu em formato de pílula fixa no topo, logo dentro do menu e CTA escuro na ponta. Painel próprio no celular. | [menus-e-headers/menu-pilula-flutuante-interfrios.html](menus-e-headers/menu-pilula-flutuante-interfrios.html) | 1 |
| Header fixo com WhatsApp flutuante (Vega) | menus-e-headers | Header fixo com menu, menu mobile em overlay e botão flutuante de WhatsApp. | [menus-e-headers/header-fixo-vega.html](menus-e-headers/header-fixo-vega.html) | 1 |
| Menu com drawer lateral no celular (Santa Boemia) | menus-e-headers | Navbar no desktop e gaveta (drawer) lateral no celular, com tokens de cor da marca e reset defensivo contra o tema. | [menus-e-headers/menu-drawer-santa-boemia.html](menus-e-headers/menu-drawer-santa-boemia.html) | 1 |
| Menu transparente que vira pílula ao rolar (Maria Rita) | menus-e-headers | No topo é uma barra transparente com texto branco; ao rolar vira uma pílula branca flutuante. No celular abre painel de baixo para cima. | [menus-e-headers/menu-transparente-vira-pilula.html](menus-e-headers/menu-transparente-vira-pilula.html) | 1 |
| Rodapé card inset com logo grande (Inter Frios) | rodapes | Rodapé completo autocontido (HTML + CSS) com navegação, contatos e redes, responsivo. | [rodapes/rodape-card-inset-interfrios.html](rodapes/rodape-card-inset-interfrios.html) | 1 |
| Rodapé com CTA e WhatsApp (Vega) | rodapes | Rodapé completo autocontido (HTML + CSS) com navegação, contatos e redes, responsivo. | [rodapes/rodape-vega.html](rodapes/rodape-vega.html) | 1 |
| Rodapé 3 colunas (Maria Rita) | rodapes | Rodapé completo autocontido (HTML + CSS) com navegação, contatos e redes, responsivo. | [rodapes/rodape-tres-colunas-maria-rita.html](rodapes/rodape-tres-colunas-maria-rita.html) | 1 |
| Rodapé com marca d'água (Rosangela) | rodapes | Rodapé completo autocontido (HTML + CSS) com navegação, contatos e redes, responsivo. | [rodapes/rodape-marca-dagua-rosangela.html](rodapes/rodape-marca-dagua-rosangela.html) | 1 |
| Linha do tempo de etapas com scroll (Renan) | secoes-prontas | Timeline vertical com eixo central e cards alternando esquerda/direita, que se revelam com o scroll. Ideal para "como funciona". | [secoes-prontas/linha-do-tempo-etapas.html](secoes-prontas/linha-do-tempo-etapas.html) | 1 |
| Seção de método com cartas voando no scroll (Maria Rita) | secoes-prontas | Seção sticky de ~9 telas em que cartas com as etapas do método entram voando conforme a rolagem. | [secoes-prontas/metodo-cartas-voando-scroll.html](secoes-prontas/metodo-cartas-voando-scroll.html) | 1 |
| FAQ em duas colunas (acordeão próprio) | secoes-prontas | Perguntas frequentes em duas colunas com abrir/fechar animado, sem depender do widget Acordeão. | [secoes-prontas/faq-duas-colunas.html](secoes-prontas/faq-duas-colunas.html) | 1 |
| Gráfico de barras de valorização (Vega) | secoes-prontas | Gráfico de barras em HTML/CSS puro com títulos e fonte dos dados. Para lançamento imobiliário mostrar valorização da região. | [secoes-prontas/grafico-valorizacao-barras.html](secoes-prontas/grafico-valorizacao-barras.html) | 1 |
| Gráfico de crescimento de faturamento (Workshop) | secoes-prontas | Gráfico escuro com barras/linha de faturamento e destaque laranja, para página de vendas mostrar resultado. | [secoes-prontas/grafico-faturamento.html](secoes-prontas/grafico-faturamento.html) | 1 |
| Tour 360 incorporado (Momento360) | secoes-prontas | Incorpora um tour 360 do Momento360 com cantos arredondados e altura responsiva. | [secoes-prontas/tour-360-momento360.html](secoes-prontas/tour-360-momento360.html) | 1 |
| Forçar autoplay de vídeo no iPhone | video-e-midia | Garante que vídeos de fundo do Elementor toquem no iOS (muted, playsinline) e, se bloqueado, toca no primeiro toque. | [video-e-midia/video-autoplay-ios.html](video-e-midia/video-autoplay-ios.html) | 1 |
| Vídeo que liga o som e abre em tela cheia ao clicar | video-e-midia | Ao clicar no container do vídeo (iframe YouTube mudo em autoplay), troca para som ligado e abre em tela cheia. | [video-e-midia/video-clique-som-tela-cheia.html](video-e-midia/video-clique-som-tela-cheia.html) | 1 |
| Tela de carregamento com logo | video-e-midia | Tela cheia escura com a logo entrando e sumindo quando a página carrega. | [video-e-midia/preloader-com-logo.html](video-e-midia/preloader-com-logo.html) | 1 |
| Botão que abre e fecha um container | interacoes | Função makeToggle: botões alternam a classe "ativo" num container (ex.: "ver mais" de um card). Estilize .ativo no CSS. | [interacoes/toggle-abrir-fechar-container.html](interacoes/toggle-abrir-fechar-container.html) | 1 |
| Container inteiro clicável | interacoes | Faz qualquer elemento com a classe "link-site" abrir um link em nova aba. | [interacoes/container-clicavel-link.html](interacoes/container-clicavel-link.html) | 1 |
| Link de WhatsApp com mensagem pronta | whatsapp-e-flutuantes | Padrão de link usado em todos os botões de CTA: wa.me + número + mensagem codificada. | [whatsapp-e-flutuantes/link-whatsapp-com-mensagem.html](whatsapp-e-flutuantes/link-whatsapp-com-mensagem.html) | 16 |
| Botão flutuante de WhatsApp com Lottie | whatsapp-e-flutuantes | Ícone animado (Lottie) fixo no canto da tela que leva ao WhatsApp. | [whatsapp-e-flutuantes/whatsapp-flutuante-lottie.md](whatsapp-e-flutuantes/whatsapp-flutuante-lottie.md) | 3 |
| Pixel da Meta (Facebook) | tracking-e-pixels | Código base do Pixel com PageView. Presente em 27 das 37 páginas. | [tracking-e-pixels/meta-pixel.html](tracking-e-pixels/meta-pixel.html) | 27 |
| Tag do Google Ads (gtag) | tracking-e-pixels | Tag global do Google Ads. Presente em 25 páginas (todas com o mesmo ID de conta AW da casa). | [tracking-e-pixels/google-ads-gtag.html](tracking-e-pixels/google-ads-gtag.html) | 25 |
| Google Tag Manager | tracking-e-pixels | Container do GTM. Usado em 3 páginas de domínio próprio do cliente. | [tracking-e-pixels/google-tag-manager.html](tracking-e-pixels/google-tag-manager.html) | 3 |
| CSS base de toda página (o que sempre uso) | utilitarios-css | Seleção de texto discreta, sem rolagem horizontal, sem margem no último parágrafo e barra de rolagem personalizada. Vai em TODAS as páginas. | [utilitarios-css/css-base-toda-pagina.css](utilitarios-css/css-base-toda-pagina.css) | 33 |
| Elemento solto (posição absoluta) | utilitarios-css | Tira o widget do fluxo para sobrepor decorações, selos e imagens. É o CSS custom mais comum depois do CSS base (24 páginas). | [utilitarios-css/elemento-posicao-absoluta.css](utilitarios-css/elemento-posicao-absoluta.css) | 27 |
| Tamanho do ícone SVG no botão | utilitarios-css | Aumenta o ícone (ex.: WhatsApp) dentro do botão do Elementor e centraliza com o texto. | [utilitarios-css/botao-icone-tamanho.css](utilitarios-css/botao-icone-tamanho.css) | 12 |
| Borda arredondada nos itens do FAQ (Alternar/Acordeão) | utilitarios-css | Arredonda o título de cada item do widget Alternar/Acordeão. | [utilitarios-css/faq-toggle-arredondado.css](utilitarios-css/faq-toggle-arredondado.css) | 10 |
| Dropdown do Menu de Navegação centralizado no celular | utilitarios-css | Faz o menu suspenso do widget Menu de Navegação ocupar 90% da tela e ficar centralizado. | [utilitarios-css/menu-dropdown-mobile-centralizado.css](utilitarios-css/menu-dropdown-mobile-centralizado.css) | 1 |
| Barra de rolagem colorida (variação) | utilitarios-css | Variação da barra de rolagem com trilho e thumb coloridos. | [utilitarios-css/scrollbar-colorida.css](utilitarios-css/scrollbar-colorida.css) | 0 |

## Origem dos snippets

22 snippets vieram da coleção original de códigos da casa (exportada do Notion) e foram limpos: o `botao6` perdia o CSS de demonstração que pintava a página inteira, o `fundoanimado` trava a rolagem por causa de `overflow: hidden` no body (avisado no snippet), o `card3d` não tem o JavaScript da inclinação (só o CSS de apoio) e o antigo `cardcantodegrade` era cópia do `card3d` (o efeito de borda brilhando está em `card-borda-degrade.css`). Os outros foram extraídos das páginas publicadas da casa. A origem de cada um está no cabeçalho do arquivo e no campo `origem` de [snippets.json](snippets.json).
