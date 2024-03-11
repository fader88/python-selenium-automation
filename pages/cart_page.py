from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import Page


class CartPage(Page):
    CART_HEADER = (By.CSS_SELECTOR, "h1[class*='StyledHeading']")

    def verify_cart_is_empty(self):
        actual_text = self.driver.find_element(*self.CART_HEADER).text
        assert 'Your cart is empty' == actual_text, f"Expected 'Your cart is empty' but got {actual_text}"
