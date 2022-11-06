

# def test_microsoft(page):
#     page.goto("https://microsoft.com")
#     page.locator("button:has-text(\"Dalej\")").click()
#     page.locator("text=Dla 1 osoby").click()
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=1000)
    page = browser.new_page()
    page.goto("https://playwright.dev")
    print(page.title())
    page.pause()
    page.goto("https://cnn.com")
    browser.close()