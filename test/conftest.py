import os
import pytest
from typing import Generator
from dotenv import load_dotenv
from playwright.sync_api import Page

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
