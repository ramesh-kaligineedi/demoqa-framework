from pages.register_page import RegisterPage

def test_register(setup):

    driver = setup

    driver.get("https://demoqa.com/register")

    obj = RegisterPage(driver)

    obj.firstName("Ramesh")
    obj.lastName("Kaligineedi")
    obj.userName("ramesh123")
    obj.passwordField("Admin@123")
    assert "register" in driver.current_url.lower()