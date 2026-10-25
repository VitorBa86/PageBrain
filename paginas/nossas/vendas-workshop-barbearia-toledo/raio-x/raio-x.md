# Raio-x de molde: vendas-workshop-barbearia-toledo

**Propósito:** medidas exatas, seção por seção, para reproduzir esta página como molde (trocar copy, cores e imagens, manter tamanhos, pesos, componentes e ritmo).
**Quando usar:** no passo 4 da SKILL (modo molde). Abra junto as imagens `secao-NN.jpg` desta pasta.
**Relacionados:** [MEDIDAS-REAIS.md](<../../../../design/MEDIDAS-REAIS.md>), [ANTI-SLOP.md](<../../../../design/ANTI-SLOP.md>)

Altura total: 7646px no desktop (1440) e 9612px no mobile (390). Mobile inteiro em `pagina-mobile.jpg`.

## Seção 01 · `secao-01.jpg`

- Altura 66px · fundo `rgb(211, 0, 36)`
- Padding `0px 16px` · interno `11px 0px` · conteúdo 1240px · direção column · gap normal
- Mobile: altura 55px · padding `0px 14px` · interno `5px 0px`

| Tamanho | Peso | Fonte | Line-height | Cor | Extra | Tag | Exemplo |
|---|---|---|---|---|---|---|---|
| 20px | 600 | Sora | 1.30em | rgb(255, 187, 53) |  | span | 00 |
| 15px | 700 | Sora | 1.35em | rgb(255, 255, 255) | uppercase ls 0.78px | p | GARANTA SEU INGRESSO ANTES DA VIRADA DE LOTE  | |
| 12px | 400 | Sora | 1.00em | rgb(255, 187, 53) |  | span | Dias |

Mobile (tamanho → exemplo): 20px/600 "00" · 12px/700 "GARANTA SEU INGRESSO ANTES D" · 9px/400 "Dias"

## Seção 02 · `secao-02.jpg`

- Altura 750px · fundo `url(pt01-TOLEDO-9cf59737.webp) sobre rgb(15, 15, 15)`
- Padding `0px` · interno `80px 0px` · conteúdo 1240px · direção column · gap normal
- Mobile: altura 711px · padding `0px 19.5px` · interno `235.156px 0px 35.0938px`

| Tamanho | Peso | Fonte | Line-height | Cor | Extra | Tag | Exemplo |
|---|---|---|---|---|---|---|---|
| 45px | 500 | Sora | 1.20em | rgb(255, 255, 255) | ls -3.3px | h1 | Sua barbearia não aumenta o faturamento porque você não tem |
| 45px | 500 | Sora | 1.20em | rgb(255, 107, 53) | ls -3.3px | span | estrutura de gestão |
| 20px | 300 | Sora | 1.60em | rgb(255, 255, 255) |  | p | Em apenas 1 dia comigo, você aprende os 4 pilares que me fizeram sair  |
| 20px | 400 | Sora | 1.60em | rgb(255, 102, 0) |  | b | 25k |
| 16px | 700 | Sora | 1.20em | rgb(0, 0, 0) | ls 0.32px | span | QUERO GARANTIR MEU INGRESSO |
| 15px | 500 | Sora | 1.50em | rgb(255, 255, 255) | uppercase | span | 13 de setembro |
| 13px | 400 | Sora | 1.60em | rgb(255, 255, 255) |  | p | 126 vagas  | 100% ao vivo  | Últimas 48 horas |

Mobile (tamanho → exemplo): 27px/500 "Sua barbearia não aumenta o " · 27px/500 "estrutura de gestão" · 16px/300 "Em apenas 1 dia comigo, você" · 16px/700 "QUERO GARANTIR MEU INGRESSO" · 16px/400 "25k" · 12px/400 "126 vagas  | 100% ao vivo  |"
- **Botão** "QUERO GARANTIR MEU INGRESSO": 16px/700 Sora, caixa none, padding `18px 32px`, raio `10px`, altura 57px, largura 363px, fundo `linear-gradient(-45deg, rgb(255, 107, 53), rgb(217, 74, 24), rgb(255, 107, 53), rgb(255, 138, 92), rgb(255, 107, 53), rgb(217, 74, 24))`, texto `rgb(0, 0, 0)`, borda `1px rgb(255, 107, 53)`, sem ícone

