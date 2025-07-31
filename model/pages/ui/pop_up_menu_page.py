from selene import browser, have, be
import allure

class PopUpMenuPage:
    def open_news_page(self):
        with allure.step('Open news page'):
            browser.all('a[itemprop="url"]').element_by(have.text('Новости')).should(be.visible).click()
            return self

    def open_events_page(self):
        with allure.step ('Open events page'):
            browser.all('a[itemprop="url"]').element_by(have.text('Афиша')).should(be.visible).click()
            return self

    def open_legacy_page(self):
        with allure.step('Open legacy page'):
            browser.all('a[itemprop="url"]').element_by(have.text('О Выставке «Россия»')).should(be.visible).click()
            return self

    def open_architecture_page_from_menu(self):
        with allure.step ('Open architecture page'):
            browser.all('a[itemprop="url"]').element_by(have.text('Рождение масштаба')).should(be.visible).click()
            return self

    def open_architecture_page_from_menu_list(self):
        with allure.step('Open architecture page from menu list'):
            browser.all('a[itemprop="url"]').element_by(have.text('Архитектурная выставка «Рождение масштаба»')).should(be.visible).click()
            return self

    def open_creative_hub_page(self):
        with allure.step ('Open creative hub page'):
            browser.all('a[itemprop="url"]').element_by(have.text('Конкурс «Креативный хаб»')).should(be.visible).click()
            return self

    def open_photobank_page_from_menu(self):
        with allure.step('Open photobank page'):
            browser.all('a[itemprop="url"]').element_by(have.text('Фотобанк')).should(be.visible).click()
            return self

    def open_photobank_RIA_page(self):
        with allure.step ('Open photobank RIA page'):
            browser.all('a[itemprop="url"]').element_by(have.text('Фотобанк «Создавая будущее»')).should(be.visible).click()
            return self

    def open_photobank_page_from_menu_list(self):
        with allure.step('Open photobank page from menu list'):
            browser.all('a[itemprop="url"]').element_by(have.text('Фотобанк Дирекции')).should(be.visible).click()
            return self

    def open_photobank_exhibitions_Russia_page(self):
        with allure.step ('Open photobank exhibitions Russia page'):
            browser.all('a[itemprop="url"]').element_by(have.text('Фотобанк Выставки «Россия»')).should(be.visible).click()
            return self

    def open_wedding_page(self):
        with allure.step('Open wedding page'):
            browser.element('a.header-menu-list__title[href="/wedding"]').should(be.visible).click()
            return self

    def open_broadcasts_page(self):
        with allure.step ('Open broadcasts page'):
            browser.element('a.header-menu-list__title[href="/broadcasts"]').should(be.visible).click()
            return self

    def open_victory_routes_page(self):
        with allure.step('Open victory routes page'):
            browser.element('a.header-menu-list__title[href="/victory_routes"]').should(be.visible).click()
            return self

    def open_dream_page(self):
        with allure.step ('Open dream page'):
            browser.element('a.header-menu-list__title[href="http://dream.russia.ru"]').should(be.visible).click()
            return self

    def open_dialog_page(self):
        with allure.step('Open dialog page'):
            browser.element('a.header-menu-list__title[href="/dialog"]').should(be.visible).click()
            return self

    def open_for_media_page(self):
        with allure.step ('Open for media page'):
            browser.element('a.header-menu-list__title[href="/for_media"]').should(be.visible).click()
            return self

    def open_for_developer_page(self):
        with allure.step('Open for developer page'):
            browser.element('a.header-menu-list__title[href="https://russia.ru/for_developer"]').should(be.visible).click()
            return self

    def open_fair_page(self):
        with allure.step ('Open fair page'):
            browser.element('a.header-menu-list__title[href="/fair"]').should(be.visible).click()
            return self

    def open_media_about_us_page(self):
        with allure.step('Open media about us page'):
            browser.element('a.header-menu-list__title[href="/media_about_us"]').should(be.visible).click()
            return self

    def open_contacts_page(self):
        with allure.step ('Open contacts page'):
            browser.element('a.header-menu-list__title[href="/contacts"]').should(be.visible).click()
            return self

    def open_future_page(self):
        with allure.step('Open future page'):
            browser.element('a.header-menu-list__title[href="https://future.russia.ru/"]').should(be.visible).click()
            return self

    def open_gallery_page(self):
        with allure.step ('Open gallery page'):
            browser.element('a.header-menu-list__title[href="/gallery"]').should(be.visible).click()
            return self

    def close_pop_up_menu(self):
        with allure.step ('Close pop up menu'):
            browser.element('#burger-menu-close').should(be.visible).should(be.visible).click()
            return self

    def change_language_ru_to_eng(self):
        with allure.step ('Change language ru to eng'):
            browser.element('a.header-menu__languages-elem').should(have.text('ENG')).should(be.visible).click()
            return self

    def change_language_eng_to_ru(self):
        with allure.step ('Change language eng to ru'):
            browser.element('a.header-menu__languages-elem').should(have.text('RU')).should(be.visible).click()
            return self

    def search_from_pop_up_menu(self, word):
        with allure.step ('Search from pop up menu'):
            browser.element('button.js-search-button-header-menu').click()
            browser.element('input.search-input-header-menu').should(be.visible).set_value(word).press_enter()
            return self

    def link_to_telegram(self):
        with allure.step ('Link to telegram '):
            browser.element('a[href="https://t.me/gowithRussia"]').should(be.visible).click()
            return self

    def link_to_vk(self):
        with allure.step ('Link to vkontakte'):
            browser.element('a[href="https://vk.com/gowithrussia"]').should(be.visible).click()
            return self

    def link_to_ok(self):
        with allure.step ('Link to odnoklassniki'):
            browser.element('a[href="https://ok.ru/gowithrussia"]').should(be.visible).click()
            return self

    def link_to_dzen(self):
        with allure.step ('Link to dzen'):
            browser.element('a[href="https://dzen.ru/gowithrussia"]').should(be.visible).click()
            return self

pop_up_menu_page = PopUpMenuPage()