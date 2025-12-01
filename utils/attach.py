import allure
from allure_commons.types import AttachmentType
from selene import browser


def add_screenshot():
    png = browser.driver.get_screenshot_as_png()
    allure.attach(png, "Screenshot", AttachmentType.PNG)


def add_html():
    html = browser.driver.page_source
    allure.attach(html, "Page Source", AttachmentType.HTML)


def add_logs():
    logs = browser.driver.get_log("browser")
    allure.attach(
        "\n".join([l["message"] for l in logs]),
        "Browser Console Logs",
        AttachmentType.TEXT
    )


def add_video(session_id):
    video_url = (
        f"https://selenoid.autotests.cloud/video/{session_id}.mp4"
    )

    allure.attach(
        f'<html><body><video width="100%" controls>'
        f'<source src="{video_url}" type="video/mp4">'
        '</video></body></html>',
        "Video",
        AttachmentType.HTML,
        extension=".html"
    )
