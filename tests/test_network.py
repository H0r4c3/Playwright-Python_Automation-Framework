'''
Example 113: Network Interception (Advanced)

'''

import pytest

class TestNetwork:
    """Network interception and mocking"""
    
    def test_intercept_api_calls(self, page):
        """Monitor network requests"""
        api_calls = []
        
        # Listen to all requests
        page.on("request", lambda request: api_calls.append(request.url))
        
        page.goto("https://www.saucedemo.com/")
        page.fill("#user-name", "standard_user")
        page.fill("#password", "secret_sauce")
        page.click("#login-button")
        
        print(f"\n📡 API calls made: {len(api_calls)}")
        for url in api_calls:
            print(f"   - {url}")
            
    def test_mock_api_response(self, page):
        """Mock API responses"""
        # Intercept and modify responses
        def handle_route(route):
            # Return mock data instead of real API
            route.fulfill(
                status=200,
                body='{"mocked": true}'
            )
        
        page.route("**/api/*", handle_route)
        page.goto("https://www.saucedemo.com/")
        
        print("✅ API responses mocked")
        
    def test_block_images(self, page):
        """Block image loading for faster tests"""
        # Block all image requests
        page.route("**/*.{png,jpg,jpeg,gif,svg}", lambda route: route.abort())
        
        page.goto("https://www.saucedemo.com/")
        page.fill("#user-name", "standard_user")
        page.fill("#password", "secret_sauce")
        page.click("#login-button")
        
        print("✅ Test ran without loading images (faster)")