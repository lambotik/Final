from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET = (By.CLASS_NAME, 'btn-add-to-basket')
class LoginPagesLocators():
    LOGIN_URL = 'http://selenium1py.pythonanywhere.com/accounts/login/'
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTR_FORM = (By.CSS_SELECTOR, '#register_form')

class ProductPageLocators():
    LOGIN_URL = 'http://selenium1py.pythonanywhere.com/accounts/login/'
    NAME_PRODUCT_ADDS = (By.XPATH, '//*[@id="content_inner"]/article/div[1]/div[2]/h1')
    NAME_PRODUCT_IN_BASKET = (By.XPATH, '//*[@id="messages"]/div[1]/div/strong')
    PRODUCT_IN_BASKET_PRICE = (By.XPATH, '//*[@id="messages"]/div[3]/div/p[1]/strong')
    PRICE_PRODUCT = (By.CSS_SELECTOR, '.col-sm-6.product_main .price_color')