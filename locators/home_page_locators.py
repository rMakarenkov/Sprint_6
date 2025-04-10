from selenium.webdriver.common.by import By


class HomePageLocators:
    HOME_PAGE_TITTLE = (By.CSS_SELECTOR, '.Home_Header__iJKdX')
    BUTTON_ORDER_ON_HOME_PAGE = (By.CSS_SELECTOR, '.Button_Button__ra12g.Button_Middle__1CSJM')

    BUTTON_QUESTION_0 = (By.ID, 'accordion__heading-0')
    LABEL_ANSWER_0 = (By.XPATH, '//div[@aria-labelledby="accordion__heading-0"]')
    BUTTON_QUESTION_1 = (By.ID, 'accordion__heading-1')
    LABEL_ANSWER_1 = (By.XPATH, '//div[@aria-labelledby="accordion__heading-1"]')
    BUTTON_QUESTION_2 = (By.ID, 'accordion__heading-2')
    LABEL_ANSWER_2 = (By.XPATH, '//div[@aria-labelledby="accordion__heading-2"]')
    BUTTON_QUESTION_3 = (By.ID, 'accordion__heading-3')
    LABEL_ANSWER_3 = (By.XPATH, '//div[@aria-labelledby="accordion__heading-3"]')
    BUTTON_QUESTION_4 = (By.ID, 'accordion__heading-4')
    LABEL_ANSWER_4 = (By.XPATH, '//div[@aria-labelledby="accordion__heading-4"]')
    BUTTON_QUESTION_5 = (By.ID, 'accordion__heading-5')
    LABEL_ANSWER_5 = (By.XPATH, '//div[@aria-labelledby="accordion__heading-5"]')
    BUTTON_QUESTION_6 = (By.ID, 'accordion__heading-6')
    LABEL_ANSWER_6 = (By.XPATH, '//div[@aria-labelledby="accordion__heading-6"]')
    BUTTON_QUESTION_7 = (By.ID, 'accordion__heading-7')
    LABEL_ANSWER_7 = (By.XPATH, '//div[@aria-labelledby="accordion__heading-7"]')
