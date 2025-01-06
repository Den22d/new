from .base_page import BasePage

from .locators import BasePageLocators

from selenium.webdriver.common.by import By
class BasketPage(BasePage):
    def no_goods(self):
         assert self.is_not_element_present(*BasePageLocators.BASKET), \
       "No goods"
    def basket_empty(self):
        x=self.browser.find_element(*BasePageLocators.BASKET_EMPTY)
        assert x.text=="Your basket is empty. Continue shopping", "no empty"
        
        
         
        
        