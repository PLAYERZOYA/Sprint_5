
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions



# функция для заполнения формы регистрации
def fill_registration_form(driver, name, email, password):
    
    driver.find_element(By.XPATH, ".//div[@id='root']/div/main/div/form/fieldset[1]/div/div/input").send_keys(name)
    driver.find_element(By.XPATH, ".//div[@id='root']/div/main/div/form/fieldset[2]/div/div/input").send_keys(email)
    driver.find_element(By.NAME, "Пароль").send_keys(password)

    driver.find_element(By.XPATH, ".//button[text()='Зарегистрироваться']").click()


# проверка регистрации с валидными данными: 

def test_successful_registration_valid_data(driver_registration):

    fill_registration_form(driver_registration, "Зоя", "zoya_kozlova_42_123@ya.ru", "qwerty")

    WebDriverWait(driver_registration, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, './/div[@id="root"]/div/main/div/form/button')))

    assert driver_registration.current_url == 'https://stellarburgers.education-services.ru/login'

# проверка регистрации с невалидным значением почты:

def test_registration_with_incorrect_password_length_5(driver_registration):
    
    fill_registration_form(driver_registration, "Зоя", "zoya_kozlova_42_125@ya.ru", "qwert")

    WebDriverWait(driver_registration, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, './/div[@id="root"]/div/main/div/form/fieldset[3]/div/p')))
    
    result = driver_registration.find_element(By.XPATH, './/div[@id="root"]/div/main/div/form/fieldset[3]/div/p')

    assert 'Некорректный пароль' in result.text