| Slot | Tipo | Tamanho na tela | Proporção | Raio | Encaixe | Arquivo original |
|---|---|---|---|---|---|---|
| S02-1 | fundo da seção | 1440x750 | 1.92 | 0px | auto | pt01-TOLEDO-9cf59737.webp |
| S02-2 | img | 290x109 | 2.66 | 0px | fill | LOGO-1-ff39bdb4.svg |

## Seção 03 · `secao-03.jpg`

- Altura 690px · fundo `url(PT02-TOLEDO-37f8d6b2.webp) sobre rgb(15, 15, 15)`
- Padding `0px` · interno `80px 0px` · conteúdo 1240px · direção column · gap normal
- Mobile: altura 999px · padding `0px 19.5px` · interno `35.0938px 0px 421.188px`

| Tamanho | Peso | Fonte | Line-height | Cor | Extra | Tag | Exemplo |
|---|---|---|---|---|---|---|---|
| 45px | 500 | Sora | 1.20em | rgb(255, 255, 255) | ls -3.3px | h2 | Sua agenda tá cheia, mas sua gestão te impede de crescer |
| 27px | 500 | Sora | 1.20em | rgb(255, 255, 255) | ls -0.68px | div | O resultado: você vira o gargalo. |
| 18px | 300 | Sora | 1.60em | rgb(176, 176, 176) |  | p | Você tem cliente chegando, mas a agenda dos seus colaboradores não est |
| 18px | 400 | Sora | 1.60em | rgb(255, 255, 255) |  | b | 60% |

Mobile (tamanho → exemplo): 27px/500 "Sua agenda tá cheia, mas sua" · 22px/500 "O resultado: você vira o gar" · 16px/300 "Você tem cliente chegando, m" · 16px/400 "60%"

| Slot | Tipo | Tamanho na tela | Proporção | Raio | Encaixe | Arquivo original |
|---|---|---|---|---|---|---|
| S03-1 | fundo da seção | 1440x690 | 2.09 | 0px | cover | PT02-TOLEDO-37f8d6b2.webp |

## Seção 04 · `secao-04.jpg`

- Altura 839px · fundo `linear-gradient(50deg, rgb(26, 26, 26) 0%, rgb(129, 48, 19) 100%)`
- Padding `0px` · interno `80px 0px` · conteúdo 1368px · direção column · gap normal
- Mobile: altura 1269px · padding `0px 20px` · interno `56px 0px`

| Tamanho | Peso | Fonte | Line-height | Cor | Extra | Tag | Exemplo |
|---|---|---|---|---|---|---|---|
| 45px | 500 | Sora | 1.20em | rgb(255, 255, 255) | ls -3.3px | h2 | Essa é a evolução do Cauan |
| 28px | 700 | Inter | 1.15em | rgb(255, 107, 53) | ls -0.84px | span | faturamento mensal |
| 28px | 700 | Inter | 1.15em | rgb(255, 255, 255) | ls -0.84px | h3 | Evolução do |
| 18px | 300 | Sora | 1.60em | rgb(255, 255, 255) |  | p | Faturava cerca de . Não conseguia formar uma equipe que jogasse junto, |
| 18px | 300 | Sora | 1.60em | rgb(255, 107, 53) |  | span | 24k |
| 16px | 700 | Sora | 1.65em | rgb(255, 255, 255) |  | b | Isso não é sorte. Não é porque Cauan deu certo de repente. É porque el |
| 16px | 400 | Inter | 1.50em | rgb(255, 255, 255) |  | li | Março: R$ 24.000 |
| 16px | 700 | Sora | 1.20em | rgb(0, 0, 0) | ls 0.32px | span | QUERO GARANTIR MEU INGRESSO |
| 12px | 400 | Inter | 1.50em | rgb(255, 255, 255) |  | text | R$ 0 |
| 12px | 600 | Inter | 1.50em | rgb(255, 255, 255) |  | text | Mês |
| 12px | 700 | Inter | 1.50em | rgb(255, 255, 255) |  | text | R$ 51 mil |

