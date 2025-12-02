import allure
from allure_commons.types import AttachmentType


def add_screenshot(browser):
    screenshot = browser.driver.get_screenshot_as_png()
    allure.attach(
        screenshot,
        name="Screenshot",
        attachment_type=AttachmentType.PNG
    )


def add_page_source(browser):
    page_source = browser.driver.page_source
    allure.attach(
        page_source,
        name="Page Source",
        attachment_type=AttachmentType.HTML
    )


def add_browser_logs(browser):
    logs = browser.driver.get_log("browser")
    log_text = "\n".join([f"{log['level']}: {log['message']}" for log in logs])
    allure.attach(
        log_text,
        name="Browser Logs",
        attachment_type=AttachmentType.TEXT
    )


def add_video(session_id):
    video_url = (
        f"https://selenoid.autotests.cloud/video/{session_id}.mp4"
    )

    allure.attach(
        f'<html><body><video width="100%" height="100%" controls>'
        f'<source src="{video_url}" type="video/mp4"></video></body></html>',
        name="Video",
        attachment_type=AttachmentType.HTML,
        extension=".html"
    )
