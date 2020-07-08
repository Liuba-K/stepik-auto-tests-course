" обработчик, который считывает из командной строки параметр language."
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_experimental_option('prefs', {'intl.accept_languages': ["ru", "en-gb","ar","ca","cs","da","de","el","es","fi","fr","it","ko","nl" "pl","pt","pt-br","ro","sk","uk","zh-hans"]})
browser = webdriver.Chrome(options=options)

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('language', ["ru", "en-gb","ar","ca","cs","da","de","el","es","fi","fr","it","ko","nl" "pl","pt","pt-br","ro","sk","uk","zh-hans"])
def test_guest_should_see_login_link(browser, language):
    link = f"http://selenium1py.pythonanywhere.com/{language}/catalogue/coders-at-work_207/"
    browser.get(link)
    browser.find_element_by_css_selector("#login_link")