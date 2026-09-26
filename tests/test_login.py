from pages.login_page import LoginPage
import time
def test_login (setup):
    driver=setup
    driver.get("https://demoqa.com/login")
    object=LoginPage(driver)
    object.USER("test@123")
    object.PASW("Admin@123")
    object.loginButton()
    assert "login" in driver.current_url.lower()

    actual = object.get_error_message()

    expected = "Invalid username or password!"

    assert actual == expected