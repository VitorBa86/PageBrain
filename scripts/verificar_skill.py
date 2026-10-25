"""PageBrain · Verificação da skill inteira.

Confere o que precisa estar certo antes de publicar ou compartilhar a skill:

  1. Links relativos dos .md e dos .html (fora de extraido/) apontam para arquivos que existem.
  2. Todo .json (fora de extraido/) é válido.
  3. Nenhum travessão nos textos escritos. Ficam de fora as transcrições de copy real, os guias originais,
     os dados medidos de páginas publicadas (style-guide.html, raio-x.json) e as linhas que ensinam a regra.
  4. Cada página da casa tem como-usar.md, ficha.json, raio-x/raio-x.md e extraido/index.html.
  5. Nenhum arquivo acima de 50 MB (o GitHub avisa) ou de 100 MB (o GitHub recusa).
  6. Nomes de arquivo sem espaço e sem acento.
  7. (com --navegador) style guides, design system e preview de códigos abrem sem erro de JS
     e sem arquivo local faltando.

Uso:
  python3 scripts/verificar_skill.py [--navegador] [--json saida.json]

Sai com código 1 se houver ERRO.
"""
import glob
import json
import os
import re
import sys
import urllib.parse

RAIZ = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
IGNORAR_DIRS = {'extraido', '.git', '__pycache__', 'node_modules'}
SEM_TRAVESSAO_EXCETO = ('copy/copys-reais/', 'copy/fontes/')


def arquivos(ext):
    for base, ds, fs in os.walk(RAIZ):
        ds[:] = [d for d in ds if d not in IGNORAR_DIRS]
        for f in fs:
            if f.endswith(ext):
                yield os.path.join(base, f)


def rel(p):
    return os.path.relpath(p, RAIZ)


erros, avisos, resumo = [], [], {}

# 1. links
MD_LINK = re.compile(r'\[[^\]]*\]\((<[^>]+>|[^)\s]+)\)')
HTML_LINK = re.compile(r'(?:href|src)="([^"]+)"')
total_links = 0
for p in list(arquivos('.md')) + list(arquivos('.html')):
    txt = open(p, encoding='utf-8', errors='replace').read()
    if p.endswith('.md'):
        txt = re.sub(r'```.*?```', '', txt, flags=re.S)  # exemplos de código não são links
        links = [m.strip('<>') for m in MD_LINK.findall(txt)]
    else:
        links = HTML_LINK.findall(txt)
    for link in links:
        if link.startswith(('http:', 'https:', 'mailto:', 'tel:', 'data:', '#', '//', 'javascript:')) or '{' in link:
            continue
        alvo = urllib.parse.unquote(link.split('#')[0].split('?')[0])
        if not alvo:
            continue
        if p.endswith('.html') and os.path.basename(p) not in ('style-guide.html', 'design-system-davi.html', 'preview.html'):
            continue  # snippets e exemplos citam imagens/IMG-NN.webp da página que vai ser criada
        total_links += 1
        if not os.path.exists(os.path.normpath(os.path.join(os.path.dirname(p), alvo))):
            erros.append(f'link quebrado em {rel(p)}: {link}')
resumo['links_verificados'] = total_links

# 2. JSON
total_json = 0
for p in arquivos('.json'):
    total_json += 1
    try:
        json.load(open(p, encoding='utf-8'))
    except Exception as e:
        erros.append(f'JSON inválido: {rel(p)} ({e})')
resumo['jsons_validos'] = total_json - sum(1 for e in erros if e.startswith('JSON'))

# 3. travessão
travessoes = 0
for p in list(arquivos('.md')) + list(arquivos('.html')) + list(arquivos('.json')):
    r = rel(p).replace(os.sep, '/')
    if r.startswith(SEM_TRAVESSAO_EXCETO) or r.startswith(('elementor/paginas/', 'elementor/secoes/', 'design/dados/')) and r.endswith('.json'):
        continue
    if r.endswith(('style-guide.html', 'raio-x.json')):
        continue  # dados medidos de páginas publicadas (citação); o raio-x.md marca como [travessão]
    for n, linha in enumerate(open(p, encoding='utf-8', errors='replace'), 1):
        if r == 'copy/tom-de-voz.md' and linha.startswith('| '):
            continue  # tabela "Em vez de / Escreva" que ensina a regra
        if ('—' in linha or '–' in linha) and not re.search(r'travess|— ou –|Em vez de|\(— e –\)|—\|–|"—" e "–"', linha, re.I):
            travessoes += 1
            avisos.append(f'travessão em {r}:{n}: {linha.strip()[:90]}')
