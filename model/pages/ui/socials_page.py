from selene import browser, have
import allure

class SocialsPage:
    def open_telegram_page(self):
        with allure.step('Open telegram page'):
            browser.element('a.tgme_action_button_new').should(have.text('VIEW IN TELEGRAM'))
            browser.element('a.tgme_action_button_new').should(have.attribute('href', 'tg://resolve?domain=gowithRussia'))
            return self

    def open_vk_page(self):
        with allure.step('Open vk page'):
            assert 'vk.com/gowithrussia' in browser.driver.current_url
            browser.element('h1.page_name').should(have.text('Национальный центр «Россия»'))
            return self

    def open_ok_page(self):
        with allure.step('Open ok page'):
            assert "ok.ru/gowithrussia" in browser.driver.current_url
            browser.element('h1.group-name_h').should(have.text('Национальный центр «Россия»'))
            return self

    def open_dzen_page(self):
        with allure.step('Open dzen page'):
            assert 'dzen.ru/gowithrussia' in browser.driver.current_url
            browser.element('h1.channel--channel-title__block-nt').should(have.text('Национальный центр «Россия»'))
            return self





socials_page = SocialsPage()