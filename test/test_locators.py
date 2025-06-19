from playwright.sync_api import expect, Playwright

def test_implicit_role(page, open_page):
    """Click a button with an implicit role (<button>)."""
    page.get_by_role("button", name='Toggle Button').click()

def test_explicit_role(page, open_page):
    """Interact with elements that use explicit ARIA roles."""
    page.get_by_role("button", name='Div with button role').highlight()
    checkbox = page.get_by_role("checkbox", name='Accept terms')
    checkbox.check()
    expect(checkbox).to_be_checked()
    page.get_by_role("alert", name='This is an important alert message!').highlight()

def test_label(page, open_page):
    """Interact with elements that use labels."""
    page.get_by_label("email").fill("John Doe")
    page.get_by_label("password").fill("ada")
    page.get_by_label("Your Age:").fill("30")
    page.get_by_label("Standard").click()
    page.get_by_label("Express").click()
    

def test_placeholder(page, open_page):
    """Interact with elements that use labels."""
    page.get_by_placeholder("Enter your full name").fill("John Doe")
    page.get_by_placeholder("Phone number (xxx-xxx-xxxx)").fill("9879879879")
    page.get_by_placeholder("Type your message here...").fill("This is a test message.")
    page.get_by_placeholder("Search products...").fill("Laptop")


def test_alt_text(page, open_page):
    """Interact with elements that use alt text."""
    page.get_by_alt_text("logo image").highlight()
    expect(page.get_by_alt_text("logo image")).to_be_visible()

def test_text(page, open_page):
    """Interact with elements that use text."""
    page.get_by_text("Submit Form").click()
    page.get_by_text("List item 1").highlight()
    page.get_by_text("Special: Unique text identifier", exact=True).highlight()
    
def test_titles(page, open_page):
    """Interact with elements that use title."""
    page.get_by_title("Home page link").click()
    page.get_by_title("HyperText Markup Language").highlight()
    expect(page.get_by_title("Tooltip text")).to_be_visible()
    page.get_by_title("Click to save your changes").click()
    
def test_testid(page, open_page):
    """Interact with elements that use data-testid."""
    page.get_by_test_id("edit-profile-btn").click()
    first_product_name = page.get_by_test_id("product-card-1").get_by_test_id("product-name").text_content()
    assert first_product_name == "Product A", f"Expected 'Product A', but got '{first_product_name}'"
    
    product_names = page.get_by_test_id("product-name").all_text_contents()
    assert len(product_names) > 0, "No product names found"
    assert "Product A" in product_names, "Product A not found in product names"

    page.get_by_test_id("nav-contact").click()


def test_custom_testid(page, open_page, playwright: Playwright):
    """Interact with elements that use custom data-testid."""
    playwright.selectors.set_test_id_attribute(attribute_name="data-pw")
    profile_name = page.get_by_test_id("profile-name").text_content()
    assert profile_name == "John Doe", f"Expected 'John Doe', but got '{profile_name}'"
    
def test_shadow_dom(page, shadow_dom_url):
    """Interact with elements in a shadow DOM."""
    page.get_by_label("Search Books").fill("Playwright")