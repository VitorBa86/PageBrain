# Como usar: PÁGINA VEGA COSTA E SILVA

**Propósito:** o que esta página da casa tem de melhor, o que copiar e o que evitar.  
**Quando usar:** ao escolher referência visual para uma página de imobiliário ou com estilo verde-escuro, laranja, serifa-display.  
**Relacionados:** [style-guide.html](style-guide.html), [ficha.json](ficha.json), [copy real](<../../../copy/copys-reais/imob-vega-costa-e-silva.md>), [JSON do Elementor](<../../../elementor/paginas/captacao/imob-vega-costa-e-silva.json>), [PADRAO-DAVI.md](../../../design/PADRAO-DAVI.md)

- **Origem:** paginas/nossas (prioridade alta) · pasta original `Vaga e Costa Imobi`
- **URL capturada:** https://lp.oreidalanding.com.br/pagina-vega-costa-e-silva/
- **Plataforma:** WordPress + Elementor · **Relevância:** 5/5
- **Nicho:** Imobiliário · **Tipo de página:** captacao

## O que tem de melhor

É a página modelo de lançamento imobiliário do guia (8 dobras). Verde-escuro + laranja, serifa display com palavra em laranja, barra de specs sobreposta ao hero, gráfico de valorização em HTML, formulário de simulação, abas com tour 360, lazer, distâncias, barra de andamento da obra e header/rodapé próprios em widget HTML.

## Para que nicho e oferta serve

Lançamento imobiliário (modelo oficial).

## Estrutura de seções (na ordem)

1. **hero**: Seu novo lar no bairro que mais cresce em Joinville
2. **numeros**: (sem título)
3. **produto**: Conheça os detalhes do seu mais novo lar
4. **prova-dados**: A cidade com a maior valorização imobiliária de Santa Catarina
5. **formulario**: Explore cada detalhe do Vega Costa e Silva
6. **produto**: Área de Lazer Completa
7. **lazer**: Localização Privilegiada
8. **localizacao**: Seu futuro já está sendo construído
9. **andamento**: Faça sua Simulação Grátis aqui
10. **formulario**: Seu novo lar está a um passo de distância.

## O que vale copiar

- Barra de specs escura sobreposta ao fim do hero
- Gráfico de valorização em HTML/CSS (snippet grafico-valorizacao-barras)
- Formulário de simulação ao lado do gráfico
- Abas com vídeo, 360°, plantas e ficha técnica
- Cards de distância (IFSC 1 min, Expoville 7 min...) + mapa
- Barra de progresso da obra animada (snippet barra-progresso-animada)
- Header fixo com WhatsApp flutuante (snippet header-fixo-vega)

## Técnicas notáveis

- Widgets HTML autocontidos para header, rodapé e gráfico
- Tour 360 Momento360
- Contador animado

Código pronto na biblioteca:

- [Animação de entrada no scroll (scroll-left/right/top/bottom)](<../../../codigos/animacoes/animacao-scroll-reveal.html>)
- [Animação de entrada no scroll com blur](<../../../codigos/animacoes/animacao-scroll-reveal-blur.css>)
- [Barra de progresso com número animado](<../../../codigos/contadores-e-progresso/barra-progresso-animada.html>)
- [Vidro fosco (backdrop blur)](<../../../codigos/cards-e-bordas/vidro-fosco.css>)
- [Header fixo com WhatsApp flutuante (Vega)](<../../../codigos/menus-e-headers/header-fixo-vega.html>)
- [Rodapé com CTA e WhatsApp (Vega)](<../../../codigos/rodapes/rodape-vega.html>)
- [Gráfico de barras de valorização (Vega)](<../../../codigos/secoes-prontas/grafico-valorizacao-barras.html>)
- [Tour 360 incorporado (Momento360)](<../../../codigos/secoes-prontas/tour-360-momento360.html>)
- [Link de WhatsApp com mensagem pronta](<../../../codigos/whatsapp-e-flutuantes/link-whatsapp-com-mensagem.html>)
- [Pixel da Meta (Facebook)](<../../../codigos/tracking-e-pixels/meta-pixel.html>)
- [Tag do Google Ads (gtag)](<../../../codigos/tracking-e-pixels/google-ads-gtag.html>)
- [CSS base de toda página (o que sempre uso)](<../../../codigos/utilitarios-css/css-base-toda-pagina.css>)
- [Tamanho do ícone SVG no botão](<../../../codigos/utilitarios-css/botao-icone-tamanho.css>)
- [Elemento solto (posição absoluta)](<../../../codigos/utilitarios-css/elemento-posicao-absoluta.css>)

## O que NÃO copiar

- 4 travessões na copy

## Design em números

- **Fundos:** #FFFFFF, #F7F4EE, #0F2F2B, #123A35, #0A1F1C
- **Textos:** #4F5552, #202422, #FFFFFF, #333333
- **Destaques:** #FEBB09, #E7E7E7, #FF981F, #0F2F2B
- **Fontes:** Inter (83%), Georgia (10%), Roboto (7%)
- **Escala desktop:** 70, 65, 63, 54, 49, 47, 35, 30, 26, 17 px · **mobile:** 41, 40, 37, 35, 34, 17, 17, 16 px
- **Botão principal:** fundo #FEBB09, texto #0A1F1C, raio 999px, padding 14px 18px, 16px peso 600 ("FALE COM UM CONSULTOR")
- **Raios:** 8px, 12px, 999px, 10%, 44px, 32px · **Sombra principal:** `rgba(0, 0, 0, 0.28) 7px 7px 22px 0px`
- **Largura de conteúdo:** 1180px · **Gaps:** 20px, 24px, 5px, 17px

## Trechos de código úteis

Os efeitos desta página que já estão na biblioteca foram listados acima em "Técnicas notáveis". Para ver o CSS customizado original, abra `extraido/assets/css/post-*.css` e procure por `Start custom CSS`.
