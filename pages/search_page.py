import re
from urllib.parse import urljoin
from pages.base_page import BasePage

class SearchPage(BasePage):
    SEARCH_INPUT = "input[name='keyword']"
    SEARCH_BTN = "input[name='searchProducts']"
    TABLE_ROWS = "#Catalog table tr:not(:first-child)" 
    BASE_URL = "https://petstore.octoperf.com/actions/"

    def search_product(self, query: str):
        self.page.fill(self.SEARCH_INPUT, query)
        self.page.click(self.SEARCH_BTN)

    def get_product_urls_under_price(self, max_price: float, limit: int = 5) -> list[str]:
        # Handle category view vs product view
        try:
            if "$" not in self.page.locator("table").inner_text():
                first_link = self.page.locator("#Catalog table tr:nth-child(2) a").first
                if first_link.is_visible():
                    first_link.click()
                    self.page.wait_for_selector(self.TABLE_ROWS, state="attached")
        except Exception:
            pass

        collected_urls = []
        rows = self.page.locator(self.TABLE_ROWS).all()
        
        for row in rows:
            if len(collected_urls) >= limit:
                break
            
            try:
                price_text = row.locator("td:nth-child(4)").inner_text()
                clean_price = re.sub(r'[^\d.]', '', price_text)
                
                if not clean_price: continue
                price = float(clean_price)
                
                if price <= max_price:
                    raw_url = row.locator("td:first-child a").get_attribute("href")
                    if raw_url:
                        full_url = urljoin(self.BASE_URL, raw_url)
                        collected_urls.append(full_url)
            except Exception:
                continue
                    
        return collected_urls