from selene import browser, have, be
import allure

class MainPage:
    def open(self):
       with allure.step('Open main page'):
           browser.open('')
           browser.element('.regions-confirm').should(be.visible).click()
           browser.element('.cookie-popup__button').should(be.visible).click()
           return self

    def opened(self):
       with allure.step('Opened main page'):
           browser.element('h2.russia-news__title').should(have.text('НОВОСТИ'))
           return self

    def close_broadcast_window(self):
        with allure.step('Close broadcast window'):
            browser.element('.live-modal__close').should(be.visible)
            browser.element('button.live-modal__close').click()
            browser.element('.live-modal__close').should(be.not_.visible)
            return self


main_page = MainPage()