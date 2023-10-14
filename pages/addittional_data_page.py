from base.base import Base


class Addittional_data(Base):
    """Класс в котором пользователь заполняет данные о себе"""
    # locators
    xpath_input_first_name = "//input[@id='first-name']"
    xpath_input_last_name = "//input[@id='last-name']"
    xpath_input_zip = "//input[@id='postal-code']"
    xpath_button_continue = "//input[@id='continue']"

    def fill_additional_data_and_click_checkout(self, text_first_name, text_last_name, text_zip):
        """На странице "дополнительные данные" вводим информацию о покупателе"""
        self.get_current_url()
        self.wait_and_complete_element(self.xpath_input_first_name, text_first_name)
        self.wait_and_complete_element(self.xpath_input_last_name, text_last_name)
        self.wait_and_complete_element(self.xpath_input_zip, text_zip)
        self.wait_and_click_element(self.xpath_button_continue)



