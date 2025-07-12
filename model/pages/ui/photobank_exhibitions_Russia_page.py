from selene import browser, have
import allure

class PhotobankExhibRussiaPage:
    def open_photobank_exhib_russia_page(self):
        with allure.step('Open photobank exhibitions Russia page'):
            browser.open('https://russia.riamediabank.ru/ru/')
            return self

    def opened_photobank_exhib_russia_page(self):
        with allure.step ('Check open photobank exhibitions Russia page'):
            browser.element('.footer__copy').should(have.text('© 2025 МИА РОССИЯ СЕГОДНЯ'))
            return self



photobank_exhib_russia_page = PhotobankExhibRussiaPage()