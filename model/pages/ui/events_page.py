import time

from selene import browser, have, be, by
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

    def open_event_page(self):
        with allure.step('Open event page'):
            browser.element('.show-card__title').should(have.text('Интерактивная экскурсия «Путешествие по России»')).click()
            return self

    def valid_individual_registration_without_guests(self):
        with allure.step('Choose day for person without guests'):
            browser.element('a.scroll-link.button--red').should(be.visible).should(have.text('Зарегистрироваться')).click()

            #Выбор дня с местами больше 0
            day = browser.element('.event-schedule__time-list._active').should(be.visible)
            available = day.all(
                by.xpath(
                    ".//div[contains(@class,'time-list__item')][@data-place-quantity!='0' and @data-show-registration='1']")
            )
            available.should(have.size_greater_than(0))
            slot = available.first
            browser.execute_script(
                'arguments[0].scrollIntoView({block:"center", inline:"nearest"});',
                slot()  # selene Element -> raw WebElement
            )
            slot.should(be.clickable).click()
            return self

    def select_region(self, region_name='Запорожская область'):
        with allure.step('Choose region'):
            browser.element('.select__head').should(be.visible).click()
            browser.all('.select__item').element_by(have.exact_text(region_name)).should(be.visible).click()
            return self

    def submit_registration(self):
        with allure.step('Submit registration'):
            browser.element('.event-registration__form-check').should(be.visible).click()
            browser.element('.event-registration__submit').should(be.visible).should(have.text('Зарегистрироваться')).click()
            return self

    def confirm_registration_popup(self):
        with allure.step('Confirm registration in popup'):
            time.sleep(0.3)
            browser.all('.js-close-form-popup').filtered_by(be.visible).first.with_(timeout=10).click()
        return self




events_page = EventsPage()