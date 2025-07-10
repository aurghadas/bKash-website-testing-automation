import re
import pytest
from playwright.sync_api import Page, expect
from urls import ( 
    BASE,
    PUJA_CELEBRATION,
    PAYMENT,
    TRAVEL,
    PAY_BILL,
    ONLINE_PAYMENT,
    DONATION,
    HELP_HOME,
    CHARGE_CALCULATOR_HELP,
    CUSTOMER_CARE_LOCATOR,
    ABOUT_PAGE,
    BASE_ENGLISH,
    BLOG_HOME,
    BIGGANCHINTA_BLOG,
    BKASH_APP,
    BKASH_SERVICES,
    CUSTOMER_CARE_BARISHAL,
    CUSTOMER_CARE_BARISHAL_SADAR 
)

def minimize_chat(page: Page) -> None:
    minimize_btn = page.frame_locator(
        'iframe[name="reve-chat-widget-holder"]'
    ).locator(
        '#reve-chat-widget-body #chat-window-background2 div'
    ).filter(has_text="Minimize")
    if minimize_btn.is_visible():
        minimize_btn.click()


def test_campaigns(page: Page) -> None:
    # Navigate to home
    page.goto(BASE)
    expect(page).to_have_url(BASE)

    # Minimize chat widget
    minimize_chat(page)

    # Switch to English
    button = page.get_by_role("button", name="English")
    button.click()
    expect(button).to_be_enabled()

    # Go to Campaigns section
    page.get_by_role("link", name="Campaigns").click()
    expect(page.get_by_role("link", name="Mobile Recharge")).to_be_visible()

    # Select Mobile Recharge → Puja Celebration
    page.get_by_role("link", name="Mobile Recharge").click()
    expect(page.get_by_role("checkbox", name="Puja Celebration")).to_be_visible()
    page.get_by_role("checkbox", name="Puja Celebration").check()
    expect(page.get_by_role("checkbox", name="Puja Celebration")).to_be_checked()

    # Navigate to Puja Celebration page
    page.goto(PUJA_CELEBRATION)
    expect(page).to_have_url(PUJA_CELEBRATION)

    # Select Payment
    page.get_by_role("checkbox", name="Payment", exact=True).check()
    expect(page.get_by_role("checkbox", name="Payment", exact=True)).to_be_checked()

    # Navigate to Payment page
    page.goto(PAYMENT)
    expect(page).to_have_url(PAYMENT)

    # Select Travel
    page.get_by_role("checkbox", name="Travel").check()
    expect(page.get_by_role("checkbox", name="Travel")).to_be_checked()

    # Navigate to Travel page
    page.goto(TRAVEL)
    expect(page).to_have_url(TRAVEL)

    # Select Pay bill
    page.get_by_role("checkbox", name="Pay bill").check()
    expect(page.get_by_role("checkbox", name="Pay bill")).to_be_checked()

    # Navigate to Pay Bill page
    page.goto(PAY_BILL)
    expect(page).to_have_url(PAY_BILL)

    # Select Online Payment
    page.get_by_role("checkbox", name="Online Payment").check()
    expect(page.get_by_role("checkbox", name="Online Payment")).to_be_checked()

    # Navigate to Online Payment page
    page.goto(ONLINE_PAYMENT)
    expect(page).to_have_url(ONLINE_PAYMENT)

    # Select Donation
    page.get_by_role("checkbox", name="Donation").check()
    expect(page.get_by_role("checkbox", name="Donation")).to_be_checked()

    # Navigate to Donation page
    page.goto(DONATION)
    expect(page).to_have_url(DONATION)


