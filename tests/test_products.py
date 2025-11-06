'''
Example 94: Products Tests

New concept: autouse=True fixture
What it does:

autouse=True runs the fixture automatically before each test
All tests start logged in
No need to repeat login code

Run the tests:
pytest tests/test_products.py -v
'''

import pytest
from pages.login_page import LoginPage
from pages.products_page import ProductsPage

class TestProducts:
    """Test suite for products page functionality"""
    
    @pytest.fixture(autouse=True)
    def setup(self, page):
        """Login before each test"""
        login_page = LoginPage(page)
        login_page.navigate()
        login_page.login("standard_user", "secret_sauce")
        self.products_page = ProductsPage(page)
        
    @pytest.mark.smoke
    def test_products_page_loads(self, page):
        """Verify products page displays correctly"""
        assert self.products_page.get_product_count() == 6
        assert "inventory" in page.url
        
    def test_add_single_product_to_cart(self, page):
        """Test adding one product to cart"""
        self.products_page.add_first_product_to_cart()
        
        assert self.products_page.get_cart_count() == 1
        
    def test_add_multiple_products_to_cart(self, page):
        """Test adding multiple products to cart"""
        self.products_page.add_product_to_cart("Sauce Labs Backpack")
        self.products_page.add_product_to_cart("Sauce Labs Bike Light")
        
        assert self.products_page.get_cart_count() == 2
        
    def test_sort_products_a_to_z(self, page):
        """Test sorting products alphabetically A to Z"""
        self.products_page.sort_products("az")
        
        product_names = self.products_page.get_all_product_names()
        assert product_names == sorted(product_names)
        
    def test_sort_products_z_to_a(self, page):
        """Test sorting products alphabetically Z to A"""
        self.products_page.sort_products("za")
        
        product_names = self.products_page.get_all_product_names()
        assert product_names == sorted(product_names, reverse=True)
        
    def test_sort_products_price_low_to_high(self, page):
        """Test sorting products by price low to high"""
        self.products_page.sort_products("lohi")
        
        prices = self.products_page.get_all_product_prices()
        assert prices == sorted(prices)
        
    def test_sort_products_price_high_to_low(self, page):
        """Test sorting products by price high to low"""
        self.products_page.sort_products("hilo")
        
        prices = self.products_page.get_all_product_prices()
        assert prices == sorted(prices, reverse=True)