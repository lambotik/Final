from .base_page import BasePage
from .locators import MainPageLocators
from .locators import ProductPageLocators
from .locators import BasePageLocators
from .locators import BasketPageLocators
from .locators import LoginPagesLocators
from selenium.common.exceptions import NoAlertPresentException # в начале файла
import time
import math

class ProductPage(BasePage):
    def add_to_basket(self):
        self.browser.find_element(*ProductPageLocators.BASKET_ADD).click()

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def should_be_name_product(self):
        name_product_adds = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT_ADDS).text
        name_product_in_basket = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT_IN_BASKET).text
        print('Название добавленного товара:', name_product_adds, '\n''Название товара в корзине:',
              name_product_in_basket)
        assert name_product_adds == name_product_in_basket, "Товар не соответствует"

    def should_be_price_in_basket(self):
        price_in_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_IN_BASKET_PRICE).text
        price_product = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT).text
        print('Цена продукта:', price_product, '\n''Цена продукта в корзине:', price_in_basket)
        assert price_in_basket == price_product, 'Цена товара не соответствует'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE),\
            "Success message is presented, but should not be"

    def should_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE),\
            "Success message is not disappeared"
    def should_be_guest_can_go_to_login_page_from_product_page(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Гость не может перейти на страницу логина"

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

    def go_to_basket_page(self):
        self.browser.find_element(*BasketPageLocators.BASKET).click()

    def find_mesege_empty(self):
        assert self.browser.find_element(*BasketPageLocators.EMPTY_BASKET), 'Корзина не пуста'

    def find_all_products_page(self):
        self.browser.find_element(*BasePageLocators.ALL_PRODUCTS_PAGE).click()



