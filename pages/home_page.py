import allure
from selenium.common import TimeoutException, ElementClickInterceptedException

from locators.home_page_locators import HomePageLocators
from pages.base_page import BasePage


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Проверяем видимость заголовка главной страницы')
    def home_page_tittle_is_present(self):
        if self.find_visability_element(*HomePageLocators.HOME_PAGE_TITTLE):
            return True
        else:
            return False

    @allure.step('Скролим страницу до кнопки "Заказать" на главной странице')
    def scroll_to_order_button_on_home_page(self):
        self.scroll_to_element(*HomePageLocators.BUTTON_ORDER_ON_HOME_PAGE)

    @allure.step('Нажимаем на кнопку "Заказать" на главной странице')
    def click_on_the_order_button_on_home_page(self):
        self.find_visability_element(*HomePageLocators.BUTTON_ORDER_ON_HOME_PAGE).click()

    @allure.step('Получаем текст ответа в соответствии с номером вопроса')
    def get_answer_text_on_home_page(self, question_number):
        try:
            button_question_locator = getattr(HomePageLocators, f'BUTTON_QUESTION_{question_number}')
            label_answer_locator = getattr(HomePageLocators, f'LABEL_ANSWER_{question_number}')
            self.scroll_to_element(*button_question_locator)
            self.find_clickabile_element(*button_question_locator).click()
            return self.find_visability_element(*label_answer_locator).text

        except TimeoutException:
            print("TimeoutException: The element took too long to load or become clickable for "
                  f"question {question_number}.")
            return None
        except ElementClickInterceptedException:
            print("ElementClickInterceptedException: The question button is not clickable for question "
                  f"{question_number}. Something might be blocking it.")
            return None
        except Exception as e:
            print(f"An unexpected error occurred for question {question_number}: {str(e)}")
            return None
