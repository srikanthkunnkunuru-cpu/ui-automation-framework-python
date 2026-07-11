from playwright.sync_api import sync_playwright

from utils.constants import HEADLESS

def run_test():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=HEADLESS)
        page = browser.new_page()

        page.goto("https://www.google.com")

        print(f"Page title: {page.title()}")

        browser.close()

run_test()