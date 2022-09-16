import pytest
import os

from selenium import webdriver

DRIVERS = os.path.expanduser("C:/Drivers")


def pytest_addoption(parser):
    parser.addoption(
        "--base_url", default="http://192.168.0.105:8081/", help="default ip"
    )

@pytest.fixture
def browser(request):
    base_url = request.config.getoption("--base_url")

    driver = webdriver.Chrome(
        executable_path=os.path.expanduser(f"{DRIVERS}/chromedriver")
    )

    driver.maximize_window()

    driver.get(base_url)

    driver.base_url = base_url

    driver.implicitly_wait(5)

    yield driver

    driver.close()
