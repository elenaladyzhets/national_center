from selene import browser, have
import allure

class NewsPage:
    def open_news_page(self):
        with allure.step('Open news page'):
            browser.open('/news')
            return self

    def opened_news_page(self):
        with allure.step ('Check open news page'):
            browser.element('.news__title').should(have.text('НОВОСТИ'))
            return self



news_page = NewsPage()