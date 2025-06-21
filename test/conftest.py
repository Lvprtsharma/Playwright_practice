import os
import pytest
from typing import Generator
from dotenv import load_dotenv
from playwright.sync_api import Page, Playwright

load_dotenv()

@pytest.fixture(scope="function")
def open_page(page: Page) -> Generator[Page, None, None]:
    """
    Fixture to open the Playwright practice page.

    Navigates to a test automation practice page before the test
    and closes the page after the test completes.
    """
    page.goto(os.getenv("BLOGSPOT_URL"))
    yield page
    page.close()


@pytest.fixture(scope="function")
def shadow_dom_url(page: Page) -> Generator[Page, None, None]:
    """
    Fixture to open a Shadow DOM sample page.

    Useful for testing interactions with shadow DOM components.
    """
    page.goto(os.getenv("SHADOW_DOM_URL"))
    yield page
    page.close()


@pytest.fixture(scope="function")
def hidden_element_base_url(page: Page) -> Generator[Page, None, None]:
    """
    Fixture to open the OrangeHRM login page.

    Useful for testing hidden or dynamic elements on login forms.
    """
    page.goto(os.getenv("HRM_LOGIN_URL"))
    yield page
    page.close()


@pytest.fixture(scope="function")
def pseudo_element_base_url(page: Page) -> Generator[Page, None, None]:
    """
    Fixture to open a registration page with pseudo-elements.

    Useful for testing form fields and CSS pseudo-element behavior.
    """
    page.goto(os.getenv("NAL_REGISTER"))
    yield page
    page.close()


@pytest.fixture(scope="function")
def svg_element_base_url(page: Page) -> Generator[Page, None, None]:
    """
    Fixture to open a page containing SVG elements.

    Useful for testing interactions with SVG shapes and graphics.
    """
    page.goto(os.getenv("SVG_ELE_URL"))
    yield page
    page.close()


@pytest.fixture(scope="session")
def orangehrm_context_args(browser_context_args: dict) -> dict:
    """
    Fixture to set up browser context with a predefined storage state
    for the OrangeHRM site.

    This allows tests to bypass login by using a saved session.
    """
    return {
        **browser_context_args,
        "storage_state": "../playwright/.auth/orangeHRM.json"
    }


@pytest.fixture(scope="function")
def dialog_base_url(page: Page) -> Generator[Page, None, None]:
    """
    Fixture to open a page containing alert(), confirm(), prompt() dialogs elements.

    Useful for testing interactions with alert(), confirm(), prompt() dialogs.
    """
    page.goto(os.getenv("ALERT_URL"))
    yield page
    page.close()
    
@pytest.fixture(scope="function")
def iframe_base_url(page: Page) -> Generator[Page, None, None]:
    """
    Fixture to open a page containing an iframe.

    Useful for testing interactions with iframe elements.
    """
    page.goto(os.getenv("IFRAME_URL"))
    yield page
    page.close()

@pytest.fixture(scope="function")
def auth_base_url(playwright: Playwright) -> Generator[Page, None, None]:
    """
    Fixture to launch a Chromium browser with HTTP Basic Authentication.

    This fixture is useful for scenarios requiring HTTP Basic Auth,
    such as accessing a protected page with credentials from environment variables.
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
        yield page
    finally:
        page.close()
        context.close()
        browser.close()