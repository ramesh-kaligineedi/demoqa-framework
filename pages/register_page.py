from selenium.webdriver.common.by import By

class RegisterPage:

    firstname = (By.ID, "firstname")
    lastname = (By.ID, "lastname")
    username = (By.ID, "userName")
    password = (By.ID, "password")

    def __init__(self, driver):
        self.driver = driver

    def firstName(self, fname):
        self.driver.find_element(*self.firstname).send_keys(fname)

    def lastName(self, lname):
        self.driver.find_element(*self.lastname).send_keys(lname)

    def userName(self, uname):
        self.driver.find_element(*self.username).send_keys(uname)

    def passwordField(self, pwd):
        self.driver.find_element(*self.password).send_keys(pwd)