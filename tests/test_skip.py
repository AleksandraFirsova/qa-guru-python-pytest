import pytest
from pages.login_page import LoginPage


@pytest.mark.parametrize("size", [
    (1920, 1080),
    (375, 812),
])
def test_sign_in_skip(size):
    width, height = size

    if width > height:
        pytest.skip("Skipped")

    LoginPage().open().click_sign_in_mobile()