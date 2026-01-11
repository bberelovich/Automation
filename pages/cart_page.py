import re
import allure
from pages.base_page import BasePage

class CartPage(BasePage):
    CART_TOTAL_ROW = "td:has-text('Sub Total')"
    
    def get_cart_total(self) -> float:
        text = self.get_text(self.CART_TOTAL_ROW)
        clean_text = re.sub(r'[^\d.]', '', text)
        return float(clean_text)

    def assert_total_not_exceeds(self, budget_per_item: float, items_count: int):
        actual_total = self.get_cart_total()
        limit = budget_per_item * items_count
        
        allure.attach(
            self.page.screenshot(), 
            name="Final Cart Status", 
            attachment_type=allure.attachment_type.PNG
        )

        assert actual_total <= limit, f"Total {actual_total} exceeds limit {limit}"