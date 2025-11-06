'''
Example 92: Login Tests (Valid & Invalid)

New concept: Test class organization with docstrings
What it does:

Groups related tests in a class
Uses descriptive test names
Docstrings explain what each test does
Mix of smoke tests and detailed tests

cd portfolio_project
pytest tests/test_login.py -v -m smoke
(Only smoke tests run)
Run all login tests:
pytest tests/test_login.py -v
'''

import pytest
from pages.login_page import LoginPage

class TestLogin:
    """Test suite for login functionality"""
    
    @pytest.mark.smoke
    def test_successful_login(self, page):
        """Test login with valid credentials"""
        login_page = LoginPage(page)
        login_page.navigate()
        login_page.login("standard_user", "secret_sauce")
        
        assert login_page.is_logged_in()
        assert "inventory.html" in page.url
        
    @pytest.mark.smoke
    def test_locked_user_login(self, page):
        """Test login with locked out user"""
        login_page = LoginPage(page)
        login_page.navigate()
        login_page.login("locked_out_user", "secret_sauce")
        
        error = login_page.get_error_message()
        assert "locked out" in error.lower()
        
    def test_invalid_username(self, page):
        """Test login with invalid username"""
        login_page = LoginPage(page)
        login_page.navigate()
        login_page.login("invalid_user", "secret_sauce")
        
        error = login_page.get_error_message()
        assert "Username and password do not match" in error
        
    def test_invalid_password(self, page):
        """Test login with invalid password"""
        login_page = LoginPage(page)
        login_page.navigate()
        login_page.login("standard_user", "wrong_password")
        
        error = login_page.get_error_message()
        assert "Username and password do not match" in error
        
    def test_empty_credentials(self, page):
        """Test login with empty fields"""
        login_page = LoginPage(page)
        login_page.navigate()
        login_page.login("", "")
        
        error = login_page.get_error_message()
        assert "Username is required" in error