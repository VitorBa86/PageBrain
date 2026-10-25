# Estrutura de página (ordem das seções)

**Propósito:** a ordem típica das seções nas páginas da casa, o objetivo de cada uma e com que frequência aparecem nas 37 páginas publicadas.
**Quando usar:** ao decidir quais dobras uma página nova vai ter e em que ordem, antes de escrever a copy.
**Relacionados:** [metodo-de-copy.md](metodo-de-copy.md), [formulas-e-modelos.md](formulas-e-modelos.md), [estrutura-secoes-por-pagina.json](estrutura-secoes-por-pagina.json) (dados brutos), [catálogo de seções JSON](<../elementor/secoes/catalogo-secoes.md>)

## Como os números foram obtidos

Cada página de `paginas/nossas` teve seus containers de topo lidos e classificados à mão em tipos de seção. A classificação completa está em [estrutura-secoes-por-pagina.json](estrutura-secoes-por-pagina.json). As 37 páginas se dividem em:

| Tipo de página | Qtde | Ação principal | Exemplos |
|---|---|---|---|
| Captação | 25 | WhatsApp (formulário só como secundário) | adv-*, psi-*, saude-*, odonto-*, imob-vega, negocio-inter-frios |
| Vendas | 6 | Checkout | vendas-* |
| Aplicação (consultoria gratuita) | 4 | Formulário ou aplicação | info-carol, info-victor-leao, harmony, rp-vision |
| Institucional | 2 | WhatsApp e catálogo | imob-mb2, negocio-hoffen |

"Posição" é a posição média da seção na página (0 = topo, 1 = rodapé).

## 1. Página de captação (o padrão principal)

### Estrutura oficial: 6 dobras (Guia de Copy, PDF)

"A ordem é sempre a mesma: atenção, identificação, solução, confiança, prova e decisão. Cada dobra termina com CTA para o WhatsApp, e o botão flutuante fica fixo na página inteira."

| # | Dobra | Objetivo | Conteúdo |
|---|---|---|---|
| 1 | **Hero** | Em 5 segundos dizer o que é, para quem, onde e o que fazer | Kicker (serviço + cidade), H1 até 12 palavras, subheadline até 30 palavras, CTA, selo ou barra com 3 ou 4 números reais |
| 2 | **Dor e para quem é** | A pessoa se reconhecer | H2 que nomeia a situação, 3 a 5 cards de dor com consequência real, bloco "Para quem é", frase de transição |
| 3 | **Solução e serviços** | Mostrar o que é oferecido, como resultado | H2 de resultado, 3 a 6 cards de serviço (nome + 1 linha de benefício), CTA "Quero saber qual é o melhor para mim" |
| 4 | **Autoridade** | Confiança | Foto real, nome, registro (OAB, CRO, CRP, CRM+RQE, CRECI), formação, tempo de atuação, 3 a 5 frases com detalhe humano, até 3 diferenciais numerados |
| 5 | **Prova social e como funciona** | Tirar o medo do primeiro contato | Depoimentos ou prints do Google (só onde o conselho permite), passo a passo de 3 ou 4 etapas começando pelo WhatsApp |
| 6 | **FAQ e CTA final** | Responder objeções e fechar | 4 a 6 perguntas (preço, convênio, online, tempo, local, sigilo), H2 de fechamento + botão, rodapé com endereço, mapa, horário, registro, CNPJ |

### O que as 25 páginas de captação têm de fato

| Seção | Frequência | Posição | Observação |
|---|---|---|---|
| hero | 25/25 (100%) | 0,00 | sempre primeira |
| sobre (autoridade) | 23/25 (92%) | 0,47 | a seção mais constante depois do hero |
| rodapé | 23/25 (92%) | 1,00 | |
| faq | 16/25 (64%) | 0,80 | quase sempre penúltima |
| prova social | 15/25 (60%) | 0,57 | ausente na maioria das de advocacia mais novas, por causa da OAB |
| como funciona | 13/25 (52%) | 0,42 | 3 a 6 etapas |
| localização | 12/25 (48%) | 0,72 | endereço, mapa, "como chegar" |
| serviços | 11/25 (44%) | 0,27 | |
| contato | 9/25 (36%) | 0,87 | |
| benefícios | 8/25 (32%) | 0,28 | |
| para quem é | 8/25 (32%) | 0,26 | forte em psi |
| diferenciais | 7/25 (28%) | 0,44 | |
| CTA final | 7/25 (28%) | 0,86 | |
| formulário | 5/25 (20%) | 0,74 | imobiliário e B2B |
| barra de números | 5/25 (20%) | 0,18 | logo abaixo do hero |
| dor | 4/25 (16%) | 0,37 | |
| antes e depois / resultados | 4/25 (16%) | 0,18 | saúde e odonto |

Média de **8,3 seções** por página de captação (sem menu e rodapé). Ou seja, as 6 dobras do guia viram cerca de 8 containers no Elementor, porque barra de números, localização e contato costumam ser containers próprios.

### Sequência recomendada (captação)

```
[menu fixo opcional] → HERO (+ barra de números) → DOR / PARA QUEM É → SERVIÇOS / SOLUÇÃO
→ SOBRE (autoridade) → COMO FUNCIONA → PROVA SOCIAL → FAQ → CTA FINAL → LOCALIZAÇÃO/CONTATO → RODAPÉ
```

