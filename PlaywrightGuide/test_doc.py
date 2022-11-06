import pytest

@pytest.mark.skip
def test_instagram(page):
    page.goto("https://www.instagram.com")
    page.locator("text=Zezwól na korzystanie z niezbędnych i opcjonalnych plików cookie").click()
    page.locator("text=Nie pamiętasz hasła?").click()
    page.wait_for_url("https://www.instagram.com/accounts/password/reset/")
    page.screenshot(path="sc1.png")
    page.locator("text=Utwórz nowe konto").click()
    page.wait_for_url("https://www.instagram.com/accounts/emailsignup/")

    page.locator("[aria-label=\"Numer telefonu komórkowego lub adres e-mail\"]").click()
    page.screenshot(path="sc2.png")
    page.locator("[aria-label=\"Numer telefonu komórkowego lub adres e-mail\"]").fill(
        "playwright@gmail.com")
    page.locator("[aria-label=\"Imię i nazwisko\"]").fill("Play")
    page.locator("[aria-label=\"Imię i nazwisko\"]").press("Tab")
    page.locator("[aria-label=\"Nazwa użytkownika\"]").fill("wright35364")
    page.locator("[aria-label=\"Hasło\"]").click()
    page.locator("[aria-label=\"Hasło\"]").fill("wright12345")
    page.screenshot(path="sc3.png")
    page.locator("button:has-text(\"Dalej\")").click()


def test_facebook(browser):

    # context = browser.new_context(record_video_dir="videos/",
    #                               record_video_size={"width": 1280,
    #                                                 "height": 720})
    context = browser.new_context()
    context.tracing.start(snapshots=True, sources=True)
    page = context.new_page()
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
    context.tracing.stop(path="tracing.zip")

    #Commands:
    # playwright show-trace tracing.zip
