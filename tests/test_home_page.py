import allure
import pytest
from locators.locators_home_page import TestLocatorsHomePage
from data import expected_texts, dzen_url, base_url


class TestHomePageScooter:

    @allure.title('Проверка раздела "Вопросы о важном"')
    @allure.description('Проверка появления соответствующего текста ответа при нажатии на каждый вопрос')
    @pytest.mark.parametrize('question_locator, answer_locator, expected_text', [
        (TestLocatorsHomePage.locator_button_question_FAQ_1, TestLocatorsHomePage.locator_answer_FAQ_1, expected_texts['faq1']),
        (TestLocatorsHomePage.locator_button_question_FAQ_2, TestLocatorsHomePage.locator_answer_FAQ_2, expected_texts['faq2']),
        (TestLocatorsHomePage.locator_button_question_FAQ_3, TestLocatorsHomePage.locator_answer_FAQ_3, expected_texts['faq3']),
        (TestLocatorsHomePage.locator_button_question_FAQ_4, TestLocatorsHomePage.locator_answer_FAQ_4, expected_texts['faq4']),
        (TestLocatorsHomePage.locator_button_question_FAQ_5, TestLocatorsHomePage.locator_answer_FAQ_5, expected_texts['faq5']),
        (TestLocatorsHomePage.locator_button_question_FAQ_6, TestLocatorsHomePage.locator_answer_FAQ_6, expected_texts['faq6']),
        (TestLocatorsHomePage.locator_button_question_FAQ_7, TestLocatorsHomePage.locator_answer_FAQ_7, expected_texts['faq7']),
        (TestLocatorsHomePage.locator_button_question_FAQ_8, TestLocatorsHomePage.locator_answer_FAQ_8, expected_texts['faq8'])

    ])
    def test_click_question_shows_answer_faq(self, driver, home_page, question_locator, answer_locator, expected_text):
        home_page.scroll_to_faq()
        home_page.click_question(question_locator)
        answer = home_page.get_answer_text(answer_locator)
        assert answer == expected_text

    @allure.title('Клик на логотип "Яндекс"')
    @allure.description('Открытие страницы Яндекс.Дзен в новой вкладке при нажатии на логотип "Яндекс"')
    def test_click_logo_yandex_opens_dzen_page(self, driver, home_page):
        home_page.click_logo_yandex_open_dzen_page()
        assert driver.current_url == dzen_url

    @allure.title('Клик на логотип "Самокат"')
    @allure.description('Переход на главную страницу при клике на логотип "Самокат"')
    def test_click_logo_scooter_opens_home_page(self, driver, home_page):
        home_page.click_button_order_header()
        home_page.click_logo_scooter_open_home_page()
        assert driver.current_url == base_url