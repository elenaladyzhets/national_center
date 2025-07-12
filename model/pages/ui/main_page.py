from selene import browser, have
import allure



class MainPage:
    def open(self):
        with allure.step('Open main page'):
            browser.open('')
            return self

    def open_news_page_from_main_page(self):
        with allure.step ('Open news page from maim page'):
            browser.element('.header__nav-link[href="/news"]').click()
            return self

    def open_events_page_from_main_page(self):
        with allure.step ('Open events page from maim page'):
            browser.element('.header__nav-link[href="/events"]').click()
            return self

    def open_legacy_page_from_main_page(self):
        with allure.step ('Open legacy page from maim page'):
            browser.element('.header__nav-link[href="/legacy"]').click()
            return self

    def open_wedding_page_from_main_page(self):
        with allure.step ('Open wedding page from maim page'):
            browser.element('.header__nav-link[href="/wedding"]').click()
            return self

    def open_victory_routes_page_from_main_page(self):
        with allure.step ('Open victory routes page from maim page'):
            browser.element('.header__nav-link[href="/victory_routes"]').click()
            return self

    def open_architecture_page_from_main_page(self):
        with allure.step ('Open architecture page from maim page'):
            browser.element('.header__nav-link[href="/architecture"]').click()
            return self

    def open_creative_hub_page_from_main_page(self):
        with allure.step ('Open creative hub page from maim page'):
            browser.element('.header__nav-link[href="/architecture"]').element('svg').hover()
            browser.element('a.nav-desktop-drop__list-item[href="/creative_hub"]').click()
            return self

    def open_broadcasts_page_from_main_page(self):
        with allure.step ('Open broadcasts page from maim page'):
            browser.element('.header__nav-link[href="/broadcasts"]').click()
            return self

    def open_photobank_page_from_main_page(self):
        with allure.step ('Open photobank page from maim page'):
            browser.element('.header__nav-link[href="https://russia.ru/photobank"]').click()
            return self

    def open_photobank_directorate_page_from_main_page(self):
        with allure.step ('Open photobank directorate page from maim page'):
            browser.element('.header__nav-link[href="https://russia.ru/photobank"]').element('svg').hover()
            browser.all('.nav-desktop-drop__list-item').element_by(have.text('Фотобанк Дирекции')).click()
            return self

    def open_photobank_RIA_page_from_main_page(self):
        with allure.step ('Open photobank RIA page from maim page'):
            browser.element('.header__nav-link[href="https://russia.ru/photobank"]').element('svg').hover()
            browser.all('.nav-desktop-drop__list-item').element_by(have.text('Фотобанк «Создавая будущее»')).click()
            return self

    def open_photobank_exhibitions_Russia_page_from_main_page(self):
        with allure.step ('Open photobank exhibitions "Russia" page from maim page'):
            browser.element('.header__nav-link[href="https://russia.ru/photobank"]').element('svg').hover()
            browser.all('.nav-desktop-drop__list-item').element_by(have.text('Фотобанк Выставки «Россия»')).click()
            return self

    def open_for_media_page_from_main_page(self):
        with allure.step ('Open for media page from maim page'):
            browser.element('.header__nav-link[href="/for_media"]').click()
            return self

    def open_fair_page_from_main_page(self):
        with allure.step ('Open fair page from maim page'):
            browser.element('.header__nav-link[href="/fair"]').click()
            return self

    def open_for_developer_page_from_main_page(self):
        with allure.step ('Open for developer page from maim page'):
            browser.element('a.header__nav-link[href="/for_developer"]').click()
        return self

    def open_contacts_page_from_main_page(self):
        with allure.step ('Open contacts page from maim page'):
            browser.element('.header__nav-link[href="/contacts"]').click()
            return self

    def open_pop_up_menu(self):
        with allure.step ('Open contacts page from maim page'):
            browser.element('#burger-menu').click()
            return self

main_page = MainPage()