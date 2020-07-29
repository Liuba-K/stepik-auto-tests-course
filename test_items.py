# Liuba Kundas
"Homework-4 Languages"
from selenium import webdriver
from conftest import lang
link = "http://selenium1py.pythonanywhere.com/{lang}/catalogue/coders-at-work_207/"

def test_languages():
    browser = webdriver.Chrome()
    try:
        browser.get(link)
        browser.get(link.format(lang=lang))
        browser.find_element_by_class_name("test_languages").click
        message = browser.find_element(*lang.messages).text.strip()
        assert message == lang[lang], "add to basket"
    finally:
        browser.guit()

if __name__ == "__main__":
    for key in lang.keys():
        test_languages(key)


#lang = {
  #'ru':'добавлен'
  #'en-gb':'added'}