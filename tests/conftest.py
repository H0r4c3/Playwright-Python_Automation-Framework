'''
Example 97: Create conftest.py for Portfolio

What it does:

Centralized fixtures for all page objects
logged_in_user fixture for tests that need pre-login
Configures custom markers programmatically

Test everything works:
cd portfolio_project
pytest tests/ -v --html=report.html --self-contained-html
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