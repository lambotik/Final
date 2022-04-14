from page.base_page import BasePage
from page.login_page import LoginPage
from page.product_page import ProductPage
from page.basket_page import BasketPage
from page import locators
from page.main_page import MainPage


def go_to_login_page(self):
    link = self.browser.find_element_by_css_selector("#login_link")
    link.click()
def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()