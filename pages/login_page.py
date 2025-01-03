from .base_page import BasePage


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
        
        assert self.is_element_present(*LoginPageLocators.REG_LINL), "No Reg Form"