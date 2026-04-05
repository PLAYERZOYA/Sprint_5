import pytest
from selenium import webdriver
import random

# фикстура для инициализации и закрытия браузера
@pytest.fixture
def driver():                         
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.education-services.ru/")
    yield driver 
    driver.quit() 
    
# фикстура для инициализации и закрытия браузера при проверке страницы регистрации
@pytest.fixture
def driver_registration():                         
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.education-services.ru/register")
    yield driver 
    driver.quit() 

# генерация почты и пароля 
@pytest.fixture
def generate_email_and_password():
    name = random.choice(['test', 'user', 'student', 'coder'])
    surname = random.choice(['testov', 'userov', 'studentov', 'coderov'])
    cohort = random.randint(10, 99)
    digits = random.randint(100, 999)

    email = f"{name}_{surname}_{cohort}_{digits}@ya.ru"
    
    password = str(random.randint(100000, 999999))

    return email, password