from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

def fill_entry_form(driver, email, password):
    driver.find_element(By.XPATH, ".//button[text()='Войти в аккаунт']").click()

    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//button[text()='Войти']")))

    driver.find_element(By.XPATH, ".//div[@id='root']/div/main/div/form/fieldset[1]/div/div/input").send_keys(email)
    driver.find_element(By.XPATH, ".//div[@id='root']/div/main/div/form/fieldset[2]/div/div/input").send_keys(password)

    driver.find_element(By.XPATH, ".//button[text()='Войти']").click()

# проверка перехода в личный кабинет пользователя
def test_click_through_to_personal_account(driver):

    fill_entry_form(driver, "zoya_kozlova_42_123@ya.ru", "qwerty")

    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//button[text()='Оформить заказ']")))

    driver.find_element(By.XPATH, ".//div[@id='root']/div/header/nav/a/p").click()

    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//button[text()='Выход']")))

    assert len(driver.find_elements(By.XPATH, ".//button[text()='Выход']")) == 1

# проверка перехода из личного кабинета в конструктор
def test_switch_from_personal_account_to_constructor_click_constructor(driver):
    fill_entry_form(driver, "zoya_kozlova_42_123@ya.ru", "qwerty")

    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//button[text()='Оформить заказ']")))

    driver.find_element(By.XPATH, ".//div[@id='root']/div/header/nav/a/p").click()

    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//button[text()='Выход']")))

    driver.find_element(By.XPATH, './/div[@id="root"]/div/header/nav/ul/li[1]/a/p').click()

    assert len(driver.find_elements(By.XPATH, ".//button[text()='Оформить заказ']")) == 1

# проверка перехода из личного кабинета в конструктор
def test_switch_from_personal_account_to_constructor_click_logo(driver):
    fill_entry_form(driver, "zoya_kozlova_42_123@ya.ru", "qwerty")

    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//button[text()='Оформить заказ']")))

    driver.find_element(By.XPATH, ".//div[@id='root']/div/header/nav/a/p").click()

    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//button[text()='Выход']")))

    driver.find_element(By.XPATH, ".//div[@id='root']/div/header/nav/div").click()

    assert len(driver.find_elements(By.XPATH, ".//button[text()='Оформить заказ']")) == 1


# проверка выхода из аккаунта
def test_log_out_of_account_in_personal_account(driver):

    fill_entry_form(driver, "zoya_kozlova_42_123@ya.ru", "qwerty")

    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//button[text()='Оформить заказ']")))

    driver.find_element(By.XPATH, ".//div[@id='root']/div/header/nav/a/p").click()

    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//button[text()='Выход']")))
    
    driver.find_element(By.XPATH, ".//button[text()='Выход']").click()

    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//button[text()='Войти']")))

    assert driver.current_url == "https://stellarburgers.education-services.ru/login"