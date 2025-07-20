import allure
from locators.locators_order import TestLocatorsOrder
from page_objects.base_page import BasePage


class OrderFormPage(BasePage):
    @allure.step('Заполнение поля "Имя"')
    def set_first_name(self, name):
        self.set_text_to_elm(TestLocatorsOrder.locator_field_first_name, name)

    @allure.step('Заполнение поля "Фамилия"')
    def set_last_name(self, last_name):
        self.set_text_to_elm(TestLocatorsOrder.locator_field_last_name, last_name)

    @allure.step('Заполнение поля "Адрес"')
    def set_address(self, address):
        self.set_text_to_elm(TestLocatorsOrder.locator_field_address, address)

    @allure.step('Выбор станции метро')
    def set_subway(self, station):
        self.click_element(TestLocatorsOrder.locator_field_subway_station)
        self.set_text_to_elm(TestLocatorsOrder.locator_field_subway_station, station)
        self.click_element(TestLocatorsOrder.locator_station_selected)

    @allure.step('Заполнение поля "Телефон"')
    def set_phone(self, number):
        self.set_text_to_elm(TestLocatorsOrder.locator_field_phone_number, number)

    @allure.step('Нажатие кнопки "Далее"')
    def click_next_button(self):
        self.click_element(TestLocatorsOrder.locator_button_continue)

    @allure.step('Установка даты доставки: {date}')
    def set_rental_date(self, date):
        date_field = self.find_element_with_wait(TestLocatorsOrder.locator_field_rental_date)
        date_field.click()
        date_field.clear()
        date_field.send_keys(date)
        self.click_element(TestLocatorsOrder.locator_form_title_rent)

    @allure.step('Выбор срока аренды')
    def set_rental_duration(self):
        self.scroll_to_element(TestLocatorsOrder.locator_field_rental_duration)
        self.click_element(TestLocatorsOrder.locator_field_rental_duration)
        self.click_element(TestLocatorsOrder.locator_dropdown_rental_period)

    @allure.step('Выбор цвета самоката')
    def set_color_field(self):
        self.click_element(TestLocatorsOrder.locator_checkbox_grey)

    @allure.step('Заполнение комментария')
    def set_comment_field(self, comment):
        self.set_text_to_elm(TestLocatorsOrder.locator_field_comment, comment)

    @allure.step('Подтверждение заказа')
    def confirm_order(self):
        self.click_element(TestLocatorsOrder.locator_button_order)
        self.click_element(TestLocatorsOrder.locator_button_yes_pop_up_order_confirmation)

    @allure.step('Заполнение персональных данных')
    def fill_personal_information(self, name, last_name, address, station, number):
        self.set_first_name(name)
        self.set_last_name(last_name)
        self.set_address(address)
        self.set_subway(station)
        self.set_phone(number)
        self.click_next_button()

    @allure.step('Заполнение данных аренды')
    def fill_rental_information(self, comment, date):
        self.set_rental_date(date)
        self.set_rental_duration()
        self.set_color_field()
        self.set_comment_field(comment)
        self.confirm_order()

    @allure.step('Проверка успешного оформления заказа')
    def is_order_completed(self):
        return self.check_element_displayed(TestLocatorsOrder.locator_pop_up_order_completed)
