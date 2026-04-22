# Task: Update Banner Logos + Add WebP Download Pipeline

## Context
`banners.html` has 11 banners, each with a desktop (1920×600) and mobile (375×600) preview. The banners currently use OLD inline SVGs for the "PRIVÉ" wordmark — stroked paths that look like outlined letterforms. These need to be replaced with the UPDATED SVG letterforms from `assets/logo-letters-v4.svg`.

## Part 1: Replace SVG Logo Text

The current inline SVGs look like this (OLD — stroked paths):
```html
<svg viewBox="-1 -2 102 48" width="320" height="150" xmlns="http://www.w3.org/2000/svg" class="hero-logo" aria-label="Privé">
  <g fill="none" stroke="#FFFFFF" stroke-width="1" stroke-linecap="square" stroke-linejoin="miter">
    <path d="M2 44 V8 H10 A7 7 0 0 1 10 22 H2"/>
    <path d="M21 44 V8 H29 A7 7 0 0 1 29 22 H21 M29 22 L37 44"/>
    <path d="M42 8 V44"/>
    <path d="M48 8 L63 44 L78 8"/>
    <path d="M84 44 V8 H97 M84 26 H94 M84 44 H97"/>
  </g>
  <line x1="90" y1="5" x2="96" y2="-1" stroke="#E87722" stroke-width="1" stroke-linecap="square"/>
</svg>
```

These appear in:
- Banner 1 (hero) — desktop and mobile versions — the main logo display
- Banner 7 (exclusivos) — may also have inline logo
- The page header `.logo-mark` at line ~1014

Replace ALL inline SVG wordmarks with an `<img>` tag pointing to `assets/logo-letters-v4.svg`, OR extract the path data from that file and inline it properly. The key requirement: the updated filled letterforms must render, not the old stroked outlines.

For the hero banner specifically, the SVG needs:
- White fill (#FFFFFF) for the letters on the navy background
- The É accent mark rendered in pumpkin (#E87722) — this is Style B
- Proper sizing to match the existing layout (the `hero-logo` class handles sizing)

For any banner that shows the logo on a white/cream background, use navy (#192E49) fill instead.

Check ALL 11 banners for inline SVG wordmarks and replace each one.

## Part 2: WebP Download Pipeline

The banners page already has `html2canvas` loaded and a `downloadPng()` function. Enhance the download system:

### Requirements:
1. Each banner must have TWO download buttons:
   - **"Desktop WebP"** — captures at 1920×600px
   - **"Mobile WebP"** — captures at 375×800px (mobile banners are taller)

2. The download function should:
   - Use `html2canvas` to render the banner div
   - Convert to WebP format using canvas.toBlob('image/webp', 0.92)
   - Auto-download with descriptive filename like `prive-hero-desktop.webp` or `prive-nuevos-mobile.webp`
   - Fall back to PNG if WebP isn't supported

3. Add a **"Download All"** button at the top of the page that downloads ALL banners (both desktop and mobile versions) as individual files.

4. File naming convention:
   - `prive-hero-desktop.webp` / `prive-hero-mobile.webp`
   - `prive-nuevos-desktop.webp` / `prive-nuevos-mobile.webp`
   - `prive-coleccion-regalos-desktop.webp` / `prive-coleccion-regalos-mobile.webp`
   - `prive-ofertas-desktop.webp` / `prive-ofertas-mobile.webp`
   - `prive-genero-desktop.webp` / `prive-genero-mobile.webp`
   - `prive-mas-vendido-desktop.webp` / `prive-mas-vendido-mobile.webp`
   - `prive-exclusivos-desktop.webp` / `prive-exclusivos-mobile.webp`
   - `prive-dia-madre-desktop.webp` / `prive-dia-madre-mobile.webp`
   - `prive-san-valentin-desktop.webp` / `prive-san-valentin-mobile.webp`
   - `prive-navidad-desktop.webp` / `prive-navidad-mobile.webp`

### Shopify Upload Requirements:
- Desktop banners: exactly 1920×600px
- Mobile banners: exactly 375×800px
- WebP format, quality 90%+
- File size ideally under 200KB each
- No transparency (opaque backgrounds only)

### Implementation:
Update the existing JavaScript download functions. The page already has html2canvas loaded. The `downloadPng` function exists — rename/refactor it to handle both desktop and mobile captures with WebP output.

### UI for Download Buttons:
Replace the current single "Download PNG" button per banner with:
```html
<div class="banner-actions">
  <button class="btn-copy" onclick="copyCss(N)">Copiar CSS</button>
  <button class="btn-download" onclick="downloadBanner(N, 'desktop')">Desktop WebP</button>
  <button class="btn-download" onclick="downloadBanner(N, 'mobile')">Mobile WebP</button>
</div>
```

Add a floating "Download All Banners" button at the top.

## Design Rules
- Follow DESIGN.md exactly for all colors and typography
- Navy: #192E49, Pumpkin: #E87722, Cream: #F5F1EC, Gold: #B8956A
- Zero border-radius on all elements
- Jost for headings (uppercase, wide tracking), Barlow for body

## Files to Modify
- `banners.html` — ONLY file to modify

## DO NOT
- Do not modify DESIGN.md
- Do not modify any files in assets/
- Do not create new files
- Do not add npm/build tooling
