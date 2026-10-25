# Checklist de copy

**Propósito:** a lista que a IA (ou quem for escrever) deve rodar antes de entregar qualquer copy de página.
**Quando usar:** no fim da escrita, antes de montar o HTML e de novo antes de publicar. Toda caixa precisa estar marcada.
**Relacionados:** [tom-de-voz.md](tom-de-voz.md), [metodo-de-copy.md](metodo-de-copy.md), [estrutura-de-pagina.md](estrutura-de-pagina.md), [template-briefing.md](template-briefing.md)

Junta o checklist do Guia de Copy (PDF, vigente), o do guia anterior (TXT) e as regras de página de vendas observadas nas páginas da casa.

## 1. Travessão e palavras proibidas (automático)

- [ ] Busquei "—" e "–" no texto e não sobrou nenhum travessão.
- [ ] Nenhuma palavra da lista proibida: transforme, revolucione, eleve, potencialize, desbloqueie, jornada, experiência única, de forma eficaz, solução completa, excelência, no cenário atual, no mundo de hoje, cada vez mais, "não é apenas X, é Y", "mais do que um X, um Y", descubra como, mergulhe, imagine só.
- [ ] "Cuidado humanizado" (ou parecido) só aparece se a frase seguinte diz o que isso é na prática.
- [ ] No máximo uma exclamação na página (nenhuma em psicologia).
- [ ] Nenhum emoji em headline ou título de card.
- [ ] No máximo uma pergunta retórica seguida de resposta.

Comando para conferir antes de entregar:

```bash
grep -nE "—|–" copy.md
grep -niE "transform|revolucion|elev[ae]|potencializ|desbloque|jornada|experiência única|de forma eficaz|solução completa|excelência|cenário atual|mundo de hoje|cada vez mais|não é apenas|mais do que um|descubra como|mergulh|imagine só" copy.md
grep -c "!" copy.md
```

## 2. Hero

- [ ] A headline continua a promessa do anúncio que leva à página.
- [ ] A headline tem até 12 palavras e uma ideia só.
- [ ] Deixa claro para quem é a página e qual problema ou objetivo ela aborda.
- [ ] A subheadline explica a oferta sem repetir a headline (até 30 palavras).
- [ ] Cidade ou região aparece na hero (kicker, H1 ou sub) e no rodapé.
- [ ] Barra de números com dados reais (ou marcados `[CONFIRMAR COM CLIENTE]`).

## 3. Estrutura e CTAs

- [ ] Até 6 dobras em captação (8 em lançamento imobiliário).
- [ ] Cada dobra tem uma função específica; nenhuma está ali só para encher.
- [ ] Todas as dobras têm CTA e o botão flutuante de WhatsApp está previsto.
- [ ] Os CTAs dizem o que acontece ao clicar, até 5 palavras, nunca "Clique aqui" ou "Saiba mais" sozinho.
- [ ] Mensagem pré-configurada do WhatsApp escrita para cada CTA de serviço.
- [ ] O passo a passo começa pelo WhatsApp.
- [ ] O FAQ responde às objeções reais do nicho (preço, convênio, online ou presencial, tempo, localização, sigilo).

## 4. Fidelidade e ética

- [ ] Toda informação factual (anos, números, prêmios, endereço, registro) veio do cliente ou está marcada `[CONFIRMAR COM CLIENTE]`.
- [ ] Nada de depoimento, número, certificação, resultado garantido ou estatística inventada.
- [ ] Registro profissional correto e junto ao nome: OAB, CRO, CRP, CRM + RQE, CRECI, registro de incorporação.
- [ ] Nada que o conselho do nicho proíbe:
  - Advocacia: sem promessa de resultado, sem valores, sem depoimentos.
  - Psicologia: sem promessa de cura, sem depoimentos de pacientes.
  - Odonto: sem preço nem promoção; antes e depois só dentro da regra do CFO.
  - Medicina: sem promessa; antes e depois só nas condições da Resolução CFM 2.336/2023.
  - Imobiliário: registro de incorporação, CRECI e "imagens ilustrativas" no rodapé.
- [ ] Ressalvas onde há promessa com condição ("*sujeito a avaliação", "rentabilidade passada não garante retorno futuro").

## 5. Escrita e layout

- [ ] Os textos cabem em componentes visuais (cards, listas, etapas) sem virar blocos extensos.
- [ ] Cards de um mesmo grupo com tamanho parecido, mas sem ritmo idêntico.
- [ ] Listas variam de tamanho (não tudo em trio).
- [ ] Sem frases repetidas nem adjetivos empilhados; fatos no lugar de adjetivos.
- [ ] Vocabulário do cliente final, não do profissional.
- [ ] Li a copy em voz alta e soa como uma pessoa falando, não como anúncio de TV.
- [ ] Entregue no formato `## DOBRA N: NOME` com os campos (Kicker, H1, Subheadline, CTA...).

## 6. Só para páginas de vendas

- [ ] Oferta com ancoragem honesta (valor de referência real), parcelado em destaque e valor à vista.
- [ ] Bônus com valor declarado e "por R$0,00" somente se o bônus for real.
- [ ] Garantia com prazo (7 dias é o padrão da casa) e como pedir o reembolso.
- [ ] Escassez só se for real (vagas, lote com data).
- [ ] Botão de compra repetido depois da oferta e no fim.
- [ ] Microcopy de segurança junto ao botão ("Pagamento 100% seguro e liberação imediata").
