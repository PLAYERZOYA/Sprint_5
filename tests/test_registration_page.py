
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from locators import REGISTRATION, AUTH_LOC



# функция для заполнения формы регистрации
def fill_registration_form(driver, name, email, password):
    
    driver.find_element(*REGISTRATION["name_input"]).send_keys(name)
    driver.find_element(*REGISTRATION["email_input"]).send_keys(email)
    driver.find_element(*REGISTRATION["password_input"]).send_keys(password)

    driver.find_element(*REGISTRATION["register_button"]).click()


# проверка регистрации с валидными данными: 

def test_successful_registration_valid_data(driver_registration, generate_email_and_password):

    email, password = generate_email_and_password

    fill_registration_form(driver_registration, "Зоя", email, password)

    WebDriverWait(driver_registration, 3).until(expected_conditions.visibility_of_element_located((AUTH_LOC["entrance_button"])))
    

    assert driver_registration.current_url == 'https://stellarburgers.education-services.ru/login'

# проверка регистрации с невалидным значением пароля:

def test_registration_with_incorrect_password_length_5(driver_registration):
    
    fill_registration_form(driver_registration, "Зоя", "zoya_kozlova_42_125@ya.ru", "qwert")

    WebDriverWait(driver_registration, 3).until(expected_conditions.visibility_of_element_located((REGISTRATION["incorrect_password_text"])))
    
    result = driver_registration.find_element(*REGISTRATION["incorrect_password_text"])

    assert 'Некорректный пароль' in result.text

