import datetime
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Base():
    """Базовый класс где будут находиться общие методы для различных страниц"""

    def __init__(self, driver):
        self.driver = driver

    def assert_words(self, word, excepted_result):
        """
        метод в котором сравнивается текст по локатору на странице с ожидаемым результатом
        word - значение локатора
        excepted_result - ожидаемый результат
        """
        value_word = word.text
        assert value_word == excepted_result
        print(f"Текст {value_word} найден - успешно")

    def get_current_url(self):
        """метод возвращает сайт где вызван метод"""
        current_url = self.driver.current_url
        print(f'Текущий url - {current_url}')

    def move_to_element(self, locator):
        """ метод позволяет перейти к элементу на странице"""
        action = ActionChains(self.driver)
        action.move_to_element(locator).perform()

    def max_resolution(self):
        """метод в котором разрешение страницы масштабируется на весь экран"""
        return self.driver.maximize_window()

    def scroll_on_page(self, x, y):
        """
        x - перемещение по горизонтали
        y - перемещение по вертикали
        метод для перемещение верстикального и/или горизонтального скролла
        """
        return self.driver.execute_script(f"window.scrollTo({x},{y})")

    def switch_to_frame(self, id):
        """метод для переключения на frame где будет происходить работа с элементом"""
        return self.driver.switch_to.frame(id)

    def get_element(self, locator):
        """
        locator - xpath элемента с которым будет происходить взаимодействие
        метод для получения локатора на страницах для дальнейшего взаимодействия с элементом
        """
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, locator)))

    def wait_and_click_element(self, locator):
        """метод для ожидание элемента на странице пока он станет кликабельным и кликает на элемент"""
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, locator))).click()

    def make_screenshoot(self, location=None):
        """
        location - название скриншота, по умолчанию None
        функция делает скриншот страницы
        """
        screen_time = datetime.datetime.utcnow().strftime('%Y.%m.%d.%H.%M.%S')
        self.driver.save_screenshot(
            f'/home/abalashov/selenium_course/thingShop/tests/screens/screen_{location}_{screen_time}.png')

    def find_element_without_wait_and_click(self, xpath):
        """
        В методе находим элемент без ожидания и кликаем на него
        xpath - локатор кнопки на который происходит клик
        """
        return self.driver.find_elements(By.XPATH, xpath)

    def wait_and_complete_element(self, locator, text):
        """метод ждет инпут на странице пока тот станет каликабельны и заполняет его"""
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, locator))).send_keys(text)
