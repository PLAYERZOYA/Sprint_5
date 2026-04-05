from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from locators import AUTH_LOC, ACCOUNT_PAGE, CONSTRUCTOR

# Функция для заполнения данных при входе в аккаунт
def fill_entry_form(driver, email, password):

    driver.find_element(*AUTH_LOC["login_account_button"]).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((AUTH_LOC["entrance_button"])))

    driver.find_element(*AUTH_LOC['email_field']).send_keys(email)
    driver.find_element(*AUTH_LOC['password_field']).send_keys(password)

    driver.find_element(*AUTH_LOC["entrance_button"]).click()

    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((ACCOUNT_PAGE['place_an_order_button'])))

# проверка перехода в раздел соусы
def test_click_burger_sauces_section_open_sauces_section(driver):

    fill_entry_form(driver, "zoya_kozlova_42_123@ya.ru", "qwerty")


    driver.find_element(*CONSTRUCTOR["sauce_section"]).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((CONSTRUCTOR["sauces"])))

    sauces = driver.find_element(*CONSTRUCTOR["sauces"])

    assert sauces.text == 'Соусы'

# проверка перехода в раздел булки
def test_click_burger_rolls_section_open_section(driver):

    fill_entry_form(driver, "zoya_kozlova_42_123@ya.ru", "qwerty")

    driver.find_element(*CONSTRUCTOR["sauce_section"]).click() #сначала переходим в раздел соусов, т.к по дефолту открыты булки
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((CONSTRUCTOR["sauces"])))

    driver.find_element(*CONSTRUCTOR["burger_rolls_section"]).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((CONSTRUCTOR["burger_rolls"])))

    burger_rolls = driver.find_element(*CONSTRUCTOR["burger_rolls"])

    assert burger_rolls.text == 'Булки'

# проверка перехода в раздел начинки
def test_click_topping_section_open_topping_section(driver):

    fill_entry_form(driver, "zoya_kozlova_42_123@ya.ru", "qwerty")

    driver.find_element(*CONSTRUCTOR["toppings_section"]).click()

    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((CONSTRUCTOR["toppings"])))

    toppings = driver.find_element(*CONSTRUCTOR["toppings"])

    assert toppings.text == 'Начинки'