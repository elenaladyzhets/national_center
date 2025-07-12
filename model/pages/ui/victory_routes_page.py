from selene import browser, have
import allure

class VictoryRoutesPage:
    def open_victory_routes_page(self):
        with allure.step('Open victory routes page'):
            browser.open('/victory_routes')
            return self

    def opened_victory_routes_page(self):
        with allure.step ('Check open victory routes page'):
            browser.element('h1').should(have.text('МАРШРУТЫ ПОБЕДЫ ПО РОССИИ И БЕЛАРУСИ'))
            return self



victory_routes_page = VictoryRoutesPage()