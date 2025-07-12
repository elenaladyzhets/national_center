from selene import browser, have
import allure

class PhotobankRIAPage:
    def open_photobank_ria_page(self):
        with allure.step('Open photobank RIA page'):
            browser.open('https://future-russia.riamediabank.ru/ru/')
            return self

    def opened_photobank_ria_page(self):
        with allure.step ('Check open photobank RIA page'):
            browser.element('.footer__copy').should(have.text('© 2025 МИА РОССИЯ СЕГОДНЯ'))
            return self



photobank_ria_page = PhotobankRIAPage()