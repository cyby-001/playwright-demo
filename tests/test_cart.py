import pytest
from pages.login_page import LoginPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

# 每个用例都需要先登录，用 fixture 搞定
@pytest.fixture
def logged_in(page):
    login = LoginPage(page)
    login.navigate()
    login.login("standard_user", "secret_sauce")
    return page

def test_add_to_cart_badge(logged_in):
    """加购后购物车数字变成 1"""
    cart = CartPage(logged_in)
    cart.add_first_item_to_cart()
    assert cart.get_cart_count() == "1"

def test_cart_shows_item(logged_in):
    """进入购物车能看到刚加的商品"""
    cart = CartPage(logged_in)
    cart.add_first_item_to_cart()
    cart.go_to_cart()
    assert cart.get_cart_item_count() == 1

def test_remove_item_from_cart(logged_in):
    """移除商品后购物车为空"""
    cart = CartPage(logged_in)
    cart.add_first_item_to_cart()
    cart.go_to_cart()
    cart.remove_item()
    assert cart.get_cart_item_count() == 0

def test_checkout_success(logged_in):
    """填写完整信息，订单提交成功"""
    cart = CartPage(logged_in)
    cart.add_first_item_to_cart()
    cart.go_to_cart()
    cart.go_to_checkout()
    checkout = CheckoutPage(logged_in)
    checkout.fill_info("张", "三", "200001")
    checkout.continue_checkout()
    checkout.finish_order()
    assert "Thank you for your order!" in checkout.get_complete_text()

@pytest.mark.parametrize("first, last, postal, expected_error", [
    ("",   "三", "200001", "First Name is required"),
    ("张",  "",  "200001", "Last Name is required"),
    ("张",  "三", "",      "Postal Code is required"),
])
def test_checkout_missing_info(logged_in, first, last, postal, expected_error):
    """结算必填项为空时显示对应错误"""
    cart = CartPage(logged_in)
    cart.add_first_item_to_cart()
    cart.go_to_cart()
    cart.go_to_checkout()
    checkout = CheckoutPage(logged_in)
    checkout.fill_info(first, last, postal)
    checkout.continue_checkout()
    assert expected_error in checkout.get_error()