import pytest
from playwright.sync_api import Page, expect

def test_checkbox(internet_herokuapp_url: Page) -> None:
    """
    Test interaction with checkbox elements.
    """
    page = internet_herokuapp_url
    
    # Check the checkbox
    checkboxes_link = page.get_by_role("link", name="Checkboxes")
    checkboxes_link.click()

    page.wait_for_url("**/checkboxes")

    # Use more specific selectors for checkboxes
    checkbox1 = page.locator("input[type='checkbox']").nth(0)
    checkbox2 = page.locator("input[type='checkbox']").nth(1)

    # Test first checkbox
    checkbox1.check()
    expect(checkbox1).to_be_checked()

    # Uncheck the checkbox
    checkbox1.uncheck()
    expect(checkbox1).not_to_be_checked()

    # Test second checkbox (it's usually pre-checked on the herokuapp)
    if checkbox2.is_checked():
        checkbox2.uncheck()
        expect(checkbox2).not_to_be_checked()
    else:
        checkbox2.check()
        expect(checkbox2).to_be_checked()