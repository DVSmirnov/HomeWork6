from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class Basepage:
    def __init__(self, driver):
        self.driver = driver

    def open(self, path):
        self.driver.get(self.driver.base_url + path)

    def click(self, element):
        ActionChains(self.driver).move_to_element(element).pause(0.1).click().perform()

    def _input(self, element, value):
        self.click(element)
        element.clear()
        element.send_keys(value)

    def element(self, locator: tuple):
        try:
            return WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            raise AssertionError(f"Ожидание {locator} превысило мое терпение")

    def elements(self, locator: tuple):
        try:
            return WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            raise AssertionError(f"Ожидание {locator} превысило мое терпение")

    def product_name_varified(self, product_name):
        return self.element((By.LINK_TEXT, product_name))

    def find_elements(self, locator: tuple):
        try:
            return WebDriverWait(self.driver, 5).until(EC.visibility_of_all_elements_located(locator))
        except TimeoutException:
            raise AssertionError(f"Ожидание {locator} превысило мое терпение")



