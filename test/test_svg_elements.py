from playwright.sync_api import Page, expect

def test_svg_elements(page: Page, svg_element_base_url: Page) -> None:
    """
    Test to verify visibility and fill color of SVG elements: <circle>, <rect>, <polygon>.

    Verifies that:
    - A red circle is present and visible.
    - A green rectangle is present and visible.
    - A blue triangle (polygon) is present and visible.
    """

    # Verify <circle>
    circle = page.locator("//div[@class='svg-container']//*[local-name()='svg'][1]//*[local-name()='circle']")
    expect(circle).to_be_visible()
    circle_fill = circle.get_attribute("fill")
    assert circle_fill == "red", f"Expected circle fill 'red', but got '{circle_fill}'"
    print("Circle verified with fill:", circle_fill)

    # Verify <rect>
    rect = page.locator("//div[@class='svg-container']//*[local-name()='svg'][2]//*[local-name()='rect']")
    expect(rect).to_be_visible()
    rect_fill = rect.get_attribute("fill")
    assert rect_fill == "green", f"Expected rectangle fill 'green', but got '{rect_fill}'"
    print("Rectangle verified with fill:", rect_fill)

    # Verify <polygon>
    triangle = page.locator("//div[@class='svg-container']//*[local-name()='svg'][3]//*[local-name()='polygon']")
    expect(triangle).to_be_visible()
    triangle_fill = triangle.get_attribute("fill")
    assert triangle_fill == "blue", f"Expected polygon fill 'blue', but got '{triangle_fill}'"
    print("Polygon verified with fill:", triangle_fill)
