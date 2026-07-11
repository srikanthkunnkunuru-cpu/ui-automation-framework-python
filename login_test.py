from playwright.sync_api import sync_playwright
import time

from utils.constants import HEADLESS

def login_test():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=HEADLESS)
        page = browser.new_page()
        page.goto("https://www.saucedemo.com")
        page.locator("#user-name").fill("standard_user")
        page.locator("#password").fill("secret_sauce")
        page.locator("#login-button").click()
        time.sleep(3)
        print("Current URL:", page.url)

        product = page.get_by_text("Sauce Labs Backpack")
        product.click()

        time.sleep(2)

        print("Product page URL:", page.url)

        browser.close()

login_test()