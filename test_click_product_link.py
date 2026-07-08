from playwright.sync_api import sync_playwright, expect
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from utils.constants import BASE_URL, VALID_USERNAME, VALID_PASSWORD

def test_click_product_link():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        login_page = LoginPage(page)
        login_page.go_to(BASE_URL)
        login_page.login(VALID_USERNAME, VALID_PASSWORD)

        inventory_page = InventoryPage(page)
        inventory_page.click_product_link("Sauce Labs Fleece Jacket")
       
        assert "inventory-item.html" in page.url, "Did not navigate to product detail page"

        print("Test passed: product link navigation works")

        browser.close()
        
