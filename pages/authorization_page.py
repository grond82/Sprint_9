import allure
from locators.authorization_page_locators import AuthorizationPageLocators
from pages.base_page import BasePage

class AuthorizationPage(BasePage):

    @allure.step("Клик на кнопку Войти в верхнем углу")
    def click_button_voiti_upper_corner(self):
        self.click_to_element(AuthorizationPageLocators.BUTTON_VOITI_UPPER_CORNER)

    @allure.step("Ввод почты")
    def enter_email(self, email):
        self.enter_text_to_element(AuthorizationPageLocators.FIELD_EMAIL, email)

    @allure.step("Ввод пароля")
    def enter_password(self, password):
        self.enter_text_to_element(AuthorizationPageLocators.FIELD_PASSWORD, password)

    @allure.step("Клик на кнопку Войти внизу")
    def click_button_voiti_bottom(self):
        self.click_to_element(AuthorizationPageLocators.BUTTON_VOITI_BOTTOM)

    @allure.step("Проверка рецепта")
    def check_receipt_page(self):
        return self.find_element_with_wait(AuthorizationPageLocators.LOCATOR_FOR_TEST_RECEIPT_PAGE).text

    @allure.step("Проверка видимости кнопки Выход")
    def check_visibility_exit_button(self):
        return self.find_element_with_wait(AuthorizationPageLocators.BUTTON_EXIT).is_displayed()