Mobile (tamanho → exemplo): 25px/500 "Essa é a evolução do Cauan" · 18px/700 "faturamento mensal" · 18px/700 "Evolução do" · 16px/300 "Faturava cerca de . Não cons" · 16px/700 "Isso não é sorte. Não é porq" · 16px/400 "Março: R$ 24.000"
- **Botão** "QUERO GARANTIR MEU INGRESSO": 16px/700 Sora, caixa none, padding `18px 32px`, raio `10px`, altura 57px, largura 363px, fundo `linear-gradient(-45deg, rgb(255, 107, 53), rgb(217, 74, 24), rgb(255, 107, 53), rgb(255, 138, 92), rgb(255, 107, 53), rgb(217, 74, 24))`, texto `rgb(0, 0, 0)`, borda `1px rgb(255, 107, 53)`, sem ícone

## Seção 05 · `secao-05.jpg`

- Altura 841px · fundo `rgb(0, 0, 0)`
- Padding `0px` · interno `80px 0px` · conteúdo 1240px · direção column · gap normal
- Mobile: altura 1054px · padding `0px 20px` · interno `56px 0px`

| Tamanho | Peso | Fonte | Line-height | Cor | Extra | Tag | Exemplo |
|---|---|---|---|---|---|---|---|
| 45px | 500 | Sora | 1.20em | rgb(255, 255, 255) | ls -3.3px | h2 | de 18k para 28-30k |
| 45px | 500 | Sora | 1.20em | rgb(255, 107, 53) | ls -3.3px | span | A matemática: |
| 36px | 700 | Sora | 1.05em | rgb(255, 0, 0) | ls -1.44px | div | R$ 18.000 |
| 36px | 700 | Sora | 1.05em | rgb(53, 255, 57) | ls -1.44px | div | R$ 28-30k |
| 16px | 400 | Roboto | 1.50em | rgb(255, 255, 255) |  | span | 235 clientes |
| 16px | 600 | Sora | 1.60em | rgb(255, 170, 0) |  | p | Sem trazer mais cliente. Sem expandir. Sem nada. |
| 16px | 700 | Sora | 1.20em | rgb(0, 0, 0) | ls 0.32px | span | QUERO GARANTIR MEU INGRESSO |
| 14px | 400 | Sora | 1.60em | rgb(176, 176, 176) |  | p | +10-12k em 12 meses |
| 12px | 700 | Sora | 1.60em | rgb(255, 255, 255) | uppercase ls 1.44px | div | Agora (Mês 1) |
| 12px | 700 | Sora | 1.60em | rgb(138, 138, 138) | uppercase ls 1.44px | div | Crescimento |

Mobile (tamanho → exemplo): 27px/500 "de 18k para 28-30k" · 27px/500 "A matemática:" · 27px/700 "R$ 18.000" · 27px/700 "R$ 28-30k" · 16px/400 "235 clientes" · 16px/600 "Sem trazer mais cliente. Sem"
- **Botão** "QUERO GARANTIR MEU INGRESSO": 16px/700 Sora, caixa none, padding `18px 32px`, raio `10px`, altura 57px, largura 363px, fundo `rgb(255, 107, 53)`, texto `rgb(0, 0, 0)`, borda `1px rgb(255, 107, 53)`, sem ícone
- **Card** (x1): 610x269px, raio `10px`, fundo `rgba(255, 0, 0, 0.21)`, padding `26px`, borda `1px rgba(255, 255, 255, 0.1)`
- **Card** (x1): 610x269px, raio `10px`, fundo `rgba(0, 0, 0, 0)`, padding `26px`, borda `1px rgb(19, 128, 21)`, sombra `rgba(53, 255, 57, 0.23) 0px 0px 13px 0px`
- **Card** (x1): 484x298px, raio `16px`, fundo `rgb(26, 26, 26)`, padding `36px 26px`, borda `1px rgba(255, 255, 255, 0.1)`

## Seção 06 · `secao-06.jpg`

- Altura 627px · fundo `rgb(26, 26, 26)`
- Padding `0px` · interno `80px 0px` · conteúdo 1240px · direção column · gap normal
- Mobile: altura 1366px · padding `0px 20px` · interno `56px 0px`

