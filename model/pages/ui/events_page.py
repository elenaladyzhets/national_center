from selene import browser, have
import allure

class EventsPage:
    def open_events_page(self):
        with allure.step('Open events page'):
            browser.open('/events')
            return self

    def opened_events_page(self):
        with allure.step ('Check open page'):
            browser.element('[data-default-title=Афиша]').should(have.text('АФИША'))
            return self



events_page = EventsPage()