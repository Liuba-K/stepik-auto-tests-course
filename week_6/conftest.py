from logging import getLogger
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from test_main_page import IMPLICIT_WAIT,WINDOW_SIZE
logger = getLogger(__name__)

def pytest_addoption(language):
    language.adoption('--language',action='store',default=None, help='Choose interface language')
    language.adoption('--browser', action='store', default='chrome', help='Choose browser')

@pytest.fixture
def driver(request):
    browser = request.config.getoption("browser")
    user_language = request.config.getoption("language")
    if browser.lower() == "chrome":
        options = Options()
        options.add_experimental_option('prefs',{'intl.accept_languages':user_language})
        driver = webdriver.Chrome(options=options)
    elif browser.lower() == "firefox":
        driver = webdriver.Firefox()
    else:
        raise pytest.UsageError("--browser_should be chrome or firefox")

    driver.implicitly_wait(IMPLICIT_WAIT)
    driver.set_window_size(*WINDOW_SIZE)
    yield driver
    driver.quit()
@pytest.mark.parametrize('language', ["ru", "en-gb","ar","ca","cs","da","de","el","es","fi","fr","it","ko","nl" "pl","pt","pt-br","ro","sk","uk","zh-hans"])
def test_guest_should_see_login_link(browser, language):
    link = f"http://selenium1py.pythonanywhere.com/{language}/catalogue/coders-at-work_207/"
    browser.get(link)
    browser.find_element_by_css_selector("#login_link")
def browser():
    print("\nstart browser for test..")
    global browser
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()
