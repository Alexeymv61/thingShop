from base.base import Base

class Authorization_page(Base):
    """Класс авторизации покупателя"""
    url = 'https://www.saucedemo.com/'

    # локаторы
    xpath_input_login = "//input[@id='user-name']"
    xpath_input_password = "//input[@id='password']"
    xpath_button_login = "//input[@id='login-button']"

    def fill_login(self, element, login):
        self.get_element(element).send_keys(login)

    def fill_password(self, element, password):
        self.get_element(element).send_keys(password)

    def authorization_steps(self, login, password):
        self.driver.get(self.url)
        self.max_resolution()
        self.fill_login(self.xpath_input_login, login)
        print("Заполнение поля login - успешно")
        self.fill_password(self.xpath_input_password, password)
        print("Заполнение поля password - успешно")
        self.wait_and_click_element(self.xpath_button_login)
        print("Авторизация прошла - успешно")