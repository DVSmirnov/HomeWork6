from page_object.base_page import Basepage
from selenium.webdriver.common.by import By


class AuthPage(Basepage):
    LOGIN = (By.CSS_SELECTOR, "#input-username")
    PASSWORD = (By.CSS_SELECTOR, "#input-password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    _path = "/admin"

    def login_to_account(self, username, password):
        self._input(self.element(self.LOGIN), username)
        self._input(self.element(self.PASSWORD), password)
        self.click(self.element(self.LOGIN_BUTTON))
