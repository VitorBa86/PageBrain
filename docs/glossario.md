# PageBrain · Glossário

**Propósito:** os termos usados pela casa e neste acervo, com o significado de cada um.
**Quando usar:** sempre que um termo dos documentos ou de um pedido do Davi não estiver claro.
**Relacionados:** [LEIA-PRIMEIRO.md](LEIA-PRIMEIRO.md), [SKILL.md](../SKILL.md), [copy/metodo-de-copy.md](<../copy/metodo-de-copy.md>)

Termos marcados com (inferido) foram deduzidos do uso nos arquivos, não definidos pelo Davi.

## Negócio e marca

| Termo | Significado |
|---|---|
| **PageBrain** | Nome deste acervo: o cérebro criador de páginas da casa. Reúne copy, design, código e conversão para Elementor. Pasta raiz `pagebrain/` (a skill), entrada em `SKILL.md`. |
| **Davi** | Davi Barros Batista, dono do método e autor do guia de copy. |
| **Zarion** | Nome da empresa/marca do Davi citado no guia de copy. |
| **O Rei da Landing** | Marca que hospeda as páginas em `lp.oreidalanding.com.br/<cliente>/`. |
| **A casa** | Neste acervo: o Davi e a empresa dele. "Padrão da casa" = o que se repete nas páginas próprias. |
| **Páginas nossas** | Páginas feitas pela casa (pasta `paginas/nossas`). Prioridade alta. |
| **Páginas gerais** | Sites de terceiros usados como referência (pasta `paginas/gerais`). |
| **Cliente final** | O público do cliente (paciente, comprador, bancário), para quem a copy fala. |

## Tipos de página

| Termo | Significado |
|---|---|
| **LP** | Landing page. Página de um objetivo só. |
| **LP de captação** | Página cujo objetivo é levar ao WhatsApp (ou formulário). A maioria das páginas da casa. |
| **Página de vendas** | Página que leva ao checkout (curso, guia, ingresso, produto). |
| **Página de aplicação** (inferido) | Página que leva a um formulário de qualificação ou agendamento de consultoria gratuita (Carol, Victor Leão, Harmony, RP Vision). |
| **Lançamento imobiliário** | Página de empreendimento na planta, com até 8 dobras e formulário. |
| **VSL** | Video Sales Letter: página de vendas centrada num vídeo (JSONs "VSL CRISTAO" e "VSL CRIPTO"). |
| **Institucional** | Site da empresa com várias áreas, não focado em uma ação (MB2, Hoffen). |

## Copy

| Termo | Significado |
|---|---|
| **Copy** | Todo o texto da página. |
| **Dobra** | Uma seção da página (o que cabe numa "dobra" da tela). A captação tem até 6. |
| **Hero / primeira dobra** | A primeira seção: kicker, H1, subheadline, CTA, selo. |
| **Kicker** | Linha pequena acima do H1 com serviço + cidade ou público. |
| **Headline / H1** | O título principal; até 12 palavras. |
| **Subheadline** | Frase abaixo do H1 que explica como resolve e para quem. |
| **Rótulo** (inferido) | Texto pequeno em caixa alta acima do H2 de cada seção ("SERVIÇOS", "COMO FUNCIONA"). |
| **CTA** | Call to action: o botão e o texto dele ("Agendar minha avaliação"). |
| **Microcopy** | Texto pequeno de apoio, como o que fica abaixo do botão ("Sem compromisso"). |
| **Mensagem pré-configurada** | Texto que já abre escrito no WhatsApp ao clicar no CTA. |
| **Prova social** | Depoimentos, avaliações do Google, números, logos de clientes. |
| **Ancoragem** | Mostrar um valor maior riscado antes do preço da oferta. |
| **Lote** | Faixa de preço por período em eventos (Lote 1, preço cheio). |
| **Bônus** | Itens extras da oferta, com valor declarado "por R$0,00". |
| **Garantia de 7 dias** | Prazo de reembolso padrão nas páginas de vendas. |
| **[CONFIRMAR COM CLIENTE]** | Marcação obrigatória para todo dado que o cliente não forneceu. |
| **Conselho de classe** | OAB (advocacia, Provimento 205/2021), CFP (psicologia), CFO (odontologia), CFM (medicina, Resolução 2.336/2023), CRECI (imobiliário). |
| **Palavras proibidas** | Lista do guia que denuncia texto de IA: transforme, jornada, excelência, eleve etc. |
| **Travessão** | Os caracteres — e –. Proibidos em qualquer copy da casa. |

## Design

| Termo | Significado |
|---|---|
| **Faixa / marquee** | Tira horizontal que corre infinitamente com palavras-chave. |
| **Marca-texto** | Fundo colorido atrás de uma palavra do título (ex.: amarelo no Santa Boemia). |
| **Barra de números / selo** | 3 ou 4 dados reais logo abaixo do hero. |
| **Botão flutuante** | Ícone fixo de WhatsApp no canto da tela. |
| **Scroll reveal** | Animação da casa: blocos com classe `scroll-bottom/left/right/top` entram quando aparecem na tela. |
| **Brilho no botão** | Faixa branca que atravessa o botão em loop. |
| **Borda degradê** | Borda de 1px com gradiente feita com `mask-composite`. |
| **Vidro fosco** | `backdrop-filter: blur()` em cards e menus. |
| **Style guide** | Arquivo `style-guide.html` de cada site: paleta, tipografia, botões, cards e estrutura. |
| **Design system Davi** | O style guide consolidado de todas as páginas da casa. |

## Elementor e código

| Termo | Significado |
|---|---|
| **Elementor** | Construtor de páginas do WordPress usado em todas as páginas da casa (versão Pro). |
| **Container** | Bloco de layout flexbox do Elementor. A casa usa só containers (nunca section/column). |
| **Boxed / Full** | Container com largura limitada (`boxed_width`, ex.: 1140px) ou de largura total. |
| **Widget** | Elemento de conteúdo: heading, text-editor, button, image, icon-box, icon-list, html... |
| **Widget HTML** | Widget que aceita HTML, CSS e JS livres. Usado para menus, rodapés, gráficos e scripts. |
| **CSS personalizado** | Campo do Elementor Pro para CSS por elemento ou por página. `selector` aponta para o próprio elemento. |
| **JSON do Elementor** | Arquivo de exportação de template (`content`, `page_settings`, `version 0.4`). |
| **Colar de outro site** | Função do Elementor para colar um JSON no formato `{"type":"elementor","elements":[...]}`. |
| **Esqueleto** | JSON de página limpo, sem conteúdo do cliente, para começar uma página nova. |
| **HTML convertível** | HTML escrito seguindo as regras de `elementor/regras-html-convertivel.md`. |
| **vw no mobile** | Padrão da casa: tamanho de fonte do mobile em unidades de viewport (ex.: 7.2vw). |
| **Happy Addons / EAE** | Plugins de addon do Elementor; deixam chaves `ha_*` e `eae_*` nos JSONs. |
| **Pixel / gtag / GTM** | Códigos de rastreio: Meta Pixel, tag do Google Ads e Google Tag Manager. |
| **extraido/** | Pasta com o site baixado (index.html + assets) dentro de cada pasta de site. |
| **captura.json** | Relatório da ferramenta que baixou o site (URL, plataforma, lista de arquivos). |
