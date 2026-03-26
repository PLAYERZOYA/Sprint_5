# модуль для хранения тестовых данных

class RegistrationData:
    valid_user = {
        "name": "Зоя",
        "email": "zoya_kozlova_42_123@ya.ru",
        "password": "qwerty"
    }

    invalid_password_user = {
        "name": "Зоя",
        "email": "zoya_kozlova_42_123@ya.ru",
        "password": "qwert" # короткий пароль
    }

class LoginData:
    valid_credentials = {
        "email": "zoya_kozlova_42_123@ya.ru",
        "password": "qwerty"
    }