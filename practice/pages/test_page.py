import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

class Ramesh:
    def __init__(self,driver):
        self.driver= driver;

    box1=(By.XPATH,"")
    box2=(By.XPATH,"")

    def   boxone (self,obe):
        self.driver.find_element(*self.box1).send_keys(obe)

