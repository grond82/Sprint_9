from selenium.webdriver.common.by import By

class CreateReceiptPageLocators:
    BUTTON_CREATE_RECEIPT = By.XPATH, "//a[contains(text(), 'Создать рецепт')]"
    FIELD_RECEIPT_TITLE = By.XPATH, "//div[contains(text(), 'Название рецепта')]//following-sibling::*[1][name()='input']"
    TAG_BREAKFAST = By.XPATH, "//button[@style='background-color: orange;']"
    FIELD_AMOUNT_INGREDIENTS = By.XPATH, "//input[contains(@class, 'ingredientsAmountValue')]"
    FIELD_TIME = By.XPATH, "//div[contains(text(), 'Время приготовления')]//following-sibling::*[1][name()='input']"
    FIELD_DESCRIPTION = By.XPATH, "//textarea[contains(@class, 'textareaField')]"
    INPUT_FILE = By.XPATH, "//input[contains(@class, 'fileInput')]"
    FIELD_INGREDIENTS = By.XPATH, "//input[contains(@class, 'ingredientsInput')]"
    INGREDIENT_1_LOCATOR = By.XPATH, "//div[contains(text(), 'творог 18%')]"
    BUTTON_ADD_INGREDIENT = By.XPATH, "//div[contains(text(), 'Добавить ингредиент')]"
    BUTTON_CREATE_RECEIPT_BOTTOM = By.XPATH, "//button[contains(text(), 'Создать рецепт')]"
    RECEIPT_TITLE = By.XPATH, "//h1[contains(@class, 'single-card__title')]"
    LOCATOR_FOR_RECEIPT_CARD = By.XPATH, "//div[contains(@class, 'card__body')]/a[contains(@class, 'card__title')]"