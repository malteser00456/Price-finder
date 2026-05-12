# Price Finder

A small Python script that fetches product prices from web pages using Playwright.  
It’s mainly built for sites that load content with JavaScript (like ICA).

---

## What it does

- Opens a product page in a real browser (Chromium)
- Waits for the page to load
- Extracts the current price
- Checks if there are any offers (like “2 for 23 kr”)

---

## Requirements

Install dependencies:

```bash
pip install playwright
python -m playwright install
