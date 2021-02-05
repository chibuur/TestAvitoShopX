from pages.base_page import BasePage
from pages.locators import MainPageLocators

class MainPage(BasePage):
    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()
       

    def go_to_product_page(self):
        product_button = self.browser.find_element(*MainPageLocators.ITEMS_LINK)
        product_button.click()
        
        #данный метод добавлен для случая, если тест продолжит работать со старой вкладкой
        new_window = self.browser.window_handles[1]
        self.browser.switch_to.window(new_window)

