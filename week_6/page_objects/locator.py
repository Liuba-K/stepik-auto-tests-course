from selenium.webdriver.common.by import By

class locators:
    add_product = (By.CSS_SELECTOR,".product_price .btn")

    registration-email = (By.ID,"id_registration-email")
    password1 = (By.ID,"id_registration-password1")
    password_repeat = (By.ID, "id_registration-password2")
    submit_user = (By.CSS_SELECTOR, "button[value='Register']")
    registration