| Tamanho | Peso | Fonte | Line-height | Cor | Extra | Tag | Exemplo |
|---|---|---|---|---|---|---|---|
| 64px | 700 | Sora | 1.00em | rgba(255, 255, 255, 0.32) |  | div | 01 |
| 45px | 500 | Sora | 1.20em | rgb(255, 255, 255) | ls -3.3px | h2 | como eu estruturei |
| 45px | 500 | Sora | 1.20em | rgb(255, 107, 53) | ls -3.3px | span | Os 4 Pilares: |
| 18px | 700 | Sora | 1.35em | rgb(255, 107, 53) | ls 0.32px | h3 | PILAR 1: VENDAS |
| 16px | 400 | Sora | 1.65em | rgb(176, 176, 176) |  | p | Cliente paga R$40 hoje. Com Pilar 1, passa a pagar . Mesmos clientes.  |
| 16px | 400 | Sora | 1.65em | rgb(255, 107, 53) |  | span | R$85 |

Mobile (tamanho → exemplo): 51px/700 "01" · 30px/500 "como eu estruturei" · 30px/500 "Os 4 Pilares:" · 21px/700 "PILAR 1: VENDAS" · 16px/400 "Cliente paga R$40 hoje. Com " · 16px/400 "R$85"
- **Card** (x4): 303x353px, raio `10px`, fundo `rgb(0, 0, 0)`, padding `24px`

## Seção 07 · `secao-07.jpg`

- Altura 1268px · fundo `rgba(0, 0, 0, 0)`
- Padding `0px` · interno `80px 0px` · conteúdo 1240px · direção column · gap normal
- Mobile: altura 1330px · padding `0px 20px` · interno `56px 0px`

| Tamanho | Peso | Fonte | Line-height | Cor | Extra | Tag | Exemplo |
|---|---|---|---|---|---|---|---|
| 45px | 500 | Sora | 1.20em | rgb(255, 255, 255) | ls -3.3px | h2 | barbeiros já implementaram os 4 pilares |
| 45px | 500 | Sora | 1.20em | rgb(255, 107, 53) | ls -3.3px | span | 200+ |
| 20px | 400 | Sora | 1.60em | rgb(224, 224, 224) |  | p | “Tava em 24k. Implementei Pilar 1 (Vendas) e 2 (Gestão). “ |
| 20px | 700 | Sora | 1.60em | rgb(255, 107, 53) |  | b | Virei 51k em 6 meses. |
| 16px | 400 | Sora | 1.65em | rgb(176, 176, 176) |  | p | Média: crescimento em 12 meses  |  Mesma estratégia, 235+ clientes |
| 16px | 700 | Sora | 1.35em | rgb(255, 255, 255) |  | h4 | Cauan Santana |
| 16px | 400 | Sora | 1.65em | rgb(255, 107, 53) |  | span | 40% |
| 13px | 400 | Sora | 1.60em | rgb(138, 138, 138) |  | p | Ticket: 40 → 85+  |  Crescimento: +114% |
| 11px | 400 | Sora | 1.50em | rgb(138, 138, 138) |  | div | SP • 3 barbeiros |

Mobile (tamanho → exemplo): 27px/500 "barbeiros já implementaram o" · 27px/500 "200+" · 18px/400 "“Tava em 24k. Implementei Pi" · 18px/700 "Virei 51k em 6 meses." · 16px/400 "Média: crescimento em 12 mes" · 16px/700 "Cauan Santana"

| Slot | Tipo | Tamanho na tela | Proporção | Raio | Encaixe | Arquivo original |
|---|---|---|---|---|---|---|
| S07-1 | img | 380x677 | 0.56 | 10px | fill | image_5_1x-6b8c8c0e.webp |
| S07-2 | img | 380x677 | 0.56 | 10px | fill | image_6_1x-bd6fc1ec.webp |
| S07-3 | img | 380x677 | 0.56 | 10px | fill | image_7_1x-1d576bd9.webp |
| S07-4 | img | 380x679 | 0.56 | 10px | fill | image_2_1x-c43974c3.webp |
| S07-5 | img | 380x677 | 0.56 | 10px | fill | image_3_1x-4d4dd1a1.webp |
| S07-6 | img | 380x679 | 0.56 | 10px | fill | image_4_1x-40e8676d.webp |
| S07-7 | img | 380x677 | 0.56 | 10px | fill | image_5_1x-6b8c8c0e.webp |
| S07-8 | img | 380x677 | 0.56 | 10px | fill | image_6_1x-bd6fc1ec.webp |
| S07-9 | img | 380x677 | 0.56 | 10px | fill | image_7_1x-1d576bd9.webp |
| S07-10 | img | 380x679 | 0.56 | 10px | fill | image_2_1x-c43974c3.webp |
| S07-11 | img | 380x677 | 0.56 | 10px | fill | image_3_1x-4d4dd1a1.webp |
| S07-12 | img | 380x679 | 0.56 | 10px | fill | image_4_1x-40e8676d.webp |

