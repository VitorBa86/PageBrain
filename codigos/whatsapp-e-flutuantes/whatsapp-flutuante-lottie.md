# Botão flutuante de WhatsApp com Lottie

<!--
  SNIPPET: Botão flutuante de WhatsApp com Lottie
  CATEGORIA: whatsapp-e-flutuantes
  O QUE FAZ: Ícone animado (Lottie) fixo no canto da tela que leva ao WhatsApp.
  COMO USAR: Configuração no Elementor, sem código. Veja o passo a passo neste arquivo.
  ONDE COLAR: Widget Lottie do Elementor
  DEPENDÊNCIAS: Arquivo JSON da animação (Animation-1714580339459.json, presente nos sites)
  ORIGEM: paginas/nossas/imob-mb2-incorporacoes e psi-julia-valdetaro
  USADO EM: 3 página(s) da casa: imob-mb2-incorporacoes, imob-vistoria-alphaville, psi-julia-valdetaro
-->

## Configuração encontrada nas páginas

1. Arraste um widget **Lottie**.
2. Fonte: arquivo de mídia, o JSON `Animation-1714580339459.json` (animação de ícone de WhatsApp; nos sites está em `/wp-content/uploads/`).
3. Link: personalizado, `https://api.whatsapp.com/send?phone=55DDDNUMERO&text=...`.
4. Loop: sim. Gatilho: ao chegar na viewport. Renderizador: SVG.
5. Avançado > Posição: **Fixa**. Largura: inicial (personalizada). Alinhe no canto inferior direito com deslocamento.

Para HTML puro (fora do Elementor) a alternativa é o botão flutuante que já vem no snippet `menus-e-headers/header-fixo-vega.html`.
