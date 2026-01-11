import allure
from pages.base_page import BasePage

class ProductPage(BasePage):
    ADD_TO_CART_BTN = "a.Button"

    def add_to_cart(self):
        self.click(self.ADD_TO_CART_BTN)
        
        allure.attach(
            self.page.screenshot(), 
            name="Item Added to Cart", 
            attachment_type=allure.attachment_type.PNG
        )