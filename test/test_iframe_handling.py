from playwright.sync_api import Page, expect, Playwright

def test_nested_frame(page: Page, iframe_base_url: Page) -> None:
    """
    Test interaction with an iframe element.
    """
    
    # Locate the iframe by its name or id
    mf = page.main_frame  # Get the main frame of the page
    for child in mf.child_frames:
        print("Child frame URL:", child.url)
        print("Child frame name:", child.name)
