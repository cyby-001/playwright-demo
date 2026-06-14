from playwright.sync_api import Page

class CartPage:
    def __init__(self, page: Page):
        self.page = page
        # 商品列表页
        self.first_item        = page.locator(".inventory_item").first
        self.add_to_cart_btn   = page.locator(".btn_inventory").first
        self.cart_badge        = page.locator(".shopping_cart_badge")
        self.cart_icon         = page.locator(".shopping_cart_link")
        # 购物车页
        self.cart_items        = page.locator(".cart_item")
        self.remove_btn        = page.locator(".cart_button").first
        self.checkout_btn      = page.locator("[data-test='checkout']")

    def add_first_item_to_cart(self):
        self.add_to_cart_btn.click()

    def get_cart_count(self) -> str:
        return self.cart_badge.inner_text()

    def go_to_cart(self):
        self.cart_icon.click()

    def get_cart_item_count(self) -> int:
        return self.cart_items.count()

    def remove_item(self):
        self.remove_btn.click()

    def go_to_checkout(self):
        self.checkout_btn.click()