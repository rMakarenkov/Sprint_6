import time

import credentials

from pages.order_page import OrderPage
from pages.home_page import HomePage


class TestOrderPage:

    def test_create_order_through_button_in_header_and_transition_home_page_successfully_operations(self, driver):
        order_page = OrderPage(driver)
        order_page.open(credentials.URLS.get('HOME_URL'))
        order_page.click_on_the_order_button_in_header()
        actual_order_message = order_page.create_order(*credentials.ORDER_ITEMS_CASE_1)

        assert 'Заказ оформлен' in actual_order_message

        order_page.go_to_order_detail()
        order_page.click_on_the_scooter_logo_in_header()
        home_page = HomePage(driver)

        assert home_page.home_page_tittle_is_present()

    def test_create_order_through_button_on_main_page_and_transition_dzen_page_successfully_operations(self, driver):
        home_page = HomePage(driver)
        home_page.open(credentials.URLS.get('HOME_URL'))
        home_page.scroll_to_order_button_on_home_page()
        home_page.click_on_the_order_button_on_home_page()
        order_page = OrderPage(driver)
        actual_order_message = order_page.create_order(*credentials.ORDER_ITEMS_CASE_2)

        assert 'Заказ оформлен' in actual_order_message

        order_page.go_to_order_detail()
        order_page.click_on_the_yandex_logo_in_header_and_switch_window()

        assert order_page.driver.current_url == credentials.URLS.get('DZEN_URL')
