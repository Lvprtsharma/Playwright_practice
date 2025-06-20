import os
from dotenv import load_dotenv
from playwright.sync_api import Playwright, expect
import pytest

load_dotenv()


@pytest.mark.skipif(os.getenv("HRM_DASHBOARD_URL") is None, reason="HRM_DASHBOARD_URL not set in .env")
def test_orangehrm_dashboard(playwright: Playwright, orangehrm_context_args: dict) -> None:
    """
    Test to verify that the OrangeHRM dashboard page loads and the 'Dashboard' heading is visible.

    Args:
        playwright (Playwright): Playwright instance injected by pytest-playwright.
        orangehrm_context_args (dict): Context arguments including storage state for login.
    """
    browser = playwright.chromium.launch()
    context = browser.new_context(**orangehrm_context_args)
    page = context.new_page()

    try:
        page.goto(os.getenv("HRM_DASHBOARD_URL"))
        expect(page.get_by_role("heading", name="Dashboard")).to_be_visible()
    finally:
        browser.close()


@pytest.mark.skipif(os.getenv("HRM_DASHBOARD_URL") is None, reason="HRM_DASHBOARD_URL not set in .env")
def test_admin_page(playwright: Playwright, orangehrm_context_args: dict) -> None:
    """
    Test to verify navigation to the Admin page from the OrangeHRM dashboard and check heading visibility.

    Args:
        playwright (Playwright): Playwright instance injected by pytest-playwright.
        orangehrm_context_args (dict): Context arguments including storage state for login.
    """
    browser = playwright.chromium.launch()
    context = browser.new_context(**orangehrm_context_args)
    page = context.new_page()

    try:
        page.goto(os.getenv("HRM_DASHBOARD_URL"))
        page.locator("ul.oxd-main-menu").get_by_role("link", name="Admin").click()
        expect(page.get_by_role("heading", name="Admin")).to_be_visible()
    finally:
        browser.close()
