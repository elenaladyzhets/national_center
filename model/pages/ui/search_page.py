from selene import browser, have
import allure

class SearchPage:
    def open_search_page(self):
        with allure.step('Open search page'):
            browser.open('/search')
            return self

    def opened_empty_search_page(self):
        with allure.step ('Opened search page'):
            browser.element('h1.organizations__title').should(have.text('ПОИСК'))
            return self

    def opened_unavailable_search_page(self):
        with allure.step ('Opened unavailable search page'):
            browser.element('h2.text-primary').should(have.text('ПО ЗАПРОСУ НИЧЕГО НЕ НАЙДЕНО...'))
            return self

    def opened_available_search_page(self):
        with allure.step ('Opened available search page'):
            browser.element('h2.js-search-result-title').should(have.text('ЭКСКУРСИЯ'))
            return self



search_page = SearchPage()