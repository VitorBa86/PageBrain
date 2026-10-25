# PageBrain · Histórico de versões

**Propósito:** o que mudou em cada versão da skill.
**Quando usar:** antes de atualizar uma instalação antiga, ou para entender por que uma regra existe.
**Relacionados:** [README.md](README.md), [SKILL.md](SKILL.md)

## 1.0.0 · 25/10/2026 · primeira versão pública

Reorganização do acervo para virar uma skill instalável e compartilhável.

- Estrutura de skill: `SKILL.md` na raiz e pastas com nomes sem espaço nem acento (`copy/`, `design/`, `codigos/`, `imagens-ia/`, `elementor/`, `paginas/`, `scripts/`, `docs/`).
- Pacote de 2,7 GB para cerca de 260 MB, sem perder conteúdo útil: saíram os zips duplicados das capturas, os prints PNG em tamanho original (viraram `print.jpg`), as fontes legadas que o navegador nunca carrega (EOT, SVG, fallbacks e subconjuntos não latinos), a cópia completa dos 32 sites de terceiros (ficaram style guide, print e as imagens do style guide) e os arquivos de construção do acervo.
- Nova página da casa: `vendas-mentoria-bancario-jessica-v2` (construcao2), com raio-x, ficha e como-usar. Total: 40 páginas.
- JSONs do Elementor renomeados com o nome da página (`elementor/paginas/captacao/psi-renan.json`).
- Scripts portáveis: acham o Google Chrome em macOS, Linux e Windows ou usam o Chromium do Playwright (`scripts/_navegador.py`).
- Conversor HTML → Elementor corrigido: classes de container agora vão em `css_classes` (como nos JSONs da casa), não em `_css_classes`, que é a chave de widget. Com a chave errada, as classes do scroll reveal nos containers corriam o risco de não aparecer no Elementor. O validador deixou de usar a saída do próprio conversor como referência (era isso que escondia o erro).
- Novo `scripts/verificar_skill.py` (links, JSONs, travessões, páginas completas, tamanho e nomes de arquivo).
- Snippets e a copy de referência de vendas sem nenhum travessão.
- SKILL.md ganhou o mapa de pastas, os requisitos e o passo "Quando o usuário aprovar uma página".

## Antes da 1.0 (13 a 25/10/2026)

- **13/10:** acervo montado: 37 páginas da casa medidas no navegador, 32 sites de referência, método de copy a partir dos guias do Davi, 67 snippets, 25 JSONs de página e 37 seções do Elementor, conversor e validador HTML → Elementor.
- **14/10:** o acervo ganhou o nome PageBrain.
- **21/10:** "modo molde" depois de um teste com cara de IA: toda página nova reproduz uma página da casa seção por seção. Entraram o `raio_x_molde.py`, `MEDIDAS-REAIS.md` (tamanhos reais, menores do que o padrão antigo dizia), `ANTI-SLOP.md` e a pasta de imagens (slots e prompts por nicho).
- **24/10:** regras fixas do PageBrain (sem menu, logo acima da headline, títulos em até 3 linhas, ícones da skill better-icons, hero com foto de fundo e fade), a referência de padrão `psi-luana-carolina-casais`, o `checar_pagina.py` e o `icone.sh`.
- **25/10:** referência de vendas escura `vendas-luana-carolina-metodo-lua` e a seção "Armadilhas já resolvidas" do SKILL.md.
