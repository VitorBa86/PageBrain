# PageBrain · Scripts

**Propósito:** as ferramentas que a skill usa no dia a dia: medir um molde, conferir uma página gerada, pegar ícones, converter para Elementor e verificar a própria skill.
**Quando usar:** nos passos 3, 5, 7 e 8 do [SKILL.md](../SKILL.md), e antes de publicar uma versão nova da skill.
**Relacionados:** [SKILL.md](../SKILL.md), [requirements.txt](../requirements.txt), [elementor/README.md](../elementor/README.md)

Rode tudo **a partir da raiz da skill** (pasta `pagebrain/`).

## Instalação

```bash
pip install -r requirements.txt
python3 -m playwright install chromium   # só se não tiver o Google Chrome instalado
```

Os scripts acham o navegador sozinhos ([_navegador.py](_navegador.py)): primeiro a variável `PAGEBRAIN_CHROME`, depois o Google Chrome instalado (macOS, Linux ou Windows) e, por fim, o Chromium do Playwright. O `icone.sh` precisa de Node.js (usa `npx`).

## Os scripts

| Script | O que faz | Uso |
|---|---|---|
| [raio_x_molde.py](raio_x_molde.py) | Fatia uma página em seções e mede tudo que a página nova precisa copiar: textos (tamanho, peso, fonte, cor, line-height), botões, cards, paddings, fundos e o tamanho de cada imagem (vira o slot). Gera `raio-x.md`, `raio-x.json`, `secao-NN.jpg` e `pagina-mobile.jpg`. | `python3 scripts/raio_x_molde.py <slug>` (página da casa) ou `python3 scripts/raio_x_molde.py pagina.html /tmp/rx` |
| [checar_pagina.py](checar_pagina.py) | Confere as regras fixas numa página gerada: sem menu, logo acima do H1, cada H1/H2 em até 3 linhas (4 se longo) e no máximo 55px em 1440 e 390px, botão da hero visível sem rolar em 390x664, sem rolagem horizontal, sem emoji como ícone. Sai com código 1 se houver ERRO. | `python3 scripts/checar_pagina.py pagina.html [--com-menu] [--logo-livre] [--prints pasta]` |
| [icone.sh](icone.sh) | Busca e pega ícones pela skill better-icons (coleção lucide por padrão) e devolve o SVG limpo para colar inline (sem tamanho fixo, traço 1,6, `currentColor`). | `scripts/icone.sh buscar "coração"` · `scripts/icone.sh pegar lucide:heart-crack` |
| [html-para-elementor.py](html-para-elementor.py) | Converte um HTML escrito com as [regras de HTML convertível](../elementor/regras-html-convertivel.md) em JSON do Elementor (containers flexbox, fonte do mobile em vw). | `python3 scripts/html-para-elementor.py pagina.html pagina.json --titulo "Cliente" [--clipboard] [--offline]` |
| [validar-json-elementor.py](validar-json-elementor.py) | Valida o JSON: estrutura, IDs únicos e vocabulário de chaves igual ao dos JSONs reais da casa. Precisa terminar com 0 erros. | `python3 scripts/validar-json-elementor.py pagina.json` |
| [elementor-para-preview.py](elementor-para-preview.py) | Gera uma pré-visualização HTML (e PNG) de um JSON do Elementor, sem WordPress. | `python3 scripts/elementor-para-preview.py pagina.json preview.html --png preview.png` |
| [shot.py](shot.py) | Screenshot de um HTML com contagem de erros de console e de arquivos locais faltando. | `python3 scripts/shot.py pagina.html saida.png --full --width 1440` |
| [medir_papeis.py](medir_papeis.py) | Mede os papéis tipográficos (hero, título de seção, corpo, botão) de todas as páginas da casa; base de [design/MEDIDAS-REAIS.md](../design/MEDIDAS-REAIS.md). | `python3 scripts/medir_papeis.py paginas/nossas design/dados/medidas-papeis.json` |
| [verificar_skill.py](verificar_skill.py) | Verifica a skill inteira: links, JSONs, travessões, páginas da casa completas, tamanho e nomes de arquivo. Com `--navegador`, abre os style guides e confere erros. | `python3 scripts/verificar_skill.py [--navegador]` |

## Incluir uma página nova da casa

1. Salve a página publicada (extensão de captura de site ou "Salvar como página completa") e coloque o conteúdo em `paginas/nossas/<nicho-nome>/extraido/` com o `index.html` na raiz.
2. `python3 scripts/raio_x_molde.py <nicho-nome>` gera o molde medido.
3. Escreva `ficha.json` e `como-usar.md` no formato das outras páginas (copie de uma do mesmo nicho) e salve um `print.jpg` da página inteira.
4. Inclua a página em `paginas/nossas/CATALOGO.md` e `paginas/nossas/catalogo.json`.
5. `python3 scripts/verificar_skill.py` sem ERRO.
