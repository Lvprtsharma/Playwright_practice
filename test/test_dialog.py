import pytest
from playwright.sync_api import Page, expect

text_alert = []

def handle_alert(dialog) -> None:
    """
    Handles a JavaScript alert dialog by accepting it and capturing the message.
    """
    text_alert.append(dialog.message)
    dialog.accept()


def handle_confirm_dialog(dialog) -> None:
    """
    Handles a JavaScript confirmation dialog by accepting it and capturing the message.
    """
    text_alert.append(dialog.message)
    dialog.accept()


def handle_prompt_dialog(dialog) -> None:
    """
    Handles a JavaScript prompt dialog by accepting it with a custom value.
    """
    text_alert.append(dialog.message)
    dialog.accept("Hello, World!")


def test_alert_auto_handle(page: Page, dialog_base_url: Page) -> None:
    """
    Automatically handles a JS alert dialog and checks the result text on the page.
    """
    text_alert.clear()
    page.get_by_text("Click for JS Alert").click()
    expect(page.get_by_text("You successfully clicked an alert")).to_be_visible()


def test_alert_manual_handle(page: Page, dialog_base_url: Page) -> None:
    """
    Manually handles a JS alert dialog using an event handler and verifies the message.
    """
    text_alert.clear()
    page.on("dialog", handle_alert)
    page.get_by_text("Click for JS Alert").click()
    assert text_alert[0] == "I am a JS Alert", "Alert message should match expected text"
    expect(page.get_by_text("You successfully clicked an alert")).to_be_visible()


def test_confirm_dialog(page: Page, dialog_base_url: Page) -> None:
    """
    Handles a JS confirm dialog using an event handler and verifies the result.
    """
    text_alert.clear()
    page.on("dialog", handle_confirm_dialog)
    page.get_by_text("Click for JS Confirm").click()
    assert text_alert[0] == "I am a JS Confirm", "Confirm dialog message should match expected text"
    expect(page.get_by_text("You clicked: Ok")).to_be_visible()


def test_prompt_dialog(page: Page, dialog_base_url: Page) -> None:
    """
    Handles a JS prompt dialog by entering a value and verifying the result.
    """
    text_alert.clear()
    page.on("dialog", handle_prompt_dialog)
    page.get_by_text("Click for JS Prompt").click()
    expect(page.get_by_text("You entered: Hello, World!")).to_be_visible()
    assert text_alert[0] == "I am a JS prompt", "Prompt dialog message should match expected text"
