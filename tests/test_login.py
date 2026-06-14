import pytest
from pages.login_page import LoginPage

def test_login_success(page):
    login = LoginPage(page)
    login.navigate()
    login.login("standard_user", "secret_sauce")
    assert "/inventory" in page.url

def test_login_fail_wrong_password(page):
    login = LoginPage(page)
    login.navigate()
    login.login("standard_user", "wrong_password")
    assert login.get_error_message() != ""