# Raio-x de molde: adv-luisa

**Propósito:** medidas exatas, seção por seção, para reproduzir esta página como molde (trocar copy, cores e imagens, manter tamanhos, pesos, componentes e ritmo).
**Quando usar:** no passo 4 da SKILL (modo molde). Abra junto as imagens `secao-NN.jpg` desta pasta.
**Relacionados:** [MEDIDAS-REAIS.md](<../../../../design/MEDIDAS-REAIS.md>), [ANTI-SLOP.md](<../../../../design/ANTI-SLOP.md>)

Altura total: 5305px no desktop (1440) e 7439px no mobile (390). Mobile inteiro em `pagina-mobile.jpg`.

## Seção 01 · `secao-01.jpg`

- Altura 790px · fundo `url(PT-01-244acdbb.webp) sobre rgb(10, 14, 26)`
- Padding `0px 10px` · interno `10px 0px` · conteúdo 1140px · direção column · gap normal
- Mobile: altura 719px · padding `0px` · interno `312px 0px 39px`

| Tamanho | Peso | Fonte | Line-height | Cor | Extra | Tag | Exemplo |
|---|---|---|---|---|---|---|---|
| 28px | 600 | Sora | 1.40em | rgb(228, 189, 84) |  | h2 | Sofreu algum problema no seu voo? Receba indenizações por isso! |
| 16px | 200 | Sora | 1.30em | rgb(255, 255, 255) |  | h2 | Sou advogada especialista em direitos dos passageiros aéreos. Transfor |
| 16px | 500 | Sora | 1.00em | rgb(255, 255, 255) |  | span | Fale comigo no Whatsapp |

Mobile (tamanho → exemplo): 25px/600 "Sofreu algum problema no seu" · 17px/500 "Fale comigo no Whatsapp" · 14px/200 "Sou advogada especialista em"
- **Botão** "Fale comigo no Whatsapp": 16px/500 Sora, caixa none, padding `20px 28px`, raio `127px`, altura 65px, largura 311px, fundo `rgb(42, 167, 22)`, texto `rgb(255, 255, 255)`, com ícone

| Slot | Tipo | Tamanho na tela | Proporção | Raio | Encaixe | Arquivo original |
|---|---|---|---|---|---|---|
| S01-1 | fundo da seção | 1440x790 | 1.82 | 0px | auto | PT-01-244acdbb.webp |

## Seção 02 · `secao-02.jpg`

- Altura 968px · fundo `rgb(240, 240, 240)`
- Padding `0px` · interno `80px 0px` · conteúdo 1140px · direção column · gap normal
- Mobile: altura 2316px · padding `0px` · interno `80px 0px`

| Tamanho | Peso | Fonte | Line-height | Cor | Extra | Tag | Exemplo |
|---|---|---|---|---|---|---|---|
| 30px | 600 | AROLSE | 1.40em | rgb(0, 0, 0) |  | h2 | Conheça seus direitos |
| 22px | 600 | Sora | 1.20em | rgb(228, 189, 84) |  | span | Voo Cancelado |
| 16px | 200 | Sora | 1.50em | rgb(255, 255, 255) |  | p | Se o seu voo foi cancelado, você tem direito a uma indenização. Verifi |
| 16px | 300 | Sora | 1.30em | rgb(0, 0, 0) |  | h2 | Fique por dentro dos seus direitos como passageiro aéreo e saiba como  |

Mobile (tamanho → exemplo): 31px/600 "Conheça seus direitos" · 22px/600 "Voo Cancelado" · 16px/300 "Fique por dentro dos seus di" · 15px/200 "Se o seu voo foi cancelado, "
- **Card** (x6): 367x319px, raio `8px`, fundo `linear-gradient(70deg, rgb(24, 33, 66) 0%, rgb(39, 51, 94) 100%)`, padding `30px`

## Seção 03 · `secao-03.jpg`

- Altura 1483px · fundo `rgb(240, 240, 240)`
- Padding `0px` · interno `20px 0px 80px` · conteúdo 1140px · direção column · gap normal
- Mobile: altura 1709px · padding `0px` · interno `20px 0px 80px`

| Tamanho | Peso | Fonte | Line-height | Cor | Extra | Tag | Exemplo |
|---|---|---|---|---|---|---|---|
| 30px | 600 | AROLSE | 1.40em | rgb(0, 0, 0) |  | h2 | Passo a passo |
| 22px | 600 | Sora | 1.20em | rgb(228, 189, 84) |  | span | Lorem Ipsum​ |
| 16px | 200 | Sora | 1.50em | rgb(197, 197, 197) |  | p | Lorem Ipsum is simply dummy text of the printing and typesetting indus |
| 16px | 300 | Sora | 1.30em | rgb(0, 0, 0) |  | h2 | Lorem Ipsum is simply dummy text of the printing and typesetting indus |

Mobile (tamanho → exemplo): 31px/600 "Passo a passo" · 22px/600 "Lorem Ipsum​" · 16px/200 "Lorem Ipsum is simply dummy " · 16px/300 "Lorem Ipsum is simply dummy "
- **Card** (x4): 684x287px, raio `8px`, fundo `rgb(24, 31, 58)`, padding `50px`

