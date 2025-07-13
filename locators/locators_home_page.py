from selenium.webdriver.common.by import By


class TestLocatorsHomePage:

    # Кнопка "Заказать" в шапке
    locator_button_order_header = By.CLASS_NAME, 'Button_Button__ra12g'
    # Кнопка "Заказать" в теле страницы
    locator_button_order_body = By.CLASS_NAME, 'Button_Middle__1CSJM'
    # Раздел "Как это работает"
    locator_block_how_it_works = By.XPATH, '//div[text()="Как это работает"]'
    # Кнопка "Принять куки"
    locator_button_cookie = By.ID, 'rcc-confirm-button'
    # Вопросы о важном
    # Первый вопрос
    locator_button_question_FAQ_1 = By.ID, 'accordion__heading-0'
    # Первый ответ
    locator_answer_FAQ_1 = By.CSS_SELECTOR, 'div[aria-labelledby="accordion__heading-0"]:not([hidden]) p'
    # Второй вопрос
    locator_button_question_FAQ_2 = By.ID, 'accordion__heading-1'
    # Второй ответ
    locator_answer_FAQ_2 = By.CSS_SELECTOR, 'div[aria-labelledby="accordion__heading-1"]:not([hidden]) p'
    # Третий вопрос
    locator_button_question_FAQ_3 = By.ID, 'accordion__heading-2'
    # Третий ответ
    locator_answer_FAQ_3 = By.CSS_SELECTOR, 'div[aria-labelledby="accordion__heading-2"]:not([hidden]) p'
    # Четвертый вопрос
    locator_button_question_FAQ_4 = By.ID, 'accordion__heading-3'
    # Четвертый ответ
    locator_answer_FAQ_4 = By.CSS_SELECTOR, 'div[aria-labelledby="accordion__heading-3"]:not([hidden]) p'
    # Пятый вопрос
    locator_button_question_FAQ_5 = By.ID, 'accordion__heading-4'
    # Пятый ответ
    locator_answer_FAQ_5 = By.CSS_SELECTOR, 'div[aria-labelledby="accordion__heading-4"]:not([hidden]) p'
    # Шестой вопрос
    locator_button_question_FAQ_6 = By.ID, 'accordion__heading-5'
    # Шестой ответ
    locator_answer_FAQ_6 = By.CSS_SELECTOR, 'div[aria-labelledby="accordion__heading-5"]:not([hidden]) p'
    # Седьмой вопрос
    locator_button_question_FAQ_7 = By.ID, 'accordion__heading-6'
    # Седьмой ответ
    locator_answer_FAQ_7 = By.CSS_SELECTOR, 'div[aria-labelledby="accordion__heading-6"]:not([hidden]) p'
    # Восьмой вопрос
    locator_button_question_FAQ_8 = By.ID, 'accordion__heading-7'
    # Восьмой ответ
    locator_answer_FAQ_8 = By.CSS_SELECTOR, 'div[aria-labelledby="accordion__heading-7"]:not([hidden]) p'
    # Логотип Яндекс
    locator_button_logo_yandex = By.CLASS_NAME, "Header_LogoYandex__3TSOI"
    # Логотип Самокат
    locator_button_logo_scooter = By.CLASS_NAME, "Header_LogoScooter__3lsAR"