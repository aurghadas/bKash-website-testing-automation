from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    # 1) headless so it actually renders
    browser = p.chromium.launch()  
    # 2) set a sane viewport
    context = browser.new_context(viewport={"width":1280,"height":720})
    page    = context.new_page()

    # 3) navigate & wait for idle
    page.goto("https://www.google.com/", wait_until="networkidle")

    # 4) (optional) ensure our target has appeared
    page.wait_for_selector("body")  

    # 5) snapshot full page
    page.screenshot(path="demo.png", full_page=True)

    browser.close()
