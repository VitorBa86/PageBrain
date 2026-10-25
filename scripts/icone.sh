#!/usr/bin/env bash
# PageBrain · Ícones com a skill better-icons (https://github.com/better-auth/better-icons)
#
# Todo ícone de página do PageBrain vem daqui (nunca desenhado à mão, nunca emoji).
# Usa a CLI do better-icons via npx (não precisa instalar nada). Coleção padrão: lucide (traço fino).
#
# Uso:
#   ./icone.sh buscar "coração"            # lista ids (lucide por padrão)
#   ./icone.sh buscar "heart" mdi          # busca em outra coleção
#   ./icone.sh pegar lucide:heart-crack    # imprime o SVG pronto para colar inline
#   ./icone.sh pegar lucide:flame 1.6 out/ # salva out/flame.svg
#
# O SVG sai limpo: sem width/height fixos (o tamanho vem do CSS), sem preenchimento sólido
# (a CLI às vezes devolve fill="currentColor" nos paths, o que deixa o ícone chapado),
# traço em currentColor com espessura 1.6 (padrão da página de referência psi-luana-carolina-casais).
#
# Na página: <span class="card-ic">SVG</span> com .card-ic svg{width:22px;height:22px}
# e a cor definida por color no .card-ic.
set -euo pipefail

acao="${1:-}"
case "$acao" in
  buscar)
    termo="${2:?informe o termo de busca}"
    colecao="${3:-lucide}"
    npx -y better-icons search "$termo" --prefix "$colecao" --limit 20
    ;;
  pegar)
    id="${2:?informe o id, ex.: lucide:heart}"
    traco="${3:-1.6}"
    destino="${4:-}"
    svg="$(npx -y better-icons get "$id" 2>/dev/null | grep '<svg' \
      | sed -E 's/ (width|height)="[^"]*"//g; s/ xmlns="[^"]*"//; s/stroke-width="[0-9.]+"/stroke-width="'"$traco"'"/g')"
    if [ -z "$svg" ]; then echo "ícone não encontrado: $id" >&2; exit 1; fi
    # ícone de traço (lucide, tabler...): tira o preenchimento sólido. Ícone sólido (mdi...): mantém.
    # (a CLI também enche <circle>, <rect> e <ellipse>: ex. lucide:award, lucide:users, lucide:lock saíam chapados)
    if [[ "$svg" == *'stroke="currentColor"'* ]]; then svg="$(printf '%s' "$svg" | sed -E 's/<(path|circle|rect|ellipse) fill="currentColor"/<\1/g')"; fi
    # a CLI às vezes perde width/height do <rect> (lucide:lock, lucide:clipboard-list): sem eles o retângulo some.
    if printf '%s' "$svg" | grep -Eq '<rect [^>]*>' && ! printf '%s' "$svg" | grep -Eq '<rect [^>]*width='; then
      echo "AVISO: $id tem <rect> sem width/height. Complete à mão (lucide:lock: width=\"18\" height=\"11\"; lucide:clipboard-list: width=\"8\" height=\"4\")." >&2
    fi
    svg="${svg/<svg /<svg aria-hidden=\"true\" }"
    if [ -n "$destino" ]; then
      mkdir -p "$destino"; nome="${id#*:}"; printf '%s\n' "$svg" > "$destino/$nome.svg"; echo "$destino/$nome.svg"
    else
      printf '%s\n' "$svg"
    fi
    ;;
  *)
    sed -n '2,20p' "$0"; exit 1;;
esac
