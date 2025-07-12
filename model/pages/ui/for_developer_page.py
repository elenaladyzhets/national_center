from selene import browser, have
import allure

class ForDeveloperPage:
    def open_for_developer_page(self):
        with allure.step('Open for developer page'):
            browser.open('/for_developer')
            return self

    def opened_for_developer_page(self):
        with allure.step ('Check open for developer page'):
            browser.element('.developers__heading').should(have.text('ДЛЯ ЗАСТРОЙЩИКА'))
            return self



for_developer_page = ForDeveloperPage()