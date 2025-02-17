from pages.order_page import OrderPage


def test_one(driver):
    order_page = OrderPage(driver)
    order_page.open('https://qa-scooter.praktikum-services.ru/order')
    success_order_message = order_page.create_order('Роман', 'Макаренков', 'Смоленск', '89001112233', 'Ожидаю')
    assert 'Заказ оформлен' in success_order_message
