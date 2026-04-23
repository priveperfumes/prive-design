#!/usr/bin/env python3
"""Render banner HTML to JPG images using Playwright with inlined SVGs."""
import asyncio
import os
import zipfile
import base64
from playwright.async_api import async_playwright

BANNERS_HTML = "/home/prive/repos/prive-design/banners.html"
SVG_PATH = "/home/prive/repos/prive-design/assets/logo-wordmark-v4.svg"
OUTPUT_DIR = "/home/prive/repos/prive-design/dist"
ZIP_PATH = "/home/prive/repos/prive-design/prive-banners-shopify.zip"

# Shopify recommended
DESKTOP_W, DESKTOP_H = 2000, 980
MOBILE_W, MOBILE_H = 750, 735

BANNERS = [
    (1, "hero"),
    (2, "nuevos"),
    (3, "coleccion-regalos"),
    (4, "ofertas"),
    (5, "genero"),
    (6, "mas-vendido"),
    (7, "exclusivos"),
    (9, "dia-madre"),
    (10, "san-valentin"),
    (11, "navidad"),
]


async def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # Inline SVG as data URI
    with open(SVG_PATH, "rb") as f:
        svg_b64 = base64.b64encode(f.read()).decode()
    data_uri = f"data:image/svg+xml;base64,{svg_b64}"

    with open(BANNERS_HTML, "r") as f:
        html = f.read().replace("assets/logo-wordmark-v4.svg", data_uri)

    tmp_html = "/tmp/banners-inline.html"
    with open(tmp_html, "w") as f:
        f.write(html)

    async with async_playwright() as p:
        browser = await p.chromium.launch()
        context = await browser.new_context(viewport={"width": 2400, "height": 1200}, device_scale_factor=1)
        page = await context.new_page()
        await page.goto(f"file://{tmp_html}", wait_until="networkidle", timeout=30000)
        await page.wait_for_timeout(3000)

        exported = []

        for bid, name in BANNERS:
            print(f"Banner {bid}: {name}")

            for variant, sel, w, h in [
                ("desktop", f"#banner-{bid} .banner-frame", DESKTOP_W, DESKTOP_H),
                ("mobile", f"#banner-{bid} .mobile-frame", MOBILE_W, MOBILE_H),
            ]:
                try:
                    el = await page.query_selector(sel)
                    if not el:
                        print(f"  ✗ {variant}: {sel} not found")
                        continue
                    await page.evaluate(f"""() => {{
                        const f = document.querySelector('{sel}');
                        if (f) {{ f.style.width='{w}px'; f.style.height='{h}px'; f.style.overflow='hidden'; }}
                    }}""")
                    await page.wait_for_timeout(300)
                    out = os.path.join(OUTPUT_DIR, f"prive-{name}-{variant}.jpg")
                    await el.screenshot(path=out, quality=92)
                    exported.append(out)
                    print(f"  ✓ {variant}: {out} ({os.path.getsize(out)/1024:.0f}KB)")
                except Exception as e:
                    print(f"  ✗ {variant}: {e}")

        await browser.close()

    print(f"\nCreating zip: {ZIP_PATH}")
    with zipfile.ZipFile(ZIP_PATH, "w", zipfile.ZIP_DEFLATED) as zf:
        for f in exported:
            if os.path.exists(f):
                zf.write(f, os.path.basename(f))
                print(f"  {os.path.basename(f)} ({os.path.getsize(f)/1024:.0f}KB)")

    print(f"\n✓ Done! {len(exported)} files → {ZIP_PATH}")


if __name__ == "__main__":
    asyncio.run(main())
