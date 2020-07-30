class LoginPage(BasePage):
    _page_path = '/accounts/login/'

    @allure.step('Register user')
    def register(self,email:str,pwd1: str,pwd2:str):
        self.find_element(LPl.email_field).send_keys(email)
        self.find_element(LPl.pwd1_field).send_keys(pwd1)
        self.find_element(LPl.pwd2_field).send_keys(pwd2)
        self.find_element(LPl.register_btn).click()
        self.wait_until_elind_element(LPl.register_btn)
