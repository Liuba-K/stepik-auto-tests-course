import pytest
from page_objects.main_page import MainPage

class TestProductPage:
    @pytest.mark.need_review_user_add
    def test_user_can_add_product_to_basket(self,driver):
        mp = MainPage(driver=driver)
        mp.open()
        mp.enter_or_register()
        self.find_element(PPL.add_product).click
        assert is_element_present((By.ID,'messages')), 'product in basket'

    @pytest.mark.need_review_guest_add
    def test_guest_can_add_product_to_basket(self,driver):
        mp = MainPage(driver=driver)
        mp.open()
        mp.search()
        self.find_element(PPL.add_product).click
        assert is_element_present((By.ID,'messages')), 'product in basket'

    @pytest.mark.need_review_guest_see
    def test_guest_cant_see_product_in_basket_opened_from_product_page(self,driver):
        mp = MainPage(driver=driver)
        mp.open()
        self.find_element(PPL.add_product).click


        assert is_element_present((By.ID,'messages')), 'product in basket'

    @pytest.mark.need_review_guest_go
    def test_guest_can_go_to_login_page_from_product_page(self,driver):
        mp = MainPage(driver=driver)
        mp.open()

        self.find_element(PPL.add_product).click
        mp.enter_user()
        assert is_element_present((By.ID,'messages')), "Succes enter"