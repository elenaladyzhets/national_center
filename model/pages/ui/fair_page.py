from selene import browser, have
import allure

class FairPage:
    def open_fair_page(self):
        with allure.step('Open fair page'):
            browser.open('/fair')
            return self

    def opened_fair_page(self):
        with allure.step ('Check open fair page'):
            browser.element('.fair__title').should(have.text('УНИВЕРМАГ'))
            return self



fair_page = FairPage()