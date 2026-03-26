from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from locators import  REGISTRATION, AUTH_LOC, ACCOUNT_PAGE

# Функция для заполнения данных при входе в аккаунт
def fill_entry_form(driver, email, password):

    driver.find_element(*AUTH_LOC['email_field']).send_keys(email)
    driver.find_element(*AUTH_LOC['password_field']).send_keys(password)

    driver.find_element(*AUTH_LOC["entrance_button"]).click()


# авторизация через кнопку 'Войти в аккаунт'
def test_authorization_button_log_in_to_account(driver):

    driver.find_element(*AUTH_LOC["login_account_button"]).click()

    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((AUTH_LOC["entrance_button"])))

    fill_entry_form(driver, "zoya_kozlova_42_123@ya.ru", "qwerty")

    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((ACCOUNT_PAGE['place_an_order_button'])))

    assert len(driver.find_elements(*AUTH_LOC['login_account_button'])) == 0


# авторизация через кнопку 'Личный кабинет'
def test_authorization_button_personal_account(driver):

    driver.find_element(*ACCOUNT_PAGE['personal_account']).click()

    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((AUTH_LOC['entrance_button'])))

    fill_entry_form(driver, "zoya_kozlova_42_123@ya.ru", "qwerty")

    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((ACCOUNT_PAGE['place_an_order_button'])))

    assert len(driver.find_elements(*AUTH_LOC['login_account_button'])) == 0

# авторизация через кнопку в форме регистрации 
def test_authorization_button_in_registration_form(driver_registration):
    
    driver_registration.find_element(*REGISTRATION["login_link"]).click()

    WebDriverWait(driver_registration, 3).until(expected_conditions.visibility_of_element_located((AUTH_LOC['entrance_button'])))

    fill_entry_form(driver_registration, "zoya_kozlova_42_123@ya.ru", "qwerty")

    WebDriverWait(driver_registration, 3).until(expected_conditions.visibility_of_element_located((ACCOUNT_PAGE['place_an_order_button'])))

    assert len(driver_registration.find_elements(*AUTH_LOC['login_account_button'])) == 0

# авторизация через кнопку в форме восстановления пароля
def test_authorization_password_recovery_form(driver):

    driver.find_element(*AUTH_LOC['login_account_button']).click()

    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((AUTH_LOC['entrance_button'])))
    
    driver.find_element(*AUTH_LOC["recover_password_link"]).click()

    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((AUTH_LOC["restore_button"])))

    driver.find_element(*AUTH_LOC["entrance_link"]).click()

    fill_entry_form(driver, "zoya_kozlova_42_123@ya.ru", "qwerty")

    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((ACCOUNT_PAGE['place_an_order_button'])))

    assert len(driver.find_elements(*AUTH_LOC['login_account_button'])) == 0