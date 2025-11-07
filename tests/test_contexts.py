'''
Example 114: Browser Contexts (Isolation)
'''

import pytest

class TestContexts:
    """Browser context examples - test isolation"""
    
    def test_multiple_users_same_time(self, browser):
        """Simulate multiple users in parallel"""
        # User 1 context
        context1 = browser.new_context()
        page1 = context1.new_page()
        page1.goto("https://www.saucedemo.com/")
        page1.fill("#user-name", "standard_user")
        page1.fill("#password", "secret_sauce")
        page1.click("#login-button")
        
        # User 2 context (completely isolated)
        context2 = browser.new_context()
        page2 = context2.new_page()
        page2.goto("https://www.saucedemo.com/")
        page2.fill("#user-name", "problem_user")
        page2.fill("#password", "secret_sauce")
        page2.click("#login-button")
        
        # Both logged in independently
        assert "inventory" in page1.url
        assert "inventory" in page2.url
        
        print("✅ Two users logged in simultaneously")
        
        context1.close()
        context2.close()
        
    def test_different_permissions(self, browser):
        """Test with different browser permissions"""
        # Context with geolocation
        context = browser.new_context(
            geolocation={"latitude": 41.85, "longitude": -87.65},
            permissions=["geolocation"]
        )
        page = context.new_page()
        
        # Test would work with location-based features
        page.goto("https://www.saucedemo.com/")
        
        print("✅ Context created with geolocation permissions")
        context.close()