def test_blog(page: Page) -> None:
    #Navigate to home
    page.goto(BASE)
    expect(page).to_have_url(BASE)

    #Minimize chat widget
    #page.locator("iframe[name=\"reve-chat-widget-holder\"]").content_frame.locator("#reve-chat-widget-body #chat-window-background2 a").filter(has_text="Minimize").click()
    minimize_chat(page)

    #Switch to English
    en_button = page.get_by_role("button", name="English")
    en_button.click()
    expect(en_button).to_be_enabled()
    minimize_chat(page)
    
    #Go to blog 
    page.locator("#top-menu-6").click()
    expect(page).to_have_url(BLOG_HOME)
    #minimize_chat(page) # If issue arrises then replace it with the descriptive one
    page.locator("iframe[name=\"reve-chat-widget-holder\"]").content_frame.locator("#reve-chat-widget-body #chat-window-background2 a").filter(has_text="Minimize").click()
    
    # Select category from dropdown
    button = page.get_by_role("combobox", name="All Categories")
    button.click()
    expect(button).to_be_focused()
    minimize_chat(page)

    # Select bKash App option
    page.get_by_role("option", name="bKash App").click()
    expect(page).to_have_url(BKASH_APP)
    minimize_chat(page)

    # Focus search box
    button1 = page.get_by_role("searchbox", name="Search by Keyword")
    button1.click()
    expect(button1).to_be_focused()
    minimize_chat(page)

    # Search for "tech"
    button2 = page.get_by_role("searchbox", name="Search by Keyword")
    button2.fill("tech")
    expect(button2).to_have_value("tech")
    minimize_chat(page)

    # Click search button
    button3 = page.get_by_role("button", name="Search ")
    button3.click()
    expect(button3).to_be_focused()
    minimize_chat(page)

    # Clear search box
    button4 = page.get_by_role("searchbox", name="Search by Keyword")
    button4.click()
    expect(button4).to_be_focused()
    minimize_chat(page)

    # Clear search query
    store = page.get_by_role("searchbox", name="Search by Keyword")
    store.fill("")
    expect(store).to_have_value("")
    minimize_chat(page)

    # Select bKash App category again
    button5 = page.get_by_role("combobox", name="bKash App")
    button5.click()
    expect(button5).to_be_focused()
    minimize_chat(page)

    # Select bKash Services option
    page.get_by_role("option", name="bKash Services").click()
    expect(page).to_have_url(BKASH_SERVICES)
    minimize_chat(page)

    # Clear filter
    button6 = page.get_by_role("button", name="Clear Filter ")
    button6.click()
    expect(button6).to_be_focused()
    minimize_chat(page)

    # Click on blog link
    link = page.get_by_role("link", name="bKash, BigganChinta organize")
    link.click()
    expect(page).to_have_url(BIGGANCHINTA_BLOG)
    minimize_chat(page)

    # Scroll to bottom of page
    page.keyboard.press("PageDown")
    page.keyboard.press("End")
    latest = page.get_by_text("Latest Articles")
    expect(latest).not_to_be_in_viewport()
    minimize_chat(page)
    
