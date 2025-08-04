import allure
from pathlib import Path
from locators.create_receipt_page_locators import CreateReceiptPageLocators
from pages.base_page import BasePage

class CreateReceiptPage(BasePage):

    @allure.step("Клик на Создать рецепт")
    def click_create_receipt(self):
        self.find_element_with_wait(CreateReceiptPageLocators.BUTTON_CREATE_RECEIPT)
        self.click_to_element(CreateReceiptPageLocators.BUTTON_CREATE_RECEIPT)

    @allure.step("Ввод названия")
    def enter_receipt_title(self, name):
        self.enter_text_to_element(CreateReceiptPageLocators.FIELD_RECEIPT_TITLE, name)

    @allure.step("Клик на тэг Завтрак")
    def click_tag_breakfast(self):
        self.find_element_with_wait(CreateReceiptPageLocators.TAG_BREAKFAST)
        self.click_to_element(CreateReceiptPageLocators.TAG_BREAKFAST)

    @allure.step("Ввод количества ингредиента")
    def enter_ingredient_amount(self, amount):
        self.enter_text_to_element(CreateReceiptPageLocators.FIELD_AMOUNT_INGREDIENTS, amount)

    @allure.step("Ввод времени")
    def enter_time(self, time):
        self.enter_text_to_element(CreateReceiptPageLocators.FIELD_TIME, time)

    @allure.step("Ввод описания")
    def enter_description(self, description):
        self.enter_text_to_element(CreateReceiptPageLocators.FIELD_DESCRIPTION, description)

    @allure.step("Получение пути к файлу")
    def file_path(self):
        file_path = Path(__file__).parent.parent/'assets/avatar.jpeg'
        return str(file_path)

    @allure.step("Загрузка файла")
    def input_file(self):
        file_path = self.file_path()
        self.find_invis_element(CreateReceiptPageLocators.INPUT_FILE).send_keys(file_path)

    @allure.step("Ввод ингредиента")
    def enter_ingredients(self, ingredient):
        self.enter_text_to_element(CreateReceiptPageLocators.FIELD_INGREDIENTS, ingredient)
        self.find_element_with_wait(CreateReceiptPageLocators.INGREDIENT_1_LOCATOR)
        self.click_to_element(CreateReceiptPageLocators.INGREDIENT_1_LOCATOR)

    @allure.step("Добавить ингредиент")
    def add_ingredient(self):
        self.click_to_element(CreateReceiptPageLocators.BUTTON_ADD_INGREDIENT)

    @allure.step("Клик на кнопку Создать рецепт на странице создания рецептов")
    def click_button_create_receipt_bottom(self):
        self.click_to_element(CreateReceiptPageLocators.BUTTON_CREATE_RECEIPT_BOTTOM)

    @allure.step("Проверка названия рецепта")
    def check_receipt_title(self):
        return self.find_element_with_wait(CreateReceiptPageLocators.RECEIPT_TITLE).text

    @allure.step("Проверка карточки рецепта")
    def check_receipt_card(self):
       title = self.find_element_with_wait(CreateReceiptPageLocators.LOCATOR_FOR_RECEIPT_CARD).text
       visibility_receipt_card = self.find_element_with_wait(CreateReceiptPageLocators.LOCATOR_FOR_RECEIPT_CARD).is_displayed()
       return title, visibility_receipt_card