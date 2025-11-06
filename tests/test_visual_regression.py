'''
Example 105: Add Visual Regression Testing


'''

import pytest
from playwright.sync_api import expect
from pages.login_page import LoginPage

class TestVisualRegression:
    """Visual regression testing with screenshots"""
    
    @pytest.mark.visual
    def test_login_page_visual(self, page):
        """Visual test for login page"""
        page.goto("https://www.saucedemo.com/")
        
        # Take screenshot and compare with baseline
        expect(page).to_have_screenshot("login-page-baseline.png", max_diff_pixels=50)
        
    @pytest.mark.visual
    def test_products_page_visual(self, page):
        """Visual test for products page"""
        login_page = LoginPage(page)
        login_page.navigate()
        login_page.login("standard_user", "secret_sauce")
        
        # Wait for page to load
        page.wait_for_selector(".inventory_item")
        
        # Visual comparison
        expect(page).to_have_screenshot("products-page-baseline.png", max_diff_pixels=100)
        
    @pytest.mark.visual
    def test_cart_icon_visual(self, page):
        """Visual test for specific element - cart icon"""
        login_page = LoginPage(page)
        login_page.navigate()
        login_page.login("standard_user", "secret_sauce")
        
        # Screenshot of cart icon only
        cart_icon = page.locator(".shopping_cart_link")
        expect(cart_icon).to_have_screenshot("cart-icon-baseline.png")