"""Uso: python3 shot.py <arquivo.html> <saida.png> [--click-all] [--width 1280] [--full]
Abre no Chrome headless, coleta erros de console e requests locais falhos, salva screenshot."""
import os, sys, pathlib
from playwright.sync_api import sync_playwright
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _navegador import chrome  # noqa: E402

src, out = sys.argv[1], sys.argv[2]
click_all = '--click-all' in sys.argv
full = '--full' in sys.argv
width = int(sys.argv[sys.argv.index('--width') + 1]) if '--width' in sys.argv else 1280
errors, failed = [], []
with sync_playwright() as p:
    b = p.chromium.launch(executable_path=chrome(), headless=True)
    pg = b.new_page(viewport={'width': width, 'height': 900})
    pg.on('console', lambda m: errors.append(m.text) if m.type == 'error' else None)
    pg.on('pageerror', lambda e: errors.append('PAGEERROR ' + str(e)))
    pg.on('requestfailed', lambda r: failed.append(r.url) if r.url.startswith('file:') else None)
    pg.goto(pathlib.Path(src).resolve().as_uri(), wait_until='load', timeout=60000)
    if click_all:
        for btn in pg.query_selector_all('[data-prev]'):
            btn.click()
        pg.wait_for_timeout(4000)
    else:
        pg.wait_for_timeout(1500)
    pg.screenshot(path=out, full_page=full)
    b.close()
print('ERRORS', len(errors))
for e in errors[:15]: print('  ', e[:200])
print('FAILED_LOCAL', len(failed))
for f in failed[:15]: print('  ', f)
