from selenium.webdriver.common.by import By

class AuthorizationPageLocators:
    BUTTON_VOITI_UPPER_CORNER = By.XPATH, "//a[contains(text(), 'Войти')]"
    FIELD_EMAIL = By.NAME, "email"
    FIELD_PASSWORD = By.NAME, "password"
    BUTTON_VOITI_BOTTOM = By.XPATH, "//button[contains(text(), 'Войти')]"
    LOCATOR_FOR_TEST_RECEIPT_PAGE = By.XPATH, "//h1[contains(text(), 'Рецепты')]"
    BUTTON_EXIT = By.XPATH, "//a[contains(text(), 'Выход')]"