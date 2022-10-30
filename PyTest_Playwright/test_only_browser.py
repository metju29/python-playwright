import pytest


@pytest.mark.only_browser("chromium")
def test_youtube(page):
    page.goto("http://youtube.com")
