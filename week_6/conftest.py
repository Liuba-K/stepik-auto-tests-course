import pytest
from faker import Faker
from selenium import webdriver
from constants
def browser():
    print("\nstart browser for test..")
    global browser
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()
