import pytest

from selenium import webdriver
from selenium.webdriver.firefox.options import Options


@pytest.fixture(scope="function")
def driver():
    try:
        options = Options()
        options.add_argument("--start-maximized")
        driver = webdriver.Firefox(options=options)
        yield driver
        driver.quit()

    except Exception as e:
        print(f"Error type: {type(e).__name__}, message: {e}")
