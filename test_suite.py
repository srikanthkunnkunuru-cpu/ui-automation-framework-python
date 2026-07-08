from playwright.sync_api import sync_playwright, expect

def test_login():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.saucedemo.com")
        page.locator("#user-name").fill("standard_user")
        page.locator("#password").fill("secret_sauce")
        page.locator("#login-button").click()

        assert "inventory" in page.url

        browser.close()

def test_add_to_cart():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.saucedemo.com")
        page.locator("#user-name").fill("standard_user")
        page.locator("#password").fill("secret_sauce")
        page.locator("#login-button").click()

        page.locator("#add-to-cart-sauce-labs-backpack").click()
        expect(page.locator(".shopping_cart_badge")).to_have_text("1")

        browser.close()

def test_invalid_login():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.saucedemo.com")
        page.locator("#user-name").fill("wrong_user")
        page.locator("#password").fill("wrong_password")
        page.locator("#login-button").click()

        error_message = page.locator("[data-test='error']")
        expect(error_message).to_be_visible()

        browser.close()

def test_login():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.saucedemo.com")
        page.locator("#user-name").fill("standard_user")
        page.locator("#password").fill("secret_sauce")
        page.locator("#login-button").click()

        print(f"Logged in successfully, current URL: {page.url}")

        assert "inventory" in page.url

        browser.close()