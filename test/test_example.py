import re
from playwright.sync_api import Page, expect

def test_example() -> None:
    """
    Simple sanity test to ensure the testing framework is working.
    """
    assert 1 + 1 == 2


def test_has_title(page: Page) -> None:
    """
    Test to verify that the Playwright homepage title contains 'Playwright'.

    Args:
        page (Page): Playwright page fixture injected by pytest-playwright.
    """
    page.goto("https://playwright.dev/")
    expect(page).to_have_title(re.compile("Playwright"))
