from playwright.sync_api import sync_playwright, expect
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from utils.constants import BASE_URL, VALID_USERNAME, VALID_PASSWORD


def test_verify_addedItem():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        login_page = LoginPage(page)
        login_page.go_to(BASE_URL)
        login_page.login(VALID_USERNAME, VALID_PASSWORD)

        inventory_page = InventoryPage(page)
        inventory_page.add_backpack_to_cart()
        expect (inventory_page.cart_badge).to_have_text("1")

        inventory_page.go_to_cart()
        expect(page.get_by_text("Sauce Labs Backpack")).to_be_visible()

        browser.close()
