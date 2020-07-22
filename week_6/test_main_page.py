from os import getenv
from page_objects.main_page import MainPage
def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    browser.get(link)
    login_link = browser.find_element_by_css_selector("#login_link")
    login_link.click()
BASE_URL = getenv('BASE_URL', "http://selenium1py.pythonanywhere.com/")
IMPLICIT_WAIT = 2
EXPLICIT_WAIT = 4
WINDOW_SIZE = ("1280", '1024')

class TestMainPage:
    def test_login_link_exist(self,driver):
        mp = MainPage(driver=driver)
        mp.open()
        assert mp.login_link_exists(), 'login link exist'

    def test_can_open_login_page_from_main_page(self,driver):
        mp = MainPage(driver)
        mp.open()
        mp.enter_or_register()
        assert 'account/login/' in mp.url, 'incorrect link'