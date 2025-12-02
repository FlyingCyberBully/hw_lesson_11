import allure
from allure_commons.types import AttachmentType


def add_screenshot(browser):
    png = browser.driver.get_screenshot_as_png()
    allure.attach(png, name='Screenshot', attachment_type=AttachmentType.PNG)


def add_logs(browser):
    log = "".join(f"{entry['level']} - {entry['message']}\n"
                  for entry in browser.driver.get_log('browser'))
    allure.attach(log, name="Browser logs", attachment_type=AttachmentType.TEXT)


def add_html(browser):
    html = browser.driver.page_source
    allure.attach(html, name='Page source', attachment_type=AttachmentType.HTML)


def add_video(browser):
    video_url = (
        f"https://selenoid.autotests.cloud/video/{browser.driver.session_id}.mp4"
    )
    allure.attach(
        f'<html><body><video width="100%" controls>'
        f'<source src="{video_url}" type="video/mp4">'
        f'</video></body></html>',
        name='Video',
        attachment_type=AttachmentType.HTML,
        extension='.html'
    )
