from page_object.base_page import Basepage
from selenium.webdriver.common.by import By

import time


class RegisterPage(Basepage):
    MYACCOUNT = (By.CSS_SELECTOR, "ul[class='list-inline'] li[class='dropdown']")
    REGISTER = (By.CSS_SELECTOR, 'li.dropdown.open > ul > li:nth-child(1) > a')
    FIRSTNAME = (By.ID, 'input-firstname')
    LASTNAME = (By.ID, 'input-lastname')
    EMAIL = (By.ID, 'input-email')
    TELEPHONE = (By.ID, 'input-telephone')
    PASSWORD = (By.ID, 'input-password')
    PASSCONFIRM = (By.ID, 'input-confirm')
    PRIVACYPOL = (By.CSS_SELECTOR, '#content > form > div > div > input[type=checkbox]:nth-child(2)')
    CONTINUE1 = (By.CSS_SELECTOR, '#content > form > div > div > input.btn.btn-primary')
    CONTINUE2 = (By.CSS_SELECTOR, '#content > div > div > a')
    MY_ACCOUNT_2 = (By.CSS_SELECTOR, "ul[class='list-inline'] li[class='dropdown']")
    LOGOUT = (By.CSS_SELECTOR, '#top-links > ul > li.dropdown.open > ul > li:nth-child(5) > a')
    LOGIN = (By.CSS_SELECTOR, 'li.dropdown.open > ul > li:nth-child(2) > a')
    LOGIN_BTN = (By.CSS_SELECTOR, '#content > div > div:nth-child(2) > div > form > input')

    def register_new_account(self, first_name, last_name, email, telephone, password, confirm_pass):
        self.click(self.element(self.MYACCOUNT))
        self.click(self.element(self.REGISTER))
        self._input(self.element(self.FIRSTNAME), first_name)
        self._input(self.element(self.LASTNAME), last_name)
        self._input(self.element(self.EMAIL), email)
        self._input(self.element(self.TELEPHONE), telephone)
        self._input(self.element(self.PASSWORD), password)
        self._input(self.element(self.PASSCONFIRM), confirm_pass)
        self.click(self.element(self.PRIVACYPOL))
        self.click(self.element(self.CONTINUE1))
        self.click(self.element(self.CONTINUE2))

    def account_to_account(self, email, password):
        self.click(self.element(self.MYACCOUNT))
        self.click(self.element(self.LOGIN))
        self._input(self.element(self.EMAIL), email)
        self._input(self.element(self.PASSWORD), password)
        self.click(self.element(self.LOGIN_BTN))
        time.sleep(5)

    def logout_from_account(self):
        self.click(self.element(self.MY_ACCOUNT_2))
        self.click(self.element(self.LOGOUT))
        self.click(self.element(self.CONTINUE2))