def test_bkash_app(page: Page) -> None:
    # Navigate to home
    page.goto(BASE)
    expect(page).to_have_url(BASE)

    # Minimize chat widget
    min_btn = (
        page.locator('iframe[name="reve-chat-widget-holder"]')
            .content_frame
            .locator('#reve-chat-widget-body #chat-window-background2 a')
            .filter(has_text="Minimize")
    )
    min_btn.click()
    expect(min_btn).not_to_be_visible()

    # Switch to English
    en_btn = page.get_by_role("button", name="English")
    en_btn.click()
    expect(en_btn).to_be_enabled()

    # bKash App → Welcome Offer!
    bkash_app = page.locator("#navigation-content").get_by_role("link", name="bKash App")
    bkash_app.click()
    welcome_offer = page.get_by_role("link", name="Welcome Offer!")
    expect(welcome_offer).to_be_visible()

    # Welcome Offer! → bKash Services
    welcome_offer.click()
    bkash_services = page.get_by_role("link", name="bKash Services", exact=True)
    expect(bkash_services).to_be_visible()

    # bKash Services → What's New in bKash
    bkash_services.click()
    whats_new = page.get_by_role("link", name="What's New in bKash")
    expect(whats_new).to_be_visible()

    # What's New → Let's Start bKash
    whats_new.click()
    lets_start = page.get_by_role("link", name="Let's Start bKash")
    expect(lets_start).to_be_visible()

    # Let's Start → Most Popular
    lets_start.click()
    most_popular = page.get_by_role("link", name="Most Popular")
    expect(most_popular).to_be_visible()

    # Most Popular → General Queries
    most_popular.click()
    general_queries = page.get_by_role("link", name="General Queries")
    expect(general_queries).to_be_visible()

    # General Queries → Student Account
    general_queries.click()
    student_account = page.get_by_role("link", name="Student Account", exact=True)
    expect(student_account).to_be_visible()

    # Student Account → Bengali
    student_account.click()
    bengali_btn = page.get_by_role("button", name="Bengali")
    expect(bengali_btn).to_be_visible()

    # Switching language to Bengali
    bengali_btn.click()
    open_bn = page.get_by_role("link", name="বিকাশ খুলো এখনই!")
    expect(open_bn).to_be_visible()

    # Welcome Offer! (Bengali)
    open_bn.click()
    welcome_bn = page.get_by_role("link", name="ওয়েলকাম অফার!")
    expect(welcome_bn).to_be_visible()

    # bKash Services (Bengali)
    welcome_bn.click()
    seba = page.get_by_role("link", name="বিকাশ-এর সেবাসমূহ")
    expect(seba).to_be_visible()

    # bKash amazing features (Bengali)
    seba.click()
    features = page.get_by_role("link", name="অ্যামেজিং সব ফিচার")
    expect(features).to_be_visible()

    # bKash with guardians (Bengali)
    features.click()
    guardian = page.get_by_role("link", name="অভিভাবকের সাথে বিকাশ")
    expect(guardian).to_be_visible()

    # Most Popular (Bengali)
    guardian.click()
    popular_bn = page.get_by_role("link", name="সবচেয়ে জনপ্রিয়")
    expect(popular_bn).to_be_visible()

    # General Queries (Bengali)
    popular_bn.click()
    q_bn = page.get_by_role("link", name="সাধারণ জিজ্ঞাসা")
    expect(q_bn).to_be_visible()

    # Welcome to bKash-verse (Bengali)
    q_bn.click()
    welcome_all = page.get_by_role("link", name="বিকাশভার্সে স্বাগতম!")
    expect(welcome_all).to_be_visible()



