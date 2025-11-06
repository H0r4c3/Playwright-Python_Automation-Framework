'''
Example 102: Add Performance Timing Tests


'''

import pytest
from pages.login_page import LoginPage

class TestPerformance:
    """Performance testing - measure page load times"""
    
    def test_login_page_load_time(self, page):
        """Measure login page load time"""
        page.goto("https://www.saucedemo.com/")
        
        # Get performance metrics
        metrics = page.evaluate("""() => {
            const timing = performance.timing;
            return {
                pageLoad: timing.loadEventEnd - timing.navigationStart,
                domReady: timing.domContentLoadedEventEnd - timing.navigationStart,
                responseTime: timing.responseEnd - timing.requestStart
            }
        }""")
        
        print(f"\n📊 Performance Metrics:")
        print(f"   Page Load Time: {metrics['pageLoad']}ms")
        print(f"   DOM Ready: {metrics['domReady']}ms")
        print(f"   Response Time: {metrics['responseTime']}ms")
        
        # Assert page loads within reasonable time (3 seconds)
        assert metrics['pageLoad'] < 3000, f"Page load too slow: {metrics['pageLoad']}ms"
        
    @pytest.mark.performance
    def test_products_page_load_time(self, page):
        """Measure products page load time after login"""
        login_page = LoginPage(page)
        login_page.navigate()
        login_page.login("standard_user", "secret_sauce")
        
        # Measure time to load products
        start_time = page.evaluate("performance.now()")
        page.wait_for_selector(".inventory_item", timeout=5000)
        end_time = page.evaluate("performance.now()")
        
        load_time = end_time - start_time
        print(f"\n📊 Products Load Time: {load_time:.2f}ms")
        
        assert load_time < 2000, f"Products loaded too slowly: {load_time:.2f}ms"