const { chromium } = require('playwright');
(async () => {
  const out = process.argv[2];
  const file = 'file:///home/user/oncology-educater/site/index.html';
  const browser = await chromium.launch();
  const shots = [
    { name: 'home-desktop', w: 1440, h: 900, hash: '', scheme: 'light' },
    { name: 'lung-desktop', w: 1440, h: 900, hash: '#lung-cancer', scheme: 'light' },
    { name: 'lung-desktop-dark', w: 1440, h: 900, hash: '#lung-cancer', scheme: 'dark' },
    { name: 'home-phone', w: 390, h: 844, hash: '', scheme: 'light' },
    { name: 'lung-phone', w: 390, h: 844, hash: '#lung-cancer', scheme: 'light' },
  ];
  const errors = [];
  for (const s of shots) {
    const ctx = await browser.newContext({ viewport: { width: s.w, height: s.h }, colorScheme: s.scheme, deviceScaleFactor: 1 });
    const page = await ctx.newPage();
    page.on('pageerror', e => errors.push(s.name + ': ' + e.message));
    page.on('console', m => { if (m.type() === 'error') errors.push(s.name + ' console: ' + m.text()); });
    await page.goto(file + s.hash, { waitUntil: 'load' });
    await page.waitForTimeout(1500);
    await page.screenshot({ path: `${out}/${s.name}.png` });
    const overflow = await page.evaluate(() => document.documentElement.scrollWidth - window.innerWidth);
    console.log(s.name, 'horizontal overflow px:', overflow);
    await ctx.close();
  }
  // scroll into the middle of lung chapter on desktop
  const ctx = await browser.newContext({ viewport: { width: 1440, height: 900 } });
  const page = await ctx.newPage();
  await page.goto(file + '#lung-cancer', { waitUntil: 'load' });
  await page.waitForTimeout(800);
  for (const [i, sel] of [['callouts', 'h3[id*="43-nsclc-iv"]'], ['regimen', 'h3[id*="54-口服標靶藥"]'], ['quiz', 'h2[id*="11-自我測驗"]']]) {
    const el = await page.$(sel);
    if (el) { await el.scrollIntoViewIfNeeded(); await page.evaluate(e => e.scrollIntoView({block:'start'}), el); await page.waitForTimeout(300); await page.screenshot({ path: `${out}/lung-${i}.png` }); }
    else console.log('missing', sel);
  }
  // open first quiz details
  const d = await page.$('h2[id*="11-自我測驗"] ~ details summary');
  if (d) { await d.click(); await page.waitForTimeout(300); await page.screenshot({ path: `${out}/lung-quiz-open.png` }); }
  // search
  await page.fill('#search', 'osimertinib');
  await page.waitForTimeout(300);
  await page.screenshot({ path: `${out}/search.png` });
  await browser.close();
  console.log('errors:', JSON.stringify(errors));
})();
