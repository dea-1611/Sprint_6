import allure
import pytest
from locators.locators_order import TestLocatorsOrder
from data import user_1, user_2


class TestOrderForm:

    @allure.title('Проверка позитивного сценария оформления заказа через кнопку "Заказать" в шапке страницы')
    @allure.description(
        'Проверка перехода в форму заказа через кнопку "Заказать" в шапке и успешного оформления заказа')
    @pytest.mark.parametrize('name, last_name, address, station, number, comment, date', [user_1])
    def test_order_form_completed_order_button_header(
            self,
            home_page,
            order_page,
            name,
            last_name,
            address,
            station,
            number,
            comment,
            date
    ):
        home_page.click_header_order_button()
        order_page.fill_personal_info(name, last_name, address, station, number)
        order_page.fill_rental_info(comment)
        order_page.confirm_order()

        assert order_page.is_order_confirmed()

    @allure.title('Проверка позитивного сценария оформления заказа через нижнюю кнопку "Заказать"')
    @allure.description(
        'Проверка перехода в форму заказа через нажатие кнопки "Заказать" в теле и успешного оформления заказа')
    @pytest.mark.parametrize('name, last_name, address, station, number, comment, date', [user_2])
    def test_order_form_completed_order_button_body(self, home_page, order_page, name, last_name, address, station,
                                                    number, comment, date):
        home_page.click_order_button_in_body()
        order_page.fill_personal_information(
            name=name,
            last_name=last_name,
            address=address,
            station=station,
            number=number
        )
        order_page.fill_rental_information(comment=comment)
        order_page.confirm_order()
        assert order_page.is_order_completed_popup_visible()
