from base.base import Base
"""Класс где пользователь выбирает товар"""

class Product_page(Base):

    # locators
    xpath_add_to_cart_backpack_1 = "//button[@id='add-to-cart-sauce-labs-backpack']"
    xpath_blackpack_price = "//div[@class='inventory_item_price'][contains(.,'$29.99')]"
    xpath_backpack_text = "//div[text()='Sauce Labs Backpack']"

    xpath_add_to_cart_bike_light_2 = "//button[@id='add-to-cart-sauce-labs-bike-light']"
    xpath_cost_bike_light = "//div[@class='inventory_item_price'][contains(.,'$9.99')]"

    xpath_add_to_cart_t_shirt_3 = "//button[@id='add-to-cart-sauce-labs-bolt-t-shirt']"

    xpath_add_to_cart_fleece_jacket_4 = "//button[@id='add-to-cart-sauce-labs-fleece-jacket']"

    xpath_add_to_cart_labs_onesie_5 = "//button[@id='add-to-cart-sauce-labs-onesie']"

    xpath_add_to_cart_t_shirt_red_6 = "//button[@id='add-to-cart-test.allthethings()-t-shirt-(red)']"

    xpath_go_shopping_cart = "//a[@class='shopping_cart_link']"


    """Проверяем цену товара и добавляем в корзину"""
    def find_price_product_go_to_cart(self, locator_price_element, product_price, locator_product):
        self.get_current_url()
        self.assert_words(self.get_element(locator_price_element), product_price)
        self.wait_and_click_element(locator_product)
        self.wait_and_click_element(self.xpath_go_shopping_cart)
