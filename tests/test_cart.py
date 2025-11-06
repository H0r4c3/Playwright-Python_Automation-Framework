'''
Run all cart tests:
pytest tests/test_cart.py -v
Run only the e2e test:
pytest tests/test_cart.py -v -m e2e
'''

import pytest
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage

class TestCart:
    """Test suite for shopping cart functionality"""
    
    @pytest.fixture(autouse=True)
    def setup(self, page):
        """Login and navigate before each test"""
        login_page = LoginPage(page)
        login_page.navigate()
        login_page.login("standard_user", "secret_sauce")
        self.products_page = ProductsPage(page)
        self.cart_page = CartPage(page)
        
    @pytest.mark.smoke
    def test_view_empty_cart(self, page):
        """Test viewing empty cart"""
        self.products_page.go_to_cart()
        
        assert self.cart_page.is_cart_empty()
        assert "cart" in page.url
        
    def test_view_cart_with_items(self, page):
        """Test viewing cart with added items"""
        self.products_page.add_product_to_cart("Sauce Labs Backpack")
        self.products_page.go_to_cart()
        
        assert self.cart_page.get_cart_item_count() == 1
        assert "Sauce Labs Backpack" in self.cart_page.get_cart_item_names()
        
    def test_remove_item_from_cart(self, page):
        """Test removing item from cart"""
        # Add items
        self.products_page.add_product_to_cart("Sauce Labs Backpack")
        self.products_page.add_product_to_cart("Sauce Labs Bike Light")
        self.products_page.go_to_cart()
        
        # Remove one item
        self.cart_page.remove_item("Sauce Labs Backpack")
        
        assert self.cart_page.get_cart_item_count() == 1
        cart_items = self.cart_page.get_cart_item_names()
        assert "Sauce Labs Backpack" not in cart_items
        assert "Sauce Labs Bike Light" in cart_items
        
    def test_remove_all_items_from_cart(self, page):
        """Test removing all items from cart"""
        # Add items
        self.products_page.add_product_to_cart("Sauce Labs Backpack")
        self.products_page.add_product_to_cart("Sauce Labs Bike Light")
        self.products_page.go_to_cart()
        
        # Remove all
        self.cart_page.remove_first_item()
        self.cart_page.remove_first_item()
        
        assert self.cart_page.is_cart_empty()
        
    def test_continue_shopping_from_cart(self, page):
        """Test continue shopping button"""
        self.products_page.go_to_cart()
        self.cart_page.continue_shopping()
        
        assert "inventory" in page.url
        
    @pytest.mark.e2e
    def test_full_shopping_flow(self, page):
        """End-to-end test: Browse → Add → View Cart → Remove → Checkout"""
        # Add products
        self.products_page.add_product_to_cart("Sauce Labs Backpack")
        self.products_page.add_product_to_cart("Sauce Labs Bike Light")
        self.products_page.add_product_to_cart("Sauce Labs Bolt T-Shirt")
        
        assert self.products_page.get_cart_count() == 3
        
        # Go to cart
        self.products_page.go_to_cart()
        assert self.cart_page.get_cart_item_count() == 3
        
        # Remove one item
        self.cart_page.remove_item("Sauce Labs Bike Light")
        assert self.cart_page.get_cart_item_count() == 2
        
        # Proceed to checkout
        self.cart_page.proceed_to_checkout()
        assert "checkout-step-one" in page.url