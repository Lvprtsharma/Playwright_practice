import pytest
from playwright.sync_api import Page, expect

    
def test_draggable(w2a_url: Page) -> None:
    """
    Test drag and drop functionality.
    """
    page = w2a_url
    
    with page.expect_popup() as popup_info:
        page.get_by_alt_text("draggable").click()
    
    new_page = popup_info.value
    
    iframe = new_page.locator("#example-1-tab-1 iframe")
    iframe.wait_for()
    
    frame = iframe.content_frame
    draggable = frame.locator("#draggable")
    draggable.wait_for(state="visible")
    
    # Get initial position
    initial_box = draggable.bounding_box()
    
    # Perform drag
    draggable.drag_to(draggable, target_position={"x": 100, "y": 100})
    
    # Verify the element moved and has positioning CSS
    final_box = draggable.bounding_box()
    final_style = draggable.get_attribute('style')
    
    # Check that position changed
    assert final_box["x"] != initial_box["x"], "X position should have changed"
    assert final_box["y"] != initial_box["y"], "Y position should have changed"
    
    # Check that jQuery UI applied positioning
    assert "inset" in final_style, "Element should have inset positioning after drag"
    
    new_page.close()