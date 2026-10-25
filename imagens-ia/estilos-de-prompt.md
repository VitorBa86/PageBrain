# PageBrain · Estilos de prompt por nicho

**Propósito:** a sua biblioteca de estilos de imagem. O Claude monta o prompt de cada slot juntando três partes: o **estilo do nicho** (daqui), o **tipo de imagem** (daqui) e o **assunto** (da copy da seção).
**Quando usar:** sempre que uma página nova tiver slots do tipo "gerar com IA". Edite à vontade: o que estiver aqui é o que a IA vai seguir.
**Relacionados:** [README.md](README.md), [SKILL.md](../SKILL.md)

> **Como preencher:** os blocos marcados com `SUGESTÃO INICIAL` foram escritos a partir das páginas da casa (por exemplo, a da Jéssica bancário e a construcao2). Funcionam como estão; troque pelos seus prompts quando tiver um estilo próprio e apague a marcação. Prompts em inglês funcionam melhor nos modelos; deixe as notas em português.

## Como o prompt é montado

```
[TIPO DE IMAGEM] + [ASSUNTO da seção] + [ESTILO DO NICHO] + [PALETA do cliente] + [REGRAS FIXAS]
```

Exemplo (slot de capa de módulo, infoproduto bancário, laranja e preto):

```
Course module cover, vertical 4:5. Subject: a glossy 3D credit card and coins floating.
Style: dark cinematic background, warm volumetric glow, 3D glass icons with soft reflections, premium.
Palette: black #0E0E0E and orange #F7931E. No text, no logos, no watermark.
```

## Regras fixas (entram em todo prompt)

- `No text, no letters, no logos, no watermark` (texto vai no HTML, não na imagem), exceto quando o slot for de capa com título e o modelo escolhido for GPT 2 ou Recraft.
- Nunca descrever o cliente para "criar" uma pessoa parecida. Pessoa real = foto do cliente como referência.
- Proporção sempre a do slot (ver `imagens.json`).
- Paleta: as 2 ou 3 cores do briefing em hex.

## Tipos de imagem

| Tipo | Onde entra | Proporção comum | SUGESTÃO INICIAL de prompt base |
|---|---|---|---|
| `hero-expert-fundo` | **padrão do PageBrain (24/10/2026):** fundo inteiro da hero com o expert, no lugar da foto recortada (snippet `hero-foto-de-fundo-fade.html`). Usa a foto do cliente como referência (Nano Banana Pro ou Seedream 5 Pro) | 16:9 (ex.: 2752x1536) | `Keep the person from the reference exactly as is (face, hair, body). Wide 16:9 photo of her standing in [ambiente do nicho, ex.: bright modern office with wooden shelves, plants and framed art], placed between 55% and 90% of the frame width, body visible from head to hips, smiling at camera. The left 45% of the frame is a clean, bright, softly lit wall or curtain with no objects, so text can sit on top. Warm natural light, shallow depth of field, editorial photography` |
| `fundo-hero` | fundo da primeira dobra sem pessoa (quando o cliente não tem foto) | 16:9 ou 1440x800 | `Wide background for a website hero, empty left side for text, subject area on the right, depth and light rays, no people` |
| `fundo-secao` | fundo de seção escura ou de oferta | 16:9 | `Subtle abstract background texture, low contrast, lots of negative space, soft gradient light from one corner` |
| `composicao-expert` | expert recortada sobre cenário (usa a foto do cliente como referência) | 4:5 ou 3:4 | `Keep the person from the reference exactly as is (face, hair, clothes). Place her in [cenário], studio lighting matching the scene` |
| `icone-3d` | ícones dos cards, elementos que flutuam no hero | 1:1, fundo transparente | `Single 3D glossy glass icon of [objeto], soft reflections, centered, isolated` |
| `capa-modulo` | carrossel de módulos e área de membros | 4:5 ou 2:3 | `Course module cover artwork about [tema do módulo], strong central object, dramatic light` |
| `mockup-bonus` | bônus, entregáveis, oferta | 4:3 | `Realistic device mockup (laptop or phone) showing [conteúdo], placed on [cor] background, soft shadow` |
| `cena-nicho` | seções de dor, para quem é, sobre o serviço | 3:2 | `Authentic photo of [cena], natural light, candid, shallow depth of field` |

