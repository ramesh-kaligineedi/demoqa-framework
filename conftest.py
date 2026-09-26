# import pytest
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager

# @pytest.fixture
# def setup():
#     driver=webdriver.Chrome(
#         service=Service(ChromeDriverManager().install())
#     )
#     driver.maximize_window()
#     driver.implicitly_wait(30)
#     # driver.get("https://demoqa.com/text-box")
#     driver.implicitly_wait(30)

#     yield driver
#     driver.quit()

import pytest
from selenium import webdriver

@pytest.fixture()
def setup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()