from playwright.sync_api import sync_playwright, expect
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from utils.constants import BASE_URL, VALID_USERNAME, VALID_PASSWORD

def test_add_to_cart_using_framework():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        login_page = LoginPage(page)
        login_page.go_to(BASE_URL)
        login_page.login(VALID_USERNAME, VALID_PASSWORD)

        assert "inventory" in page.url, "Login did not redirect to inventory page"

        inventory_page = InventoryPage(page)
        inventory_page.add_backpack_to_cart()

        expect(inventory_page.cart_badge).to_have_text("1")

        print("Test passed: framework-based add to cart works")

        browser.close()