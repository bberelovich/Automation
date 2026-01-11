from playwright.sync_api import Page

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def navigate(self, url: str):
        self.page.goto(url)

    def get_text(self, selector: str) -> str:
        return self.page.locator(selector).inner_text().strip()
    
    def click(self, selector: str):
        self.page.locator(selector).click()