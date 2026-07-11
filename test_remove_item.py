from playwright.sync_api import sync_playwright, expect
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from utils.constants import BASE_URL, VALID_USERNAME, VALID_PASSWORD
from utils.constants import HEADLESS

def test_remove_item():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=HEADLESS)
        page = browser.new_page()

        login_page = LoginPage(page)
        login_page.go_to(BASE_URL)
        login_page.login(VALID_USERNAME, VALID_PASSWORD)

        inventory_page = InventoryPage(page)
        inventory_page.add_backpack_to_cart()
        expect(inventory_page.cart_badge).to_have_text("1")
        inventory_page.remove_backpack_from_cart()
        expect(inventory_page.cart_badge).to_be_hidden()

        print("Test passed: item added and removed correctly")

        browser.close()

