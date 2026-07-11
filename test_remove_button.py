from playwright.sync_api import sync_playwright, expect
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from utils.constants import BASE_URL, VALID_USERNAME, VALID_PASSWORD
from utils.constants import HEADLESS


def test_remove_button():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=HEADLESS)
        page = browser.new_page()

        loginPage = LoginPage(page)
        loginPage.go_to(BASE_URL)
        loginPage.login(VALID_USERNAME, VALID_PASSWORD)

        inventory_page = InventoryPage(page)
        inventory_page.add_backpack_to_cart()

        assert inventory_page.is_remove_button_visible(), "Remove button did not appear after adding to cart"

        print("Test passed: Remove button appeared correctly")

        browser.close()
        
