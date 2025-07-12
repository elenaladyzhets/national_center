from selene import browser, have
import allure

class MediaAboutUsPage:
    def open_media_about_us_page(self):
        with allure.step('Open media about us page'):
            browser.open('/media_about_us')
            return self

    def opened_media_about_us_page(self):
        with allure.step ('Check open media about us page'):
            browser.element('h1.news__title').should(have.text('СМИ О НАС'))
            return self



media_about_us_page = MediaAboutUsPage()