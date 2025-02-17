from datetime import datetime


class Helper:
    @staticmethod
    def prepare_current_day():
        current_day = datetime.today().strftime("%d")
        if current_day[0] == '0':
            return str(int(current_day))
        else:
            return current_day
