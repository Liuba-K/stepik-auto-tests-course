class LoginPage(BasePage):
    _page_path = '/accounts/login/'

    @allure.step('Register user')
    def register(self,email:str,pwd1: str,pwd2:str):
        self.find_element(LPl.email_field).send_keys(email)
        ...