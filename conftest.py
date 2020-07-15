def browser():
    print("\nstart browser for test..")
    global browser
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()
