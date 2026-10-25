# Como usar: PÁGINA CONTADOR GONCONT

**Propósito:** o que esta página da casa tem de melhor, o que copiar e o que evitar.  
**Quando usar:** ao escolher referência visual para uma página de serviço b2b ou com estilo vermelho-bordo, branco, corporativo.  
**Relacionados:** [style-guide.html](style-guide.html), [ficha.json](ficha.json), [copy real](<../../../copy/copys-reais/servico-goncont-contador.md>), [JSON do Elementor](<../../../elementor/paginas/captacao/servico-goncont-contador.json>), [PADRAO-DAVI.md](../../../design/PADRAO-DAVI.md)

- **Origem:** paginas/nossas (prioridade alta) · pasta original `Godim COntador`
- **URL capturada:** https://lp.oreidalanding.com.br/goncont/
- **Plataforma:** WordPress + Elementor · **Relevância:** 3/5
- **Nicho:** Serviço B2B · **Tipo de página:** captacao

## O que tem de melhor

Contabilidade para profissionais da saúde em vermelho bordô. Cards vermelhos dentro de um container branco que sobe sobre o hero, 'para quem é' com checks, timeline de 3 passos em zigue-zague e depoimentos em grid.

## Para que nicho e oferta serve

Contabilidade, consultoria financeira, serviços B2B para profissionais liberais.

## Estrutura de seções (na ordem)

1. **hero**: Reduza sua carga tributária de forma legal e estratégica com uma contabilidade e
2. **servicos**: Soluções contábeis estratégicas para profissionais da saúde
3. **para-quem-e**: PARA QUEM É?
4. **sobre**: Quem sou eu?
5. **como-funciona**: Nosso processo para reduzir seus impostos com segurança
6. **prova-social**: (sem título)
7. **faq**: O que nossos clientes dizem:
8. **contato**: Perguntas Frequentes
9. **rodape**: Gondim Organização Contábil ©2026 - Todos os direitos reservados

## O que vale copiar

- Container branco sobreposto ao hero com cards vermelhos
- Lista 'para quem é' em checks dentro de card vermelho
- Processo em 3 passos zigue-zague com moldura
- Cards de suporte (WhatsApp e e-mail) ao lado do FAQ

## Técnicas notáveis

- CSS base e scroll-reveal colados em widget HTML (sem CSS custom da página)

Código pronto na biblioteca:

- [Animação de entrada no scroll (scroll-left/right/top/bottom)](<../../../codigos/animacoes/animacao-scroll-reveal.html>)
- [Pixel da Meta (Facebook)](<../../../codigos/tracking-e-pixels/meta-pixel.html>)
- [Tag do Google Ads (gtag)](<../../../codigos/tracking-e-pixels/google-ads-gtag.html>)
- [CSS base de toda página (o que sempre uso)](<../../../codigos/utilitarios-css/css-base-toda-pagina.css>)
- [Borda arredondada nos itens do FAQ (Alternar/Acordeão)](<../../../codigos/utilitarios-css/faq-toggle-arredondado.css>)
- [Elemento solto (posição absoluta)](<../../../codigos/utilitarios-css/elemento-posicao-absoluta.css>)

## O que NÃO copiar

- 'Excelência' e exclamações

## Design em números

- **Fundos:** #F5F5F5, #FFFFFF, #940C0C, #360505
- **Textos:** #FFFFFF, #4E4E4E, #0C0C0C, #940C0C
- **Destaques:** #940C0C
- **Fontes:** Inter (99%)
- **Escala desktop:** 61, 42, 33, 23, 22, 20, 18 px · **mobile:** 28, 25, 24, 22, 20, 18, 18, 18 px
- **Botão principal:** fundo #940C0C, texto #FFFFFF, raio 12px, padding 18px 38px, 20px peso 500 ("Falar com contador")
- **Raios:** 12px, 10%, 10px, 6px, 32px, 25px · **Sombra principal:** `rgba(0, 0, 0, 0.08) 5px 5px 10px 0px`
- **Largura de conteúdo:** 1140px · **Gaps:** 20px, 5px, 15px, 33px

## Trechos de código úteis

Os efeitos desta página que já estão na biblioteca foram listados acima em "Técnicas notáveis". Para ver o CSS customizado original, abra `extraido/assets/css/post-*.css` e procure por `Start custom CSS`.
