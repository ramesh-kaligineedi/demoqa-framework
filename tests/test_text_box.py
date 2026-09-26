from pages.text_box_page import TextBoxPage
def test_text_box(setup):
    driver= setup
    driver.get("https://demoqa.com/text-box")
    textbox=TextBoxPage(driver)
    textbox.enter_fullname("abcd")
    textbox.enter_email("abc@gmail.com")
    textbox.enter_current_address("test1")
    textbox.enter_permanent_address("test2")
    textbox.click_submit() 
    assert "text-box" in driver.current_url   