## Seção 08 · `secao-08.jpg`

- Altura 1607px · fundo `rgba(0, 0, 0, 0)`
- Padding `0px` · interno `80px 0px` · conteúdo 1240px · direção column · gap normal
- Mobile: altura 1431px · padding `0px 20px` · interno `56px 0px`

| Tamanho | Peso | Fonte | Line-height | Cor | Extra | Tag | Exemplo |
|---|---|---|---|---|---|---|---|
| 45px | 500 | Sora | 1.20em | rgb(255, 255, 255) | ls -3.3px | h2 | Quanto você precisará investir? |
| 33px | 600 | Sora | 2.50em | rgb(14, 255, 0) |  | span | R$ |
| 32px | 500 | Sora | 1.40em | rgb(255, 255, 255) | ls -2px | div | Aumentar ticket de R$46 para R$85 |
| 20px | 600 | Sora | 1.40em | rgb(255, 255, 255) |  | h2 | Por apenas 3X de: |
| 18px | 400 | Sora | 1.40em | rgb(255, 255, 255) |  | h2 | ou 27 à vista |
| 16px | 300 | Sora | 1.60em | rgb(255, 255, 255) |  | h2 | Nesse workshop de 1 dia inteiro, vou passar os 4 pilares na ordem corr |
| 16px | 400 | Sora | 1.50em | rgb(255, 255, 255) |  | span | Workshop ao vivo (8h de conteúdo) |
| 16px | 300 | Sora | 1.40em | rgb(255, 255, 255) |  | h2 | Recebe o acesso imediatamente após a confirmação de pagamento. |
| 16px | 400 | Sora | 1.65em | rgb(176, 176, 176) |  | p | 235 clientes × R$39 = |
| 16px | 400 | Sora | 1.40em | rgb(255, 255, 255) |  | b | Compra 100% segura! |
| 16px | 700 | Sora | 1.20em | rgb(0, 0, 0) | uppercase ls 0.32px | span | Comprar agora! |
| 16px | 700 | Sora | 1.65em | rgb(4, 165, 26) |  | b | +R$9.165/mês |

Mobile (tamanho → exemplo): 31px/500 "Quanto você precisará invest" · 30px/600 "R$" · 27px/500 "Aumentar ticket de R$46 para" · 19px/600 "Por apenas 3X de:" · 16px/300 "Nesse workshop de 1 dia inte" · 16px/400 "Workshop ao vivo (8h de cont"
- **Botão** "COMPRAR AGORA!": 16px/700 Sora, caixa uppercase, padding `18px 32px`, raio `10px`, altura 57px, largura 409px, fundo `rgb(255, 107, 53)`, texto `rgb(0, 0, 0)`, borda `1px rgb(255, 107, 53)`, sem ícone
- **Card** (x1): 583x1166px, raio `12px`, fundo `rgba(0, 0, 0, 0)`, padding `35px`, borda `1px rgb(255, 107, 53)`
- **Card** (x1): 471x250px, raio `10px`, fundo `rgba(0, 0, 0, 0.7)`, padding `26px`, borda `1px rgba(255, 255, 255, 0.1)`

| Slot | Tipo | Tamanho na tela | Proporção | Raio | Encaixe | Arquivo original |
|---|---|---|---|---|---|---|
| S08-1 | img | 511x255 | 2.00 | 0px | fill | TICKET-1024x512-9dcbc93d.webp |

## Seção 09 · `secao-09.jpg`

- Altura 250px · fundo `rgb(194, 74, 29)`
- Padding `0px` · interno `50px 0px` · conteúdo 1240px · direção column · gap normal
- Mobile: altura 324px · padding `0px 20px` · interno `56px 0px`

