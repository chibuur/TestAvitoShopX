from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, ".header-services-menu-link-not-authenticated-3kAga")
    ITEMS_LINK = (By.CSS_SELECTOR, ".iva-item-titleStep-2bjuh")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR,'[name="login"]')
    PASSWORD_FORM = (By.CSS_SELECTOR, '[name="password"]')
    BUTTON_SUBMIT = (By.CSS_SELECTOR, '[name="submit"]')

class ProductPageLocators():
    BUTTON_BUY_DELIVERY = (By.CSS_SELECTOR, ".item-buyer-button-1-zak")
    NUMBER_FORM = (By.CSS_SELECTOR, '[name="phone"]')
