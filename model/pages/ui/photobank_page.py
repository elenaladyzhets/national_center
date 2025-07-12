from selene import browser, have
import allure

class PhotobankPage:
    def open_photobank_page(self):
        with allure.step('Open photobank page'):
            browser.open('/photobank')
            return self

    def opened_photobank_page(self):
        with allure.step ('Check open photobank page'):
            browser.element('.photobank__title').should(have.text('ФОТОБАНК'))
            return self



photobank_page = PhotobankPage()