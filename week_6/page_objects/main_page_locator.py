from selenium.webdriver.common.by import By

class MainPageLocators:
    search_field = (By.ID, "id_q")
    search_button = (By.CSS_SELECTOR, 'input.btn')

    login_link = (By.ID, 'login_link')

    enter_email = (By.ID, 'id_login-username')
    enter_pwd = (By.ID, 'id_login-password')