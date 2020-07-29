import pytest
class TestProductPage:
    @pytest.mark.need_review_user_add
    def test_user_can_add_product_to_basket(self,driver,register):
        add_product_to_basket = self.driver.find_element("*add_product")
        add_product_to_basket.click
        message = browser.find_element_by_id("messages")
        assert "" in message.text

    @pytest.mark.need_review_guest_add
    def test_guest_can_add_product_to_basket(self,driver):
        add_product_to_basket = self.driver.find_element(*add_product)
        add_product_to_basket.click
        message = browser.find_element_by_id("messages")
        assert "" in message.text

    @pytest.mark.need_review_guest_see
    def test_guest_cant_see_product_in_basket_opened_from_product_page(self,driver):
        add_product_to_basket = self.driver.find_element(*add_product)
        add_product_to_basket.click


        message = browser.find_element_by_id("messages")
        assert "" in message.text

    @pytest.mark.need_review_guest_go
    def test_guest_can_go_to_login_page_from_product_page(self,driver):
        add_product_to_basket = self.driver.find_element(*add_product)
        add_product_to_basket.click
        message = browser.find_element_by_id("messages")
        assert "" in message.text