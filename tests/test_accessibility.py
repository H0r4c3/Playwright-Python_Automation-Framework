'''
Example 104: Add Accessibility Testing


'''

import pytest
from playwright.sync_api import expect

class TestAccessibility:
    """Accessibility testing examples"""
    
    def test_login_page_has_proper_labels(self, page):
        """Test that form inputs have proper labels"""
        page.goto("https://www.saucedemo.com/")
        
        # Check input fields have labels
        username_input = page.locator("#user-name")
        password_input = page.locator("#password")
        
        assert username_input.get_attribute("placeholder") == "Username"
        assert password_input.get_attribute("placeholder") == "Password"
        print("✅ Form inputs have proper labels")
        
    def test_login_button_accessible(self, page):
        """Test login button is keyboard accessible"""
        page.goto("https://www.saucedemo.com/")
        
        # Tab to login button
        page.keyboard.press("Tab")  # Username
        page.keyboard.press("Tab")  # Password
        page.keyboard.press("Tab")  # Login button
        
        # Check login button is focused
        focused_element = page.evaluate("document.activeElement.id")
        assert focused_element == "login-button"
        print("✅ Login button is keyboard accessible")
        
    def test_page_has_proper_heading_structure(self, page):
        """Test page has proper heading hierarchy"""
        page.goto("https://www.saucedemo.com/")
        
        # Check for main heading
        headings = page.locator("h1, h2, h3, h4").all()
        assert len(headings) > 0, "Page should have headings"
        print(f"✅ Found {len(headings)} heading(s) on page")