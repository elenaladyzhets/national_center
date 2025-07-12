from selene import browser, have
import allure

class PopUpMenuPage:
    def open_news_page(self):
        with allure.step('Open news page'):
            browser.all('a[itemprop="url"]').element_by(have.text('Новости')).click()
            return self

    def open_events_page(self):
        with allure.step ('Open events page'):
            browser.all('a[itemprop="url"]').element_by(have.text('Афиша')).click()
            return self

    def open_legacy_page(self):
        with allure.step('Open legacy page'):
            browser.all('a[itemprop="url"]').element_by(have.text('О Выставке «Россия»')).click()
            return self

    def open_architecture_page_from_menu(self):
        with allure.step ('Open architecture page'):
            browser.all('a[itemprop="url"]').element_by(have.text('Рождение масштаба')).click()
            return self

    def open_architecture_page_from_menu_list(self):
        with allure.step('Open architecture page from menu list'):
            browser.all('a[itemprop="url"]').element_by(have.text('Архитектурная выставка «Рождение масштаба»')).click()
            return self

    def open_creative_hub_page(self):
        with allure.step ('Open creative hub page'):
            browser.all('a[itemprop="url"]').element_by(have.text('Конкурс «Креативный хаб»')).click()
            return self

    def open_photobank_page_from_menu(self):
        with allure.step('Open photobank page'):
            browser.all('a[itemprop="url"]').element_by(have.text('Фотобанк')).click()
            return self

    def open_photobank_RIA_page(self):
        with allure.step ('Open photobank RIA page'):
            browser.all('a[itemprop="url"]').element_by(have.text('Фотобанк «Создавая будущее»')).click()
            return self

    def open_photobank_page_from_menu_list(self):
        with allure.step('Open photobank page from menu list'):
            browser.all('a[itemprop="url"]').element_by(have.text('Фотобанк Дирекции')).click()
            return self

    def open_photobank_exhibitions_Russia_page(self):
        with allure.step ('Open photobank exhibitions Russia page'):
            browser.all('a[itemprop="url"]').element_by(have.text('Фотобанк Выставки «Россия»')).click()
            return self

    def open_wedding_page(self):
        with allure.step('Open wedding page'):
            browser.element('a.header-menu-list__title[href="/wedding"]').click()
            return self

    def open_broadcasts_page(self):
        with allure.step ('Open broadcasts page'):
            browser.element('a.header-menu-list__title[href="/broadcasts"]').click()
            return self

    def open_victory_routes_page(self):
        with allure.step('Open victory routes page'):
            browser.element('a.header-menu-list__title[href="/victory_routes"]').click()
            return self

    def open_dream_page(self):
        with allure.step ('Open dream page'):
            browser.element('a.header-menu-list__title[href="http://dream.russia.ru"]').click()
            return self

    def open_dialog_page(self):
        with allure.step('Open dialog page'):
            browser.element('a.header-menu-list__title[href="/dialog"]').click()
            return self

    def open_for_media_page(self):
        with allure.step ('Open for media page'):
            browser.element('a.header-menu-list__title[href="/for_media"]').click()
            return self

    def open_for_developer_page(self):
        with allure.step('Open for developer page'):
            browser.element('a.header-menu-list__title[href="https://russia.ru/for_developer"]').click()
            return self

    def open_fair_page(self):
        with allure.step ('Open fair page'):
            browser.element('a.header-menu-list__title[href="/fair"]').click()
            return self

    def open_media_about_us_page(self):
        with allure.step('Open media about us page'):
            browser.element('a.header-menu-list__title[href="/media_about_us"]').click()
            return self

    def open_contacts_page(self):
        with allure.step ('Open contacts page'):
            browser.element('a.header-menu-list__title[href="/contacts"]').click()
            return self

    def open_future_page(self):
        with allure.step('Open future page'):
            browser.element('a.header-menu-list__title[href="https://future.russia.ru/"]').click()
            return self

    def open_gallery_page(self):
        with allure.step ('Open gallery page'):
            browser.element('a.header-menu-list__title[href="/gallery"]').click()
            return self

pop_up_menu_page = PopUpMenuPage()