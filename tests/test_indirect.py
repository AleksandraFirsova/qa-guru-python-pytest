import pytest
from pages.login_page import LoginPage


@pytest.mark.parametrize("browser_setup", [(1920, 1080)], indirect=True)
def test_sign_in_desktop(browser_setup):
    LoginPage().open().click_sign_in_desktop()


@pytest.mark.parametrize("browser_setup", [(375, 812)], indirect=True)
def test_sign_in_mobile(browser_setup):
    LoginPage().open().click_sign_in_mobile()