| Tamanho | Peso | Fonte | Line-height | Cor | Extra | Tag | Exemplo |
|---|---|---|---|---|---|---|---|
| 27px | 700 | Sora | 1.00em | rgb(255, 255, 255) |  | b | Se passar dessa data, próximo é daqui a 3 meses. |
| 27px | 400 | Sora | 1.00em | rgb(255, 255, 255) |  | p | 126 vagas. Evento é amanhã (13 de setembro). |
| 16px | 700 | Sora | 1.20em | rgb(0, 0, 0) | ls 0.32px | span | QUERO COMEÇAR AGORA |

Mobile (tamanho → exemplo): 23px/700 "Se passar dessa data, próxim" · 23px/400 "126 vagas. Evento é amanhã (" · 16px/700 "QUERO COMEÇAR AGORA"
- **Botão** "QUERO COMEÇAR AGORA": 16px/700 Sora, caixa none, padding `18px 32px`, raio `10px`, altura 57px, largura 292px, fundo `rgb(255, 107, 53)`, texto `rgb(0, 0, 0)`, borda `1px rgb(255, 107, 53)`, sem ícone

## Seção 10 · `secao-10.jpg`

- Altura 505px · fundo `rgb(15, 15, 15)`
- Padding `0px` · interno `80px 0px` · conteúdo 1240px · direção column · gap normal
- Mobile: altura 901px · padding `0px 19.5px` · interno `35.0938px 0px 421.188px`

| Tamanho | Peso | Fonte | Line-height | Cor | Extra | Tag | Exemplo |
|---|---|---|---|---|---|---|---|
| 52px | 500 | Sora | 1.06em | rgb(255, 255, 255) | ls -2.34px | h2 | Tá bem. Qual é sua situação? |
| 18px | 400 | Sora | 1.65em | rgb(176, 176, 176) |  | p | Você tem 235 clientes, 3 pessoas, 18k/mês. Tá deixando em cima da mesa |
| 18px | 900 | Sora | 1.50em | rgb(255, 107, 53) |  | b | Mas precisa decidir agora. Vagas fecham amanhã à noite. |
| 18px | 700 | Sora | 1.65em | rgb(255, 107, 53) |  | b | Você consegue fazer igual. |
| 18px | 700 | Sora | 1.65em | rgb(255, 255, 255) |  | b | R$10k/mês |
| 16px | 700 | Sora | 1.20em | rgb(0, 0, 0) | ls 0.32px | span | QUERO COMEÇAR |
| 13px | 400 | Sora | 1.60em | rgb(138, 138, 138) |  | p | 13 de setembro  |  100% ao vivo  | |
| 13px | 700 | Sora | 1.60em | rgb(255, 107, 53) |  | b | ÚLTIMAS 48 HORAS |

Mobile (tamanho → exemplo): 32px/500 "Tá bem. Qual é sua situação?" · 17px/900 "Mas precisa decidir agora. V" · 16px/400 "Você tem 235 clientes, 3 pes" · 16px/700 "Você consegue fazer igual." · 16px/700 "QUERO COMEÇAR" · 16px/700 "R$10k/mês"
- **Botão** "QUERO COMEÇAR": 16px/700 Sora, caixa none, padding `18px 32px`, raio `10px`, altura 57px, largura 223px, fundo `rgb(255, 107, 53)`, texto `rgb(0, 0, 0)`, borda `1px rgb(255, 107, 53)`, sem ícone

## Seção 11 · `secao-11.jpg`

- Altura 202px · fundo `rgb(10, 10, 10)`
- Padding `0px` · interno `40px 0px` · conteúdo 1240px · direção column · gap normal
- Mobile: altura 171px · padding `0px 20px` · interno `32px 0px`

| Tamanho | Peso | Fonte | Line-height | Cor | Extra | Tag | Exemplo |
|---|---|---|---|---|---|---|---|
| 14px | 400 | Sora | 1.60em | rgb(255, 255, 255) |  | p | © 2026 MVP Education | Workshop Barbearia Lucrativa |

Mobile (tamanho → exemplo): 12px/400 "© 2026 MVP Education | Works"

| Slot | Tipo | Tamanho na tela | Proporção | Raio | Encaixe | Arquivo original |
|---|---|---|---|---|---|---|
| S11-1 | img | 236x89 | 2.66 | 0px | fill | LOGO-1-ff39bdb4.svg |
