from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from locators import  REGISTRATION, AUTH_LOC, ACCOUNT_PAGE

# Функция для заполнения данных при входе в аккаунт
def fill_entry_form(driver, email, password):

    driver.find_element(*AUTH_LOC["login_account_button"]).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((AUTH_LOC["entrance_button"])))

    driver.find_element(*AUTH_LOC['email_field']).send_keys(email)
    driver.find_element(*AUTH_LOC['password_field']).send_keys(password)

    driver.find_element(*AUTH_LOC["entrance_button"]).click()

    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((ACCOUNT_PAGE['place_an_order_button'])))

# проверка перехода в личный кабинет пользователя
def test_click_through_to_personal_account(driver):

    fill_entry_form(driver, "zoya_kozlova_42_123@ya.ru", "qwerty")


    driver.find_element(*ACCOUNT_PAGE["personal_account"]).click()

    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((ACCOUNT_PAGE["exit_button"])))

    assert len(driver.find_elements(*ACCOUNT_PAGE["exit_button"])) == 1

# проверка перехода из личного кабинета в конструктор
def test_switch_from_personal_account_to_constructor_click_constructor(driver):

    fill_entry_form(driver, "zoya_kozlova_42_123@ya.ru", "qwerty")

    driver.find_element(*ACCOUNT_PAGE["personal_account"]).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((ACCOUNT_PAGE["exit_button"])))

    driver.find_element(*ACCOUNT_PAGE["constructor_button"]).click()

    assert len(driver.find_elements(*ACCOUNT_PAGE["place_an_order_button"])) == 1

# проверка перехода из личного кабинета по нажатию на логотип
def test_switch_from_personal_account_to_constructor_click_logo(driver):

    fill_entry_form(driver, "zoya_kozlova_42_123@ya.ru", "qwerty")

    driver.find_element(*ACCOUNT_PAGE["personal_account"]).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((ACCOUNT_PAGE["exit_button"])))

    driver.find_element(*ACCOUNT_PAGE["logo"]).click()

    assert len(driver.find_elements(*ACCOUNT_PAGE["place_an_order_button"])) == 1


# проверка выхода из аккаунта
def test_log_out_of_account_in_personal_account(driver):

    fill_entry_form(driver, "zoya_kozlova_42_123@ya.ru", "qwerty")

    driver.find_element(*ACCOUNT_PAGE["personal_account"]).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((ACCOUNT_PAGE["exit_button"])))
    
    driver.find_element(*ACCOUNT_PAGE["exit_button"]).click()

    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((AUTH_LOC["entrance_button"])))

    assert driver.current_url == "https://stellarburgers.education-services.ru/login"