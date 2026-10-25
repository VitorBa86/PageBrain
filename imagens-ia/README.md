# PageBrain · Imagens: slots e geração com IA

**Propósito:** como toda página nova reserva o lugar certo para cada imagem (slot com tamanho e proporção do molde) e como essas imagens são geradas com IA a partir dos seus estilos de prompt por nicho.
**Quando usar:** no passo 5 da SKILL (montar o HTML) e no passo 6b (gerar imagens).
**Relacionados:** [estilos-de-prompt.md](estilos-de-prompt.md), [slot-de-imagem.html](slot-de-imagem.html), [imagens-modelo.json](imagens-modelo.json), [SKILL.md](../SKILL.md), [ANTI-SLOP.md](<../design/ANTI-SLOP.md>)

## 1. Como a página reserva as imagens

Toda página gerada tem uma pasta `imagens/` ao lado do `index.html` e cada imagem entra assim:

```html
<img class="pb-slot" src="imagens/IMG-03.webp" width="454" height="333"
     alt="Notebook com os scripts de venda abertos"
     data-slot="IMG-03" data-prompt="(prompt completo)">
```

- **O nome do arquivo é o ID do slot** (`IMG-01.webp`, `IMG-02.webp`...). Você solta o arquivo com esse nome na pasta `imagens/` e ele aparece na página. Não precisa editar o HTML.
- Enquanto o arquivo não existe, o script de [slot-de-imagem.html](slot-de-imagem.html) mostra uma caixa no tamanho certo com o ID, o tamanho em px, a proporção e um botão para copiar o prompt.
- **Imagem de fundo de seção** usa `data-bg-slot="IMG-01"` no container, com `background-image:url(imagens/IMG-01.webp)` no CSS. O script marca o lugar se o arquivo faltar.
- **Hero (padrão desde 24/10/2026):** dois slots. `IMG-01` é a foto de fundo 16:9 (2400 a 2880px de largura) com a pessoa entre 55% e 90% da largura e o lado esquerdo claro e limpo para o texto (tipo `hero-expert-fundo` em [estilos-de-prompt.md](estilos-de-prompt.md)). `IMG-01-mobile` é um **recorte** da IMG-01, quase quadrado, centralizado no corpo da pessoa, feito com o `ffmpeg` que está no topo de [hero-foto-de-fundo-fade.html](<../codigos/fundos-e-texturas/hero-foto-de-fundo-fade.html>). Não gere uma segunda imagem para o mobile: é a mesma foto, recortada. Referência aprovada: `paginas/nossas/psi-luana-carolina-casais/extraido/assets/hero-bg.jpg` e `hero-bg-mobile.jpg`.
- **Tamanho e proporção vêm do molde**: a tabela "Slot" do `raio-x.md` da página da casa usada como molde diz, por exemplo, que o print de depoimento é 280x498 (0,56) e o mockup de bônus é 454x333 (1,36). Gere a imagem com 2x esse tamanho.
- A lista completa fica em `imagens/imagens.json` (formato em [imagens-modelo.json](imagens-modelo.json)): ID, seção, tipo, tamanho, proporção, prompt, origem (gerar, foto do cliente, print do cliente) e status.

## 2. Três origens de imagem

| Origem | Exemplos | Regra |
|---|---|---|
| **Foto do cliente** | foto do expert no hero e no "quem sou eu", logo | Nunca gerar uma pessoa no lugar do cliente. Usar a foto real; a IA pode **recortar, trocar fundo ou compor** usando a foto como referência, sempre com aprovação do cliente |
| **Print do cliente** | depoimentos de WhatsApp, resultados, avaliações | Nunca gerar print falso. Slot vazio até o cliente mandar. Borrar foto e trocar nome quando o cliente pedir |
| **Gerar com IA** | fundo do hero, fundos de seção, ícones 3D, capas de módulo, mockups de bônus, texturas | Prompt montado a partir de [estilos-de-prompt.md](estilos-de-prompt.md) (estilo do nicho + o que a imagem mostra + proporção) |

## 3. Onde gerar

### Opção recomendada: Magnific (Freepik) conectado ao Claude

Com o conector do Magnific ligado no Claude, o próprio Claude gera, baixa e encaixa as imagens da página. Custos medidos em 21/10/2026 (confira sempre com `simulate_cost`, porque mudam):

| Modelo no Magnific | Uso | Custo por imagem |
|---|---|---|
| Seedream 5 Pro | padrão: fundos, cenas, composição com a foto do expert como referência | 100 créditos |
| Nano Banana 2 Lite | rascunhos rápidos e variações baratas | 60 créditos |
| Nano Banana Pro | peça final com máxima fidelidade à foto de referência | mais caro, conferir com `simulate_cost` |
| GPT 2 / Recraft | ícones, imagens com texto legível, capas com título | conferir com `simulate_cost` |

Uma LP com 12 a 15 imagens geradas custa entre 1.000 e 1.500 créditos. **Pelo conector, a geração consome créditos** (planos com geração ilimitada costumam valer só no site, não na integração). Por isso o Claude sempre mostra a lista de imagens e o custo total e **espera o OK antes de gerar**.

Fluxo que o Claude segue:

1. Monta `imagens/imagens.json` com todos os slots e prompts.
2. Para slots com foto do cliente como referência, sobe a foto para o Magnific (upload de arquivo local) e usa como referência do tipo `image`.
3. Simula o custo total, mostra a lista e pede confirmação.
4. Gera com a proporção do slot, baixa o resultado, converte para WebP com o nome `IMG-NN.webp` e salva em `imagens/`.
5. Atualiza o status no `imagens.json` e tira um print da página para aprovação.

### Opção sem conector: gerar onde você preferir

1. Peça ao Claude a página "só com os prompts".
2. Abra a página, clique em "Copiar prompt" em cada slot e gere na ferramenta que você usa (Magnific, Midjourney, Gemini, ChatGPT...), na proporção indicada na caixa.
3. Salve cada imagem como `IMG-NN.webp` (ou `.jpg`/`.png`, avisando o Claude) na pasta `imagens/`. A página mostra sozinha.

### Gratuitos testados

O Pollinations (gratuito, sem chave) foi testado em 21/10/2026: respondeu em 9 segundos, mas entregou um modelo fraco e com marca d'água. Serve só para rascunho de layout, não para página de cliente. O Google AI Studio permite gerar com Nano Banana de graça na interface web, mas não na integração automática.

## 4. Antes de publicar

- [ ] Todo slot tem arquivo real ou está listado como pendência para o cliente.
- [ ] Nenhuma pessoa gerada fingindo ser o cliente; nenhum print ou número falso.
- [ ] Imagens em WebP, com no máximo 2x o tamanho do slot (hero até 2880px de largura).
- [ ] `alt` descritivo em todas.
- [ ] Para o Elementor: subir as imagens na biblioteca do WordPress e trocar o `src` (o conversor avisa).
