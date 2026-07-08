from playwright.sync_api import sync_playwright

"""def test_login():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.saucedemo.com")
        page.locator("#user-name").fill("standard_user")
        page.locator("#password").fill("secret_sauce")
        page.locator("#login-button").click()

        assert "inventory" in page.url, "Login did not redirect to inventory page"

        browser.close()"""


from playwright.sync_api import sync_playwright, expect
def test_login2():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.saucedemo.com")
        page.locator("#user-name").fill("standard_user")
        page.locator("#password").fill("secret_sauce")
        page.locator("login_button").click()

        page.locator("#add-to-cart-sauce-labs-backpack").click()

        expect(page.locator(".shopping_cart_badge")).to_have_text("1")
    
    print("Test passed: item added to cart")

    browser.close()

