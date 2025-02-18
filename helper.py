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
    @allure.step('Производим сравнение actual_text: {actual_text} и expected_text: {expected_text}')
    def compare_act_and_exp_text(actual_text, expected_text):
        if actual_text.__eq__(expected_text):
            return True
        else:
            return False
