# Como usar: PÁGINA MENTORIA BANCÁRIO V2 FUTURISTA [JESSICA] (construcao2)

**Propósito:** o que esta página de vendas da casa tem de melhor, o que copiar e o que evitar.
**Quando usar:** como molde de página de vendas escura e "futurista" (laranja sobre preto, objetos 3D de vidro, expert na hero), principalmente em infoproduto para profissionais (bancário, vendas, finanças). Foi a referência que a cliente do teste "Método Renda Bancária" mandou.
**Relacionados:** [style-guide.html](style-guide.html), [ficha.json](ficha.json), [raio-x/raio-x.md](raio-x/raio-x.md), [versão 1 da mesma página](../vendas-mentoria-bancario-jessica/como-usar.md), [PADRAO-DAVI.md](../../../design/PADRAO-DAVI.md), [ANTI-SLOP.md](../../../design/ANTI-SLOP.md)

- **Origem:** paginas/nossas (prioridade alta) · `lp.oreidalanding.com.br/construcao2/`, capturada em 19/10/2026
- **Plataforma:** WordPress + Elementor · **Relevância:** 5/5
- **Nicho:** Página de vendas (mentoria para bancários) · **Tipo de página:** vendas

## O que tem de melhor

Versão 2 da página de vendas da Jéssica, com cara mais moderna que a versão 1: fundo preto com um túnel de luz laranja na hero, a expert real à direita e três ícones 3D de vidro (escudo, cartão, moedas) que vêm **dentro da arte**, não desenhados em HTML. O resto da página alterna seções pretas com faixas laranja finas e fecha com dois planos lado a lado (um escuro, um branco).

## Estrutura de seções (na ordem)

1. **hero** (800px): foto de fundo com a expert, H1 de 33px com a segunda metade em laranja, sub, botão pílula laranja, prova curta "+ de 120 pessoas bateram suas metas" com avatares.
2. **faixa** laranja de 30px.
3. **dor**: "Bater metas no banco não é sorte. É estratégia." com texto e botão escuro.
4. **faixa** de transição.
5. **para quem é**: rótulo em pílula "PARA QUEM É?" + H2 + cards.
6. **conteúdo**: carrossel contínuo de capas de módulo (284x391, raio 4px) + botão.
7. **faixa** amarela de 30px.
8. **bônus**: 3 cards brancos com mockup (464x~350), "BÔNUS 01" espaçado, valor riscado "por R$0,00".
9. **depoimentos**: carrossel contínuo de prints 280x404 (raio 8px).
10. **oferta**: 2 planos (curso online escuro e mentoria branca), lista com check laranja e linha pontilhada, preço 39px, selo "Pagamento 100% seguro".
11. **quem sou eu**: H2 52px, texto e foto 547x667.
12. **FAQ**.
13. **rodapé** de 60px.

## O que vale copiar

- Hero com foto de fundo que já traz os objetos 3D na própria arte (é o jeito certo de ter "elementos flutuando" sem cair no anti-slop).
- Botão pílula com gradiente radial laranja para amarelo, 20px/500 em caixa alta, 72px de altura.
- Rótulo de seção em pílula com borda fina ("INVESTIMENTO", "PARA QUEM É?").
- Faixas finas coloridas (30px) separando blocos pretos.
- Dois planos lado a lado com contraste escuro e claro, lista com check e linha pontilhada entre os itens.
- Carrosséis contínuos para módulos e depoimentos (snippet `codigos/faixas-e-carrosseis/carrossel-linear-continuo.css`).

## O que NÃO copiar

- Os títulos usam `h2` até na hero (não há `<h1>`). Na página nova, o título da hero é `<h1>`.
- Exclamação nos botões ("QUERO COMEÇAR AGORA!"): o guia de copy pede no máximo uma por página.
- Menu: esta página não tem, e a regra fixa do PageBrain também não usa.
- Preços, nomes e prints de depoimento são da cliente. Nunca reaproveite.

## Design em números

- **Fundos:** `#000000`, `#160A06` (hero), gradiente `#000000 → #201002`, branco no plano claro e nos cards de bônus
- **Destaque:** laranja `#F5811E` com amarelo `#FDD16E` no gradiente do botão e das faixas
- **Fontes:** Inter em quase tudo; Manrope só nos rótulos espaçados ("BÔNUS 01", "CURSO ONLINE")
- **Escala desktop:** hero 33px/500 · H2 de seção 33px/600 · "Quem sou eu" 52px · preço 39px · título de plano 30px · corpo 18px/300
- **Botão principal:** gradiente radial laranja, raio 104px, padding 26px 42px, 20px/500 caixa alta, 72px de altura
- **Largura de conteúdo:** 1140px

Medidas completas, seção por seção, e o tamanho de cada imagem (slots): [raio-x/raio-x.md](raio-x/raio-x.md).
