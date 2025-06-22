import os
import asyncio
from pathlib import Path
from dotenv import load_dotenv
from playwright.async_api import async_playwright

load_dotenv()

async def save_login_session():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()
        page = await context.new_page()

        # Navigate to the OrangeHRM login page
        await page.goto(os.getenv("HRM_LOGIN_URL"))

        # Fill in the login form
        await page.get_by_placeholder("Username").fill(os.getenv("HRM_USERNAME"))
        await page.get_by_placeholder("Password").fill(os.getenv("HRM_PASSWORD"))

        # Click the login button
        await page.get_by_role("button", name="Login").click()

        # Wait for the dashboard to be visible
        await page.wait_for_selector("text=Dashboard")

        auth_dir = Path(__file__).parent.parent / "playwright" / ".auth"
        auth_dir.mkdir(parents=True, exist_ok=True)
        auth_path = auth_dir / "orangeHRM.json"

        await context.storage_state(path=str(auth_path))
        print(f"Storage state saved at: {auth_path}")

        await browser.close()

asyncio.run(save_login_session())