## Estilos por nicho

Cada bloco descreve o "clima" das imagens daquele nicho. Os exemplos citados são páginas da casa (`paginas/nossas`).

### Infoproduto e vendas (Jéssica bancário, construcao2, Morelli, barbearia Toledo)
SUGESTÃO INICIAL:
```
Dark cinematic environment, near-black background, strong warm volumetric glow in the brand color,
3D glossy glass objects with reflections, premium tech mood, high contrast, sharp details.
```

### Advocacia (Barros e Carvalho, Calgarotto, Gustavo Kehl)
SUGESTÃO INICIAL:
```
Sober and premium office atmosphere, dark wood, books, marble, soft window light, deep navy and gold tones,
editorial photography, serious and trustworthy, no gavel cliches.
```

### Psicologia (Renan, Maria Rita, Rosangela, Vivian)
SUGESTÃO INICIAL:
```
Calm and warm interior, natural light, linen and plants, soft beige and earthy tones,
quiet and welcoming, film photography feel, no clinical look, no sad stock faces.
```

### Saúde e estética (Cecília Borges, Luciano Grisotto, Pedro Camargo)
SUGESTÃO INICIAL:
```
Clean high-end clinic, soft diffused light, neutral palette with one brand accent,
elegant and reassuring, editorial beauty photography, no surgery or blood.
```

### Odontologia (JV Clínica, Rubiane Vitali)
SUGESTÃO INICIAL:
```
Bright modern dental clinic, natural smiles, soft beige and white, warm daylight, friendly and premium.
```

### Imobiliário (Vega, Vitta, The Palace, MB2)
SUGESTÃO INICIAL:
```
Architectural photography, golden hour, wide angle, premium residential building and interiors,
realistic materials, aspirational lifestyle, no fake signage.
```

### Negócio local (Santa Boemia, Inter Frios, Hoffen, Harmony)
SUGESTÃO INICIAL:
```
Authentic photo of the real place and work, vivid but natural colors, people in action, documentary feel.
```

## Seus estilos

Adicione abaixo estilos próprios com nome, para pedir "usa o estilo X":

```
### [nome do estilo]
Quando usar:
Prompt:
Modelo preferido (Seedream 5 Pro, Nano Banana, GPT 2...):
Exemplo de página onde usei:
```

### Beleza escura com glow violeta
Quando usar: hero e fundos de páginas de vendas de estética, beleza e harmonização com visual escuro e premium (lábios, pele, maquiagem). Troque o gesto e a roupa pelo do nicho.
Prompt (hero-expert-fundo, 16:9, com 2 fotos reais da expert como referência):
```
Keep the woman from the reference photos exactly as she is: same face, same hair, same eyes, same features.
Wide 16:9 studio beauty photo for a website hero. She stands on the right side of the frame, between 58% and 88%
of the width, body visible from head to waist, facing camera with a soft confident look, [GESTO DO NICHO, ex.:
applying clear lip gloss with the applicator wand near her lips]. She wears a [COR DA MARCA] off-the-shoulder fitted top.
Background: deep near-black studio (#0D0B12) with large soft-focus glowing violet [ELEMENTO DO NICHO, ex.: lip-print
shapes] floating out of focus behind her, a gentle violet rim light and a soft halo glow behind her head and shoulders.
The left 45% of the frame is dark, clean and empty, so text can sit on top. Cinematic editorial beauty photography,
shallow depth of field, sharp skin detail, natural skin texture. No text, no letters, no logos, no watermark.
```
Modelo preferido: Seedream 5 Pro no Magnific (100 créditos, 2560x1440). No Paper, `google-nano-banana-2-1` com a prancheta de fotos reais em `reference_nodes` funcionou; `nano-banana-pro-edit` deu erro.
Exemplo de página onde usei: `paginas/nossas/vendas-luana-carolina-metodo-lua` (IMG-01).
Cuidados: a imagem gerada pelo Paper veio com uma emenda vertical no meio do fundo (a referência era um painel com 2 fotos lado a lado); um fade mais largo (até 1180px) escondeu. Prefira uma prancheta de referência com 1 foto só.
