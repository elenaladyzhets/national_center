from selene import browser, have, be
import allure

class FuturePage:
    def open_future_page(self):
        with allure.step('Open future page'):
            browser.open('https://future.russia.ru/')
            return self

    def opened_future_page(self):
        with allure.step ('Check open future page'):
            browser.element('.intro__future').should(be.visible).should(have.text('СОЗДАВАЯ БУДУЩЕЕ'))
            return self



future_page = FuturePage()