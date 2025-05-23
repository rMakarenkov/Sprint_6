import credentials
import pytest
import allure

from pages.home_page import HomePage
from helper import Helper


@pytest.mark.home_page
class TestHomePage:
    @pytest.mark.parametrize('number', [0, 1, 2, 3, 4, 5, 6, 7])
    @allure.title('"Вопросы о важном": проверка отображения соответствующего текста в зависимости от выбранного вопроса')
    def test_checking_functionality_questions_about_important_successfully_operaions(self, driver, number):
        home_page = HomePage(driver)
        home_page.open(credentials.URLS.get('HOME_URL'))
        actual_text = home_page.get_answer_text_on_home_page(number)
        expected_text = credentials.EXPECTED_ANSWERS.get(number)

        assert Helper.compare_act_and_exp_text(actual_text, expected_text), 'Actual answer not match expected answer'
