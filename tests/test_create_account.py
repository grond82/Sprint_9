import allure
from url import TestUrl
from pages.create_account_page import CreateAccountPage
from helpers import Helpers

class TestCreateAccount:

    @allure.title("Проверка создания аккаунта")
    def test_create_account(self, driver):
        create_account_page = CreateAccountPage(driver)
        create_account_page.go_to_url(TestUrl.HOMEPAGE_URL)
        create_account_page.click_create_account_home_page()
        helpers = Helpers()
        name, surname, user_name, email, password = helpers.generate_new_account_param()
        create_account_page.enter_field_name(name)
        create_account_page.enter_field_surname(surname)
        create_account_page.enter_field_user_name(user_name)
        create_account_page.enter_field_email(email)
        create_account_page.enter_field_password(password)
        create_account_page.click_create_account_registration()
        assert create_account_page.check_authorization_page() == True

    @allure.title("Проверка видимости формы авторизации после создания аккаунта")
    def test_visibility_authorization_form_after_create_account(self, driver):
        create_account_page = CreateAccountPage(driver)
        create_account_page.go_to_url(TestUrl.HOMEPAGE_URL)
        create_account_page.click_create_account_home_page()
        helpers = Helpers()
        name, surname, user_name, email, password = helpers.generate_new_account_param()
        create_account_page.enter_field_name(name)
        create_account_page.enter_field_surname(surname)
        create_account_page.enter_field_user_name(user_name)
        create_account_page.enter_field_email(email)
        create_account_page.enter_field_password(password)
        create_account_page.click_create_account_registration()
        assert create_account_page.check_authorization_form() == True