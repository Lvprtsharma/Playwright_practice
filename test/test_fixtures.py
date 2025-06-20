import os
from dotenv import load_dotenv
import pytest
from playwright.sync_api import Page, expect, BrowserContext

load_dotenv()


@pytest.fixture(scope="function", autouse=True)
def before_each_after_each(page: Page) -> None:
    """
    Fixture that runs before and after each test function.
    """
    print("Running before each test case")
    yield
    print("Running after each test case")


@pytest.fixture(scope="module", autouse=True)
def before_all_after_all() -> None:
    """
    Fixture that runs once before all tests in the module and once after all tests.
    """
    print("Running before all test cases")
    yield
    print("Running after all test cases")


def test_title(page: Page) -> None:
    """
    Test that verifies the title of the Google homepage.
    """
    page.goto(os.getenv("GOOGLE_URL"))
    expect(page).to_have_title("Google")


def test_url(page: Page) -> None:
    """
    Test that verifies the current URL after navigation.
    """
    page.goto(os.getenv("GOOGLE_URL"))
    expect(page).to_have_url("https://www.google.com/")


def test_search_box(context: BrowserContext) -> None:
    """
    Test that verifies the visibility and input capability of the search box on Google.
    """
    with context.new_page() as page:
        page.goto(os.getenv("GOOGLE_URL"))
        search_box = page.locator("textarea[name='q']")
        expect(search_box).to_be_visible()
        search_box.fill("Playwright")
        expect(search_box).to_have_value("Playwright")


def test_browser_context(context: BrowserContext) -> None:
    """
    Test that performs multiple validations using a new browser context page.
    """
    with context.new_page() as page:
        page.goto(os.getenv("GOOGLE_URL"))
        expect(page).to_have_title("Google")
        expect(page).to_have_url("https://www.google.com/")

        # Check the search box
        search_box = page.locator("textarea[name='q']")
        expect(search_box).to_be_visible()
        search_box.fill("Playwright")
        expect(search_box).to_have_value("Playwright")


@pytest.mark.browser_context_args(timezone_id="Europe/Berlin", locale="en-GB")
def test_browser_context_args(page: Page) -> None:
    """
    Test to validate the browser's locale and timezone using browser_context_args.
    """
    assert page.evaluate("window.navigator.languages") == ["en-GB"]
