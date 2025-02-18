from selenium.webdriver.common.by import By

class BasePageLocators:
    LOGO_YANDEX = (By.CSS_SELECTOR, '.Header_LogoYandex__3TSOI')
    LOGO_SCOOTER = (By.CSS_SELECTOR, '.Header_LogoScooter__3lsAR')
    BUTTON_ORDER = (By.XPATH, '//div[@class="Header_Nav__AGCXC"]//button[text()="Заказать"]')
