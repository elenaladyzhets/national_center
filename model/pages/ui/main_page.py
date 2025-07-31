from selene import browser, have
import allure

class MainPage:
    def open(self):
       with allure.step('Open main page'):
           browser.open('')
           return self

    def opened(self):
       with allure.step('Opened main page'):
           browser.element('h2.russia-news__title').should(have.text('НОВОСТИ'))
           return self

main_page = MainPage()