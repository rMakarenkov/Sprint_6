from datetime import datetime


class Helper:
    @staticmethod
    def receive_current_day():
        current_day = datetime.today().strftime("%d.%m.%Y")[0:2]


