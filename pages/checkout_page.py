from playwright.sync_api import Page

class CheckoutPage:
    def __init__(self, page: Page):
        self.page = page
        self.first_name  = page.locator("[data-test='firstName']")
        self.last_name   = page.locator("[data-test='lastName']")
        self.postal_code = page.locator("[data-test='postalCode']")
        self.continue_btn= page.locator("[data-test='continue']")
        self.finish_btn  = page.locator("[data-test='finish']")
        self.error_msg   = page.locator("[data-test='error']")
        self.complete_header = page.locator(".complete-header")

    def fill_info(self, first: str, last: str, postal: str):
        self.first_name.fill(first)
        self.last_name.fill(last)
        self.postal_code.fill(postal)

    def continue_checkout(self):
        self.continue_btn.click()

    def finish_order(self):
        self.finish_btn.click()

    def get_error(self) -> str:
        return self.error_msg.inner_text()

    def get_complete_text(self) -> str:
        return self.complete_header.inner_text()