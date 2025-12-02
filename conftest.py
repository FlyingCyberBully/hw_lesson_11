import pytest
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from utils.attach import (
    add_screenshot,
    add_logs,
    add_html,
    add_video
)


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    options = Options()
    options.set_capability("browserName", "chrome")
    options.set_capability("browserVersion", "100.0")
    options.set_capability(
        "selenoid:options",
        {
            "enableVNC": True,
            "enableVideo": True,
        }
    )

    driver = webdriver.Remote(
        command_executor=f"https://user1:1234@selenoid.autotests.cloud/wd/hub",
        options=options
    )

    browser.config.driver = driver
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.config.base_url = "https://demoqa.com"
    browser.config.timeout = 6

    yield

    add_screenshot()
    add_html()
    add_logs()
    add_video(driver.session_id)

    browser.quit()
