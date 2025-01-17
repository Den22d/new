﻿from pages.base_page import BasePage
from pages.locators import LoginPageLocators
from selenium.webdriver.common.by import By
import time
class LoginPage(BasePage):
    
    
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        x=self.browser.current_url
        assert 'login' in x,"no login"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        
        assert self.is_element_present(*LoginPageLocators.LOG_LINK),"NO Log form"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        
        assert self.is_element_present(*LoginPageLocators.REG_LINK), "No Reg Form"
    def register_new_user(self,email,password):
        email = str(time.time()) + "@fakemail.org"
        self.browser.find_element(*LoginPageLocators.EMAIL_LINK).send_keys(email)
        self.browser.find_element(*LoginPageLocators.PW1_LINK).send_keys(password)
        self.browser.find_element(*LoginPageLocators.PW2_LINK).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REG_LINK).click()

   
    