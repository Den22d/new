from .base_page import BasePage

from .locators import ProductPageLocators

from selenium.webdriver.common.by import By


class ProductPage(BasePage):
    def add_to_basket(self):

        basket_link = self.browser.find_element(*ProductPageLocators.B_LINK)

        basket_link.click()

    def xxx(self):
        x=self.browser.find_elements(By.CSS_SELECTOR,".alertinner ")
        x1=self.browser.find_element(By.CSS_SELECTOR,".product_main>h1").text
        x2=self.browser.find_element(By.CSS_SELECTOR,"p.price_color").text
        print(x[0].text,x[2].text )
        assert x1 in x[0].text,"no name"
        assert x2 in x[2].text,"no price"
    def should_not_be_success_message(self):
         assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
       "Success message is presented, but should not be"
    def should_see_as_disappearing_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
        "Success message is presented, but it must disappear"
    
  