## Seção 04 · `secao-04.jpg`

- Altura 725px · fundo `rgb(10, 14, 26)`
- Padding `0px 10px` · interno `10px 0px` · conteúdo 1140px · direção column · gap normal
- Mobile: altura 951px · padding `0px` · interno `312px 0px 39px`

| Tamanho | Peso | Fonte | Line-height | Cor | Extra | Tag | Exemplo |
|---|---|---|---|---|---|---|---|
| 40px | 600 | AROLSE | 1.30em | rgb(255, 255, 255) |  | h2 | Quem sou eu? |
| 16px | 200 | Sora | 1.30em | rgb(255, 255, 255) |  | h2 | Advogada há 4 anos pela UFRJ, pós graduanda pela UERJ, já trabalhou em |
| 16px | 200 | Sora | 1.30em | rgb(228, 189, 84) | ls 2.7px | h2 | Luisa Bastos l Advogada dos Passageiros Aéreos |

Mobile (tamanho → exemplo): 39px/600 "Quem sou eu?" · 16px/200 "Advogada há 4 anos pela UFRJ" · 16px/200 "Luisa Bastos l Advogada dos "

## Seção 05 · `secao-05.jpg`

- Altura 725px · fundo `rgb(19, 25, 44)`
- Padding `0px 10px` · interno `10px 0px` · conteúdo 1140px · direção column · gap normal
- Mobile: altura 956px · padding `0px` · interno `80px 0px 50px`

| Tamanho | Peso | Fonte | Line-height | Cor | Extra | Tag | Exemplo |
|---|---|---|---|---|---|---|---|
| 32px | 600 | AROLSE | 1.30em | rgb(255, 255, 255) |  | h2 | Diferenciais do meu Serviço: |
| 16px | 200 | Sora | 1.30em | rgb(255, 255, 255) |  | h2 | Descubra o que torna nosso atendimento único e como garantimos a melho |
| 16px | 200 | Sora | 1.50em | rgb(255, 255, 255) |  | span | Atendimento online em todo o Brasil |
| 16px | 500 | Sora | 1.00em | rgb(255, 255, 255) |  | span | Fale comigo no Whatsapp |

Mobile (tamanho → exemplo): 31px/600 "Diferenciais do meu Serviço:" · 17px/500 "Fale comigo no Whatsapp" · 15px/200 "Descubra o que torna nosso a" · 15px/200 "Atendimento online em todo o"
- **Botão** "Fale comigo no Whatsapp": 16px/500 Sora, caixa none, padding `20px 28px`, raio `127px`, altura 65px, largura 311px, fundo `rgb(42, 167, 22)`, texto `rgb(255, 255, 255)`, com ícone

## Seção 06 · `secao-06.jpg`

- Altura 553px · fundo `rgb(19, 25, 44)`
- Padding `0px 10px` · interno `10px 0px` · conteúdo 1140px · direção column · gap normal
- Mobile: altura 679px · padding `0px` · interno `0px 0px 80px`

| Tamanho | Peso | Fonte | Line-height | Cor | Extra | Tag | Exemplo |
|---|---|---|---|---|---|---|---|
| 28px | 600 | AROLSE | 1.30em | rgb(255, 255, 255) |  | h2 | Entre em Contato Comigo! |
| 16px | 200 | Sora | 1.30em | rgb(255, 255, 255) |  | h2 | Lorem Ipsum is simply dummy text of the Lorem Ipsum is simply dummy te |
| 16px | 200 | Sora | 1.50em | rgb(255, 255, 255) |  | span | (XX)XXXXX-XXXX |
| 16px | 400 | Sora | 1.50em | rgb(255, 255, 255) |  | b | Telefone: |
| 16px | 500 | Sora | 1.00em | rgb(255, 255, 255) |  | span | Fale comigo no Whatsapp |

Mobile (tamanho → exemplo): 28px/600 "Entre em Contato Comigo!" · 16px/200 "Lorem Ipsum is simply dummy " · 16px/200 "(XX)XXXXX-XXXX" · 16px/400 "Telefone:" · 16px/500 "Fale comigo no Whatsapp"
- **Botão** "Fale comigo no Whatsapp": 16px/500 Sora, caixa none, padding `20px 28px`, raio `127px`, altura 65px, largura 469px, fundo `rgb(42, 167, 22)`, texto `rgb(255, 255, 255)`, com ícone
- **Card** (x1): 673x533px, raio `8px`, fundo `rgba(0, 0, 0, 0)`, padding `40px`, borda `1px rgba(255, 255, 255, 0.11)`

## Seção 07 · `secao-07.jpg`

- Altura 60px · fundo `rgb(9, 12, 22)`
- Padding `0px 10px` · interno `10px 0px` · conteúdo 1140px · direção column · gap normal
- Mobile: altura 109px · padding `0px` · interno `30px 0px`

| Tamanho | Peso | Fonte | Line-height | Cor | Extra | Tag | Exemplo |
|---|---|---|---|---|---|---|---|
| 13px | 200 | Sora | 1.30em | rgb(255, 255, 255) |  | h2 | Todos os direitos reservados © 2024 |

Mobile (tamanho → exemplo): 13px/200 "Todos os direitos reservados"
