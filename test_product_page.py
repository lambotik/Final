from page.product_page import ProductPage
from page.login_page import LoginPage
import pytest


@pytest.mark.parametrize('promo_link', [i for i in range(10)])
def test_guest_can_add_product_to_basket(browser, promo_link):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_link}"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_name_product()
    page.should_be_price_in_basket()

@pytest.mark.xfail
def test_visability_succes_message(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer'
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_not_be_success_message()

@pytest.mark.xfail
def test_guest_cant_see_success_message(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer'
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer'
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_disappeared()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_guest_can_go_to_login_page_from_product_page()

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/'
    page = ProductPage(browser, link)
    page.open()
    page.find_all_products_page()
    page.go_to_basket_page()
    page.find_mesege_empty()

@pytest.mark.login
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self,browser):
        self.browser = browser
        page = LoginPage(self.browser,'http://selenium1py.pythonanywhere.com/accounts/login/')
        page.open()
        page.register_new_user()
        page.should_be_authorized_user()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self,link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"):
        page = ProductPage(self.browser, link)
        page.open()
        page.add_to_basket()
        page.solve_quiz_and_get_code()
        page.should_be_name_product()
        page.should_be_price_in_basket()

    def test_user_cant_see_success_message(self,link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer'):
        page = ProductPage(self.browser, link)
        page.open()
        page.should_not_be_success_message()