Exemplos reais muito próximos dessa sequência: [psi-renan](copys-reais/psi-renan.md), [negocio-inter-frios-refrigeracao](copys-reais/negocio-inter-frios-refrigeracao.md), [imob-vistoria-alphaville](copys-reais/imob-vistoria-alphaville.md), [saude-luciano-grisotto-mastopexia](copys-reais/saude-luciano-grisotto-mastopexia.md).

## 2. Lançamento imobiliário (exceção: até 8 dobras)

Estrutura do guia, aplicada em [imob-vega-costa-e-silva](copys-reais/imob-vega-costa-e-silva.md):

1. Hero: lugar + momento, selo de specs, CTA
2. Detalhes: grid de 6 cards (metragem, quartos, vagas, lazer, torres, localização)
3. Valorização: dados de fonte pública (FipeZap, Sinduscon) com a fonte citada
4. Conheça o empreendimento: abas com vídeo, fotos, plantas, ficha técnica (e tour 360)
5. Lazer: itens com imagem e legenda curta
6. Localização: endereço, acessos e cards de distância + mapa
7. Andamento da obra: barra de progresso, marcos com datas, urgência real
8. Formulário: nome, e-mail, telefone, CTA "Receber a tabela"

Obrigatório no rodapé: registro de incorporação (Lei 4.591/64), CRECI e nota de que as imagens são ilustrativas.

## 3. Página de vendas (infoproduto, curso, evento)

6 páginas, média de **10,5 seções**.

| Seção | Frequência | Posição |
|---|---|---|
| hero | 6/6 (100%) | 0,02 |
| oferta / preço | 6/6 (100%) | 0,65 |
| prova social | 5/6 (83%) | 0,46 |
| faq | 5/6 (83%) | 0,90 |
| sobre | 4/6 (67%) | 0,65 |
| garantia | 4/6 (67%) | 0,74 |
| bônus | 3/6 (50%) | 0,55 |
| para quem é | 3/6 (50%) | 0,31 |
| conteúdo / módulos | 3/6 (50%) | 0,45 |
| dor | 3/6 (50%) | 0,17 |
| solução | 3/6 (50%) | 0,35 |
| faixa (marquee) | 2/6 (33%) | 0,38 |

Sequência recomendada (inferida das 6 páginas):

```
HERO → (faixa) → DOR → SOLUÇÃO/PRODUTO → PARA QUEM É → CONTEÚDO/MÓDULOS → BÔNUS
→ PROVA SOCIAL → OFERTA (ancoragem + parcelado + à vista) → GARANTIA → SOBRE → FAQ → RODAPÉ
```

Página mais completa do tipo: [vendas-scripts-consignado-jessica](copys-reais/vendas-scripts-consignado-jessica.md). Evento com lotes: [vendas-morelli-churrasco-networking](copys-reais/vendas-morelli-churrasco-networking.md). Workshop com urgência e contador: [vendas-workshop-barbearia-toledo](copys-reais/vendas-workshop-barbearia-toledo.md).

## 4. Página de aplicação (consultoria ou diagnóstico gratuito)

4 páginas. Hero, método próprio com pilares e "sobre" aparecem nas 4. Resultados e prova social em 3 de 4.

```
HERO (promessa + formulário ou botão de aplicação) → PROVA SOCIAL (vídeos) → DOR ("por que você não fatura mais")
→ MÉTODO com nome próprio (SCINK, V.I.S.A.O, Efeito Presença, 7 pilares) → RESULTADOS → SOBRE → FAQ ("não é preciso participar da reunião...") → RODAPÉ
```

## Objetivo de cada tipo de seção

| Tipo | Objetivo | Regra de ouro |
|---|---|---|
| hero | Prender e dizer o essencial | H1 continua o anúncio; cidade na hero |
| barra de números | Prova rápida | 3 ou 4 dados reais, sem inventar |
| faixa (marquee) | Ritmo visual e palavras-chave | 3 a 4 termos curtos repetidos |
| dor / para quem é | Identificação | palavras do cliente final |
| situações | Mostrar quem tem direito (advocacia) | uma situação por card |
| serviços / solução | O que é oferecido | nome + 1 linha de benefício |
| benefícios | Resultado para a pessoa | benefício antes de característica |
| diferenciais | Por que este e não outro | fato no lugar de adjetivo |
| sobre | Autoridade | foto real, registro, detalhe humano |
| como funciona | Tirar o medo do primeiro passo | etapa 1 sempre é o WhatsApp |
| prova social | Confiança de terceiros | só onde o conselho permite |
| oferta | Decisão de compra | ancoragem, parcelado em destaque, à vista |
| bônus | Aumentar valor percebido | valor riscado "por R$0,00" |
| garantia | Remover risco | 7 dias, texto curto |
| faq | Objeções reais | respostas de 2 ou 3 frases |
| CTA final | Fechar | H2 de fechamento + botão |
| localização / contato | Confiança local | endereço, mapa, horário |
| rodapé | Dados legais | registro, CNPJ, cidade, políticas |
