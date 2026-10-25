# Como usar: Página PDB TEMPLATES [JARDEL]

**Propósito:** o que esta página da casa tem de melhor, o que copiar e o que evitar.  
**Quando usar:** ao escolher referência visual para uma página de página de vendas ou com estilo preto, azul-petroleo, claro-e-escuro.  
**Relacionados:** [style-guide.html](style-guide.html), [ficha.json](ficha.json), [copy real](<../../../copy/copys-reais/vendas-templates-arquiteto-jardel.md>), [PADRAO-DAVI.md](../../../design/PADRAO-DAVI.md)

- **Origem:** paginas/nossas (prioridade alta) · pasta original `Venda Template Arquiteto`
- **URL capturada:** https://lp.oreidalanding.com.br/templates-jardel/
- **Plataforma:** WordPress + Elementor · **Relevância:** 4/5
- **Nicho:** Página de vendas · **Tipo de página:** vendas

## O que tem de melhor

Venda de template de Revit, alternando preto e cinza claro, com renders 3D de casas. Linhas verticais animadas no fundo, botão com borda de luz girando, cards de entregável claros com lista e render, oferta com 50% de desconto e selo circular de garantia.

## Para que nicho e oferta serve

Produtos digitais técnicos (templates, arquivos, ferramentas).

## Estrutura de seções (na ordem)

1. **hero**: TEMPLATES PDB
2. **faixa**: (sem título)
3. **beneficios**: BENEFÍCIOS
4. **produto**: Conheça o Template por dentro
5. **para-quem-e**: Para quem é o Template Descomplicando o BIM?
6. **entregaveis**: O QUE VOU RECEBER?
7. **faixa**: (sem título)
8. **prova-social**: Centenas de profissionais estão economizando horas e triplicando sua produtivida
9. **oferta**: Qual investimento?
10. **garantia**: JARDEL MENDES
11. **sobre**: Perguntas Frequentes
12. **faq**: Todos os direitos reservados © 2026

## O que vale copiar

- Linhas verticais com luz descendo no fundo (snippet linhas-verticais-animadas)
- Botão com borda de luz girando (snippet botao-borda-girando-conic)
- Cards de entregável claros com lista e render 3D
- Elementos 3D flutuando ao redor da oferta

## Técnicas notáveis

- Borda degradê
- Elementos flutuando

Código pronto na biblioteca:

- [Botão com borda de luz girando (conic)](<../../../codigos/botoes/botao-borda-girando-conic.css>)
- [Animação de entrada no scroll (scroll-left/right/top/bottom)](<../../../codigos/animacoes/animacao-scroll-reveal.html>)
- [Texto que aparece palavra por palavra no scroll (GSAP)](<../../../codigos/animacoes/gsap-texto-palavras-no-scroll.html>)
- [Elementos decorativos flutuando](<../../../codigos/animacoes/elementos-flutuando.css>)
- [Card de vidro com borda degradê](<../../../codigos/cards-e-bordas/card-borda-degrade.css>)
- [Vidro fosco (backdrop blur)](<../../../codigos/cards-e-bordas/vidro-fosco.css>)
- [Faixa (marquee) infinita com lista de ícones](<../../../codigos/faixas-e-carrosseis/faixa-animada-infinita.html>)
- [Linhas verticais com luz descendo](<../../../codigos/fundos-e-texturas/linhas-verticais-animadas.html>)
- [Pixel da Meta (Facebook)](<../../../codigos/tracking-e-pixels/meta-pixel.html>)
- [Tag do Google Ads (gtag)](<../../../codigos/tracking-e-pixels/google-ads-gtag.html>)
- [CSS base de toda página (o que sempre uso)](<../../../codigos/utilitarios-css/css-base-toda-pagina.css>)
- [Borda arredondada nos itens do FAQ (Alternar/Acordeão)](<../../../codigos/utilitarios-css/faq-toggle-arredondado.css>)
- [Elemento solto (posição absoluta)](<../../../codigos/utilitarios-css/elemento-posicao-absoluta.css>)

## O que NÃO copiar

- Headline com 17 palavras

## Design em números

- **Fundos:** #000000, #ECECEC, #161616, #F5F5F5, #0071A2
- **Textos:** #FFFFFF, #414141, #353535, #000000
- **Destaques:** #0071A2, #158ABD
- **Fontes:** Manrope (79%), Nunito Sans (17%)
- **Escala desktop:** 104, 85, 43, 41, 40, 35, 34, 29, 25 px · **mobile:** 33, 29, 27, 22, 21, 20, 19, 18 px
- **Botão principal:** fundo #0071A2, texto #FFFFFF, raio 122px, padding 20px 30px, 18px peso 500, uppercase ("QUERO MEU TEMPLATE PROFISSIONAL")
- **Raios:** 22px, 122px, 18px, 35px, 6px, 43px · **Sombra principal:** `rgba(0, 160, 220, 0.5) 0px 0px 16px 4px, rgba(255, 255, 255, 0.18) 0px 0px 9.7px 4px inset`
- **Largura de conteúdo:** 1140px · **Gaps:** 20px, 5px, 60px, 15px

## Trechos de código úteis

Os efeitos desta página que já estão na biblioteca foram listados acima em "Técnicas notáveis". Para ver o CSS customizado original, abra `extraido/assets/css/post-*.css` e procure por `Start custom CSS`.
