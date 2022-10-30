import asyncio
from playwright.async_api import Playwright, async_playwright, expect
async def run(playwright: Playwright) -> None:
    browser = await playwright.chromium.launch(headless=False)
    context = await browser.new_context()
    # Open new page
    page = await context.new_page()
    # Go to https://www.wikipedia.org/
    await page.goto("https://www.wikipedia.org/")
    # Click text=Polski 1 512 000+ haseł English 6 458 000+ articles 日本語 1 314 000+ 記事 Español 1
    await page.locator("text=Polski 1 512 000+ haseł English 6 458 000+ articles 日本語 1 314 000+ 記事 Español 1 ").click()
    # Click input[name="search"]
    await page.locator("input[name=\"search\"]").click()
    # Fill input[name="search"]
    await page.locator("input[name=\"search\"]").fill("dog")
    # Click a:has-text("Dog niemieckijedna z ras psów zaliczanych do molosów w typie doga")
    await page.locator("a:has-text(\"Dog niemieckijedna z ras psów zaliczanych do molosów w typie doga\")").click()
    await page.wait_for_url("https://pl.wikipedia.org/wiki/Dog_niemiecki")
    # Click div[role="navigation"] >> text=Choroby
    await page.locator("div[role=\"navigation\"] >> text=Choroby").click()
    await page.wait_for_url("https://pl.wikipedia.org/wiki/Dog_niemiecki#Choroby")
    await page.pause()
    # ---------------------
    await context.close()
    await browser.close()
async def main() -> None:
    async with async_playwright() as playwright:
        await run(playwright)
asyncio.run(main())