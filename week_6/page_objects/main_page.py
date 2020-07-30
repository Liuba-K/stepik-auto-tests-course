class MainPage(BasePage):
    @allure.step('Search product')
    def search(self,text_to_search: str):
        self.find_element(MPl.search_field).send_keys(text_to_search)
        self.find_element(MPl.search_button).click()

    def enter_or_register(self):
        self.find_element(MPl.login_link).click()

    def enter_user(self):
        self.find_element(MPl.login_link).click()
        self.find_element(MPl.enter_email).send_keys("aaa@bbb.xxx")
        self.find_element(MPl.enter_pwd).send_keys("ххххххччч")

    def login_link_exists(self)->bool:
        return self.is_element_present(MPl.login_link)