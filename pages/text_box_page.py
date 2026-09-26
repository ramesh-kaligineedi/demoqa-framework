from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TextBoxPage:

    def __init__(self, driver):
        self.driver = driver

    fullname = (By.ID, "userName")
    email = (By.ID, "userEmail")
    currentaddress = (By.ID, "currentAddress")
    permanentaddress = (By.ID, "permanentAddress")
    submit = (By.ID, "submit")
    

    def enter_fullname(self, name):
        self.driver.find_element(*self.fullname).send_keys(name)

    def enter_email(self, mail):
        self.driver.find_element(*self.email).send_keys(mail)
        wait= WebDriverWait(self.driver,10)
        wait.until(
            EC.visibility_of_element_located(self.email)
        ).send_keys(mail)

    def enter_current_address(self, address):
        self.driver.find_element(*self.currentaddress).send_keys(address)

    def enter_permanent_address(self, address):
        self.driver.find_element(*self.permanentaddress).send_keys(address)

    def click_submit(self):
        self.driver.execute_script("window.scrollBy(0,500)")
        time.sleep(10)
        self.driver.find_element(*self.submit).click()