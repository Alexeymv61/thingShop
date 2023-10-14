from base.base import Base


class Final_page(Base):
    """Класс где покупатель сверяет данные о товаре и завершает покупку"""
    # locators
    xpath_product_name = "//div[@class='inventory_item_name']"
    xpath_product_price = "//div[@class='inventory_item_price']"
    xpath_button_finish = "//button[@id='finish']"

    def check_name_price_and_click_finish(self, name, price):
        """Финальные проверки цены и завершение покупки, переход на страницу поздравлений и создание скриншота"""
        self.get_current_url()
        self.assert_words(self.get_element(self.xpath_product_name), name)
        self.assert_words(self.get_element(self.xpath_product_price), price)
        self.wait_and_click_element(self.xpath_button_finish)
        self.get_current_url()
        self.make_screenshoot()


