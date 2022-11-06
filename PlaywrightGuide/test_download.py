def test_download(page):
    page.goto("https://www.jetbrains.com/pycharm/download/#section=windows")
    with page.expect_download() as download_info:
        page.locator("text=Download PyCharmWindowsmacOSLinuxProfessionalFor both Scientific and Web Python  >> "
                     "[data-test=\"button\"]").first.click()
        download = download_info.value
        print(download.path())
        download.save_as("/Users/metju29/PycharmProjects/python-playwright/PlaywrightGuide/at.txt")
