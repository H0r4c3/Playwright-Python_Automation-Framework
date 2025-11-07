"""
Playwright configuration for Python
Note: This is for documentation purposes.
Python Playwright doesn't use config files like TypeScript,
but you can create helper functions with these settings.

Use it in conftest.py:
pythonimport pytest
from playwright.sync_api import Browser
from playwright_config import PlaywrightConfig

@pytest.fixture
def context(browser: Browser):
    '''Create context with custom config'''
    context = browser.new_context(**PlaywrightConfig.get_browser_context_options())
    yield context
    context.close()

@pytest.fixture
def page(context):
    '''Create page from context'''
    page = context.new_page()
    page.set_default_timeout(PlaywrightConfig.TIMEOUT)
    yield page
    page.close()
"""

class PlaywrightConfig:
    """Centralized configuration"""
    
    # Base URL
    BASE_URL = "https://www.saucedemo.com"
    
    # Timeouts (milliseconds)
    TIMEOUT = 30000
    NAVIGATION_TIMEOUT = 30000
    
    # Browser settings
    HEADLESS = False
    SLOW_MO = 0  # Slow down by X ms
    
    # Screenshot settings
    SCREENSHOT_ON_FAILURE = True
    VIDEO_ON_FAILURE = True
    
    # Viewport
    VIEWPORT = {"width": 1280, "height": 720}
    
    # User credentials
    VALID_USERNAME = "standard_user"
    VALID_PASSWORD = "secret_sauce"
    
    @classmethod
    def get_browser_context_options(cls):
        """Get browser context options"""
        return {
            "viewport": cls.VIEWPORT,
            "base_url": cls.BASE_URL,
        }