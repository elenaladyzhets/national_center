from selene import browser, have
import allure

class DreamPage:
    def open_dream_page(self):
        with allure.step('Open dream page'):
            browser.open('https://dream.russia.ru/')
            return self

    def opened_dream_page(self):
        with allure.step ('Check open dream page'):
            browser.element('h3.contest-theme__title-h3').should(have.text('«Мечты о будущем»'))
            return self



dream_page = DreamPage()