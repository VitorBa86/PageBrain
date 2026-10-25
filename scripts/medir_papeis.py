"""PageBrain · Mede os papéis tipográficos (título do hero, título de seção, corpo, botão) de cada página da casa em 1440px e 390px.

Uso: python3 medir_papeis.py ../paginas/nossas ../design/dados/medidas-papeis.json
Resultado consolidado em design/MEDIDAS-REAIS.md.
"""
import sys, asyncio, json, os, glob
from playwright.async_api import async_playwright
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _navegador import chrome  # noqa: E402
JS = r"""(vw) => {
 const items=[];
 const vis=e=>{const r=e.getBoundingClientRect();return r.width>0&&r.height>0};
 document.querySelectorAll('body *').forEach(e=>{
   if(!vis(e)||['SCRIPT','STYLE','SVG','PATH'].includes(e.tagName))return;
   const own=[...e.childNodes].filter(n=>n.nodeType==3).map(n=>n.textContent.trim()).join(' ').trim();
   if(own.length<3)return;
   const cs=getComputedStyle(e); if(cs.opacity==='0'&&false)return;
   const r=e.getBoundingClientRect();
   items.push({t:own.slice(0,60),n:own.length,fs:parseFloat(cs.fontSize),fw:+cs.fontWeight,lh:cs.lineHeight,ff:cs.fontFamily.split(',')[0].replace(/["']/g,''),tt:cs.textTransform,ls:cs.letterSpacing,top:r.top+scrollY,tag:e.tagName});
 });
 const btn=[];
 document.querySelectorAll('a,button').forEach(a=>{const cs=getComputedStyle(a);if(!vis(a))return;
  const txt=a.innerText.trim(); if(txt.length<6||txt.length>60)return;
  if(cs.backgroundImage!='none'||(cs.backgroundColor!='rgba(0, 0, 0, 0)'&&cs.backgroundColor!='transparent')){
   const r=a.getBoundingClientRect(); btn.push({t:txt,fs:cs.fontSize,fw:cs.fontWeight,pad:cs.padding,rad:cs.borderRadius,tt:cs.textTransform,h:Math.round(r.height),w:Math.round(r.width),ff:cs.fontFamily.split(',')[0]})}});
 return {items,btn:btn.slice(0,3),H:document.body.scrollHeight};}"""
async def run(pg,url,w):
    await pg.set_viewport_size({'width':w,'height':900})
    await pg.goto(url, wait_until='domcontentloaded', timeout=30000); await pg.wait_for_timeout(1200)
    return await pg.evaluate(JS, w)
def summarize(d, hero_h):
    it=d['items']
    hero=[i for i in it if i['top']<hero_h]
    rest=[i for i in it if i['top']>=hero_h]
    ht=max(hero,key=lambda i:i['fs']) if hero else None
    # section titles: elements with fs>=22 below hero, count by size
    from collections import Counter
    c=Counter(round(i['fs']) for i in rest if i['fs']>=22 and i['n']<140)
    body=Counter(); 
    for i in it:
        if i['fs']<22: body[round(i['fs'])]+=i['n']
    fam=Counter()
    for i in it: fam[i['ff']]+=i['n']
    ttl=[i for i in rest if i['fs']>=22 and i['n']<140]
    tw=Counter(i['fw'] for i in ttl)
    return {'hero_title':[round(ht['fs']),ht['fw'],ht['ff'],ht['t'][:40]] if ht else None,
            'titulos':c.most_common(4),'peso_titulos':tw.most_common(2),'corpo':body.most_common(3),'fontes':[f for f,_ in fam.most_common(3)],'botao':d['btn'][:1],'altura':d['H']}
async def main(root,out):
    res={}
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path=chrome())
        pg=await b.new_page()
        await pg.route('**/*', lambda r: r.abort() if r.request.url.startswith('http') and r.request.resource_type in ('script','media') else r.continue_())
        for f in sorted(glob.glob(root+'/*/extraido/index.html')):
            slug=f.split('/')[-3]
            try:
                d=await run(pg,'file://'+os.path.abspath(f),1440); m=await run(pg,'file://'+os.path.abspath(f),390)
                res[slug]={'desktop':summarize(d,900),'mobile':summarize(m,800)}
                print(slug, res[slug]['desktop']['hero_title'][:2], res[slug]['desktop']['titulos'][:2], res[slug]['desktop']['corpo'][:1], '| mob', res[slug]['mobile']['hero_title'][:1], res[slug]['mobile']['titulos'][:1], res[slug]['mobile']['corpo'][:1], flush=True)
            except Exception as e: print(slug,'ERRO',e, flush=True)
        await b.close()
    json.dump(res,open(out,'w'),ensure_ascii=False,indent=1)
asyncio.run(main(sys.argv[1],sys.argv[2]))
