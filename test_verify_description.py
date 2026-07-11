from playwright.sync_api import sync_playwright, expect
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from utils.constants import BASE_URL, VALID_USERNAME, VALID_PASSWORD
from utils.constants import HEADLESS


def test_verify_description():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=HEADLESS)
        page = browser.new_page()

        loginPage = LoginPage(page)
        loginPage.go_to(BASE_URL)
        loginPage.login(VALID_USERNAME, VALID_PASSWORD)

        inventory_page = InventoryPage(page)
        description = inventory_page.get_description_for_product("Sauce Labs Backpack")

        print("Description found: {description}")

        expected_description = "carry.allTheThings() with the sleek, streamlined Sly Pack that melds uncompromising style with unequaled laptop and tablet protection."

        assert description == expected_description, f"Expected '{expected_description}' but got '{description}'"

        print("Test passed: description verified correctly")

        browser.close()
