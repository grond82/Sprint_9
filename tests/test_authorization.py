from url import TestUrl
import allure
from pages.authorization_page import AuthorizationPage
from data import Data

class TestAuthorization:

    @allure.title("Проверка авторизации")
    def test_authorization_receipt_page(self, driver):
        authorization_page = AuthorizationPage(driver)
        authorization_page.go_to_url(TestUrl.HOMEPAGE_URL)
        authorization_page.click_button_voiti_upper_corner()
        authorization_page.enter_email(Data.EMAIL)
        authorization_page.enter_password(Data.PASSWORD)
        authorization_page.click_button_voiti_bottom()
        assert authorization_page.check_receipt_page() == Data.CHECK_RECEIPT_PAGE

    @allure.title("Проверка видимости кнопки Выход после авторизации")
    def test_authorization_visibility_exit_button(self, driver):
        authorization_page = AuthorizationPage(driver)
        authorization_page.go_to_url(TestUrl.HOMEPAGE_URL)
        authorization_page.click_button_voiti_upper_corner()
        authorization_page.enter_email(Data.EMAIL)
        authorization_page.enter_password(Data.PASSWORD)
        authorization_page.click_button_voiti_bottom()
        assert authorization_page.check_visibility_exit_button() == True