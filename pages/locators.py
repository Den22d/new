from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
class LoginPageLocators():
    REG_LINK=(By.CSS_SELECTOR,"[value='Register']")
    LOG_LINK=(By.CSS_SELECTOR,"[value='Log In']")
class ProductPageLocators():
    B_LINK=(By.CSS_SELECTOR,".btn-add-to-basket")