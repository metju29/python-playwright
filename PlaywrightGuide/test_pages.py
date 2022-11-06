import pytest


@pytest.mark.skip
def test_page(page):
    page.goto("http://google.com")
    page.locator("button:has-text(\"Zaakceptuj wszystko\")").click()
    page.locator("[aria-label=\"Szukaj\"]").click()
    page.locator("[aria-label=\"Szukaj\"]").fill("Mike Tyson")
    page.locator("text=Mike TysonBokser >> span").first.click()

    print(page.url)

@pytest.mark.skip
def test_page2(context):
    page = context.new_page()
    page1 = context.new_page()
    page.goto("http://google.com")
    page1.goto("http://google.com")

    page1.locator("button:has-text(\"Zaakceptuj wszystko\")").click()
    page1.locator("[aria-label=\"Szukaj\"]").click()
    page1.locator("[aria-label=\"Szukaj\"]").fill("Mike Tyson")
    page1.locator("text=Mike TysonBokser >> span").first.click()

def test_page3(context):
    page = context.new_page()
    page.goto("https://www.rrc.texas.gov/resource-center/research/gis-viewer/gis-popup-blocker-test/#")

    with page.expect_popup() as popup_info:
        page.locator("text=RUN POPUP TEST").click()

    page1 = popup_info.value
    page.wait_for_url("https://www.rrc.texas.gov/resource-center/research/gis-viewer/gis-popup-blocker-test/#")

    page1.close()
    print(page.url)
