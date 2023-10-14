import time


from base.base import Base


class Order_data_page(Base):
    """Класс в котором указываются доп. данные заказа"""

    # локаторы
    xpath_popular = "//a[@id='ctl00_ctl00_b_b_repDeliveryList_ctl02_hlDelivName']"
    xpath_button_submit = "//input[@id='ctl00_ctl00_b_b_btnSubmit']"
    xpath_cart = "//a[@class='shop-functions__cart js-cartfull']"
    xpath_cart_delete_product = "//a[@id='slbDelete']"

    def complete_data_and_click_button(self):
        """complete_data_and_click_button - выбираем способ доставки товара, делаем скриин страницы и кликаем на кнопку"""
        self.get_current_url()
        self.wait_and_click_element(self.xpath_popular)
        print('способ доставки выбран - успешно')
        time.sleep(1)
        self.make_screenshoot('check_order_page')
        self.scroll_on_page(0, 500)
        time.sleep(1)
        self.make_screenshoot('check_order_button')
        #клик на кнопку сделать заказ закомментирован, так как сайт является боевым
        # self.wait_and_click_element(self.xpath_button_submit)
        # переход в корзину с товарами
        self.scroll_on_page(0, 0)
        self.wait_and_click_element(self.xpath_cart)
        # удаление товара
        self.wait_and_click_element(self.xpath_cart_delete_product)
