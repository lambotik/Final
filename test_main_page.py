import pytest
from page.base_page import BasePage
from page.login_page import LoginPage
from page.product_page import ProductPage
from page.basket_page import BasketPage
from page import locators
from page.main_page import MainPage


@pytest.mark.login_guest
class TestLoginFromMainPage():
    def test_guest_can_go_to_login_page(self,browser):
        link = "http://selenium1py.pythonanywhere.com"
        page = BasePage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()
    def test_guest_should_see_login_link(self,browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = LoginPage(browser, link)
        page.open()
        page.should_be_login_link()



def test_login_url(browser):
    link = "http://selenium1py.pythonanywhere.com/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_url()

def test_login_form(browser):
    link = "https://selenium1py.pythonanywhere.com/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_form()

def test_registr_form(browser):
    link = "https://selenium1py.pythonanywhere.com/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_register_form()

def go_to_login_page(self):
    link = self.browser.find_element_by_css_selector("#login_link")
    link.click()



def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/'
    page = BasketPage(browser, link)
    page.open()
    page.go_to_basket_page()
    page.find_mesege_empty()






