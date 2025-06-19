import pytest
from playwright.sync_api import Page

@pytest.fixture(scope="function")
def open_page(page):
    page.goto("https://testautomationpractice.blogspot.com/p/playwrightpractice.html")
    yield page
    page.close()  # Ensure the page is closed after the test completes
    
@pytest.fixture(scope="function")
def shadow_dom_url(page: Page):
    """Fixture to open a custom URL."""
    page.goto("https://books-pwakit.appspot.com/")
    yield page
    page.close()