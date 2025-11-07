'''
Example 97: Create conftest.py for Portfolio

What it does:

Centralized fixtures for all page objects
logged_in_user fixture for tests that need pre-login
Configures custom markers programmatically

Test everything works:
cd portfolio_project
pytest tests/ -v --html=report.html --self-contained-html

Example 111: Playwright Trace Viewer (VERY Important!)
Traces are recordings of your test execution - amazing for debugging!
Enable Tracing in Tests:
Update portfolio_project/tests/conftest.py:
pythonimport pytest

@pytest.fixture(scope="function", autouse=True)
def trace_on_failure(page, request):
    """Record trace on test failure"""
    # Start tracing
    page.context.tracing.start(screenshots=True, snapshots=True, sources=True)
    
    yield
    
    # Stop tracing and save if test failed
    if request.node.rep_call.failed:
        page.context.tracing.stop(path=f"test-results/trace-{request.node.name}.zip")
    else:
        page.context.tracing.stop()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Store test result for trace decision"""
    outcome = yield
    rep = outcome.get_result()
    setattr(item, f"rep_{rep.when}", rep)
View Traces:
bash# View a specific trace
playwright show-trace test-results/trace-test_name.zip

# Or use online viewer
# Upload to: https://trace.playwright.dev/
What Traces Show:

✅ Every action taken
✅ Screenshots at each step
✅ Network requests
✅ Console logs
✅ Page source at each step
✅ Timing information

This is GOLD for debugging!
'''

import pytest
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage

@pytest.fixture
def login_page(page):
    """Provides LoginPage instance"""
    return LoginPage(page)

@pytest.fixture
def products_page(page):
    """Provides ProductsPage instance"""
    return ProductsPage(page)

@pytest.fixture
def cart_page(page):
    """Provides CartPage instance"""
    return CartPage(page)

@pytest.fixture
def logged_in_user(page):
    """Logs in a standard user and returns page"""
    login = LoginPage(page)
    login.navigate()
    login.login("standard_user", "secret_sauce")
    return page

def pytest_configure(config):
    """Configure pytest with custom settings"""
    config.addinivalue_line(
        "markers", "smoke: Quick smoke tests"
    )
    config.addinivalue_line(
        "markers", "e2e: End-to-end scenarios"
    )
    

@pytest.fixture(scope="function", autouse=True)
def trace_on_failure(page, request):
    """Record trace on test failure"""
    # Start tracing
    page.context.tracing.start(screenshots=True, snapshots=True, sources=True)
    
    yield
    
    # Stop tracing and save if test failed
    if request.node.rep_call.failed:
        page.context.tracing.stop(path=f"test-results/trace-{request.node.name}.zip")
    else:
        page.context.tracing.stop()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Store test result for trace decision"""
    outcome = yield
    rep = outcome.get_result()
    setattr(item, f"rep_{rep.when}", rep)
    

import pytest
from playwright.sync_api import Browser
from playwright_config import PlaywrightConfig

@pytest.fixture
def context(browser: Browser):
    """Create context with custom config"""
    context = browser.new_context(**PlaywrightConfig.get_browser_context_options())
    yield context
    context.close()

@pytest.fixture
def page(context):
    """Create page from context"""
    page = context.new_page()
    page.set_default_timeout(PlaywrightConfig.TIMEOUT)
    yield page
    page.close()
    
import pytest

@pytest.fixture(scope="function")
def context_with_video(browser):
    """Create context that records video"""
    context = browser.new_context(
        record_video_dir="test-results/videos/",
        record_video_size={"width": 1280, "height": 720}
    )
    yield context
    context.close()

@pytest.fixture
def page_with_video(context_with_video):
    """Page that records video"""
    page = context_with_video.new_page()
    yield page
    page.close()
    
    # Video is saved automatically when context closes
    video_path = page.video.path()
    print(f"\n🎥 Video saved: {video_path}")
    
