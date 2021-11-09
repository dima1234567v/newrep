from selenium.webdriver.chrome.options import Options


import pytest
import time
import math
from selenium import webdriver




@pytest.fixture(scope="function")
def browser():

    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    time.sleep(3)
    browser.quit()


