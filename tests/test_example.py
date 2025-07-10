from playwright.sync_api import Page

def test_example_domain(page: Page):
    page.goto("https://example.com")
    assert page.title() == "Example Domain"
