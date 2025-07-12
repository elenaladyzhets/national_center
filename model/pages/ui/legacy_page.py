from selene import browser, have
import allure

class LegacyPage:
    def open_legacy_page(self):
        with allure.step('Open legacy page'):
            browser.open('/legacy')
            return self

    def opened_legacy_page(self):
        with allure.step ('Check open legacy page'):
            browser.element('.legacy__heading').should(have.text('О МЕЖДУНАРОДНОЙ ВЫСТАВКЕ-ФОРУМЕ «РОССИЯ»'))
            return self



legacy_page = LegacyPage()