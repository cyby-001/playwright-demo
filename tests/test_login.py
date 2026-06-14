import pytest
from pages.login_page import LoginPage

# 登录成功
def test_login_success(page):
    login = LoginPage(page)
    login.navigate()
    login.login("standard_user", "secret_sauce")
    assert "/inventory" in page.url, "登录成功后应跳转到商品页"

# 用参数化一次测试多种失败场景
@pytest.mark.parametrize("username, password, expected_error", [
    ("standard_user",  "wrong_pass",   "Epic sadface"),   # 密码错误
    ("",               "secret_sauce", "Username is required"),  # 用户名为空
    ("standard_user",  "",             "Password is required"),  # 密码为空
    ("locked_out_user","secret_sauce", "Sorry, this user has been locked out"),  # 被锁定用户
])
def test_login_fail(page, username, password, expected_error):
    login = LoginPage(page)
    login.navigate()
    login.login(username, password)
    error_text = login.get_error_message()
    assert expected_error in error_text, f"期望报错包含: {expected_error}，实际: {error_text}"