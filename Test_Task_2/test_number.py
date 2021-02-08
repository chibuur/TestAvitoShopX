from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.product_page import ProductPage
import time

def test_number_value(browser):
    link = "https://www.avito.ru/sochi/lichnye_veschi?cd=1&d=1"
    
    #данные пользователя для авторизации
    login = ""
    password = ""
    
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, link, login, password)
    login_page.should_be_login_page()
    time.sleep(50)
    page.go_to_product_page()
    product_page = ProductPage(browser, link)
    product_page.should_be_buy_delivery_and_check_number_value()
    
    time.sleep(50)

