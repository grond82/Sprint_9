import random
import string

class Helpers:

    @staticmethod
    def generate_new_account_param():
        def generate_random_yandex_email(length):
            letters = string.ascii_lowercase
            random_string = ''.join(random.choice(letters) for i in range(length))
            random_string = random_string + '@yandex.ru'
            return random_string
        def generate_random_string(length):
            letters = string.ascii_lowercase
            random_string = ''.join(random.choice(letters) for i in range(length))
            return random_string
        name = generate_random_string(10)
        surname = generate_random_string(10)
        user_name = generate_random_string(10)
        email = generate_random_yandex_email(10)
        password = generate_random_string(10)
        return name, surname, user_name, email, password

    @staticmethod
    def generate_receipt_title():
        def generate_random_string(length):
            letters = string.ascii_lowercase
            random_string = ''.join(random.choice(letters) for i in range(length))
            return random_string
        title = generate_random_string(5)
        return title