from page.main_page import MainPage
from page.login_page import LoginPage
from selenium.webdriver.common.by import By
from page.locators import MainPageLocators

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