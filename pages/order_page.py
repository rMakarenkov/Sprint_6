
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


class OrderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def set_name(self, name):
        self.find_clickabile_element(*OrderPageLocators.INPUT_NAME).send_keys(name)

    def set_surname(self, surname):
        self.find_clickabile_element(*OrderPageLocators.INPUT_SURNAME).send_keys(surname)

    def set_address(self, address):
        self.find_clickabile_element(*OrderPageLocators.INPUT_ADDRESS).send_keys(address)

    def set_metro_station(self):
        self.find_clickabile_element(*OrderPageLocators.INPUT_METRO_STATION).click()
        self.find_visability_element(*OrderPageLocators.HIDDEN_LIST_METRO_STATION)
        self.find_clickabile_element(*OrderPageLocators.LABEL_METRO_STATION_BEL).click()

    def set_telephone_number(self, telephone_number):
        self.find_clickabile_element(*OrderPageLocators.INPUT_TELEPHONE).send_keys(telephone_number)

    def go_to_second_step_placing_order(self):
        self.find_clickabile_element(*OrderPageLocators.BUTTON_NEXT_STEP).click()

    def set_date_order(self):
        self.find_clickabile_element(*OrderPageLocators.INPUT_WHEN_DATE).click()
        self.find_visability_element(*OrderPageLocators.DATA_PICKER)
        self.find_clickabile_element(*OrderPageLocators.CURRENT_DATE).click()

    def set_rental_period(self, rental_period):
        self.find_clickabile_element(*OrderPageLocators.INPUT_RENTAL_PERIOD).click()
        match rental_period:
            case 1:
                self.find_clickabile_element(*OrderPageLocators.LABEL_RENTAL_PERIOD_DAY).click()
            case 7:
                self.find_clickabile_element(*OrderPageLocators.LABEL_RENTAL_PERIOD_MAX_DAYS).click()

    def set_color_scooter(self, color):
        match color:
            case 'black':
                self.find_clickabile_element(*OrderPageLocators.CHECKBOX_BLACK_SCOOTER).click()
            case 'grey':
                self.find_clickabile_element(*OrderPageLocators.CHECKBOX_GREY_SCOOTER).click()

    def set_comment_by_courier(self, comment_by_courier):
        self.find_clickabile_element(*OrderPageLocators.INPUT_COMMENT_BY_COURIER).send_keys(comment_by_courier)

    def go_to_third_step_placing_order(self):
        self.find_clickabile_element(*OrderPageLocators.BUTTON_ORDER).click()

    def order_confirmation(self):
        self.find_clickabile_element(*OrderPageLocators.BUTTON_YES).click()

    def go_to_order_detail(self):
        self.find_clickabile_element(*OrderPageLocators.BUTTON_CHECK_DETAIL).click()

    def create_order(self, name, surname, address, telephone_number, rental_period, color, comment_by_courier):
        self.set_name(name)
        self.set_surname(surname)
        self.set_address(address)
        self.set_metro_station()
        self.set_telephone_number(telephone_number)
        self.go_to_second_step_placing_order()
        self.set_date_order()
        self.set_rental_period(rental_period)
        self.set_color_scooter(color)
        self.set_comment_by_courier(comment_by_courier)
        self.go_to_third_step_placing_order()
        self.order_confirmation()
        return self.find_visability_element(*OrderPageLocators.LABEL_SUCCESS_ORDER).text
