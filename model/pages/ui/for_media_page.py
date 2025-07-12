from selene import browser, have
import allure

class ForMediaPage:
    def open_for_media_page(self):
        with allure.step('Open for media page'):
            browser.open('/for_media')
            return self

    def opened_for_media_page(self):
        with allure.step ('Check open for media page'):
            browser.element('.default-section__title').should(have.text('ДЛЯ СМИ'))
            return self



for_media_page = ForMediaPage()