"""PageBrain · Acha o navegador usado pelos scripts (Playwright).

Ordem: variável PAGEBRAIN_CHROME, Google Chrome instalado (macOS, Linux, Windows) e, se nada
for achado, o Chromium do próprio Playwright (instale com `python3 -m playwright install chromium`).
"""
import os

CANDIDATOS = [
    os.environ.get('PAGEBRAIN_CHROME'),
    '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
    '/usr/bin/google-chrome',
    '/usr/bin/google-chrome-stable',
    '/usr/bin/chromium',
    '/usr/bin/chromium-browser',
    r'C:\Program Files\Google\Chrome\Application\chrome.exe',
    r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe',
]


def chrome():
    """Caminho do Chrome, ou None para usar o Chromium do Playwright."""
    for c in CANDIDATOS:
        if c and os.path.exists(c):
            return c
    return None
