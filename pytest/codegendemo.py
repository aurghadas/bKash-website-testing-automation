import re
from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("https://www.saucedemo.com/", wait_until="networkidle")
    page.fill("[data-test=username]", "standard_user")
    page.fill("[data-test=password]", "secret_sauce")
    page.click("[data-test=login-button]")
    # verify that we landed on the inventory page:

    # or:
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