resumo['travessoes_fora_das_excecoes'] = travessoes

# 4. páginas da casa completas
nossas = sorted(d for d in glob.glob(os.path.join(RAIZ, 'paginas', 'nossas', '*')) if os.path.isdir(d))
for d in nossas:
    for f in ('como-usar.md', 'ficha.json', os.path.join('raio-x', 'raio-x.md'), os.path.join('extraido', 'index.html')):
        if not os.path.exists(os.path.join(d, f)):
            erros.append(f'página da casa sem {f}: {rel(d)}')
resumo['paginas_da_casa'] = len(nossas)

# 5 e 6. tamanho e nomes
total_bytes, maior = 0, (0, '')
for base, ds, fs in os.walk(RAIZ):
    ds[:] = [d for d in ds if d not in ('.git', '__pycache__')]
    for nome in ds + fs:
        if ' ' in nome or not nome.isascii():
            erros.append(f'nome com espaço ou acento: {rel(os.path.join(base, nome))}')
    for f in fs:
        p = os.path.join(base, f)
        s = os.path.getsize(p)
        total_bytes += s
        maior = max(maior, (s, rel(p)))
        if s > 100 * 1024 * 1024:
            erros.append(f'arquivo acima de 100 MB (o GitHub recusa): {rel(p)}')
        elif s > 50 * 1024 * 1024:
            avisos.append(f'arquivo acima de 50 MB: {rel(p)}')
resumo['tamanho_total_mb'] = round(total_bytes / 1024 / 1024, 1)
resumo['maior_arquivo'] = f'{maior[1]} ({round(maior[0] / 1024 / 1024, 1)} MB)'

# 7. navegador (opcional)
if '--navegador' in sys.argv:
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from _navegador import chrome
    from playwright.sync_api import sync_playwright
    alvos = sorted(glob.glob(os.path.join(RAIZ, 'paginas', '*', '*', 'style-guide.html')))
    alvos += [os.path.join(RAIZ, 'design', 'design-system-davi.html'), os.path.join(RAIZ, 'codigos', 'preview.html')]
    with sync_playwright() as pw:
        b = pw.chromium.launch(executable_path=chrome(), headless=True)
        for a in alvos:
            js, falhas = [], []
            pg = b.new_page()
            pg.route('http*://**', lambda r: r.abort())
            pg.on('pageerror', lambda e: js.append(str(e)))
            pg.on('requestfailed', lambda r: falhas.append(r.url) if r.url.startswith('file:') else None)
            pg.goto('file://' + a, wait_until='load', timeout=60000)
            pg.close()
            if js:
                avisos.append(f'erro de JS em {rel(a)}: {js[0][:100]}')
            for f in falhas:
                erros.append(f'arquivo local faltando em {rel(a)}: {urllib.parse.unquote(f)[-90:]}')
        b.close()
    resumo['paginas_abertas_no_navegador'] = len(alvos)

print('PageBrain · verificação da skill')
for k, v in resumo.items():
    print(f'  {k}: {v}')
for a in avisos[:40]:
    print('AVISO', a)
if len(avisos) > 40:
    print(f'AVISO ... e mais {len(avisos) - 40}')
for e in erros[:60]:
    print('ERRO ', e)
if len(erros) > 60:
    print(f'ERRO  ... e mais {len(erros) - 60}')
print('Resultado:', 'OK' if not erros else f'{len(erros)} erro(s)')
if '--json' in sys.argv:
    json.dump({'resumo': resumo, 'erros': erros, 'avisos': avisos},
              open(sys.argv[sys.argv.index('--json') + 1], 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
sys.exit(1 if erros else 0)
