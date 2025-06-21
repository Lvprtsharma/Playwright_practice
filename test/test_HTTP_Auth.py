import os
from dotenv import load_dotenv
from playwright.sync_api import Page, expect, Playwright

load_dotenv()

def test_basic_auth(playwright: Playwright) -> None:
    """
    Test basic HTTP authentication by navigating to a page that requires credentials.
    """
    browser = playwright.chromium.launch()
    context = browser.new_context(
        http_credentials={
            "username": os.getenv("BASIC_AUTH_USERNAME"),
            "password": os.getenv("BASIC_AUTH_PASSWORD")
        }
    )
    page = context.new_page()
    try:
        page.goto(os.getenv("BASIC_AUTH_URL"))
        expect(page.get_by_text("Congratulations! You must have the proper credentials.")).to_be_visible()
        page.wait_for_timeout(2000)
    finally:
        page.close()
        context.close()
        browser.close()
        

def test_network_events(playwright: Playwright):
    chromium = playwright.chromium
    browser = chromium.launch()
    context = browser.new_context(
        http_credentials={
            "username": os.getenv("BASIC_AUTH_USERNAME"),
            "password": os.getenv("BASIC_AUTH_PASSWORD")
        }
    )
    page = context.new_page()
    try:
        page = browser.new_page()
        page.on("request", lambda request: print("REQUEST >>>>>> ", request.method, request.url))
        page.on("response", lambda response: print("RESPONSE <<<<< ", response.status, response.url, response.body))
        page.goto(os.getenv("BASIC_AUTH_URL"))
    finally:
        page.close()
        context.close()
        browser.close()
