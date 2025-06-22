import pytest
import random
import string
import uuid


def generate_random_email():
    """
    Generate a random email address.
    """
    random_string = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
    random_domain = ''.join(random.choices(string.ascii_lowercase, k=5)) + ".com"
    return f"{random_string}@{random_domain}"

@pytest.mark.parametrize(
    "username, lastname",
    [
        ("testuser1", "TestLast1"),
        ("testuser2", "TestLast2"),
        ("testuser3", "TestLast3"),
        ("testuser4", "TestLast4")
    ]
)
def test_registration_form(page, username, lastname, ) -> None:
    """
    Test filling out a registration form with various input types.
    """
    page.goto("https://demo.nopcommerce.com/register?returnUrl=%2F")
    
    # page.locator("#gender-male").check()
    page.fill("#FirstName", username)
    page.fill("#LastName", lastname)
    page.locator("#Email").fill(generate_random_email())
    page.locator("#Company").fill("Test Company")
    page.locator("#Newsletter").check()
    page.locator("#Password").fill("Test@1234")
    page.locator("#ConfirmPassword").fill("Test@1234")  
    page.get_by_role("button", name="Register").click()
    page.wait_for_timeout(2000)
    
    # page.locator("#gender-male").check()
    # page.locator("//input[@id='FirstName']").fill(username)
    # page.locator("//input[@id='LastName']").fill(lastname)
    # page.locator("#Email").fill(generate_random_email())
    
    # page.locator("#Company").fill("Test Company")

    # page.locator("#Newsletter").check()
    # page.locator("#Password").fill("Test@1234")
    # page.locator("#ConfirmPassword").fill("Test@1234")
    # page.get_by_role("button", name="Register").click()
    # page.wait_for_timeout(2000)