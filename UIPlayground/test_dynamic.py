def test_dynamic(page):
    page.goto("http://uitestingplayground.com/")
    page.locator("a:has-text(\"Dynamic Table\")").click()
    assert page.url == "http://uitestingplayground.com/dynamictable"
    # war_var = page.locator(".bg-warning").all_inner_texts()[0].split(" ")[-1]
    war_var = page.locator(".bg-warning").inner_text().split(" ")[-1]
    # print(f"\n{war_var}")

    table_list = page.locator("span[role=\"cell\"]").all_inner_texts()
    # print(f"\n{table_list}")
    chrome_index = table_list.index("Chrome")
    chrom_values = table_list[chrome_index:
                              chrome_index+5]
    # print(f"\n{chrom_values}")
    tab_val = None
    for value in chrom_values:
        if "%" in value:
            tab_val = value
            break
    # print(f"\n{tab_val}")

    print(f"\nWarning value: {war_var}")
    print(f"Table value: {tab_val}")
    assert tab_val == war_var
