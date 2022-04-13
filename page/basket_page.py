from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from .locators import BasePageLocators
from .locators import ProductPageLocators
from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def go_to_basket_page(self):
        self.browser.find_element(*BasketPageLocators.BASKET).click()
    def find_mesege_empty(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET), "В корзине не дожно быть товара"