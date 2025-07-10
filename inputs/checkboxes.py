# tests/test_checkbox.py

import os
import re
from pathlib import Path
from playwright.sync_api import Page, expect

# ensure the screenshots folder exists at your project root
PROJECT_ROOT = Path(__file__).resolve().parent.parent
SCREENSHOT_DIR = PROJECT_ROOT / "screenshots"
SCREENSHOT_DIR.mkdir(exist_ok=True)

def test_check_home_checkbox(page: Page) -> None:
    # 1) navigate (wait for network to quiet down)
    page.goto("https://demoqa.com/checkbox", wait_until="networkidle")

    # 2) expand the “Home” node (it’s collapsed by default)
    page.click("button.rct-collapse")

    # 3) check the actual <input> checkbox
    page.check("input#tree-node-home")

    # 4) assert the result text shows “home” was selected
    expect(page.locator("#result")).to_have_text(
        re.compile(r"You have selected :\s*home", re.IGNORECASE)
    )

    # 5) take your screenshot under screenshots/checkbox.png
    page.screenshot(path=str(SCREENSHOT_DIR / "checkbox.png"))

