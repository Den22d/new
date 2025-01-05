<<<<<<< HEAD
﻿from selenium.webdriver.common.by import By
=======
﻿from selenium.webdriver.common.by import By
>>>>>>> 5b8bd2b5bac4dc1f40057b2407c3e7c9b483516d

from pages.main_page import MainPage


<<<<<<< HEAD

from pages.test_login_page import LoginPage

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"

    page = MainPage(browser, link)
    page.open()                      
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page() 


def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"

    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()
=======

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"

    page = MainPage(browser, link)
    page.open()                      
    page.go_to_login_page() 


def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"

    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()
    
>>>>>>> 5b8bd2b5bac4dc1f40057b2407c3e7c9b483516d
