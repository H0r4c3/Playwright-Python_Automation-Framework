'''
Example 103: Add Mobile Testing


'''

import pytest
from pages.login_page import LoginPage

class TestMobile:
    """Mobile responsive testing"""
    
    @pytest.mark.mobile
    def test_login_on_iphone(self, playwright, browser):
        """Test login on iPhone 12"""
        iphone = playwright.devices["iPhone 12"]
        context = browser.new_context(**iphone)
        page = context.new_page()
        
        login_page = LoginPage(page)
        login_page.navigate()
        login_page.login("standard_user", "secret_sauce")
        
        assert login_page.is_logged_in()
        print("✅ Login successful on iPhone 12")
        
        context.close()
        
    @pytest.mark.mobile
    def test_login_on_ipad(self, playwright, browser):
        """Test login on iPad"""
        ipad = playwright.devices["iPad Pro"]
        context = browser.new_context(**ipad)
        page = context.new_page()
        
        login_page = LoginPage(page)
        login_page.navigate()
        login_page.login("standard_user", "secret_sauce")
        
        assert login_page.is_logged_in()
        print("✅ Login successful on iPad Pro")
        
        context.close()
        
    @pytest.mark.mobile
    def test_login_on_android(self, playwright, browser):
        """Test login on Android device"""
        android = playwright.devices["Pixel 5"]
        context = browser.new_context(**android)
        page = context.new_page()
        
        login_page = LoginPage(page)
        login_page.navigate()
        login_page.login("standard_user", "secret_sauce")
        
        assert login_page.is_logged_in()
        print("✅ Login successful on Pixel 5")
        
        context.close()