import pytest


@pytest.mark.skip
def test_facebook(page):

    page.goto("https://www.facebook.com/register")

    page.locator("text=Zezwól na korzystanie z niezbędnych i opcjonalnych plików cookie").click()

    page.locator("[aria-label=\"Imię\"]").click()
    page.locator("[aria-label=\"Imię\"]").fill("Jack")
    page.locator("[aria-label=\"Imię\"]").press("Tab")

    page.locator("[aria-label=\"Nazwisko\"]").fill("Jones")

    page.locator("[aria-label=\"Numer telefonu komórkowego lub e-mail\"]").click()
    page.locator("[aria-label=\"Numer telefonu komórkowego lub e-mail\"]").fill("123456")
    page.locator("[aria-label=\"Numer telefonu komórkowego lub e-mail\"]").press("Tab")

    page.locator("[aria-label=\"Nowe hasło\"]").fill("12345678")

    page.locator("[aria-label=\"Dzień\"]").select_option("23")
    page.locator("[aria-label=\"Miesiąc\"]").select_option("9")
    page.locator("[aria-label=\"Rok\"]").select_option("2011")

    page.locator("input[name=\"sex\"]").nth(1).check()

    page.locator("button[name=\"websubmit\"]").click()

@pytest.mark.skip
def test_checkbox(page):
    page.goto("https://www.w3.org/WAI/ARIA/apg/example-index/checkbox/checkbox")

    page.locator("li:has-text(\"Sprouts\")").click()

    sprouts = page.locator("div[role=\"checkbox\"]:has-text(\"Sprouts\")")
    sprouts.click()

    assert sprouts.is_checked() is True

    mustard = page.locator("div[role=\"checkbox\"]:has-text(\"Mustard\")")
    mustard.click()

    assert mustard.is_checked() is True

    page.locator("div[role=\"checkbox\"]:has-text(\"Lettuce\")").click()

    page.locator("div[role=\"checkbox\"]:has-text(\"Tomato\")").click()

@pytest.mark.skip
def test_type(page):
    page.goto("https://www.google.com")

    page.locator("button:has-text(\"Zaakceptuj wszystko\")").click()

    page.locator("[aria-label=\"Szukaj\"]").click()
    page.locator("[aria-label=\"Szukaj\"]").type("social media")
    page.locator("[aria-label=\"Szukaj\"]").press("Enter")

def test_upload(page):
    page.goto("https://www.filemail.com/share/upload-file")
    page.locator("text=Dodaj plik").click()

    page.locator("#addBtn input[type=\"file\"]").set_input_files(
        "/Users/metju29/PycharmProjects/python-playwright/PlaywrightGuide/test1.txt")

    page.locator("button:has-text(\"Wyślij\")").click()

