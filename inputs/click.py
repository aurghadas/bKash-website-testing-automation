# to run this: python3 inputs/clicks.py
import asyncio
from playwright.async_api import async_playwright, expect

async def main():
    async with async_playwright() as p:
        # Launch browser in headed mode so you can see what's happening
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()

        # Start tracing to capture screenshots, DOM snapshots, and source files
        await context.tracing.start(screenshots=True, snapshots=True, sources=True)

        page = await context.new_page()
        await page.set_viewport_size({"width": 1000, "height": 1200})
        await page.goto("https://demoqa.com/buttons")

        # Generic Click - Dynamic Selector
        button = page.locator("text=Click Me").nth(2)
        await button.click()
        await page.screenshot(path="screenshots/dynamicClick.png")

        # Assertion
        await expect(page.locator("#dynamicClickMessage")).to_have_text(
            "You have done a dynamic click"
        )

        # Double Click
        button = page.locator("text=Click Me").nth(0)
        await button.dblclick()
        await page.screenshot(path="screenshots/doubleClick.png")

        # Assertion
        await expect(page.locator("#doubleClickMessage")).to_have_text(
            "You have done a double click"
        )

        # Stop tracing and save to disk
        await context.tracing.stop(path="logs/trace.zip")

        # Close the browser
        await browser.close()

        # --- Right-click example (commented out until that issue is resolved) ---
        # Right Click - behavior is currently under discussion:
        # https://github.com/microsoft/playwright-python/issues/1426
        #
        # button = page.locator("text=Click Me").nth(1)
        # await button.click(button="right")
        # await page.screenshot(path="screenshots/rightClick.png")
        # await expect(page.locator("#rightClickMessage")).to_have_text(
        #     "You have done a right click"
        # )
        # await browser.close()

asyncio.run(main())
