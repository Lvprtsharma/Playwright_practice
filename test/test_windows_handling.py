from playwright.sync_api import Page

def test_handle_new_window_using_frame_locator(w2a_url: Page) -> None:
    """
    Test handling new tabs in Playwright.
    """
    page = w2a_url
    
    with page.expect_popup() as popup_info:
        page.get_by_alt_text("frames-and-windows").click()
    
    new_window = popup_info.value
    
    iframe = new_window.locator("#example-1-tab-1 iframe")
    iframe.wait_for()
    frame = iframe.content_frame
    
    frame.get_by_text("New Browser Tab").highlight()


def test_handle_new_window_using_frame(w2a_url: Page) -> None:
    """
    Test handling new tabs in Playwright.
    """
    page = w2a_url
    
    with page.expect_popup() as popup_info:
        page.get_by_alt_text("frames-and-windows").click()
    
    new_window = popup_info.value
    
    # Wait for the new window to load
    new_window.wait_for_load_state("networkidle")
    
    # Get frame by URL (fix typo if needed)
    iframe = new_window.frame(url="frames-windows/default1.html")
    
    # Check if frame exists before interacting
    if iframe:
        iframe.locator("a", has_text="New Browser Tab").highlight()
    else:
        print("Frame not found")
    