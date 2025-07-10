import re
import pytest
from playwright.sync_api import Page, expect


def test_campaigns(page: Page) -> None:
    page.goto("https://dev.bkash.com/")
    page.locator("iframe[name=\"reve-chat-widget-holder\"]").content_frame.locator("#reve-chat-widget-body #chat-window-background2 a").filter(has_text="Minimize").click()
    page.get_by_role("button", name="English").click()

    page.get_by_role("link", name="Campaigns").click()
    page.get_by_role("link", name="Mobile Recharge").click()
    page.get_by_role("checkbox", name="Puja Celebration").check()
    page.goto("https://dev.bkash.com/en/campaign/search?category=mobile-recharge%2Cpuja-celebration")
    page.get_by_role("checkbox", name="Payment", exact=True).check()
    page.goto("https://dev.bkash.com/en/campaign/search?category=mobile-recharge%2Cpuja-celebration%2Cpayment")
    page.get_by_role("checkbox", name="Travel").check()
    page.goto("https://dev.bkash.com/en/campaign/search?category=mobile-recharge%2Cpuja-celebration%2Cpayment%2Ctravel")
    page.get_by_role("checkbox", name="Pay bill").check()
    page.goto("https://dev.bkash.com/en/campaign/search?category=mobile-recharge%2Cpuja-celebration%2Cpayment%2Ctravel%2Cpay-bill")
    page.get_by_role("checkbox", name="Online Payment").check()
    page.goto("https://dev.bkash.com/en/campaign/search?category=mobile-recharge%2Cpuja-celebration%2Cpayment%2Ctravel%2Cpay-bill%2Conline-payment")
    page.get_by_role("checkbox", name="Donation").check()
    page.goto("https://dev.bkash.com/en/campaign/search?category=mobile-recharge%2Cpuja-celebration%2Cpayment%2Ctravel%2Cpay-bill%2Conline-payment%2Cdonation")


def test_blog(page: Page) -> None:
    page.goto("https://dev.bkash.com/")
    page.locator("iframe[name=\"reve-chat-widget-holder\"]").content_frame.locator("#reve-chat-widget-body #chat-window-background2 a").filter(has_text="Minimize").click()
    page.get_by_role("button", name="English").click()
    
    page.locator("#top-menu-6").click()
    page.get_by_role("combobox", name="All Categories").click()
    page.get_by_role("option", name="bKash App").click()
    page.get_by_role("searchbox", name="Search by Keyword").click()
    page.get_by_role("searchbox", name="Search by Keyword").fill("tech")
    page.get_by_role("button", name="Search ").click()
    page.get_by_role("searchbox", name="Search by Keyword").click()
    page.get_by_role("searchbox", name="Search by Keyword").fill("")
    page.get_by_role("combobox", name="bKash App").click()
    page.get_by_role("option", name="bKash Services").click()
    page.get_by_role("button", name="Clear Filter ").click()
    page.get_by_role("link", name="bKash, BigganChinta organize").click()

    # scroll one “page” down
    page.keyboard.press("PageDown")

    # jump straight to bottom
    page.keyboard.press("End")


def test_bkash_app(page: Page) -> None:
    page.goto("https://dev.bkash.com/")
    page.locator("iframe[name=\"reve-chat-widget-holder\"]").content_frame.locator("#reve-chat-widget-body #chat-window-background2 a").filter(has_text="Minimize").click()
    page.get_by_role("button", name="English").click()

    page.locator("#navigation-content").get_by_role("link", name="bKash App").click()
    page.get_by_role("link", name="Welcome Offer!").click()
    page.get_by_role("link", name="bKash Services", exact=True).click()
    page.get_by_role("link", name="What's New in bKash").click()
    page.get_by_role("link", name="Let's Start bKash").click()
    page.get_by_role("link", name="Most Popular").click()
    page.get_by_role("link", name="General Queries").click()
    page.get_by_role("link", name="Student Account", exact=True).click()
    page.get_by_role("button", name="Bengali").click()
    page.get_by_role("link", name="বিকাশ খুলো এখনই!").click()
    page.get_by_role("link", name="ওয়েলকাম অফার!").click()
    page.get_by_role("link", name="বিকাশ-এর সেবাসমূহ").click()
    page.get_by_role("link", name="অ্যামেজিং সব ফিচার").click()
    page.get_by_role("link", name="অভিভাবকের সাথে বিকাশ").click()
    page.get_by_role("link", name="সবচেয়ে জনপ্রিয়").click()
    page.get_by_role("link", name="সাধারণ জিজ্ঞাসা").click()
    page.get_by_role("link", name="বিকাশভার্সে স্বাগতম!").click()


def minimize_chat(page: Page) -> None:
    minimize_btn = page.frame_locator(
        'iframe[name="reve-chat-widget-holder"]'
    ).locator(
        '#reve-chat-widget-body #chat-window-background2 div'
    ).filter(has_text="Minimize")
    if minimize_btn.is_visible():
        minimize_btn.click()


def test_charge_calculator(page: Page) -> None:
    page.goto("https://dev.bkash.com/")
    minimize_chat(page)

    page.get_by_role("button", name="English").click()
    minimize_chat(page)

    page.goto("https://dev.bkash.com/en/help")
    minimize_chat(page)

    page.get_by_role("link", name="charge calculator_en Charge").click()
    minimize_chat(page)

    page.get_by_role("combobox", name="Select Service").click()
    minimize_chat(page)

    page.get_by_role("option", name="Cash Out - To Non Priyo Agent").click()
    minimize_chat(page)

    page.get_by_role("spinbutton", name="Amount (BDT)").click()
    minimize_chat(page)

    page.get_by_role("spinbutton", name="Amount (BDT)").fill("1000")
    minimize_chat(page)

    page.get_by_text("Amount (BDT) Calculate").click()
    minimize_chat(page)

    page.get_by_role("button", name="Calculate").click()
    minimize_chat(page)

    page.get_by_role("link", name="bKash Logo").click()
    minimize_chat(page)






