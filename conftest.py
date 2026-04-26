import pytest
from selenium import webdriver
from selene import browser


@pytest.fixture
def desktop_browser():
    driver = webdriver.Chrome()

    width, height = 1920, 1080

    browser.config.driver = driver
    browser.config.window_width = width
    browser.config.window_height = height

    print(f"\n DESKTOP: {width}x{height}")

    yield driver

    print("Close desktop browser")
    driver.quit()


@pytest.fixture
def mobile_browser():
    driver = webdriver.Chrome()

    width, height = 375, 812

    browser.config.driver = driver
    browser.config.window_width = width
    browser.config.window_height = height

    print(f"\n MOBILE: {width}x{height}")

    yield driver

    print("Close mobile browser")
    driver.quit()


@pytest.fixture
def browser_setup(request):
    width, height = request.param

    driver = webdriver.Chrome()

    browser.config.driver = driver
    browser.config.window_width = width
    browser.config.window_height = height

    mode = "DESKTOP" if width > 800 else "MOBILE"
    print(f"\n {mode}: {width}x{height}")

    yield driver

    print("Close browser")
    driver.quit()