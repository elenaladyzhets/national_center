from selene import browser, have, be
import allure
from dotenv import load_dotenv
import os

load_dotenv()

LOGIN = os.getenv("USER_LOGIN")
PASSWORD = os.getenv("USER_PASSWORD")


class HeaderPage:
    def open_news_page_from_header(self):
        with allure.step ('Open news page from header'):
            browser.element('.header__nav-link[href="/news"]').should(be.visible).click()
            return self

    def open_events_page_from_header(self):
        with allure.step ('Open events page from header'):
            browser.element('.header__nav-link[href="/events"]').should(be.visible).click()
            return self

    def open_legacy_page_from_header(self):
        with allure.step ('Open legacy page from header'):
            browser.element('.header__nav-link[href="/legacy"]').should(be.visible).click()
            return self

    def open_guides_kids_page_from_header(self):
        with allure.step ('Open guides kids page from header'):
            browser.element('.header__nav-link[href="https://guides.kids.russia.ru/"]').should(be.visible).click()
            return self

    def open_go_with_Russia_page_from_header(self):
        with allure.step ('Open go with Russia page from header'):
            browser.element('.header__nav-link[href="https://russia.ru/gowithRussia"]').should(be.visible).click()
            return self

    def open_wedding_page_from_header(self):
        with allure.step ('Open wedding page from header'):
            browser.element('.header__nav-link[href="/wedding"]').should(be.visible).click()
            return self

    def open_victory_routes_page_from_header(self):
        with allure.step ('Open victory routes page from header'):
            browser.element('.header__nav-link[href="/victory_routes"]').should(be.visible).click()
            return self

    def open_architecture_page_from_header(self):
        with allure.step ('Open architecture page from header'):
            browser.element('.header__nav-link[href="/architecture"]').should(be.visible).click()
            return self

    def open_creative_hub_page_from_header(self):
        with allure.step ('Open creative hub page from header'):
            browser.element('.header__nav-link[href="/architecture"]').element('svg').hover()
            browser.element('a.nav-desktop-drop__list-item[href="/creative_hub"]').should(be.visible).click()
            return self

    def open_broadcasts_page_from_header(self):
        with allure.step ('Open broadcasts page from header'):
            browser.element('.header__nav-link[href="/broadcasts"]').should(be.visible).click()
            return self

    def open_photobank_page_from_header(self):
        with allure.step ('Open photobank page from header'):
            browser.element('.header__nav-link[href="https://russia.ru/photobank"]').should(be.visible).click()
            return self

    def open_photobank_directorate_page_from_header(self):
        with allure.step ('Open photobank directorate page from header'):
            browser.element('.header__nav-link[href="https://russia.ru/photobank"]').element('svg').hover()
            browser.all('.nav-desktop-drop__list-item').element_by(have.text('Фотобанк Дирекции')).should(be.visible).click()
            return self

    def open_photobank_RIA_page_from_header(self):
        with allure.step ('Open photobank RIA page from header'):
            browser.element('.header__nav-link[href="https://russia.ru/photobank"]').element('svg').hover()
            browser.all('.nav-desktop-drop__list-item').element_by(have.text('Фотобанк «Создавая будущее»')).should(be.visible).click()
            return self

    def open_photobank_exhibitions_Russia_page_from_header(self):
        with allure.step ('Open photobank exhibitions "Russia" page from header'):
            browser.element('.header__nav-link[href="https://russia.ru/photobank"]').element('svg').hover()
            browser.all('.nav-desktop-drop__list-item').element_by(have.text('Фотобанк Выставки «Россия»')).should(be.visible).click()
            return self

    def open_for_media_page_from_header(self):
        with allure.step ('Open for media page from header'):
            browser.element('.header__nav-link[href="/for_media"]').should(be.visible).click()
            return self

    def open_fair_page_from_header(self):
        with allure.step ('Open fair page from header'):
            browser.element('.header__nav-link[href="/fair"]').should(be.visible).click()
            return self

    def open_for_developer_page_from_header(self):
        with allure.step ('Open for developer page from header'):
            browser.element('a.header__nav-link[href="/for_developer"]').should(be.visible).click()
        return self

    def open_contacts_page_from_header(self):
        with allure.step ('Open contacts page from header'):
            browser.element('.header__nav-link[href="/contacts"]').should(be.visible).click()
            return self

    def open_pop_up_menu(self):
        with allure.step ('Open contacts page from header'):
            browser.element('#burger-menu').should(be.visible).click()
            return self

    def change_language_ru_to_eng(self):
        with allure.step ('change language ru to eng'):
            browser.element('h2.russia-news__title').should(have.text('NEWS'))
            return self

    def search_available_from_header(self, word):
        with allure.step ('Search from header'):
            browser.element('button.js-search-button').click()
            browser.element('input.search-input').should(be.visible).set_value(word).should(be.visible).press_enter()
            return self

    def search_unavailable_from_header(self):
        with allure.step ('Search from header'):
            browser.element('button.js-search-button').click()
            browser.element('input.search-input').should(be.visible).set_value('Араппоапгепоп').should(be.visible).press_enter()
            return self

    def log_in_from_header(self):
        with allure.step('Log in from header'):
            browser.element('button.js-auth-open').should(be.visible).click()
            browser.element('input#email').should(be.visible).type(LOGIN)
            browser.element('input#password').should(be.visible).type(PASSWORD)
            browser.element('button[type="submit"].base-button--full').click()
            return self


header_page = HeaderPage()