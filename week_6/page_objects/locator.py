from selenium.webdriver.common.by import By

class locators:
    add_product = (By.CSS_SELECTOR,".product_price .btn")

    email = (By.ID,"id_registration-email")
    pwd1 = (By.ID,"id_registration-password1")
    pwd2 = (By.ID, "id_registration-password2")
    submit_user = (By.CSS_SELECTOR, "button[value='Register']")
    registration