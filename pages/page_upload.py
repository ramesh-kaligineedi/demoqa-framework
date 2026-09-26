from selenium import webdriver
from selenium.webdriver.common.by import By

class Upload:
    def __init__(self,driver):
        self.driver=driver

    file= (By.ID,"uploadFile")
    uploaded_file = (By.ID, "uploadedFilePath")

    def uploadfile(self, path):
        self.driver.find_element(*self.file).send_keys(path)

    def get_uploaded_file(self):
        return self.driver.find_element(*self.uploaded_file).text       