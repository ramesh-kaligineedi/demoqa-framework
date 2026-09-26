from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class LoginPage:
    def __init__(self,driver):
        self.driver=driver

    username=(By.ID,"userName")
    password=(By.ID,"password")
    login=(By.ID,"login")
    error_msg=(By.XPATH,"//p[@id='name']")

    def USER(self,users):
        self.driver.find_element(*self.username).send_keys(users)
    def PASW(self,paswd):
        self.driver.find_element(*self.password).send_keys(paswd)
    def loginButton(self):
        self.driver.find_element(*self.login).click()        
    def get_error_message(self):
        return WebDriverWait(self.driver, 10).until(
          EC.visibility_of_element_located(self.error_msg)
        ).text       
