from selene import browser, have
import allure

class DialogPage:
    def open_dialog_page(self):
        with allure.step('Open dialog page'):
            browser.open('/dialog')
            return self

    def opened_dialog_page(self):
        with allure.step ('Check open dialog page'):
            browser.element('.js-open-form-popup').should(have.text('СТАТЬ УЧАСТНИКОМ ОТКРЫТОГО ДИАЛОГА'))
            return self



dialog_page = DialogPage()