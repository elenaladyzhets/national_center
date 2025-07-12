from selene import browser, have
import allure

class WeddingPage:
    def open_wedding_page(self):
        with allure.step('Open wedding page'):
            browser.open('/wedding')
            return self

    def opened_wedding_page(self):
        with allure.step ('Check open wedding page'):
            browser.element('h1.text-3\\.5xl.leading-10').should(have.text('II ВСЕРОССИЙСКИЙ СВАДЕБНЫЙ ФЕСТИВАЛЬ «РОССИЯ. СОЕДИНЯЯ СЕРДЦА»'))
            return self



wedding_page = WeddingPage()