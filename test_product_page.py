from page.product_page import ProductPage
import pytest


@pytest.mark.parametrize('promo_link', [i for i in range(10)])
def test_guest_can_add_product_to_basket(browser, promo_link):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_link}"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_name_product()
    page.should_be_price_in_basket()