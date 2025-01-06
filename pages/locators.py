from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
class LoginPageLocators():
    REG_LINK=(By.CSS_SELECTOR,"[value='Register']")
    LOG_LINK=(By.CSS_SELECTOR,"[value='Log In']")
    EMAIL_LINK=(By.CSS_SELECTOR,"#id_registration-email")
    PW1_LINK=(By.CSS_SELECTOR,"#id_registration-password1")
    PW2_LINK=(By.CSS_SELECTOR,"#id_registration-password2")
class ProductPageLocators():
    B_LINK=(By.CSS_SELECTOR,".btn-add-to-basket")
    SUCCESS_MESSAGE=(By.CSS_SELECTOR,"#message .alert:nth-child(1) .alertinner")
class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK=(By.CSS_SELECTOR, ".btn-group>.btn-default")
    BASKET=(By.CSS_SELECTOR, "div.basket-mini")
    BASKET_EMPTY=(By.CSS_SELECTOR, "#content_inner")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")