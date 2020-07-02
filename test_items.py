import pytest
from selenium import webdriver



link ="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_language_for_button(browser):

    button = None

    browser.get(link)
    button = browser.find_element_by_css_selector(
        ".btn.btn-lg.btn-primary.btn-add-to-basket"
    )
    
    import time
    time.sleep(5) # Это чтобы успеть увидеть страничку
    

