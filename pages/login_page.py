from selene import browser


class LoginPage:

    def open(self):
        browser.open("https://github.com")
        return self

    def click_sign_in_desktop(self):
        browser.element('a.HeaderMenu-link--sign-in').click()
        return self

    def click_sign_in_mobile(self):
        browser.element('a[href="/login"]').click()
        return self