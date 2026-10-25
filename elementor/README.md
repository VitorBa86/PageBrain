# PageBrain · Elementor

**Propósito:** índice da pasta com os JSONs de página inteira do Elementor e toda a documentação para ler, editar, gerar e converter HTML em JSON no padrão da casa.
**Quando usar:** quando a página precisa ir para o Elementor, seja importando um JSON pronto, partindo de um esqueleto ou convertendo um HTML.
**Relacionados:** [SKILL.md](../SKILL.md), [secoes/catalogo-secoes.md](secoes/catalogo-secoes.md), [design/PADRAO-DAVI.md](<../design/PADRAO-DAVI.md>)

## Conteúdo

| Arquivo | O que é |
|---|---|
| [paginas/captacao/](paginas/captacao/) | 17 JSONs de páginas de captação (WhatsApp), com o nome da página da casa (`psi-renan.json`, `adv-calgarotto.json`...). |
| [paginas/vendas/](paginas/vendas/) | 8 JSONs de páginas de vendas. |
| [secoes/](secoes/README.md) | 37 seções isoladas em 13 tipos, com preview. |
| [previews/](previews/) | Pré-visualização `.jpg` de cada JSON de página. |
| [indice.md](indice.md) / [indice.json](indice.json) | Cada JSON com título, nicho, nº de seções, widgets, fontes, cores, página publicada correspondente e observações. |
| [anatomia-json-elementor.md](anatomia-json-elementor.md) | A estrutura do JSON explicada campo a campo. **Só containers flexbox**, versão 0.4. |
| [padroes-recorrentes.md](padroes-recorrentes.md) | Valores que se repetem: 1140/1240px, padding 80/80, gap 20, hero 800px, fonte em vw no mobile, classes e CSS custom. |
| [mapa-html-para-elementor.md](mapa-html-para-elementor.md) | Tabela HTML/CSS para widget/setting, o que não tem equivalente e as limitações do conversor. |
| [regras-html-convertivel.md](regras-html-convertivel.md) | Como escrever HTML que converte bem. |
| [templates/](templates/) | Esqueletos limpos e página de exemplo (ver abaixo). |
| [scripts/html-para-elementor.py](../scripts/html-para-elementor.py) | Conversor HTML para JSON do Elementor. |
| [scripts/validar-json-elementor.py](../scripts/validar-json-elementor.py) | Validador: estrutura, IDs únicos e vocabulário de chaves igual ao da casa. |

### templates/

| Arquivo | Uso |
|---|---|
| [esqueleto-captacao-psi-12-secoes.json](templates/esqueleto-captacao-psi-12-secoes.json) | Página de captação completa (base: psi-renan), sem conteúdo do cliente: textos `[TÍTULO n]`, `[TEXTO n]`, `[CTA]`, imagens placeholder, links `wa.me/55DDDNUMERO`. 148 elementos. |
| [esqueleto-vendas-produto-digital.json](templates/esqueleto-vendas-produto-digital.json) | Página de vendas completa (base: scripts-consignado), limpa. 128 elementos. |
| [exemplo-pagina-convertivel.html](templates/exemplo-pagina-convertivel.html) | Página HTML de exemplo que segue todas as regras de conversão. |
| [exemplo-pagina-convertida.json](templates/exemplo-pagina-convertida.json) | Resultado do conversor sobre o exemplo acima. Importável no Elementor. |

Os esqueletos mantêm todo o design (cores, tipografia, espaçamentos, responsivo, classes de animação e CSS base em `page_settings`), sem as chaves de addons (`ha_*`, `eae_*`). Os widgets HTML foram esvaziados com um comentário indicando o snippet a colar.

## Três caminhos para chegar ao Elementor

1. **Página parecida com uma da casa:** importe o JSON original (ver [indice.md](indice.md)) e troque textos e imagens.
2. **Página nova a partir de estrutura padrão:** importe um esqueleto de `templates/` e preencha.
3. **Página escrita em HTML pela IA:** siga [regras-html-convertivel.md](regras-html-convertivel.md) e rode o conversor.

## Teste do conversor

| Entrada | Resultado |
|---|---|
| `templates/exemplo-pagina-convertivel.html` (HTML seguindo as regras) | 8 seções, 63 elementos (22 containers, 18 text-editor, 12 heading, 4 html, 3 button, 2 image, 1 icon-list, 1 toggle). **0 erros, 0 chaves fora do vocabulário da casa.** Mobile com `flex_direction_mobile: column`, `padding_mobile` e fonte em vw. |
| `paginas/nossas/psi-renan/extraido/index.html` (HTML gerado pelo Elementor) | 807 elementos contra 182 do JSON original: os wrappers internos do Elementor viram containers. **Não use o conversor para páginas já feitas no Elementor**: use o JSON original. |
| `paginas/gerais/adv-garcia-almeida-trabalhista` (site externo, sem as regras) | 13 seções, 294 elementos, 43 widgets HTML. Converte, mas exige limpeza manual. Serve para acelerar uma cópia de layout, não para publicar direto. |

As limitações completas estão em [mapa-html-para-elementor.md](mapa-html-para-elementor.md#limitações-do-conversor-scriptshtml-para-elementorpy). A validação é estrutural e por vocabulário de chaves (o JSON só usa o que aparece nos JSONs reais da casa). Antes de entregar ao cliente, importe uma vez num WordPress de teste.

## Dependências dos scripts

- Python 3.9+ e `pip install -r requirements.txt` (na raiz da skill).
- Google Chrome instalado ou o Chromium do Playwright (`python3 -m playwright install chromium`). Os scripts acham o navegador sozinhos; para forçar um, use `--chrome CAMINHO` ou a variável `PAGEBRAIN_CHROME`.
- Rode os comandos a partir da raiz da skill: `python3 scripts/html-para-elementor.py ...`.
