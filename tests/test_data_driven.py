'''
Example 106: Add Data-Driven Tests
'''

import pytest
from pages.login_page import LoginPage

class TestDataDriven:
    """Data-driven testing with parametrize"""
    
    @pytest.mark.parametrize("username,password,expected_error", [
        ("", "", "Username is required"),
        ("user", "", "Password is required"),
        ("", "pass", "Username is required"),
        ("wrong_user", "wrong_pass", "Username and password do not match"),
    ])
    def test_invalid_login_scenarios(self, page, username, password, expected_error):
        """Test multiple invalid login scenarios"""
        login_page = LoginPage(page)
        login_page.navigate()
        login_page.login(username, password)
        
        error = login_page.get_error_message()
        assert expected_error in error
        print(f"✅ Verified error for {username}/{password}")
        
    @pytest.mark.parametrize("user_type", [
        "standard_user",
        "problem_user",
        "performance_glitch_user",
    ])
    def test_different_user_types_login(self, page, user_type):
        """Test login with different user types"""
        login_page = LoginPage(page)
        login_page.navigate()
        login_page.login(user_type, "secret_sauce")
        
        if user_type != "locked_out_user":
            assert login_page.is_logged_in()
            print(f"✅ {user_type} logged in successfully")