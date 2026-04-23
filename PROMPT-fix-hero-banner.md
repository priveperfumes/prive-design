# Task: Fix Hero Banner — Logo Size + Orange Accent

You are fixing `banners.html`. The hero banner (Banner 1) has two problems:

## Problem 1: Logo is Too Small
The PRIVÉ wordmark is tiny inside the 2000×980px banner. The `width="320" height="84"` on the logo `<img>` is way too small for a 2000px wide banner.

**Fix:** Scale the wordmark up significantly. For a 2000×980 banner, the wordmark should be at least 600-800px wide to have real presence. Try `width="700" height="184"` (maintaining the 3.8:1 aspect ratio of the viewBox `340 790 1320 345`).

Also check the mobile version — `width="140" height="37"` may need scaling up too for a 750×735 canvas. Try `width="400" height="105"`.

## Problem 2: Orange Accent Mark is Broken
There's a `<div>` simulating the É accent mark as a small orange line. It's currently a CSS-positioned `<div>` with:
```
style="position: absolute; top: 8px; right: 28px; width: 12px; height: 2px; background: #E87722; transform: rotate(-45deg);"
```

This looks broken — it appears as a random floating orange line above the logo, not as a proper accent mark on the É.

**Fix:** Remove these fake accent divs entirely. The `logo-wordmark-v4.svg` already has a pumpkin (#E87722) accent path built into it for the É diacritical mark. The SVG's own accent should render correctly — no need for a fake overlay.

Check the SVG content: it has a path at the end with `fill="#E87722"` for the accent. The `filter: brightness(0) saturate(100%) invert(100%)` CSS filter is inverting ALL colors, which turns the pumpkin accent into a wrong color!

**Root cause of both problems:**
1. The `filter: invert(100%)` turns the white letters white (good) but turns the pumpkin #E87722 accent into a wrong color (bad)
2. The logo is scaled too small

**Solution:**
- Remove the `filter: brightness(0) saturate(100%) invert(100%)` from the `<img>` tags
- Instead, the SVG already uses `fill="#FFFFFF"` for letters — but since the SVG is designed for a dark background with white fill baked in, it should work as-is on the navy banner background
- Remove the fake orange accent `<div>` overlays
- Scale the logo up: desktop hero `width="700" height="184"`, mobile `width="400" height="105"`
- The SVG's built-in #E87722 accent path will render correctly without the invert filter

If the SVG letterforms appear as the wrong color without the filter (because the original SVG uses white fill for dark backgrounds), then the correct approach is:
- Keep the img WITHOUT the invert filter
- The SVG paths have `fill="#FFFFFF"` which is correct for navy backgrounds
- The accent path has `fill="#E87722"` which will render as pumpkin — correct!

## Also Fix the Page Header Logo
Line ~1015 has the same SVG with `filter: invert(100%)` at `width="120" height="31"`. Remove the filter there too, and slightly increase the size to `width="140" height="37"`.

## Files to Modify
- `banners.html` ONLY

## DO NOT
- Do not modify any SVG files
- Do not modify DESIGN.md
- Do not create new files
- Use Read to inspect, Edit to make changes
