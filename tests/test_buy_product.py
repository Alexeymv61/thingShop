import time
from selenium import webdriver

from pages.authorization_page import Authorization_page
from pages.product_page import Product_page
from pages.cart_page import Cart_page
from pages.addittional_data_page import Addittional_data
from pages.final_pages import Final_page


def test_buy_product():
    """расписаны шаги теста в page object style"""
    driver = webdriver.Chrome(executable_path="../chromedriver-linux64/chromedriver")

    print("Старт")

    """создание экземпляра класса Authorization_page"""
    ap = Authorization_page(driver)
    """вызов метода authorization_steps с значениями аргументов login = '9102736884' и password = 'nKf3bsj'"""
    ap.authorization_steps('standard_user', 'secret_sauce')
    print('Авторизация прошла успешно')

    print("Приветствую тебя в нашем интернет магазине")
    print("Выбери один из следующих товаров и укажи его номер: 1 - Sauce Labs Backpack, 2 - Sauce Labs Bike Light,"
          " 3 - Sauce Labs Bolt T-Shirt, 4 - Sauce Labs Fleece Jacket, 5 - Sauce Labs Onesie,"
          " 6 - Test.allTheThings() T-Shirt (Red)")
    my_list = ["Sauce Labs Backpack", "Sauce Labs Bike Light", "Sauce Labs Bolt T-Shirt", "Sauce Labs Fleece Jacket",
               "Sauce Labs Onesie", "Test.allTheThings() T-Shirt (Red)"]
    my_digit = int(input())

    if my_digit == 1:
        print(f'Выбран товар - {my_list[0]}')
        prp = Product_page(driver)
        prp.find_price_product_go_to_cart("//div[@class='inventory_item_price'][contains(.,'$29.99')]",
                                          '$29.99',
                                          "//button[@id='add-to-cart-sauce-labs-backpack']")
        cp = Cart_page(driver)
        cp.get_cost_and_click_checkout('$29.99')
        adp = Addittional_data(driver)
        adp.fill_additional_data_and_click_checkout('customer1_first_name', 'customer1_last_name', '111')
        fp = Final_page(driver)
        fp.check_name_price_and_click_finish('Sauce Labs Backpack', '$29.99')

    elif my_digit == 2:
        print(f'Выбран товар - {my_list[1]}')
        prp = Product_page(driver)
        prp.find_price_product_go_to_cart("//div[@class='inventory_item_price'][contains(.,'$9.99')]",
                                          "$9.99",
                                          "//button[@id='add-to-cart-sauce-labs-bike-light']")
        cp = Cart_page(driver)
        cp.get_cost_and_click_checkout("$9.99")
        adp = Addittional_data(driver)
        adp.fill_additional_data_and_click_checkout('customer2_first_name', 'customer2_last_name', '222')
        fp = Final_page(driver)
        fp.check_name_price_and_click_finish('Sauce Labs Bike Light', '$9.99')

    elif my_digit == 3:
        print(f'Выбран товар - {my_list[2]}')
        prp = Product_page(driver)
        prp.find_price_product_go_to_cart("(//div[@class='inventory_item_price'][contains(.,'$15.99')])[1]",
                                          "$15.99",
                                          "//button[@id='add-to-cart-sauce-labs-bolt-t-shirt']")
        cp = Cart_page(driver)
        cp.get_cost_and_click_checkout("$15.99")
        adp = Addittional_data(driver)
        adp.fill_additional_data_and_click_checkout('customer3_first_name', 'customer3_last_name', '333')
        fp = Final_page(driver)
        fp.check_name_price_and_click_finish('Sauce Labs Bolt T-Shirt', '$15.99')
    elif my_digit == 4:
        print(f'Выбран товар - {my_list[3]}')
        prp = Product_page(driver)
        prp.find_price_product_go_to_cart("//div[@class='inventory_item_price'][contains(.,'$49.99')]",
                                          "$49.99",
                                          "//button[@id='add-to-cart-sauce-labs-fleece-jacket']")
        cp = Cart_page(driver)
        cp.get_cost_and_click_checkout("$49.99")
        adp = Addittional_data(driver)
        adp.fill_additional_data_and_click_checkout('customer4_first_name', 'customer4_last_name', '444')
        fp = Final_page(driver)
        fp.check_name_price_and_click_finish('Sauce Labs Fleece Jacket', '$49.99')

    elif my_digit == 5:
        print(f'Выбран товар - {my_list[3]}')
        prp = Product_page(driver)
        prp.find_price_product_go_to_cart("//div[@class='inventory_item_price'][contains(.,'$7.99')]",
                                          "$7.99",
                                          "//button[@id='add-to-cart-sauce-labs-onesie']")
        cp = Cart_page(driver)
        cp.get_cost_and_click_checkout("$7.99")
        adp = Addittional_data(driver)
        adp.fill_additional_data_and_click_checkout('customer5_first_name', 'customer5_last_name', '555')
        fp = Final_page(driver)
        fp.check_name_price_and_click_finish('Sauce Labs Onesie', '$7.99')

    elif my_digit == 6:
        print(f'Выбран товар - {my_list[5]}')
        prp = Product_page(driver)
        prp.find_price_product_go_to_cart("(//div[@class='inventory_item_price'][contains(.,'$15.99')])[2]",
                                          "$15.99",
                                          "//button[@id='add-to-cart-test.allthethings()-t-shirt-(red)']")
        cp = Cart_page(driver)
        cp.get_cost_and_click_checkout("$15.99")
        adp = Addittional_data(driver)
        adp.fill_additional_data_and_click_checkout('customer6_first_name', 'customer6_last_name', '666')
        fp = Final_page(driver)
        fp.check_name_price_and_click_finish('Test.allTheThings() T-Shirt (Red)', '$15.99')
    else:
        print('Введена некорректная цифра, введите значение от 1 до 6')

    print("Финиш")
    time.sleep(5)
    driver.quit()
