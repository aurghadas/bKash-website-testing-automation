from playwright.sync_api import Page
import pytest
import test

#@pytest.mark.skip_browser("chromium")
#@pytest.mark.only_browser("chromium")
def test_title(page: Page):
    # Navigate to the login page
    page.goto("/", wait_until="networkidle")
    # Call the title() method (not the attribute) and compare
    assert page.title() == "Swag Labs"

def test_inventory_site(page: Page):
    page.goto("/inventory.html")
    assert page.inner_text('h3') == "Epic sadface: You can only access '/inventory.html' when you are logged in."