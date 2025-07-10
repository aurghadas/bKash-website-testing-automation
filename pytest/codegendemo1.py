from playwright.sync_api import Page

def test_shopping_checkout_flow(page: Page) -> None:
    # 1. Go to the login page
    page.goto("https://www.saucedemo.com/", wait_until="networkidle")
    # 2. Log in
    page.locator("[data-test=username]").click()
    page.locator("[data-test=username]").fill("standard_user")
    page.locator("[data-test=password]").click()
    page.locator("[data-test=password]").fill("secret_sauce")
    page.locator("[data-test=login-button]").click()

    # 3. Add four items to the cart
    page.locator("[data-test=add-to-cart-sauce-labs-backpack]").click()
    page.locator("[data-test=add-to-cart-sauce-labs-bolt-t-shirt]").click()
    page.locator("[data-test=add-to-cart-sauce-labs-fleece-jacket]").click()
    page.locator("[data-test=add-to-cart-sauce-labs-bike-light]").click()

    # 4. Open cart and remove three of them
    page.locator("[data-test=shopping-cart-link]").click()
    page.locator("[data-test=remove-sauce-labs-backpack]").click()
    page.locator("[data-test=remove-sauce-labs-bolt-t-shirt]").click()
    page.locator("[data-test=remove-sauce-labs-fleece-jacket]").click()

    # 5. Proceed to checkout
    page.locator("[data-test=checkout]").click()
    page.locator("[data-test=firstName]").click()
    page.locator("[data-test=firstName]").fill("Aurgha")
    page.locator("[data-test=lastName]").dblclick()
    page.locator("[data-test=lastName]").fill("Das")
    page.locator("[data-test=postalCode]").dblclick()
    page.locator("[data-test=postalCode]").fill("8600")
    page.locator("[data-test=continue]").click()

    # 6. Finish the purchase and return to products
    page.locator("[data-test=finish]").click()
    page.locator("[data-test=back-to-products]").click()
