import pytest


@pytest.mark.skip_browser("chromium")
def test_youtube(page):
    page.goto("http://youtube.com")