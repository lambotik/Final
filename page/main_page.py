from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import MainPageLocators
from .locators import ProductPageLocators
from .login_page import LoginPage
from selenium.common.exceptions import NoAlertPresentException # в начале файла
import math

class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)