def test_charge_calculator(page: Page) -> None:
    # Navigate to home page
    page.goto(BASE)
    expect(page).to_have_url(BASE)
    minimize_chat(page)

    # Switch interface to English
    e_button = page.get_by_role("button", name="English")
    e_button.click()
    expect(e_button).to_be_enabled()
    minimize_chat(page)

    # Go to Help & Support section
    page.goto(HELP_HOME)
    expect(page).to_have_url(HELP_HOME)
    minimize_chat(page)

    # Open Charge Calculator helper
    charge_calc = page.get_by_role("link", name="charge calculator_en Charge")
    charge_calc.click()
    expect(page).to_have_url(CHARGE_CALCULATOR_HELP)
    minimize_chat(page)

    # --- Test Case: Cash Out to Non Priyo Agent ---
    # Select "Cash Out" service
    combo_box = page.get_by_role("combobox", name="Select Service")
    combo_box.click()
    expect(combo_box).to_be_focused()
    minimize_chat(page)
    page.get_by_role("option", name="Cash Out - To Non Priyo Agent").click()
    expect(page.get_by_label("Cash Out - To Non Priyo Agent (USSD & App)")).to_be_visible()
    minimize_chat(page)

    # Enter amount for Cash Out
    amount_box = page.get_by_role("spinbutton", name="Amount (BDT)")
    amount_box.click()
    expect(amount_box).to_be_focused()
    minimize_chat(page)
    amount_box.fill("1000")
    expect(amount_box).to_have_value("1000")
    minimize_chat(page)

    # Calculate charge for Cash Out
    button3 = page.get_by_text("Amount (BDT) Calculate")
    button3.click()
    expect(button3).to_be_visible()
    minimize_chat(page)
    page.get_by_role("button", name="Calculate").click()
    expect(page.get_by_text(
        "Charge for 1000 BDT CASH OUT - TO NON PRIYO AGENT (USSD & APP): 18.5 BDT"
    )).to_be_visible()
    minimize_chat(page)

    # Reset back to Charge Calculator helper
    page.goto(CHARGE_CALCULATOR_HELP)
    expect(page).to_have_url(CHARGE_CALCULATOR_HELP)
    minimize_chat(page)

    # --- Test Case: Electricity Bill through App/#247# ---
    # Select "Electricity Bill" service
    combo_box2 = page.get_by_role("combobox", name="Select Service")
    combo_box2.click()
    expect(combo_box2).to_be_focused()
    minimize_chat(page)
    page.get_by_role(
        "option",
        name="Electricity Bill - Through App/*247# - Others Bidyut Bill"
    ).click()
    expect(page.get_by_label(
        "Electricity Bill - Through App/*247# - Others Bidyut Bill"
    )).to_be_visible()
    minimize_chat(page)

    # Enter amount for Electricity Bill
    button1 = page.get_by_role("spinbutton", name="Amount (BDT)")
    button1.click()
    expect(button1).to_be_focused()
    minimize_chat(page)
    button1.fill("5000")
    expect(button1).to_have_value("5000")
    minimize_chat(page)

    # Calculate charge for Electricity Bill
    button2 = page.get_by_text("Amount (BDT) Calculate")
    button2.click()
    expect(button2).to_be_visible()
    minimize_chat(page)
    page.get_by_role("button", name="Calculate").click()
    expect(page.get_by_text(
        "Charge for 5000 BDT ELECTRICITY BILL - THROUGH APP/*247# - OTHERS BIDYUT BILL: 30 BDT"
    )).to_be_visible()
    minimize_chat(page)

    # Reset back to Charge Calculator helper
    page.goto(CHARGE_CALCULATOR_HELP)
    expect(page).to_have_url(CHARGE_CALCULATOR_HELP)
    minimize_chat(page)

    # --- Test Case: Credit Card Bill ---
    # Select "Credit Card Bill" service
    button4 = page.get_by_role("combobox", name="Select Service")
    button4.click()
    expect(button4).to_be_focused()
    minimize_chat(page)
    page.get_by_role("option", name="Credit Card Bill").click()
    expect(page.get_by_label("Credit Card Bill")).to_be_visible()
    minimize_chat(page)

    # Enter amount for Credit Card Bill
    button5 = page.get_by_role("spinbutton", name="Amount (BDT)")
    button5.click()
    expect(button5).to_be_focused()
    minimize_chat(page)
    button5.fill("100000")
    expect(button5).to_have_value("100000")
    minimize_chat(page)

    # Calculate charge for Credit Card Bill
    button5 = page.get_by_text("Amount (BDT) Calculate")
    button5.click()
    expect(button5).to_be_visible()
    minimize_chat(page)
    page.get_by_role("button", name="Calculate").click()
    expect(page.get_by_text(
        "Charge for 100000 BDT CREDIT CARD BILL: 1000 BDT"
    )).to_be_visible()
    minimize_chat(page)

    # Return to English home via logo
    page.get_by_role("link", name="bKash Logo").click()
    expect(page).to_have_url(BASE_ENGLISH)
    minimize_chat(page)



