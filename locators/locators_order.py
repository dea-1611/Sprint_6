from selenium.webdriver.common.by import By

class TestLocatorsOrder:
    # Экран "Для кого самокат"
    # Поле Имя
    locator_field_first_name = By.XPATH, "//input[@placeholder='* Имя']"
    # Поле Фамилия
    locator_field_last_name = By.XPATH, "//input[@placeholder='* Фамилия']"
    # Поле Адрес
    locator_field_address = By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']"
    # Поле Станция метро
    locator_field_subway_station = By.XPATH, "//input[@placeholder='* Станция метро']"
    # Список станций метро
    locator_field_subway_station_list = By.CLASS_NAME, 'select-search__select'
    # Выбранная станция метро
    locator_station_selected = (By.XPATH, ".//li[@class='select-search__row']")
    # Поле Телефон
    locator_field_phone_number = By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']"
    # Кнопка Далее
    locator_button_continue = By.XPATH, '//button[text()="Далее"]'
    # Экран "Про аренду"
    # Заголовок формы Про аренду
    locator_form_title_rent = By.CLASS_NAME, 'Order_Header__BZXOb'
    # Поле Когда привезти самокат
    locator_field_rental_date = By.CSS_SELECTOR, 'input[placeholder="* Когда привезти самокат"]'
   # Календарь
    locator_calendar = By.XPATH, "//div[@class='react-datepicker-popper']"
    # Поле "Срок аренды"
    locator_field_rental_duration = By.CLASS_NAME, 'Dropdown-placeholder'
    # Выбор даты в календаре
    locator_calendar_date = (By.XPATH, "//div[@class='react-datepicker__day' and not(contains(@class, 'disabled'))]")
    # Выпадающий список с количеством дней аренды
    locator_list_rental_duration = By.CLASS_NAME, 'Dropdown-menu'
    # Трое суток
    locator_dropdown_rental_period = (By.XPATH, ".//div[@class = 'Dropdown-menu']/div[text() ='трое суток']")
    # Поле Срок аренды после выбора срока
    locator_rental_duration_after_input = By.CLASS_NAME, 'Dropdown-placeholder is-selected'
    # Поле выбора цвета
    locator_field_colour = By.XPATH, '//div[text()="Цвет самоката"]'
    # Цвет серый
    locator_checkbox_grey = By.ID, 'grey'
    # Поле "Комментарий"
    locator_field_comment = By.XPATH, '//input[@placeholder="Комментарий для курьера"]'
    # Кнопка "Заказать"
    locator_button_order = By.XPATH, '//button[@class="Button_Button__ra12g Button_Middle__1CSJM" and text()="Заказать"]'
    # Окно "Хотите оформить заказ?"
    locator_pop_up_order_confirmation = By.CLASS_NAME, 'Order_ModalHeader__3FDaJ'
    # Кнопка Да в окне Хотите оформить заказ?
    locator_button_yes_pop_up_order_confirmation = By.XPATH, '//button[text()="Да"]'
    # Окно "Заказ оформлен"
    locator_pop_up_order_completed = By.CLASS_NAME, 'Order_ModalHeader__3FDaJ'