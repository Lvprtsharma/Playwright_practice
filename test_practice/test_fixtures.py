import pytest
from playwright.sync_api import Page, expect

@pytest.fixture(scope="function", autouse=True)
def before_each_after_each(page: Page):
    
    print("Running before each test case")
    
    page.goto("https://www.google.com")
    yield
    
    print("Running after each test case")
    

@pytest.fixture(scope="module", autouse=True)
def before_all_after_all():
    
    print("Running before all test cases")

    yield
    
    print("Running after all test cases")
    

def test_title(page: Page):
    
    expect(page).to_have_title('Google')
    
def test_url(page: Page):
    
    expect(page).to_have_url('https://www.google.com/')