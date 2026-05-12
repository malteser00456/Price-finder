from playwright.sync_api import sync_playwright

url = "https://url.com"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)

    page = browser.new_page()

    page.goto(url, wait_until="networkidle")

    # Get the price
    page.wait_for_selector('div[data-test="price-container"] span')

    price = page.locator(
        'div[data-test="price-container"] span'
    ).first.inner_text()

    print("Pris:", price)

   # FInding deals
    offer_locator = page.locator("h3")

    found_offer = False

    for i in range(offer_locator.count()):
        text = offer_locator.nth(i).inner_text()

        if "2 för 23 kr" in text:
            print("Erbjudande hittat:", text)
            found_offer = True
            break

    if not found_offer:
        print("Inget erbjudande hittades")

    browser.close()
