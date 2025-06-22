from playwright.sync_api import Page, expect

def test_dropdown_non_select_type(openqa_url: Page) -> None:
    """
    Test interaction with dropdowns that are not standard <select> elements.
    """
    page = openqa_url

    page.get_by_role("heading", name="Forms").click()
    page.get_by_text("Practice Form").click()
    
    page.locator(".subjects-auto-complete__input > input").fill("m")
    page.get_by_text("Maths", exact=True).click()

    expect(page.locator(".subjects-auto-complete__multi-value").filter(has_text="Maths")).to_be_visible()
    
    

