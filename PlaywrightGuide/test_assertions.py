"""
expect(locator).not_to_be_checked(**kwargs)
expect(locator).not_to_be_disabled(**kwargs)
expect(locator).not_to_be_editable(**kwargs)
expect(locator).not_to_be_empty(**kwargs)
expect(locator).not_to_be_enabled(**kwargs)
expect(locator).not_to_be_focused(**kwargs)
expect(locator).not_to_be_hidden(**kwargs)
expect(locator).not_to_be_visible(**kwargs)
expect(locator).not_to_contain_text(expected, **kwargs)
expect(locator).not_to_have_attribute(name, value, **kwargs)
expect(locator).not_to_have_class(expected, **kwargs)
expect(locator).not_to_have_count(count, **kwargs)
expect(locator).not_to_have_css(name, value, **kwargs)
expect(locator).not_to_have_id(id, **kwargs)
expect(locator).not_to_have_js_property(name, value, **kwargs)
expect(locator).not_to_have_text(expected, **kwargs)
expect(locator).not_to_have_value(value, **kwargs)
expect(locator).not_to_have_values(values, **kwargs)
expect(locator).to_be_checked(**kwargs)
expect(locator).to_be_disabled(**kwargs)
expect(locator).to_be_editable(**kwargs)
expect(locator).to_be_empty(**kwargs)
expect(locator).to_be_enabled(**kwargs)
expect(locator).to_be_focused(**kwargs)
expect(locator).to_be_hidden(**kwargs)
expect(locator).to_be_visible(**kwargs)
expect(locator).to_contain_text(expected, **kwargs)
expect(locator).to_have_attribute(name, value, **kwargs)
expect(locator).to_have_class(expected, **kwargs)
expect(locator).to_have_count(count, **kwargs)
expect(locator).to_have_css(name, value, **kwargs)
expect(locator).to_have_id(id, **kwargs)
expect(locator).to_have_js_property(name, value, **kwargs)
expect(locator).to_have_text(expected, **kwargs)
expect(locator).to_have_value(value, **kwargs)
expect(locator).to_have_values(values, **kwargs)
expect(page).not_to_have_title(title_or_reg_exp, **kwargs)
expect(page).not_to_have_url(url_or_reg_exp, **kwargs)
expect(page).to_have_title(title_or_reg_exp, **kwargs)
expect(page).to_have_url(url_or_reg_exp, **kwargs)
expect(api_response).not_to_be_ok()
expect(api_response).to_be_ok()

"""
from playwright.sync_api import Page, expect


def test_submitted(page: Page) -> None:
    page.goto("https://www.google.com")
    page.locator("button:has-text(\"Zaakceptuj wszystko\")").click()
    page.locator("div[role=\"button\"]:has-text(\"Ustawienia\")").click()
    expect(page.locator("text=Ustawienia wyszukiwania")).to_have_text("Ustawienia wyszukiwania")

def test_visible(page: Page) -> None:
    page.goto("https://www.google.com")
    page.locator("button:has-text(\"Zaakceptuj wszystko\")").click()
    page.locator("div[role=\"button\"]:has-text(\"Ustawienia\")").click()
    expect(page.locator("a[class=\"pHiOh\"]:has-text(\"Warunki\")")).to_be_visible()

