import pytest
from playwright.sync_api import Page
from pages.login_page import LoginPage

@pytest.fixture
def page(browser):
    page = browser.new_page()
    yield page
    page.close()

@pytest.fixture
def logged_in(page):
    """
    登录 fixture：自动登录，返回已登录的页面
    所有需要登录的测试都可以用这个 fixture
    """
    login = LoginPage(page)
    login.navigate()
    login.login("standard_user", "secret_sauce")
    return page