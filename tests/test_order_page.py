import allure
import pytest
from locators.locators_order import TestLocatorsOrder
from data import user_1, user_2


class TestOrderForm:

    @allure.title('Проверка позитивного сценария оформления заказа через кнопку "Заказать" в шапке страницы')
    @allure.description('Проверка перехода в форму заказа через кнопку "Заказать" в шапке и успешного оформления заказа')
    @pytest.mark.parametrize('name, last_name, address, station, number, comment, date', [user_1])
    def test_order_form_completed_order_button_header(self, driver, home_page, order_page, name, last_name, address, station, number, comment, date):
        home_page.click_button_order_header()
        order_page.personal_information_input(name, last_name, address, station, number)
        order_page.rental_information_input(comment)
        order_page.click_yes_button_confirmation_pop_up()
        assert driver.find_element(*TestLocatorsOrder.locator_pop_up_order_completed).is_displayed()

    @allure.title('Проверка позитивного сценария оформления заказа через нижнюю кнопку "Заказать')
    @allure.description('Проверка перехода в форму заказа через нажатие кнопки "Заказать" в теле и успешного оформления заказа')
    @pytest.mark.parametrize('name, last_name, address, station, number, comment, date', [user_2])
    def test_order_form_completed_order_button_body(self, driver, home_page, order_page, name, last_name, address, station, number, comment, date):
        home_page.click_button_order_body()
        order_page.personal_information_input(name, last_name, address, station, number)
        order_page.rental_information_input(comment)
        order_page.click_yes_button_confirmation_pop_up()
        assert driver.find_element(*TestLocatorsOrder.locator_pop_up_order_completed).is_displayed()