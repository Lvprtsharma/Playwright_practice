import os
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright

load_dotenv()

def open_google_page(headless: bool = True) -> None:
    """
    Launches a Chromium browser, navigates to Google, and prints the page title.

    Args:
        headless (bool): Whether to run the browser in headless mode.
                         Set to False to see the browser window.
    """
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=headless)
        page = browser.new_page()
        page.goto(os.getenv("GOOGLE_URL"))
        print("Page Title (Headless =", headless, "):", page.title())
        browser.close()

# Headless mode (no browser UI)
open_google_page(headless=True)

# Headed mode (visible browser UI)
open_google_page(headless=False)
