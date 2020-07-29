from logging import getLogger
import pytest
from faker import Faker
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from test_main_page import IMPLICIT_WAIT,WINDOW_SIZE
logger = getLogger(__name__)

def pytest_addoption(parser):
    parser.adoption('--language',action='store',default="en-gb", help='Choose interface language')
    parser.adoption('--browser', action='store', default='chrome', help='Choose browser: chrome or firefox')

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

@pytest.fixture
def test_email(request):
    try:
        params = request.param
        if params == "free":
            return Faker().ascii_free_email()
        elif params == "company":
            return Faker().ascii_company_email()
        else:
            logger.warning(f"incorrect request param:{params}")
            return Faker().email()
    except AttributeError:
        return Faker().email()