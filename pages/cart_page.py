from base.base import Base


class Cart_page(Base):
    """Класс где происходит переход в каталог аккумулторов и добавление найденного аккумулятора в корзину"""
    # locators
    xpath_button_continue = "//a[contains(@id, 'slbInvokeSubmit')]"
    xpath_button_checkout = "//button[@id='checkout']"
    xpath_cost_product = "//div[@class='inventory_item_price']"

    def get_cost_and_click_checkout(self, locator_price):
        """На странице "корзины" сверяем цену и кликаем на кнопку прожолжить оформление"""
        self.get_current_url()
        self.assert_words(self.get_element(self.xpath_cost_product), locator_price)
        self.wait_and_click_element(self.xpath_button_checkout)

