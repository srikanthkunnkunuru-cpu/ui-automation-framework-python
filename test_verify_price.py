from playwright.sync_api import sync_playwright, expect
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from utils.constants import BASE_URL, VALID_USERNAME, VALID_PASSWORD
from utils.constants import HEADLESS


def test_verify_price():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=HEADLESS)
        page = browser.new_page()

        loginPage=LoginPage(page)
        loginPage.go_to(BASE_URL)
        loginPage.login(VALID_USERNAME,VALID_PASSWORD)

        inventoryPage = InventoryPage(page)
        price = inventoryPage.get_price_for_product("Sauce Labs Backpack")
        
        print(f"Price found: {price}")

        assert price == "$29.99", f"Expected $29.99 but got {price}"

        print("Test passed: price verified correctly")

        browser.close()