# Como usar: Vistoria Alphaville · Laudo de Vistoria Detalhado

**Propósito:** o que esta página da casa tem de melhor, o que copiar e o que evitar.  
**Quando usar:** ao escolher referência visual para uma página de imobiliário ou com estilo claro, azul-marinho, dourado.  
**Relacionados:** [style-guide.html](style-guide.html), [ficha.json](ficha.json), [copy real](<../../../copy/copys-reais/imob-vistoria-alphaville.md>), [PADRAO-DAVI.md](../../../design/PADRAO-DAVI.md)

- **Origem:** paginas/nossas (prioridade alta) · pasta original `Vistoria Alphaville`
- **URL capturada:** https://vistoriaalphaville.com.br/
- **Plataforma:** WordPress + Elementor · **Relevância:** 5/5
- **Nicho:** Imobiliário · **Tipo de página:** captacao

## O que tem de melhor

Serviço B2B de vistoria imobiliária, muito completo e organizado. Hero com card de serviços, faixa animada com checks, cards brancos com listas de check por serviço, etapas numeradas em cards navy, 'para quem é' em cards brancos e diferenciais em grid de checks.

## Para que nicho e oferta serve

Serviços técnicos B2B, empresas com vários serviços.

## Estrutura de seções (na ordem)

1. **hero**: Segurança técnica do início ao fim da locação
2. **numeros**: (sem título)
3. **solucao**: SOLUÇÕES COMPLETAS PARA LOCAÇÕES IMOBILIÁRIAS
4. **servicos**: NOSSAS SOLUÇÕES
5. **como-funciona**: UMA SOLUÇÃO DO INÍCIO AO FIM
6. **como-funciona**: COMO FUNCIONA
7. **para-quem-e**: PARA QUEM SÃO AS NOSSAS SOLUÇÕES?
8. **diferenciais**: DIFERENCIAIS
9. **dor**: Evite que a entrega do imóvel se transforme em um problema
10. **prova-social**: AVALIAÇÕES DOS NOSSOS CLIENTES
11. **faq**: PERGUNTAS FREQUENTES
12. **cta-final**: Precisa receber ou entregar um imóvel?
13. **contato**: CONTATO
14. **rodape**: Alameda Grajaú 614 | The Office

## O que vale copiar

- Card de serviços no canto do hero
- Faixa (marquee) com checks e números
- Card de serviço com descrição + lista do que o laudo contempla + botão próprio
- Fluxo 1 a 5 em cards navy
- Grid de 12 diferenciais com check
- Bloco Google reviews + FAQ longo

## Técnicas notáveis

- Faixa animada (icon-list carrossel)
- Uma mensagem de WhatsApp por CTA de serviço

Código pronto na biblioteca:

- [Animação de entrada no scroll (scroll-left/right/top/bottom)](<../../../codigos/animacoes/animacao-scroll-reveal.html>)
- [Animação de entrada no scroll com blur](<../../../codigos/animacoes/animacao-scroll-reveal-blur.css>)
- [Vidro fosco (backdrop blur)](<../../../codigos/cards-e-bordas/vidro-fosco.css>)
- [Faixa (marquee) infinita com lista de ícones](<../../../codigos/faixas-e-carrosseis/faixa-animada-infinita.html>)
- [Link de WhatsApp com mensagem pronta](<../../../codigos/whatsapp-e-flutuantes/link-whatsapp-com-mensagem.html>)
- [Botão flutuante de WhatsApp com Lottie](<../../../codigos/whatsapp-e-flutuantes/whatsapp-flutuante-lottie.md>)
- [CSS base de toda página (o que sempre uso)](<../../../codigos/utilitarios-css/css-base-toda-pagina.css>)
- [Tamanho do ícone SVG no botão](<../../../codigos/utilitarios-css/botao-icone-tamanho.css>)
- [Elemento solto (posição absoluta)](<../../../codigos/utilitarios-css/elemento-posicao-absoluta.css>)

## O que NÃO copiar

- Página muito longa (14 seções); em captação o guia pede até 6 dobras

## Design em números

- **Fundos:** #FFFFFF, #0F223C, #234F80, #1A3454, #0E1B2C
- **Textos:** #141414, #FFFFFF, #234F80, #EAF0F7
- **Destaques:** #234F80, #A78555, #0F223C, #1A3454
- **Fontes:** Sora (90%), Nunito Sans (7%), Trustindex Poppins (3%)
- **Escala desktop:** 42, 36, 32, 22, 20, 18 px · **mobile:** 25, 24, 20, 18, 18, 16, 16, 16 px
- **Botão principal:** fundo #00000000, texto #A78555, raio 6px, padding 16px 26px, 16px peso 400 ("Solicitar vistoria de entrada")
- **Raios:** 12px, 8px, 6px, 30px, 10%, 23px · **Sombra principal:** `rgba(0, 0, 0, 0.11) 5px 6px 12px -4px`
- **Largura de conteúdo:** 1140px · **Gaps:** 20px, 14px, 12px, 30px

## Trechos de código úteis

Os efeitos desta página que já estão na biblioteca foram listados acima em "Técnicas notáveis". Para ver o CSS customizado original, abra `extraido/assets/css/post-*.css` e procure por `Start custom CSS`.
