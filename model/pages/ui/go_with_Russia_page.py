from selene import browser,  be
import allure

class GoWithRussiaPage:
    def open_go_with_Russia_page(self):
        with allure.step('Open go with Russia page'):
            browser.open('/gowithRussia')
            return self

    def opened_go_with_Russia_page(self):
        with allure.step ('Check open go with Russia page'):
            browser.element('#intro--btn').should(be.visible)
            return self



go_with_Russia_page = GoWithRussiaPage()