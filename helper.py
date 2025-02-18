import allure
from datetime import datetime


class Helper:

    @staticmethod
    @allure.step('Получаем значение текущего дня месяца')
    def prepare_current_day():
        current_day = datetime.today().strftime("%d")
        if current_day[0] == '0':
            return str(int(current_day))
        else:
            return current_day

    @staticmethod
    @allure.step('Производим сравнение actual_answer: {actual_answer} и expected_answer: {expected_answer}')
    def compare_act_and_exp_answers(actual_answer, expected_answer):
        if actual_answer.__eq__(expected_answer):
            return True
        else:
            return False
