from playwright.sync_api import sync_playwright
import time

def run_test():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://www.google.com")

        search_box = page.get_by_role("combobox", name="Search")
        search_box.fill("Playwright automation")
        search_box.press("Enter")

        time.sleep(10)

        print(f"Page title after search: {page.title()}")

        browser.close()

run_test()