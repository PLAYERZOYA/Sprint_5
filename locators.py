from selenium.webdriver.common.by import By

REGISTRATION = {

"name_input": (By.XPATH, ".//fieldset[1]/div/div/input"), #поле ввода имени в форме регистрации

"email_input": (By.XPATH, ".//fieldset[2]/div/div/input"), # поле ввода почты в форме регистрации

"password_input": (By.NAME, "Пароль"), # поле ввода пароля в форме регистрации

"register_button": (By.XPATH, ".//button[text()='Зарегистрироваться']"), # кнопка Зарегистрироваться

"incorrect_password_text": (By.XPATH, ".//p[text()='Некорректный пароль']"), # текст о некорректном пароле

"login_link": (By.LINK_TEXT, "Войти") # ссылка Войти

}

AUTH_LOC = {

"login_account_button": (By.XPATH, ".//button[text()='Войти в аккаунт']"), # кнопка войти в аккаунт

"email_field": (By.XPATH, ".//fieldset[1]/div/div/input"), #поле ввода почты

"password_field": (By.CSS_SELECTOR, "input[type='password'][name='Пароль']"), # поле ввода пароля

"entrance_button": (By.XPATH, ".//button[text()='Войти']"), # кнопка Войти


"recover_password_link": (By.LINK_TEXT, "Восстановить пароль"), # ссылка Восстановить пароль

"restore_button": (By.XPATH, ".//button[text()='Восстановить']"), # кнопка Восстановить в форме восстановления пароля

"entrance_link": (By.LINK_TEXT, "Войти") # ссылка Войти в форме восстановления пароля

}


ACCOUNT_PAGE = {

"place_an_order_button": (By.XPATH, ".//button[text()='Оформить заказ']"), # кнопка Оформить заказ

"personal_account": (By.CSS_SELECTOR, "a[href='/account']"), # кнопка Личный кабинет

"exit_button": (By.XPATH, ".//button[text()='Выход']"), # кнопка Выход из аккаунта

"constructor_button": (By.CSS_SELECTOR, "a[href='/']") , # кнопка для перехода в раздел Конструктор

"logo": (By.XPATH, "//a[@href='/']") # логотип
}

CONSTRUCTOR = {

"sauce_section": (By.XPATH, "//span[text()='Соусы']"), # вкладка Соусы

"sauces": (By.XPATH, "//h2[text()='Соусы']"), # текст Соусы в секции соусов

"burger_rolls_section": (By.XPATH, "//span[text()='Соусы']"), # вкладка Бургеры

"burger_rolls": (By.XPATH, "//h2[text()='Булки']"), # текст Булки в секции булок

"toppings_section": (By.XPATH, "//span[text()='Начинки']"), # вкладка Начинки

"toppings": (By.XPATH, "//h2[text()='Начинки']") # текст Начинки в секции Начинок

}