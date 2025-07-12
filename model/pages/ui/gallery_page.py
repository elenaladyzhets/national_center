from selene import browser, have
import allure

class GalleryPage:
    def open_gallery_page(self):
        with allure.step('Open gallery page'):
            browser.open('/gallery')
            return self

    def opened_gallery_page(self):
        with allure.step ('Check open gallery page'):
            browser.element('h1.gallery__title').should(have.text('ВЫСТАВКА «НАСЛЕДИЕ ДЛЯ БУДУЩЕГО»'))
            return self



gallery_page = GalleryPage()