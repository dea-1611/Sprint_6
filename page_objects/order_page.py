import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.locators_order import TestLocatorsOrder
from page_objects.base_page import BasePage


class OrderFormPage(BasePage):

    @allure.step('Заполнение поля "Имя"')
    def set_first_name(self, name):
        self.set_text_to_elm(TestLocatorsOrder.locator_field_first_name, name)
        return self

    @allure.step('Заполнение поля "Фамилия"')
    def set_last_name(self, last_name):
        self.set_text_to_elm(TestLocatorsOrder.locator_field_last_name, last_name)
        return self

    @allure.step('Проверка, что в поле "Имя" содержится значение')
    def check_first_name_value(self, expected_value):
        field = self.find_element_with_wait(TestLocatorsOrder.locator_field_first_name)
        assert field.get_attribute('value') == expected_value

    @allure.step('Заполнение поля "Адрес"')
    def set_address(self, address):
        self.set_text_to_elm(TestLocatorsOrder.locator_field_address, address)
        return self

    @allure.step('Заполнение поля "Метро"')
    def set_subway(self, station):
        self.click_element(TestLocatorsOrder.locator_field_subway_station)
        self.set_text_to_elm(TestLocatorsOrder.locator_field_subway_station, station)
        self.click_element(TestLocatorsOrder.locator_station_selected)
        return self

    def check_subway_value(self, station):
        field = self.find_element_with_wait(TestLocatorsOrder.locator_field_subway_station)
        expected_value = station
        assert field.get_attribute('value') == expected_value, "Значение в поле 'Метро' не совпадает с ожидаемым"

    @allure.step('Заполнение поля "Телефон"')
    def set_phone(self, number):
        self.set_text_to_elm(TestLocatorsOrder.locator_field_phone_number, number)
        return self

    @allure.step('Клик на кнопку "Далее"')
    def click_next_button(self):
        self.click_element(TestLocatorsOrder.locator_button_continue)

    @allure.step('Отображение заголовка второй формы')
    def check_the_title_of_second_form_displaying(self):
        self.check_element_displayed(TestLocatorsOrder.locator_form_title_rent)

    @allure.step('Заполнить поле "Дата аренды"')
    def set_rental_date(self):
        self.click_element(TestLocatorsOrder.locator_field_rental_date)
        self.find_element_with_wait(TestLocatorsOrder.locator_calendar)
        today = self.find_element_with_wait(TestLocatorsOrder.locator_today)
        tomorrow = today.find_element(*TestLocatorsOrder.locator_tomorrow)
        tomorrow.click()
        return self

    @allure.step('Заполнение поля "Срок аренды"')
    def set_rental_duration(self):
        self.click_element(TestLocatorsOrder. locator_field_rental_duration)
        self.find_element_with_wait(TestLocatorsOrder.locator_list_rental_duration)
        self.click_element(TestLocatorsOrder.locator_dropdown_rental_period)


    def set_color_field(self):
        self.click_element(TestLocatorsOrder.locator_checkbox_grey)
        return self

    def set_comment_field(self, comment):
        self.set_text_to_elm(TestLocatorsOrder.locator_field_comment, comment)
        return self

    @allure.step('Клик на кнопку "Заказать"')
    def click_button_order(self):
        self.click_element(TestLocatorsOrder.locator_button_order)
        self.find_element_with_wait(TestLocatorsOrder.locator_pop_up_order_confirmation)

    @allure.step('Отображение окна подтверждения после клика на кнопку Заказать')
    def check_displaying_of_confirm_window(self):
        self.check_element_displayed(TestLocatorsOrder.locator_pop_up_order_confirmation)

    @allure.step('Клик на кнопку "Да" в окне подтверждения заказа')
    def click_yes_button_confirmation_pop_up(self):
        self.click_element(TestLocatorsOrder.locator_button_yes_pop_up_order_confirmation)
        self.find_element_with_wait(TestLocatorsOrder.locator_pop_up_order_completed)
        return self


    @allure.step('Заполнение первой части формы и нажатие кнопки "Далее"')
    def personal_information_input(self, name, last_name, address, station, number):
        self.set_first_name(name)
        self.set_last_name(last_name)
        self.set_address(address)
        self.set_subway(station)
        self.check_subway_value(station)
        self.set_phone(number)
        self.click_next_button()
        self.check_the_title_of_second_form_displaying()

    @allure.step('Заполнение второй части формы и окно подтверждения')
    def rental_information_input(self, comment):
        self.set_rental_date()
        self.set_rental_duration()
        self.set_color_field()
        self.set_comment_field(comment)
        self.click_button_order()
        self.check_displaying_of_confirm_window()

    def fill_personal_information(self, name, last_name, address, station, number):
        pass

    def fill_rental_information(self, comment):
        pass

    def confirm_order(self):
        pass

    def is_order_completed_popup_visible(self):
        return self.driver.find_element(*TestLocatorsOrder.locator_pop_up_order_completed).is_displayed()
