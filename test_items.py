# Liuba Kundas
"Homework-4 Languages"
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_guest_should_add_book(browser, language):
    link = f"http://selenium1py.pythonanywhere.com/{language}/catalogue/coders-at-work_207/"
    browser.get(link)
    browser.find_element_by_css_selector("#login_link")
    WebDriverWait(browser, 12).until(EC.element_to_be_clickable((By.ID, "add_to_basket_form")))
    browser.find_element_by_id("add_to_basket_form").click
    message = browser.find_element_by_id("messages")
    assert message == True, "add to basket"

