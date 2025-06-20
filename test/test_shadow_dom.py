from playwright.sync_api import Page, expect

def test_shadow_dom(page: Page, shadow_dom_url: Page) -> None:
    """
    Test interacting with an input field inside a shadow DOM.

    Verifies that the 'Search Books' input can be filled.
    """
    search_input = page.get_by_label("Search Books")
    search_input.fill("Playwright")
    expect(search_input).to_have_value("Playwright")
