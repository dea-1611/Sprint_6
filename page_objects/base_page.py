from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import allure


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Поиск элемента')
    def find_element_with_wait(self, locator):
        WebDriverWait(self.driver, 8).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step('Скролл до элемента')
    def scroll_to_element(self, locator):
        element = self.find_element_with_wait(locator)
        self.driver.execute_script('arguments[0].scrollIntoView();', element)

    def wait_url_to_be(self, url):
        return WebDriverWait(self.driver, 8).until((expected_conditions.url_to_be(url)))

    @allure.step('Клик на элемент')
    def click_element(self, locator):
        element = self.find_element_with_wait(locator)
        element.click()

    @allure.step('Ввод значения в поле')
    def set_text_to_elm(self, locator, text):
        element = self.find_element_with_wait(locator)
        element.send_keys(text)

    @allure.step('Получение текста на элементе')
    def get_text_on_element(self, locator):
        element = self.find_element_with_wait(locator)
        return element.text

    @allure.step('Переход на другую вкладку')
    def browse_to_next_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

    @allure.step('Проверка отображения элемента')
    def check_element_displayed(self, locator):
        return self.find_element_with_wait(locator).is_displayed()