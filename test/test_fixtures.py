import pytest
from playwright.sync_api import Page, expect, BrowserContext

@pytest.fixture(scope="function", autouse=True)
def before_each_after_each(page: Page):
    
    print("Running before each test case")
    
    print("Running after each test case")
    

@pytest.fixture(scope="module", autouse=True)
def before_all_after_all():
    
    print("Running before all test cases")

    yield
    
    print("Running after all test cases")
    

def test_title(page: Page):
    
    page.goto("https://www.google.com")
    expect(page).to_have_title('Google')
    
def test_url(page: Page):

    page.goto("https://www.google.com")
    expect(page).to_have_url('https://www.google.com/')

# This test checks if the search box is visible and can be filled with text
def test_search_box(context: BrowserContext):
        with context.new_page() as page:
            page.goto("https://www.google.com")
            search_box = page.locator("textarea[name='q']")
            expect(search_box).to_be_visible()
            search_box.fill("Playwright")
            expect(search_box).to_have_value("Playwright")
            

def test_browser_context(context: BrowserContext):
    with context.new_page() as page:
        page.goto("https://www.google.com")
        expect(page).to_have_title("Google")
        expect(page).to_have_url("https://www.google.com/")
        
        # Check if the search box is present
        search_box = page.locator("textarea[name='q']")
        expect(search_box).to_be_visible()
        
        # Fill the search box and check its value
        search_box.fill("Playwright")
        expect(search_box).to_have_value("Playwright")
    
@pytest.mark.browser_context_args(timezone_id="Europe/Berlin", locale="en-GB")
def test_browser_context_args(page):
    assert page.evaluate("window.navigator.languages") == ["en-GB"]