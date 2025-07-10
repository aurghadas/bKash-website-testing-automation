import re
import pytest
from playwright.sync_api import Page, expect

BASE = "https://demoqa.com"

@pytest.fixture(autouse=True)
def go_home(page: Page):
    # always start from the home page
    page.goto(BASE)
    yield

def test_text_box_submission(page: Page):
    # Navigate directly to the form
    page.goto(f"{BASE}/text-box")
    # Fill in the form
    page.fill("#userName", "Aurgha Das")
    page.fill("#userEmail", "aurghadas04@gmail.com")
    page.fill("#currentAddress", "Uttara, Dhaka")
    page.fill("#permanentAddress", "Barishal, Bangladesh")
    # Submit and verify the output panel
    page.click("#submit")
    output = page.locator("#output")
    expect(output.locator("#name")).to_have_text("Name:Aurgha Das")
    expect(output.locator("#email")).to_have_text("Email:aurghadas04@gmail.com")
    expect(output).to_contain_text("Uttara, Dhaka")
    expect(output).to_contain_text("Barishal, Bangladesh")

def test_radio_button_and_checkbox(page: Page):
    # Radio buttons
    page.goto(f"{BASE}/radio-button")
    page.click("label[for='impressiveRadio']")
    expect(page.locator(".text-success")).to_have_text("Impressive")

    # Checkboxes
    page.goto(f"{BASE}/checkbox")
    # expand Home and select Desktop
    page.click("button[title='Expand all']")
    page.check("label[for='tree-node-desktop'] span.rct-checkbox")
    expect(page.locator(".display-result")).to_contain_text("desktop")



    '''def test_example(page: Page) -> None:
    page.goto("https://dev.bkash.com/")
    page.locator("iframe[name=\"reve-chat-widget-holder\"]").content_frame.locator("#reve-chat-widget-body #chat-window-background2 div").filter(has_text="Minimize").click()
    page.get_by_role("button", name="English").click()

    page.goto("https://dev.bkash.com/en/help")
    
    page.get_by_role("link", name="charge calculator_en Charge").click()
    page.get_by_role("combobox", name="Select Service").click()
    page.get_by_role("option", name="Cash Out - To Non Priyo Agent").click()
    page.get_by_role("spinbutton", name="Amount (BDT)").click()
    page.get_by_role("spinbutton", name="Amount (BDT)").fill("1000")
    page.get_by_text("Amount (BDT) Calculate").click()
    page.get_by_role("button", name="Calculate").click()
    page.get_by_role("link", name="bKash Logo").click()'''
