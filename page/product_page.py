from .base_page import BasePage
from .locators import MainPageLocators
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException # в начале файла
import math

class ProductPage(BasePage):
    def add_to_basket(self):
        self.browser.find_element(*MainPageLocators.BASKET).click()

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