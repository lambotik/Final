from .base_page import BasePage
from .locators import LoginPagesLocators
from .locators import BasePageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        #тут я проверял присутствует ли текст login в тексте ссылки http://selenium1py.pythonanywhere.com/accounts/login/
        assert 'login' in self.browser.current_url, 'Переходит на страницу с формами для регистрации'

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPagesLocators.LOGIN_FORM), 'Есть форма входа'

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPagesLocators.REGISTR_FORM), 'Есть форма регистрации'

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

