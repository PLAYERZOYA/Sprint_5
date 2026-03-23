from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

# Функция для заполнения данных при входе в аккаунт
def fill_entry_form(driver, email, password):

    driver.find_element(By.XPATH, ".//div[@id='root']/div/main/div/form/fieldset[1]/div/div/input").send_keys(email)
    driver.find_element(By.XPATH, ".//div[@id='root']/div/main/div/form/fieldset[2]/div/div/input").send_keys(password)

    driver.find_element(By.XPATH, ".//button[text()='Войти']").click()


# авторизация через кнопку 'Войти в аккаунт'
def test_authorization_button_log_in_to_account(driver):

    driver.find_element(By.XPATH, ".//button[text()='Войти в аккаунт']").click()

    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//button[text()='Войти']")))

    fill_entry_form(driver, "zoya_kozlova_42_123@ya.ru", "qwerty")

    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//button[text()='Оформить заказ']")))

    assert len(driver.find_elements(By.XPATH, ".//button[text()='Войти в аккаунт']")) == 0


# авторизация через кнопку 'Личный кабинет'
def test_authorization_button_personal_account(driver):

    driver.find_element(By.XPATH, ".//button[text()='Войти в аккаунт']").click()

    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//div[@id='root']/div/header/nav/a/p")))

    fill_entry_form(driver, "zoya_kozlova_42_123@ya.ru", "qwerty")

    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//button[text()='Оформить заказ']")))

    assert len(driver.find_elements(By.XPATH, ".//button[text()='Войти в аккаунт']")) == 0

# авторизация через кнопку в форме регистрации 
def test_authorization_button_in_registration_form(driver_registration):
    
    driver_registration.find_element(By.LINK_TEXT, "Войти").click()

    WebDriverWait(driver_registration, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//button[text()='Войти']")))

    fill_entry_form(driver_registration, "zoya_kozlova_42_123@ya.ru", "qwerty")

    WebDriverWait(driver_registration, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//button[text()='Оформить заказ']")))

    assert len(driver_registration.find_elements(By.XPATH, ".//button[text()='Войти в аккаунт']")) == 0

# авторизация через кнопку в форме восстановления пароля
def test_authorization_password_recovery_form(driver):

    driver.find_element(By.XPATH, ".//button[text()='Войти в аккаунт']").click()

    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//button[text()='Войти']")))
    
    driver.find_element(By.LINK_TEXT, "Восстановить пароль").click()

    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//div[@id='root']/div/main/div/h2")))

    driver.find_element(By.LINK_TEXT, "Войти").click()

    fill_entry_form(driver, "zoya_kozlova_42_123@ya.ru", "qwerty")

    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//button[text()='Оформить заказ']")))

    assert len(driver.find_elements(By.XPATH, ".//button[text()='Войти в аккаунт']")) == 0