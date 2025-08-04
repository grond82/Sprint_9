import allure
from locators.create_account_page_locators import CreateAccountPageLocators
from pages.base_page import BasePage

class CreateAccountPage(BasePage):

    @allure.step("Клик на Создать аккаунт на домашней странице")
    def click_create_account_home_page(self):
        self.click_to_element(CreateAccountPageLocators.BUTTON_CREATE_ACCOUNT_HOME_PAGE)

    @allure.step("Ввести имя")
    def enter_field_name(self, name):
        self.enter_text_to_element(CreateAccountPageLocators.FIELD_NAME, name)

    @allure.step("Ввести фамилию")
    def enter_field_surname(self, surname):
        self.enter_text_to_element(CreateAccountPageLocators.FIELD_SURNAME, surname)

    @allure.step("Ввести имя пользователя")
    def enter_field_user_name(self, user_name):
        self.enter_text_to_element(CreateAccountPageLocators.FIELD_USER_NAME, user_name)

    @allure.step("Ввести почту")
    def enter_field_email(self, email):
        self.enter_text_to_element(CreateAccountPageLocators.FIELD_EMAIL, email)

    @allure.step("Ввести пароль")
    def enter_field_password(self, password):
        self.enter_text_to_element(CreateAccountPageLocators.FIELD_PASSWORD, password)

    @allure.step("Клик на создать аккаунт на странице регистрации")
    def click_create_account_registration(self):
        self.click_to_element(CreateAccountPageLocators.BUTTON_CREATE_ACCOUNT_CREATE_ACCOUNT_PAGE)

    @allure.step("Проверка страницы авторизации")
    def check_authorization_page(self):
        return self.find_element_with_wait(CreateAccountPageLocators.LOCATOR_FOR_TEST_AUTHORIZATION_PAGE).is_displayed()

    @allure.step("Проверка формы авторизации")
    def check_authorization_form(self):
        return self.find_element_with_wait(CreateAccountPageLocators.LOCATOR_FOR_TEST_AUTHORIZATION_FORM_AFTER_CREATE_USER).is_displayed()