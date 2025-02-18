from locators.home_page_locators import HomePageLocators
from pages.base_page import BasePage


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def home_page_tittle_is_present(self):
        if self.find_visability_element(*HomePageLocators.HOME_PAGE_TITTLE):
            return True
        else:
            return False

    def scroll_to_order_button_on_home_page(self):
        self.scroll_to_element(*HomePageLocators.BUTTON_ORDER_ON_HOME_PAGE)

    def click_on_the_order_button_on_home_page(self):
        self.find_visability_element(*HomePageLocators.BUTTON_ORDER_ON_HOME_PAGE).click()