def test_customer_care(page: Page) -> None:
    # Navigate to home page
    page.goto(BASE)
    expect(page).to_have_url(BASE)
    minimize_chat(page)

    # Switch interface to English
    en_button = page.get_by_role("button", name="English")
    en_button.click()
    expect(en_button).to_be_enabled()
    minimize_chat(page)

    # Go to Help & Support section
    page.goto(HELP_HOME)
    expect(page).to_have_url(HELP_HOME)
    minimize_chat(page)

    # Open Customer Care locator
    customer_care = page.get_by_role("link", name="help_customer_care_en")
    customer_care.click()
    expect(page).to_have_url(CUSTOMER_CARE_LOCATOR)
    minimize_chat(page)

    # Select district dropdown
    button6 = page.get_by_role("combobox", name="District")
    button6.click()
    expect(button6).to_be_enabled()
    minimize_chat(page)

    # Choose Barishal district
    button7 = page.get_by_role("option", name="Barishal")
    button7.click()
    expect(page).to_have_url(CUSTOMER_CARE_BARISHAL)
    minimize_chat(page)

    # Open thana dropdown
    button7 = page.get_by_role("combobox", name="Thana")
    button7.click()
    expect(button7).to_be_enabled()
    minimize_chat(page)

    # Choose Barisal Sadar thana
    page.get_by_role("option", name="Barisal Sadar").click()
    expect(page).to_have_url(CUSTOMER_CARE_BARISHAL_SADAR)
    minimize_chat(page)

    # Scroll down to check visibility of points
    page.keyboard.press("PageDown")
    page.keyboard.press("End")
    latest = page.get_by_label("Customer Care Points check")
    expect(latest).not_to_be_in_viewport()

    # Return to Customer Care locator
    page.goto(CUSTOMER_CARE_LOCATOR)
    expect(page).to_have_url(CUSTOMER_CARE_LOCATOR)
    minimize_chat(page)

    # Focus on search box
    search_box = page.get_by_role("searchbox", name="Search by Keyword")
    search_box.click()
    expect(search_box).to_be_enabled()
    minimize_chat(page)

    # Enter keyword "Jessore"
    search_box1 = page.get_by_role("searchbox", name="Search by Keyword")
    search_box1.fill("Jessore")
    expect(search_box1).to_have_value("Jessore")
    minimize_chat(page)

    # Execute search
    button1 = page.get_by_role("button", name="Search ")
    button1.click()
    expect(button1).to_be_enabled()
    minimize_chat(page)

    # Clear the search input
    button2 = page.get_by_role("searchbox", name="Search by Keyword")
    button2.dblclick()
    expect(button2).to_be_enabled()
    minimize_chat(page)

    # Return to English home via logo
    page.get_by_role("link", name="bKash Logo").click()
    expect(page).to_have_url(BASE_ENGLISH)
    minimize_chat(page)


def test_about(page: Page) -> None:
    # Navigate to home page
    page.goto(BASE)
    expect(page).to_have_url(BASE)

    # Minimize the chat widget
    page.locator(
        'iframe[name="reve-chat-widget-holder"]'
    ).content_frame.locator(
        "#reve-chat-widget-body #chat-window-background2 a"
    ).filter(has_text="Minimize").click()

    # Switch interface to English
    en_button = page.get_by_role("button", name="English")
    en_button.click()
    expect(en_button).to_be_enabled()

    # Open the About page via top menu
    page.locator("#top-menu-5").click()
    page.goto(ABOUT_PAGE)
    expect(page).to_have_url(ABOUT_PAGE)

    # Scroll down the page and verify the "2012" label is in view at the bottom
    for i in range(9):
        page.keyboard.press("ArrowDown")
        if i == 8:
            latest = page.get_by_label("2012")
            expect(latest).to_be_in_viewport()

    # For each year slider from 2012–2024, verify its current value and advance it by one
    for year in range(2012, 2025):
        slider = page.get_by_role("slider", name=str(year))
        expect(slider).to_have_value(str(year))
        slider.fill(str(year + 1))








