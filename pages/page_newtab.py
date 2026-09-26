from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class NewTab:

    new_tab = (By.ID, "tabButton")

    def __init__(self, driver):
        self.driver = driver

    def click_new_tab(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.new_tab)
        ).click()
    time.sleep(10)   
