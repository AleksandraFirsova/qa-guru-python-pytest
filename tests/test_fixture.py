from pages.login_page import LoginPage


def test_sign_in_desktop(desktop_browser):
    LoginPage().open().click_sign_in_desktop()


def test_sign_in_mobile(mobile_browser):
    LoginPage().open().click_sign_in_mobile()