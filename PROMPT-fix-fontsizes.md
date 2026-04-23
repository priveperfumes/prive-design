# Task: Audit and Fix ALL Banner Font Sizes for Desktop + Mobile

You are fixing `banners.html`. The banners are rendered at:
- **Desktop:** 2000×980px (Shopify recommended)
- **Mobile:** 750×735px

The problem: font sizes across ALL banners were designed for the OLD 1920×600 dimensions. Now that banners are 2000×980 (much taller), the text looks too small — especially on the Ofertas banner and mobile views.

## What to Do

### Step 1: Read the file and audit ALL banner text sizes
Use the Read tool to inspect `banners.html`. For EVERY banner (1-11), find:
- `.heading` font sizes
- `.subtext` font sizes  
- `.cta-bar` / button text sizes
- Any other text elements

### Step 2: Fix font sizes for the new 2000×980 canvas

Here are the 11 banners and what to check:

**Banner 1: Hero** — The PRIVÉ logo is already fixed (700×184 desktop, 260×68 mobile). Check that the tagline "Fragancias que definen quien eres" and "Luxury Perfumes · Honduras" are properly sized.

**Banner 2: Nuevos Ingresos** — "Nuevos Ingresos" heading + subtext. Make sure heading is large enough for a 2000px wide banner.

**Banner 3: Colección de Regalos (Estuches)** — Gift icon text, heading, subtext, CTA.

**Banner 4: Ofertas Especiales** — THIS IS THE WORST ONE. The "OFERTAS ESPECIALES" heading and discount text are too small. Needs significant scaling up.

**Banner 5: Género (Hombre/Mujer)** — Two-column with gender categories.

**Banner 6: Más Vendido** — Best sellers heading.

**Banner 7: Exclusivos** — Exclusive fragrances.

**Banner 9: Día de la Madre** — Mother's day banner with rose motif.

**Banner 10: San Valentín** — Valentine's banner with rings motif.

**Banner 11: Navidad** — Christmas banner.

### Step 3: Size Guidelines

For **desktop (2000×980)**:
- Main banner headings: 48-72px
- Subtext/descriptions: 20-28px
- CTA button text: 16-18px (button height 56-64px)
- Taglines: 22-28px

For **mobile (750×735)** — these are the `.mobile-frame .banner` versions:
- Scale desktop sizes down by roughly 0.4x
- Main headings: 20-30px
- Subtext: 12-16px
- CTA: 12-14px

### Step 4: Check for mobile-specific overrides
Some banners may have inline `style="font-size: Xpx"` on mobile versions. Find and fix these too.

### Important Notes
- The mobile banner is 750px wide now (not 375px), so mobile fonts should be proportionally larger than they were
- Don't just scale Ofertas — check ALL banners systematically
- The CSS for each banner variant is in the `<style>` block — look for `.banner--hero`, `.banner--nuevos`, `.banner--ofertas`, etc.
- Some banners may have text sizing in the inline print CSS block near the bottom of the file

## Files to Modify
- `banners.html` ONLY

## DO NOT
- Do not modify DESIGN.md
- Do not modify any SVG files in assets/
- Do not create new files
- Use Read to inspect, Edit to make changes
