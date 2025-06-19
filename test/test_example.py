import re
from playwright.sync_api import Page, expect, sync_playwright

def test_example():
    assert 1 + 1 == 2


def test_has_title(page: Page):
    page.goto('https://playwright.dev/')

    expect(page).to_have_title(re.compile("Playwright"))


