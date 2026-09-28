from pages.page_upload import Upload
import time
import os
def test_practice (setup):
    driver=setup
    driver.get("https://demoqa.com/upload-download")
    obj=Upload(driver)
    # obj.uploadfile(r"C:\Users\kalig\OneDrive\Documents\QA-- Ramesh.K.pdf")
    obj.uploadfile(os.path.abspath("test_data/sample.txt"))
    time.sleep(10)
    # assert "QA-- Ramesh.K.pdf" in obj.get_uploaded_file()
    assert "sample.txt" in obj.get_uploaded_file()
