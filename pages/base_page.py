from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class BasePage:
    def __init__(self, driver, timeout = 5):
        self.driver = driver
        self.timeout = timeout

    def open(self, url):
        self.driver.get(url)

    def find_clickabile_element(self, how, what):
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

