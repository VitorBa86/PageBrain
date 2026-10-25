# PageBrain · Medidas reais das páginas da casa

**Propósito:** os tamanhos de texto, pesos e botões que as 37 páginas da casa realmente usam, medidos no navegador por papel (título do hero, título de seção, título de card, corpo, botão). Substitui as faixas antigas do PADRAO-DAVI, que estavam infladas (diziam H2 de 40 a 52px).
**Quando usar:** sempre que for definir tamanhos numa página nova. Se houver molde (SKILL, passo 4), os números do `raio-x.md` do molde vencem esta tabela; esta tabela é o padrão quando não há molde.
**Relacionados:** [PADRAO-DAVI.md](PADRAO-DAVI.md), [ANTI-SLOP.md](ANTI-SLOP.md), [SKILL.md](../SKILL.md), dados brutos em [medidas-papeis.json](dados/medidas-papeis.json)

Medição de 21/10/2026 com `scripts/medir_papeis.py` sobre `extraido/index.html` das 37 páginas, em 1440px e 390px. "Q1 a Q3" é a faixa onde cai metade das páginas; fuja dela só com motivo.

## 1. Tipografia por papel

| Papel | Desktop: mediana (Q1 a Q3) | Mobile: mediana (Q1 a Q3) | Peso mais comum |
|---|---|---|---|
| Título do hero (H1) | **40px** (33 a 45) | **27px** (25 a 29) | 600, depois 400 e 500 |
| Título de seção (H2) | **36 a 42px** (30 a 46) | **25px** (22 a 28) | 600 ou 500 |
| Título de card / subtítulo | **20 a 22px** | 18 a 22px | 600 |
| Corpo | **16px** (16 a 18) | **16px** (15 a 16) | 300 ou 400 |
| Rótulo acima do título | 16 a 20px, caixa alta, peso 300 a 500, muitas vezes dentro de pílula com borda | 14 a 16px | 300 a 500 |
| Rodapé | 13 a 14px | 12 a 13px | 300 |

Leituras importantes:

- **Regra fixa do PageBrain (24/10/2026):** o tamanho final de cada H1 e H2 é o que faz o título caber em **até 3 linhas** na coluna dele (4 se a frase passar de 70 caracteres), dentro das faixas acima e nunca acima de **55px**. Na referência de padrão (`psi-luana-carolina-casais`): H1 46px desktop / 29px mobile, H2 48px / 26px. Conta rápida em Inter 600: caracteres por linha ≈ largura da coluna ÷ (0,52 × fonte).

- **Títulos da casa são moderados.** Só 5 de 37 páginas passam de 50px no hero (Vega, Vivian, Santa Boemia, Morelli, Entre para Trip). Página de vendas da casa não é "título gigante": a Jéssica bancário usa 27px no hero e 29 a 34px nas seções.
- **Peso 800 e 900 não aparecem em título.** Pesos de título: 600 (14 páginas), 500 (9), 400 (9), 700 (4).
- **Título de card nunca é caixa alta em negrito pesado.** É frase normal, 20 a 22px, peso 600.
- **Line-height** nas páginas medidas: títulos 1,2 a 1,4em; corpo 1,5em (sempre em `em`).
- **Fonte:** Inter em 15 páginas, Poppins em 7, Sora em 4, Montserrat e Manrope em 2 cada. Uma família só na página inteira é o caso comum; a segunda família entra só em título serifado (psi, saúde, alto padrão).

## 2. Botão principal

| Item | Valor medido |
|---|---|
| Tamanho do texto | **18px** (14 páginas), 16px (10), 20px (5) |
| Peso | **500** (16 páginas), 600 (8), 400 (8) |
| Caixa | frase normal em 28 de 37; **CAIXA ALTA em página de vendas** |
| Altura | **58px** de mediana (56 a 65); páginas de vendas chegam a 72px |
| Padding | perto de **20px 40px** |
| Raio | duas famílias: 4 a 14px (advocacia, B2B, boa parte de vendas) ou pílula 40 a 999px (psi, saúde, imobiliário, algumas vendas) |
| Conteúdo | só o texto, ou texto + ícone do WhatsApp/seta **solto à direita**. Nunca ícone dentro de um quadradinho branco |

## 3. Página e seções

| Item | Valor medido |
|---|---|
| Altura da página no desktop | mediana 7.400px (5.500 a 9.300) |
| Hero | ~800px no desktop |
| Padding vertical | 80px (desktop), 50px (mobile) no container interno |
| Largura do conteúdo | 1140px (dominante) ou 1240px |

## 4. Como regenerar

```bash
# a partir da raiz da skill
python3 scripts/medir_papeis.py paginas/nossas design/dados/medidas-papeis.json
```

Para medir uma página específica, seção por seção, use o raio-x: `python3 scripts/raio_x_molde.py <slug>` (gera `paginas/nossas/<slug>/raio-x/`).
