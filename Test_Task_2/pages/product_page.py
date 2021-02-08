from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By


class ProductPage(BasePage):
    
    def should_be_buy_delivery_and_check_number_value(self):
        self.add_to_delivery()
        self.should_be_number_value()
    
    def add_to_delivery(self):
        add_button = self.browser.find_element(*ProductPageLocators.BUTTON_BUY_DELIVERY)
        add_button.click()
    
    def should_be_number_value(self):
        number_form = self.browser.find_element(*ProductPageLocators.NUMBER_FORM)
        self.browser.execute_script("return arguments[0].scrollIntoView(true);", number_form)
        number_value = number_form.get_attribute("value")
        assert "+7" not in number_value, "Phone field is not empty!"
