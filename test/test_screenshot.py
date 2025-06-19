import datetime
from playwright.sync_api import sync_playwright

def test_screenshot():
    datestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    """Take a screenshot of the Playwright documentation homepage with a timestamp."""
    with sync_playwright() as p:
        browser = p.webkit.launch()
        page = browser.new_page()
        page.goto("https://playwright.dev/")
        page.screenshot(path="screenshots/playwright_homepage_{}.png".format(datestamp))
        browser.close()