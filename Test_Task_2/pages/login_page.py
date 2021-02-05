from .base_page import BasePage
from pages.locators import LoginPageLocators


class LoginPage(BasePage):
    
    def __init__(self, browser, url, login, password):
        BasePage.__init__(self, browser, url)
        self.login = login
        self.password = password
    
    def should_be_login_page(self):
        self.should_be_login_form()
        self.should_be_password_form()
        self.should_be_to_puch_button()

    def should_be_login_form(self):
        # вводим логин
        login_input = self.browser.find_element(*LoginPageLocators.LOGIN_FORM)
        login_input.send_keys(self.login)

    def should_be_password_form(self):
        # вводим пароль
        password_input= self.browser.find_element(*LoginPageLocators.PASSWORD_FORM)
        password_input.send_keys(self.password)

    def should_be_to_puch_button(self):
        #нажатие кнопки "войти"
        submit = self.browser.find_element(*LoginPageLocators.BUTTON_SUBMIT)
        submit.click()
