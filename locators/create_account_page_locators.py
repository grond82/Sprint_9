from selenium.webdriver.common.by import By

class CreateAccountPageLocators:
    BUTTON_CREATE_ACCOUNT_HOME_PAGE = By.XPATH, "//a[contains(text(), 'Создать аккаунт')]"
    FIELD_NAME = By.NAME, "first_name"
    FIELD_SURNAME = By.NAME, "last_name"
    FIELD_USER_NAME = By.NAME, "username"
    FIELD_EMAIL = By.NAME, "email"
    FIELD_PASSWORD = By.NAME, "password"
    BUTTON_CREATE_ACCOUNT_CREATE_ACCOUNT_PAGE = By.XPATH, "//button[contains(text(), 'Создать аккаунт')]"
    LOCATOR_FOR_TEST_AUTHORIZATION_PAGE = By.XPATH, "//h1[contains(text(), 'Войти на сайт')]"
    LOCATOR_FOR_TEST_AUTHORIZATION_FORM_AFTER_CREATE_USER = By.XPATH, "//form[contains(@class, 'styles_form')]"