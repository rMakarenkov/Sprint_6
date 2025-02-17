from selenium.webdriver.common.by import By

class OrderPageLocators:
    # first step
    LABEL_FROM_WHOM_SCOOTER = (By.XPATH, '//div[text()="Для кого самокат"]')
    INPUT_NAME = (By.XPATH, '//input[@placeholder="* Имя"]')
    INPUT_SURNAME = (By.XPATH, '//input[@placeholder="* Фамилия"]')
    INPUT_ADDRESS = (By.XPATH, '//input[@placeholder="* Адрес: куда привезти заказ"]')
    INPUT_METRO_STATION = (By.CSS_SELECTOR, '.select-search__input')
    HIDDEN_LIST_METRO_STATION = (By.CSS_SELECTOR, '.select-search__select')
    LABEL_METRO_STATION_BEL = (By.XPATH, '//button[@value="29"]')
    INPUT_TELEPHONE = (By.XPATH, '//input[@placeholder="* Телефон: на него позвонит курьер"]')
    BUTTON_NEXT_STEP = (By.XPATH, '//button[text()="Далее"]')
    # second step
    INPUT_WHEN_DATE = (By.XPATH, '//input[@placeholder="* Когда привезти самокат"]')
    DATA_PICKER = (By.CSS_SELECTOR, '.react-datepicker__month-container')
    CURRENT_DATE = (By.XPATH, '//div[text()="18"]')
    INPUT_RENTAL_PERIOD = (By.XPATH, '//div[text()="* Срок аренды"]')
    LABEL_RENTAL_PERIOD_DAY = (By.XPATH, '//div[text()="сутки"]')
    CHECKBOX_BLACK_SCOOTER = (By.XPATH, '//input[@id="black"]')
    INPUT_COMMENT_BY_COURIER = (By.XPATH, '//input[@placeholder="Комментарий для курьера"]')
    BUTTON_ORDER = (By.XPATH, '//button[text()="Заказать" and @class="Button_Button__ra12g Button_Middle__1CSJM"]')
    # third step
    LABEL_WANT_PLACE_ORDER =  (By.XPATH, '//div[text()="Хотите оформить заказ?"]')
    BUTTON_YES = (By.XPATH, '//button[text()="Да"]')
    # modal window
    LABEL_SUCCESS_ORDER = (By.XPATH, '//div[text()="Заказ оформлен"]')
