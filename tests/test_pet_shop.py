import json
import pytest
import allure
from pages.search_page import SearchPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage

@pytest.fixture(scope="session")
def config_data():
    with open('config.json', 'r') as f:
        return json.load(f)

@allure.feature("Shopping Cart Flow")
@allure.story("Add items within budget")
def test_pet_store_e2e(page, config_data):
    query = config_data['search_query']
    max_price = config_data['max_price']
    items_limit = config_data['items_to_select']
    budget = config_data['budget_per_item']

    search_page = SearchPage(page)
    product_page = ProductPage(page)
    cart_page = CartPage(page)

    with allure.step(f"Search for '{query}'"):
        search_page.navigate("https://petstore.octoperf.com/actions/Catalog.action")
        search_page.search_product(query)
    
    with allure.step(f"Filter items under {max_price}"):
        product_urls = search_page.get_product_urls_under_price(max_price, items_limit)
        assert len(product_urls) > 0, f"No products found for '{query}' under {max_price}"

    with allure.step("Add items to cart"):
        for url in product_urls:
            page.goto(url)
            product_page.add_to_cart()

    with allure.step("Verify cart total"):
        cart_page.navigate("https://petstore.octoperf.com/actions/Cart.action?viewCart=")
        cart_page.assert_total_not_exceeds(budget, len(product_urls))