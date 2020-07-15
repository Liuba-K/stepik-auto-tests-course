from selenium.webdriver.common.by import By
link= "http://selenium1py.pythonanywhere.com"

class locators:
    login_link = (By.ID,"login_link")
    registration-email = (By.ID,"id_registration-email")
    password1 = (By.ID,"id_registration-password1")
    password_repeat = (By.ID, "id_registration-password2")
    submit_user = (By.CSS_SELECTOR, "button[value='Register']")
    registration

class LoginPage(BasePage):
    def go_to_login_page(self):
        login_link = self.browser.find_element(*login_link)
        login_link.click()

    def fill_email_registration_field(self):
        email = self.browser.find_element(*registration)
        email.send_keys("aaa@bbb.xxx")

    def fill_password_registration(self):
        field = self.browser.find_element(*password1)
        field.send_keys("ххххххччч")

    def fill_confirmation_registration(self):
        field_repeat = self.browser.find_element(*password_repeat)
        field_repeat.send_keys("ххххххччч")

    def submit_user(self):
        button = self.browser.find_element(*submit_user)
        button.click()

    def should_be_success_confirmation(self):
        success_message = self.browser.find_element(*registration)

        assert "Thanks for registering!" in success_message

class TestMakeReport:
    def test_registration_user(self,browser,link):
        page = MainPage(browser,link)
        page.open()
        login_page = page.go_to_login_page()
        login_page.fill_email_registration_field()
        login_page.fill_password_registration_field()
        login_page.fill_password_confirmation_field()
        user_page = UserPage(browser, browser.current_url)
        user_page.should_be_success_confirmation()

