from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

def fill_entry_form(driver, email, password):
    driver.find_element(By.XPATH, ".//button[text()='Войти в аккаунт']").click()

    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//button[text()='Войти']")))

    driver.find_element(By.XPATH, ".//div[@id='root']/div/main/div/form/fieldset[1]/div/div/input").send_keys(email)
    driver.find_element(By.XPATH, ".//div[@id='root']/div/main/div/form/fieldset[2]/div/div/input").send_keys(password)

    driver.find_element(By.XPATH, ".//button[text()='Войти']").click()

# проверка перехода в раздел соусы
def test_click_burger_sauces_section_open_sauces_section(driver):

    fill_entry_form(driver, "zoya_kozlova_42_123@ya.ru", "qwerty")

    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//button[text()='Оформить заказ']")))

    driver.find_element(By.XPATH, './/div[@id="root"]/div/main/section[1]/div[1]/div[2]').click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, './/div[@id="root"]/div/main/section[1]/div[2]/ul[2]')))

    sauces = driver.find_element(By.XPATH, './/div[@id="root"]/div/main/section[1]/div[2]/h2[2]')

    assert sauces.text == 'Соусы'

# проверка перехода в раздел булки
def test_click_burger_rolls_section_open_section(driver):

    fill_entry_form(driver, "zoya_kozlova_42_123@ya.ru", "qwerty")

    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//button[text()='Оформить заказ']")))

    driver.find_element(By.XPATH, './/div[@id="root"]/div/main/section[1]/div[1]/div[2]').click() #сначала переходим в раздел соусов, т.к по дефолту открыты булки
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, './/div[@id="root"]/div/main/section[1]/div[2]/h2[2]')))

    driver.find_element(By.XPATH, './/div[@id="root"]/div/main/section[1]/div[1]/div[1]').click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, './/div[@id="root"]/div/main/section[1]/div[2]/ul[1]')))

    burger_rolls = driver.find_element(By.XPATH, './/div[@id="root"]/div/main/section[1]/div[2]/h2[1]')

    assert burger_rolls.text == 'Булки'

# проверка перехода в раздел начинки
def test_click_topping_section_open_topping_section(driver):

    fill_entry_form(driver, "zoya_kozlova_42_123@ya.ru", "qwerty")

    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//button[text()='Оформить заказ']")))

    driver.find_element(By.XPATH, './/div[@id="root"]/div/main/section[1]/div[1]/div[3]').click()

    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, './/div[@id="root"]/div/main/section[1]/div[2]/h2[3]')))

    toppings = driver.find_element(By.XPATH, './/div[@id="root"]/div/main/section[1]/div[2]/h2[3]')

    assert toppings.text == 'Начинки'