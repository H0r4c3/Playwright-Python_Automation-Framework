'''
Example 116: Authentication State (Save Login)

Very useful for skipping login in every test!

Use saved auth in tests:
python@pytest.fixture
def authenticated_page(browser):
    """Page with pre-loaded authentication"""
    context = browser.new_context(storage_state="auth.json")
    page = context.new_page()
    yield page
    context.close()

def test_skip_login(authenticated_page):
    """Test starts already logged in!"""
    authenticated_page.goto("https://www.saucedemo.com/inventory.html")
    
    # Already logged in, no login needed!
    assert "inventory" in authenticated_page.url
    print("✅ Test started with saved login state")
'''

from playwright.sync_api import sync_playwright

def save_authentication_state():
    """Save login state to file"""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        
        # Login
        page.goto("https://www.saucedemo.com/")
        page.fill("#user-name", "standard_user")
        page.fill("#password", "secret_sauce")
        page.click("#login-button")
        
        # Wait for login
        page.wait_for_url("**/inventory.html")
        
        # Save authentication state
        context.storage_state(path="auth.json")
        print("✅ Authentication state saved to auth.json")
        
        browser.close()

if __name__ == "__main__":
    save_authentication_state()
    
    