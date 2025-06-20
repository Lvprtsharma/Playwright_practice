import os
from dotenv import load_dotenv
from playwright.sync_api import Playwright, expect

load_dotenv()

def test_hidden_elements(playwright: Playwright, orangehrm_context_args: dict) -> None:
    """
    Test interacting with hidden and dynamic dropdown elements on the OrangeHRM site.

    Steps:
    - Log in to OrangeHRM.
    - Navigate to the PIM section.
    - Open the job title dropdown.
    - Select 'QA Lead' from the list.
    - Assert that 'QA Lead' is visible after selection.
    """
    browser = playwright.chromium.launch()
    context = browser.new_context(**orangehrm_context_args)
    page = context.new_page()

    page.goto(os.getenv("HRM_DASHBOARD_URL"))
    expect(page.get_by_role("heading", name="Dashboard")).to_be_visible()

    # Navigate to PIM > Job Title dropdown
    page.locator("ul.oxd-main-menu").get_by_role("link", name="PIM").click()
    page.locator(
        "div:nth-child(6) > .oxd-input-group > div:nth-child(2) > "
        ".oxd-select-wrapper > .oxd-select-text"
    ).click()
    
    page.wait_for_timeout(500)  # Wait for dropdown to be ready

    # Select 'QA Lead' from dropdown
    list_items = page.locator("//div[@role='listbox']//div")
    count = list_items.count()
    print("List items count:", count)

    found = False
    for i in range(count):
        item = list_items.nth(i)
        text = item.text_content()
        print(f"Item {i + 1}: {text}")
        if text == "QA Lead":
            item.click()
            found = True
            break


    assert found, "'QA Lead' option not found in the dropdown"

    # Wait until QA Lead is selected visibly
    expect(page.locator("//div[contains(text(),'QA Lead')]")).to_be_visible()
