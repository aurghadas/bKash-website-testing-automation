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

    # scroll one page down
    page.keyboard.press("PageDown")
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

    page.goto("https://dev.bkash.com/en/help/charge-calculator")
    minimize_chat(page)

    page.get_by_role("combobox", name="Select Service").click()
    minimize_chat(page)

    page.get_by_role("option", name="Electricity Bill - Through App/*247# - Others Bidyut Bill").click()
    minimize_chat(page)

    page.get_by_role("spinbutton", name="Amount (BDT)").click()
    minimize_chat(page)

    page.get_by_role("spinbutton", name="Amount (BDT)").fill("5000")
    minimize_chat(page)

    page.get_by_text("Amount (BDT) Calculate").click()
    minimize_chat(page)

    page.get_by_role("button", name="Calculate").click()
    minimize_chat(page)

    page.goto("https://dev.bkash.com/en/help/charge-calculator")
    minimize_chat(page)

    page.get_by_role("combobox", name="Select Service").click()
    minimize_chat(page)

    page.get_by_role("option", name="Credit Card Bill").click()
    minimize_chat(page)

    page.get_by_role("spinbutton", name="Amount (BDT)").click()
    minimize_chat(page)

    page.get_by_role("spinbutton", name="Amount (BDT)").fill("100000")
    minimize_chat(page)

    page.get_by_text("Amount (BDT) Calculate").click()
    minimize_chat(page)

    page.get_by_role("button", name="Calculate").click()
    minimize_chat(page)

    page.get_by_role("link", name="bKash Logo").click()
    minimize_chat(page)


def test_customer_care(page: Page) -> None:
    page.goto("https://dev.bkash.com/")
    minimize_chat(page)

    page.get_by_role("button", name="English").click()
    minimize_chat(page)

    page.goto("https://dev.bkash.com/en/help")
    minimize_chat(page)

    page.get_by_role("link", name="help_customer_care_en").click()
    minimize_chat(page)

    page.get_by_role("combobox", name="District").click()
    minimize_chat(page)

    page.get_by_role("option", name="Barishal").click()
    minimize_chat(page)

    page.get_by_role("combobox", name="Thana").click()
    minimize_chat(page)

    page.get_by_role("option", name="Barisal Sadar").click()
    minimize_chat(page)

    # scroll page down
    page.keyboard.press("PageDown")
    page.keyboard.press("End")

    page.goto("https://dev.bkash.com/en/help/locator/customer-care-points")
    minimize_chat(page)

    page.get_by_role("searchbox", name="Search by Keyword").click()
    minimize_chat(page)

    page.get_by_role("searchbox", name="Search by Keyword").fill("Jessore")
    minimize_chat(page)

    page.get_by_role("button", name="Search ").click()
    minimize_chat(page)

    page.get_by_role("searchbox", name="Search by Keyword").dblclick()
    minimize_chat(page)

    page.get_by_role("link", name="bKash Logo").click()
    minimize_chat(page)

def test_about(page: Page) -> None:
    page.goto("https://dev.bkash.com/")
    page.locator("iframe[name=\"reve-chat-widget-holder\"]").content_frame.locator("#reve-chat-widget-body #chat-window-background2 a").filter(has_text="Minimize").click()
    page.get_by_role("button", name="English").click()

    page.locator("#top-menu-5").click()
    page.goto("https://dev.bkash.com/en/about")

    page.keyboard.press("ArrowDown")
    page.keyboard.press("ArrowDown")
    page.keyboard.press("ArrowDown")
    page.keyboard.press("ArrowDown")
    page.keyboard.press("ArrowDown")
    page.keyboard.press("ArrowDown")
    page.keyboard.press("ArrowDown")
    page.keyboard.press("ArrowDown")
    page.keyboard.press("ArrowDown")

    page.get_by_role("slider", name="2012").fill("2013")
    page.get_by_role("slider", name="2013").fill("2014")
    page.get_by_role("slider", name="2014").fill("2015")
    page.get_by_role("slider", name="2015").fill("2016")
    page.get_by_role("slider", name="2016").fill("2017")
    page.get_by_role("slider", name="2017").fill("2018")
    page.get_by_role("slider", name="2018").fill("2019")
    page.get_by_role("slider", name="2019").fill("2020")
    page.get_by_role("slider", name="2020").fill("2021")
    page.get_by_role("slider", name="2021").fill("2022")
    page.get_by_role("slider", name="2022").fill("2023")
    page.get_by_role("slider", name="2023").fill("2024")
    page.get_by_role("slider", name="2024").fill("2025")

    





