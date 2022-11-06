def test_navigator(page):
    page.goto("https://www.instagram.com")
    page.locator("text=Zezwól na korzystanie z niezbędnych i opcjonalnych plików cookie").click()
    page.locator("text=Nie pamiętasz hasła?").click()
    page.wait_for_url("https://www.instagram.com/accounts/password/reset/")
    page.locator("text=Utwórz nowe konto").click()
    page.wait_for_url("https://www.instagram.com/accounts/emailsignup/")

    page.locator("[aria-label=\"Numer telefonu komórkowego lub adres e-mail\"]").click()
    page.locator("[aria-label=\"Numer telefonu komórkowego lub adres e-mail\"]").fill(
        "playwright@gmail.com")

    page.locator("[aria-label=\"Imię i nazwisko\"]").fill("Play")
    page.locator("[aria-label=\"Imię i nazwisko\"]").press("Tab")

    page.locator("[aria-label=\"Nazwa użytkownika\"]").fill("wright35364")

    page.locator("[aria-label=\"Hasło\"]").click()
    page.locator("[aria-label=\"Hasło\"]").fill("wright12345")

    page.locator("button:has-text(\"Dalej\")").click()