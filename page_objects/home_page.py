import allure
from locators.locators_home_page import TestLocatorsHomePage
from page_objects.base_page import BasePage
from data import dzen_url


class HomePageScooter(BasePage):

    @allure.step('Клик на кнопку "Заказать" в шапке')
    def click_button_order_header(self):
        self.find_element_with_wait(TestLocatorsHomePage.locator_button_order_header)
        self.click_element(TestLocatorsHomePage.locator_button_order_header)

    @allure.step('Скролл до кнопки "Заказать" в теле страницы')
    def scroll_to_button_order_body(self):
        self.scroll_to_element(TestLocatorsHomePage.locator_block_how_it_works)
        self.find_element_with_wait(TestLocatorsHomePage.locator_button_order_body)

    @allure.step('Клик на кнопку "Заказать" в теле страницы')
    def click_button_order_body(self):
        self.click_element(TestLocatorsHomePage.locator_button_order_body)

    @allure.step('Закрытие окна cookie')
    def close_cookie(self):
        self.find_element_with_wait(TestLocatorsHomePage.locator_button_cookie)
        self.click_element(TestLocatorsHomePage.locator_button_cookie)

    @allure.step('Скролл до блока "Вопросы о важном"')
    def scroll_to_faq(self):
        self.scroll_to_element(TestLocatorsHomePage.locator_button_question_FAQ_8)
        self.find_element_with_wait(TestLocatorsHomePage.locator_button_question_FAQ_8)

    @allure.step('Клик на вопрос')
    def click_question(self, locator_question):
        self.find_element_with_wait(locator_question)
        self.click_element(locator_question)

    @allure.step('Вывод ответа')
    def get_answer_text(self, answer_locator):
        self.find_element_with_wait(answer_locator)
        answer = self.get_text_on_element(answer_locator)
        return answer

    @allure.step('Клик на логотип "Яндекс"')
    def click_logo_yandex_open_dzen_page(self):
        self.find_element_with_wait(TestLocatorsHomePage.locator_button_logo_yandex)
        self.click_element(TestLocatorsHomePage.locator_button_logo_yandex)
        self.browse_to_next_tab()
        self.wait_url_to_be(dzen_url)

    @allure.step('Клик на логотип "Самокат"')
    def click_logo_scooter_open_home_page(self):
        self.find_element_with_wait(TestLocatorsHomePage.locator_button_logo_scooter)
        self.click_element(TestLocatorsHomePage.locator_button_logo_scooter)