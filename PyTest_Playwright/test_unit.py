import unittest

import pytest
from playwright.sync_api import Page

class MyTest(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def setup(self, page: Page):
        self.page = page

    def test_foobar(self):
        self.page.goto("https://microsoft.com")
        self.page.locator("button:has-text(\"Dalej\")").click()
        self.page.locator("text=Dla 1 osoby").click()
        assert self.page.evaluate("1 + 1") == 2