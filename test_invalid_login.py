from playwright.sync_api import sync_playwright, expect
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from utils.constants import BASE_URL, INVALID_PASSWORD, INVALID_USERNAME, VALID_USERNAME, VALID_PASSWORD

def test_invalid_login():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        login_page = LoginPage(page)
        login_page.go_to(BASE_URL)
        login_page.login(INVALID_USERNAME,INVALID_PASSWORD)

        expect(login_page.error_message).to_be_visible()

        browser.close()
        