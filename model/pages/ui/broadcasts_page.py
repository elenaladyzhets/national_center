from selene import browser, have
import allure

class BroadcastsPage:
    def open_broadcasts_page(self):
        with allure.step('Open broadcasts page'):
            browser.open('/broadcasts')
            return self

    def opened_broadcasts_page(self):
        with allure.step ('Check open broadcasts page'):
            browser.element('.show-collections__title').should(have.text('ТРАНСЛЯЦИИ И ЗАПИСИ'))
            return self



broadcasts_page = BroadcastsPage()