# assertion added on the following methods. 1st one working but the second one is not working for now.

def test_campaigns(page: Page) -> None:
    page.goto("https://dev.bkash.com/")
    page.locator("iframe[name=\"reve-chat-widget-holder\"]")\
        .content_frame\
        .locator("#reve-chat-widget-body #chat-window-background2 a")\
        .filter(has_text="Minimize")\
        .click()
    page.get_by_role("button", name="English").click()

    page.get_by_role("link", name="Campaigns").click()
    page.get_by_role("link", name="Mobile Recharge").click()

    # Puja Celebration
    page.get_by_role("checkbox", name="Puja Celebration").check()
    expect(page.get_by_role("checkbox", name="Puja Celebration")).to_be_checked()

    page.goto(
        "https://dev.bkash.com/en/campaign/search?"
        "category=mobile-recharge%2Cpuja-celebration"
    )

    # Payment
    page.get_by_role("checkbox", name="Payment", exact=True).check()
    expect(page.get_by_role("checkbox", name="Payment", exact=True)).to_be_checked()

    page.goto(
        "https://dev.bkash.com/en/campaign/search?"
        "category=mobile-recharge%2Cpuja-celebration%2Cpayment"
    )

    # Travel
    page.get_by_role("checkbox", name="Travel").check()
    expect(page.get_by_role("checkbox", name="Travel")).to_be_checked()

    page.goto(
        "https://dev.bkash.com/en/campaign/search?"
        "category=mobile-recharge%2Cpuja-celebration%2Cpayment%2Ctravel"
    )

    # Pay bill
    page.get_by_role("checkbox", name="Pay bill").check()
    expect(page.get_by_role("checkbox", name="Pay bill")).to_be_checked()

    page.goto(
        "https://dev.bkash.com/en/campaign/search?"
        "category=mobile-recharge%2Cpuja-celebration%2Cpayment%2Ctravel%2Cpay-bill"
    )

    # Online Payment
    page.get_by_role("checkbox", name="Online Payment").check()
    expect(page.get_by_role("checkbox", name="Online Payment")).to_be_checked()

    page.goto(
        "https://dev.bkash.com/en/campaign/search?"
        "category=mobile-recharge%2Cpuja-celebration%2Cpayment%2Ctravel"
        "%2Cpay-bill%2Conline-payment"
    )

    # Donation
    page.get_by_role("checkbox", name="Donation").check()
    expect(page.get_by_role("checkbox", name="Donation")).to_be_checked()

    page.goto(
        "https://dev.bkash.com/en/campaign/search?"
        "category=mobile-recharge%2Cpuja-celebration%2Cpayment%2Ctravel"
        "%2Cpay-bill%2Conline-payment%2Cdonation"
    )


def test_blog(page: Page) -> None:
    page.goto("https://dev.bkash.com/")
    # minimize chat widget
    minimize_btn = page.locator(
        "iframe[name=\"reve-chat-widget-holder\"]"
    ).content_frame.locator(
        "#reve-chat-widget-body #chat-window-background2 a"
    ).filter(has_text="Minimize")
    minimize_btn.click()
    expect(minimize_btn).not_to_be_visible()

    # switch to English
    english_btn = page.get_by_role("button", name="English")
    english_btn.click()
    expect(english_btn).to_be_focused()

    # open blog menu
    top_menu = page.locator("#top-menu-6")
    top_menu.click()
    expect(top_menu).to_be_focused()

    # open categories dropdown
    cat_combo = page.get_by_role("combobox", name="All Categories")
    cat_combo.click()
    expect(cat_combo).to_be_focused()

    # pick "bKash App"
    opt_app = page.get_by_role("option", name="bKash App")
    opt_app.click()
    expect(opt_app).to_be_focused()

    # search "tech"
    search_box = page.get_by_role("searchbox", name="Search by Keyword")
    search_box.click()
    expect(search_box).to_be_focused()
    search_box.fill("tech")
    expect(search_box).to_have_value("tech")

    # submit search
    search_btn = page.get_by_role("button", name="Search ")
    search_btn.click()
    expect(search_btn).to_be_focused()

    # clear the search box
    search_box.click()
    expect(search_box).to_be_focused()
    search_box.fill("")
    expect(search_box).to_have_value("")

    # change category to "bKash Services"
    cat_combo.click()
    expect(cat_combo).to_be_focused()
    opt_srv = page.get_by_role("option", name="bKash Services")
    opt_srv.click()
    expect(opt_srv).to_be_focused()

    # clear filters
    clear_btn = page.get_by_role("button", name="Clear Filter ")
    clear_btn.click()
    expect(clear_btn).to_be_focused()

    # open an article
    article_link = page.get_by_role("link", name="bKash, BigganChinta organize")
    article_link.click()
    expect(article_link).to_be_focused()

    # scroll down
    page.keyboard.press("PageDown")
    page.keyboard.press("End")
    scroll_y = page.evaluate("window.scrollY")
    assert scroll_y > 0, f"Expected page to scroll down, but scrollY={scroll_y}"
