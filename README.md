# PageBrain

**O cérebro criador de landing pages do O Rei da Landing, empacotado como skill para o Claude.**

Você pede "uma LP de captação para uma psicóloga de casais em Curitiba" e o PageBrain conduz o Claude pelo mesmo processo que a casa usa nas páginas dela: briefing, copy no método da casa, escolha de uma página real como molde, HTML medido seção por seção, snippets testados, prompts de imagem e, se você quiser, o JSON pronto para importar no Elementor.

A diferença para "pedir uma página para a IA" é o **modo molde**: toda página nova é irmã de uma página real da casa, com os mesmos tamanhos de texto, botões, espaçamentos e ritmo. Por isso ela não sai com cara de template genérico.

## O que vem no pacote

| | |
|---|---|
| **40 páginas da casa** | advocacia, psicologia, saúde, odonto, imobiliário, negócio local, infoproduto e vendas. Cada uma com a página salva (abre offline), o **raio-x** (medidas e print de cada seção), ficha, guia de uso e print |
| **Método de copy** | processo em 7 passos, tom de voz, regras por conselho de classe (OAB, CFP, CFO, CFM, CRECI), fórmulas com exemplos reais, banco de headlines e CTAs, checklist e 37 copys reais transcritas |
| **Padrão de design** | o padrão da casa, os tamanhos reais medidos, a lista anti "cara de IA" e um design system |
| **68 snippets** | CSS base, animação de entrada, WhatsApp, pixels, hero com foto de fundo, botões, cards, faixas, menus, rodapés e seções prontas, com preview ao vivo |
| **Imagens com IA** | slots de imagem no tamanho do molde e estilos de prompt por nicho (com geração direta pelo Magnific, opcional) |
| **Elementor** | 25 JSONs de página, 37 seções prontas, esqueletos, conversor HTML → JSON e validador |
| **32 sites de referência** | estudados (style guide, print e notas) para ideias de componente e efeito |

## Instalação (Claude Code)

1. Copie esta pasta para a pasta de skills do Claude Code, com o nome `pagebrain`:

   ```bash
   # para todos os seus projetos
   git clone <URL-DESTE-REPOSITORIO> ~/.claude/skills/pagebrain
   # ou só para um projeto
   git clone <URL-DESTE-REPOSITORIO> .claude/skills/pagebrain
   ```

2. Instale as dependências dos scripts (Python 3.9+):

   ```bash
   cd ~/.claude/skills/pagebrain
   pip install -r requirements.txt
   python3 -m playwright install chromium   # só se não tiver o Google Chrome instalado
   ```

3. Tenha o [Node.js](https://nodejs.org) instalado (os ícones vêm da CLI do better-icons pelo `npx`).
4. Confira a instalação:

   ```bash
   python3 scripts/verificar_skill.py
   ```

   Precisa terminar com `Resultado: OK`.

Opcional: o conector do **Magnific (Freepik)** no Claude, para gerar as imagens da página. Sem ele, a página sai com os prompts prontos em cada espaço de imagem para você gerar onde preferir.

## Como usar

Abra o Claude Code numa pasta de trabalho e peça a página. Exemplos:

- "Cria uma landing page de captação para a Dra. Ana, dentista de implantes em Campinas. WhatsApp 19 9xxxx-xxxx."
- "Quero uma página de vendas escura para o curso de confeitaria da Marina, no estilo da página da Jéssica bancário."
- "Escreve só a copy de uma LP para advogado previdenciário em Recife."
- "Converte esta página HTML para JSON do Elementor."

O Claude vai pedir o que faltar do briefing, mostrar o molde escolhido e entregar:

1. a copy no formato de dobras, com as mensagens de WhatsApp e a lista do que confirmar com o cliente;
2. `pagina.html` (abre no navegador);
3. `imagens/` com as imagens ou os prompts;
4. (se pedido) o JSON do Elementor validado.

## Regras que toda página segue

- Nenhum travessão no texto, nada inventado (o que o cliente não deu vai como `[CONFIRMAR COM CLIENTE]`) e respeito ao conselho de classe do nicho.
- Toda página reproduz um molde da casa, seção por seção.
- Sem menu, logo acima da headline, títulos em até 3 linhas, ícones da skill better-icons e hero com foto de fundo e fade.
- CTA para o WhatsApp (ou checkout) em toda dobra.

O fluxo completo está no [SKILL.md](SKILL.md). Para entender o acervo, comece por [docs/LEIA-PRIMEIRO.md](docs/LEIA-PRIMEIRO.md).

## Estrutura

```
pagebrain/
├── SKILL.md            ← entrada da skill (o fluxo em 8 passos)
├── docs/               ← leia-primeiro e glossário
├── copy/               ← método de copy, tom, fórmulas, banco, checklist, briefing, copys reais
├── design/             ← padrão da casa, medidas reais, anti-slop, design system
├── paginas/
│   ├── nossas/         ← 40 páginas da casa (molde + raio-x)
│   └── gerais/         ← 32 sites de referência
├── codigos/            ← 68 snippets + preview
├── imagens-ia/         ← slots de imagem e estilos de prompt
├── elementor/          ← JSONs de página, seções, esqueletos e documentação
└── scripts/            ← raio-x, checagem, ícones, conversor, validador, verificação
```

## Licença e conteúdo

Uso conforme [LICENSE.md](LICENSE.md). As páginas de `paginas/nossas` foram feitas pela casa para clientes reais e servem como molde de estrutura e medida: **não copie textos, fotos, marcas nem dados de contato delas**. Os sites de `paginas/gerais` são de terceiros e entram só como estudo (print, notas e paleta).

Feito por Davi Barros Batista · Zarion · O Rei da Landing. Histórico em [CHANGELOG.md](CHANGELOG.md).
