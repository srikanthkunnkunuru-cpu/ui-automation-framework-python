'''from playwright.sync_api import sync_playwright
import time

def test_add_to_cart():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Step 1: Login
        page.goto("https://www.saucedemo.com")
        page.locator("#user-name").fill("standard_user")
        page.locator("#password").fill("secret_sauce")
        page.locator("#login-button").click()
        time.sleep(2)

        # Step 2: Add product to cart
        page.locator("#add-to-cart-sauce-labs-backpack").click()
        time.sleep(1)

        # Step 3: Read the cart badge text
        cart_count = page.locator(".shopping_cart_badge").inner_text()

        # Step 4: Assert it shows "1"
        assert cart_count == "1", f"Expected cart count to be '1' but got '{cart_count}'"

        # Step 5: Only runs if assertion passed
        print("Test passed: item added to cart")

        browser.close()

test_add_to_cart()'''



'''from playwright.sync_api import sync_playwright

def test_practice():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.saucedemo.com")
        page.locator("#user-name").fill("standard_user")
        page.locator("#password").fill("secret_sauce")
        page.locator("#login-button").click()

        if "inventory" in page.url:
            print("login succesfull")
        else:
            print("login unsuccesfull")

        browser.close()

test_practice()'''
            


from playwright.sync_api import sync_playwright

def test_login():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.saucedemo.com")
        page.locator("#user-name").fill("standard_user")
        page.locator("#password").fill("secret_sauce")
        page.locator("#login-button").click()

        assert "inventory" in page.url, "Login did not redirect to inventory page"

        browser.close()