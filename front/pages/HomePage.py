from front.pages.locators.HomePageLocator import HomePageLocator
from front.pages.CartPage import CartPage
from front.seleniumExtended import SeleniumExtended
from front.helpers.config_helpers import get_base_url
import logging as Logger
from time import sleep


class HomePage(HomePageLocator):

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def go_to_my_homepage(self):
        base_url = get_base_url()
        my_account_url = base_url
        Logger.info(f"Going to: {my_account_url}")
        self.driver.get(my_account_url)

    def add_item_to_cart(self):
        self.sl.wait_until_element_is_clickble(self.ADD_TO_CART_BUTTON, 10)
        Logger.info("added item to the cart")

    def click_on_cart_button(self):
        self.sl.wait_until_element_is_clickble(self.CART_BUTTON)
        Logger.info("clicked on cart button")
