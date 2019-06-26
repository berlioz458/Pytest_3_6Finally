link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_guest_should_see_button_add(browser):
    browser.get(link)
    browser.find_element_by_css_selector("button.btn-add-to-basket")
