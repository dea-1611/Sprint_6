import allure
import pytest
from data import user_1, user_2


class TestOrderForm:
    @allure.title('Оформление заказа через кнопку в шапке')
    @pytest.mark.parametrize('user_data', [user_1])
    def test_order_via_header_button(self, home_page, order_page, user_data):
        name, last_name, address, station, number, comment, date = user_data

        home_page.click_button_order_header()
        order_page.fill_personal_information(name, last_name, address, station, number)
        order_page.fill_rental_information(comment, date)

        assert order_page.is_order_completed()

    @allure.title('Оформление заказа через нижнюю кнопку')
    @pytest.mark.parametrize('user_data', [user_2])
    def test_order_via_body_button(self, home_page, order_page, user_data):
        name, last_name, address, station, number, comment, date = user_data

        home_page.scroll_to_button_order_body()
        home_page.click_button_order_body()
        order_page.fill_personal_information(name, last_name, address, station, number)
        order_page.fill_rental_information(comment, date)

        assert order_page.is_order_completed()
