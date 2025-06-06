import credentials
import allure

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from locators.base_page_locators import BasePageLocators


class BasePage:
    def __init__(self, driver, timeout=5):
        self.driver = driver
        self.timeout = timeout

    @allure.step('Открываем страницу: {url}')
    def open(self, url):
        self.driver.get(url)

    def find_clickable_element(self, how, what):
        try:
            web_element = WebDriverWait(self.driver, self.timeout).until(EC.element_to_be_clickable((how, what)))
            return web_element

        except TimeoutException:
            print(f"\nElement not clickable after {self.timeout} seconds")
            return None
        except Exception as e:
            print(f"\nAn error occurred while finding the clickable element: {e}")
            return None

    def find_visability_element(self, how, what):
        try:
            web_element = WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located((how, what)))
            return web_element

        except TimeoutException:
            print(f"\nElement not visability after {self.timeout} seconds")
            return None
        except Exception as e:
            print(f"\nAn error occurred while finding the visability element: {e}")
            return None

    def scroll_to_element(self, how, what):
        try:
            web_element = WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located((how, what)))
            return self.driver.execute_script('arguments[0].scrollIntoView();', web_element)

        except TimeoutException:
            print(f"\nElement not visability after {self.timeout} seconds")
            return None
        except Exception as e:
            print(f"\nAn unexpected error occurred while scrolling to the element: {e}")
            return None

    @allure.step('Нажимаем на кнопку "Заказать" в header')
    def click_on_the_order_button_in_header(self):
        return self.find_clickable_element(*BasePageLocators.BUTTON_ORDER).click()

    @allure.step('Нажимаем на логотип "Самокат" в header')
    def click_on_the_scooter_logo_in_header(self):
        return self.find_clickable_element(*BasePageLocators.LOGO_SCOOTER).click()

    @allure.step('Нажимаем на логотип "Яндекс" в header. Переходим в новое окно браузера')
    def click_on_the_yandex_logo_in_header_and_switch_window(self):
        try:
            self.find_clickable_element(*BasePageLocators.LOGO_YANDEX).click()
            all_tabs = self.driver.window_handles
            self.driver.switch_to.window(all_tabs[-1])
            return WebDriverWait(self.driver, timeout=20).until(EC.url_to_be(credentials.URLS.get('DZEN_URL')))

        except TimeoutException:
            print(f"Timeout: URL did not match {credentials.URLS.get('DZEN_URL')} after {self.timeout} seconds.")
            return None
        except Exception as e:
            print(f"An error occurred: {e}")
            return None
