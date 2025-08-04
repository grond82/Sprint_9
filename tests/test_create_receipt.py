from url import TestUrl
import allure
from pages.authorization_page import AuthorizationPage
from pages.create_receipt_page import CreateReceiptPage
from data import Data
from helpers import Helpers

class TestCreateReceipt:

    @allure.title("Проверка создания рецепта")
    def test_create_receipt_title(self, driver):
        authorization_page = AuthorizationPage(driver)
        authorization_page.go_to_url(TestUrl.HOMEPAGE_URL)
        authorization_page.click_button_voiti_upper_corner()
        authorization_page.enter_email(Data.EMAIL)
        authorization_page.enter_password(Data.PASSWORD)
        authorization_page.click_button_voiti_bottom()
        helpers = Helpers()
        title = helpers.generate_receipt_title()
        create_receipt_page = CreateReceiptPage(driver)
        create_receipt_page.click_create_receipt()
        create_receipt_page.enter_receipt_title(title)
        create_receipt_page.click_tag_breakfast()
        create_receipt_page.enter_ingredients(Data.INGREDIENT_1)
        create_receipt_page.enter_ingredient_amount(Data.INGREDIENT_AMOUNT)
        create_receipt_page.add_ingredient()
        create_receipt_page.enter_time(Data.TIME)
        create_receipt_page.enter_description(Data.DESCRIPTION)
        create_receipt_page.input_file()
        create_receipt_page.click_button_create_receipt_bottom()
        assert create_receipt_page.check_receipt_title() == title

    @allure.title("Проверка создания рецепта и отображения его карточки")
    def test_create_receipt_card(self, driver):
        authorization_page = AuthorizationPage(driver)
        authorization_page.go_to_url(TestUrl.HOMEPAGE_URL)
        authorization_page.click_button_voiti_upper_corner()
        authorization_page.enter_email(Data.EMAIL)
        authorization_page.enter_password(Data.PASSWORD)
        authorization_page.click_button_voiti_bottom()
        helpers = Helpers()
        title = helpers.generate_receipt_title()
        create_receipt_page = CreateReceiptPage(driver)
        create_receipt_page.click_create_receipt()
        create_receipt_page.enter_receipt_title(title)
        create_receipt_page.click_tag_breakfast()
        create_receipt_page.enter_ingredients(Data.INGREDIENT_1)
        create_receipt_page.enter_ingredient_amount(Data.INGREDIENT_AMOUNT)
        create_receipt_page.add_ingredient()
        create_receipt_page.enter_time(Data.TIME)
        create_receipt_page.enter_description(Data.DESCRIPTION)
        create_receipt_page.input_file()
        create_receipt_page.click_button_create_receipt_bottom()
        create_receipt_page.go_to_url(TestUrl.RECIPES_URL)
        created_title, visibility_receipt_card = create_receipt_page.check_receipt_card()
        assert created_title == title and visibility_receipt_card == True