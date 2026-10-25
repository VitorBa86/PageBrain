#!/usr/bin/env python3
"""
validar-json-elementor.py
Confere se um JSON gerado (ex.: pelo html-para-elementor.py) usa apenas tipos de elemento, widgetTypes
e chaves de settings que aparecem nos JSONs reais da casa (pastas elementor/paginas e elementor/secoes). Também valida a estrutura mínima.
Uso: python3 validar-json-elementor.py arquivo.json [pasta_de_referencia]
"""
import json, sys, glob, os
alvo = sys.argv[1]
ref = sys.argv[2] if len(sys.argv) > 2 else os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'elementor')
keys = {}; wtypes = set()
def coleta(n):
    for x in n:
        k = x.get('widgetType') or x['elType']; wtypes.add(k)
        s = x.get('settings') if isinstance(x.get('settings'), dict) else {}
        keys.setdefault(k, set()).update(s.keys()); coleta(x.get('elements', []))
for f in glob.glob(os.path.join(ref, 'paginas', '*', '*.json')) + glob.glob(os.path.join(ref, 'secoes', '**', '*.json'), recursive=True):
    try:
        d = json.load(open(f)); coleta(d.get('content') or d.get('elements') or [])
    except Exception: pass
d = json.load(open(alvo))
erros, avisos, total = [], [], [0]
raiz = d.get('content') if 'content' in d else d.get('elements')
if raiz is None: erros.append('sem "content" (export) nem "elements" (clipboard)')
if 'content' in d:
    for k in ('version', 'title', 'type'):
        if k not in d: erros.append(f'falta chave de topo "{k}"')
ids = set()
def checa(n, path):
    for x in n:
        total[0] += 1
        for k in ('id', 'elType', 'settings', 'elements'):
            if k not in x: erros.append(f'{path}: falta "{k}"')
        if x.get('id') in ids: erros.append(f'{path}: id repetido {x.get("id")}')
        ids.add(x.get('id'))
        t = x.get('widgetType') or x.get('elType')
        if x.get('elType') == 'widget' and t not in wtypes: avisos.append(f'widgetType "{t}" não aparece nos JSONs da casa')
        for k in (x.get('settings') or {}):
            if k not in keys.get(t, set()): avisos.append(f'{t}: chave "{k}" não aparece nos JSONs da casa')
        checa(x.get('elements', []), path + '/' + str(t))
checa(raiz or [], 'raiz')
print(f'Elementos: {total[0]} | erros: {len(erros)} | avisos: {len(set(avisos))}')
for e in erros: print('ERRO', e)
for a in sorted(set(avisos)): print('AVISO', a)
sys.exit(1 if erros else 0)
