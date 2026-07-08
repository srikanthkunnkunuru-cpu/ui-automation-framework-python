class InventoryPage:
    def __init__(self, page):
        self.page = page
        self.cart_badge = page.locator(".shopping_cart_badge")
        self.cart_icon = page.locator(".shopping_cart_link")

    def add_backpack_to_cart(self):
        self.page.locator("#add-to-cart-sauce-labs-backpack").click()

    def add_bike_light_to_cart(self):
        self.page.locator("#add-to-cart-sauce-labs-bike-light").click()

    def is_remove_button_visible(self):
        return self.page.locator("#remove-sauce-labs-backpack").is_visible()
    
    def remove_backpack_from_cart(self):
        self.page.locator("#remove-sauce-labs-backpack").click()

    def get_cart_count(self):
        return self.cart_badge.inner_text()

    def go_to_cart(self):
        self.cart_icon.click()

    def get_price_for_product(self, product_name):
        product_card = self.page.locator(".inventory_item").filter(has_text=product_name)
        return product_card.locator(".inventory_item_price").inner_text()
    
    def get_description_for_product(self, product_name):
        product_card = self.page.locator(".inventory_item").filter(has_text=product_name)
        return product_card.locator(".inventory_item_desc").inner_text()
    
    def click_product_link(self, product_name):
        self.page.get_by_text(product_name).click()