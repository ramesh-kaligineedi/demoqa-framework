from pages.page_newtab import NewTab
import time

def test_newtab(setup):
    driver = setup
    driver.get("https://demoqa.com/browser-windows")

    browser = NewTab(driver)

    # Parent Window
    parent_window = driver.current_window_handle

    # Click New Tab
    browser.click_new_tab()

    # All opened windows/tabs
    all_windows = driver.window_handles

    # Switch to New Tab
    for window in all_windows:
        if window != parent_window:
            driver.switch_to.window(window)
            break

    print("Title :", driver.title)
    print("URL :", driver.current_url)

    # Close New Tab
    driver.close()

    # Back to Parent
    driver.switch_to.window(parent_window)

    print("Back to Parent :", driver.title)
    time.sleep(10)
    # browser.click_new_tab()

    # time.sleep(5)