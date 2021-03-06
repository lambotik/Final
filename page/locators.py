from selenium.webdriver.common.by import By


class MainPageLocators():
    pass

class LoginPagesLocators():
    LOGIN_URL = 'http://selenium1py.pythonanywhere.com/accounts/login/'
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTR_FORM = (By.CSS_SELECTOR, '#register_form')
    ENTER_EMAIL = (By.ID, 'id_login-username')
    ENTER_PASSWORD = (By.ID, 'id_login-password')
    REGISTR_EMAIL = (By.ID, 'id_registration-email')
    REGISTR_PASSWORD = (By.ID,'id_registration-password1')
    REPIT_PASSWORD = (By.ID,'id_registration-password2')
    BTN_REGISTR = (By.CSS_SELECTOR,"[name='registration_submit']")

class ProductPageLocators():
    LOGIN_URL = 'http://selenium1py.pythonanywhere.com/accounts/login/'
    NAME_PRODUCT_ADDS = (By.XPATH, '//*[@id="content_inner"]/article/div[1]/div[2]/h1')
    NAME_PRODUCT_IN_BASKET = (By.XPATH, '//*[@id="messages"]/div[1]/div/strong')
    PRODUCT_IN_BASKET_PRICE = (By.XPATH, '//*[@id="messages"]/div[3]/div/p[1]/strong')
    PRICE_PRODUCT = (By.CSS_SELECTOR, '.col-sm-6.product_main .price_color')
    SUCCESS_MESSAGE = (By.CLASS_NAME, 'alertinner')
    BASKET_ADD = (By.CLASS_NAME, 'btn-add-to-basket')


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    ALL_PRODUCTS_PAGE = (By.CSS_SELECTOR, '[href="/en-gb/catalogue/"]')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    BASKET = (By.CLASS_NAME, 'btn-group .btn-default')
    EMPTY_BASKET = (By.CSS_SELECTOR, '#content_inner')