from selene import browser, have
import allure

class FashionRussiaPage:
    def open_fashion_Russia_page(self):
        with allure.step('Open fashion Russia page'):
            browser.open('https://modnayarussia.ru/')
            return self

    def opened_fashion_Russia_page(self):
        with allure.step ('Check open fashion Russia page'):
            browser.element('h1.tn-atom').should(have.text('Модная Россия: проекты, которые меняют города и жизни'))
            return self



fashion_Russia_page = FashionRussiaPage()