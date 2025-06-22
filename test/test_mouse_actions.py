from playwright.sync_api import Page, expect


def test_hover(openqa_url: Page) -> None:
    """
    Test interaction with dropdowns that are not standard <select> elements.
    """
    page = openqa_url

    page.get_by_role("heading", name="Forms").click()
    page.get_by_text("Widgets").click()
    page.get_by_text("Menu", exact=True).click()
    
    page.get_by_role("link", name="Main Item 2").hover()

    expect(page.get_by_role("link", name="SUB SUB LIST »")).to_be_visible() 