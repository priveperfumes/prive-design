# Task: Update Banner Dimensions to Shopify Recommended + Fix Logo

You are working on `banners.html` — a single-page HTML+CSS+JS file that shows banner previews and has a download/export system.

## Two Changes Required

### 1. Update ALL Banner Dimensions from 1920×600 to Shopify Recommended 2000×980

Shopify recommends **2000×980px** for banner images. Update EVERY reference:

**CSS variables:**
- `--banner-w: 1920px` → `--banner-w: 2000px`
- `--banner-h: 600px` → `--banner-h: 980px`

**CSS aspect-ratio:**
- Desktop frame: `aspect-ratio: 1920 / 600` → `aspect-ratio: 2000 / 980`
- Mobile frame: adjust proportionally — mobile width stays 375px, height should be `375 * (980/2000) ≈ 184px`

**Banner CSS (print media / inline styles for each banner):**
- Every banner has explicit `width: 1920px; height: 600px;` in the `<style>` block near the bottom
- Change ALL of them to `width: 2000px; height: 980px;`

**JavaScript download functions:**
- `const width = isDesktop ? 1920 : 375` → `const width = isDesktop ? 2000 : 750`
- `const height = isDesktop ? 600 : 800` → `const height = isDesktop ? 980 : 735`
- `windowWidth` and `windowHeight` params similarly
- Any other hardcoded 1920/600 values in the JS

**Info text:**
- `1920 × 600px` → `2000 × 980px`
- Any helper text mentioning old dimensions

**IMPORTANT:** Use the Read tool to inspect the file, then use Edit to make changes. Do NOT use any external tools or scripts that might corrupt the file with line numbers.

### 2. Verify Logo SVG References Are Correct

The file should already reference `assets/logo-wordmark-v4.svg` (NOT `logo-letters-v4.svg`). Verify this and make sure dimensions match the SVG's viewBox aspect ratio (~3.8:1). The wordmark SVG has viewBox `"340 790 1320 345"`.

If any logo references are still pointing to `logo-letters-v4.svg`, fix them.

## Quality Check
After all edits, verify:
- No remaining `1920` references (except line numbers or unrelated text)
- All banner previews render correctly in the page
- Download functions output at 2000×980 for desktop
- The SVG logo images have correct aspect ratio (not squished)

## Files to Modify
- `banners.html` — ONLY file

## DO NOT
- Do not modify DESIGN.md
- Do not modify any files in assets/
- Do not create new files
- Do not use execute_code or any tool that might add line numbers to the file
- Use Read to inspect, Edit to make changes, one at a time or in batches
