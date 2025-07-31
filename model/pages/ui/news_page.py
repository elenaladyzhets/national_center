from selene import browser, have, be, query
import allure

class NewsPage:
    def open_news_page(self):
        with allure.step('Open news page'):
            browser.open('news')
            return self

    def opened_news_page(self):
        with allure.step ('Check open news page'):
            browser.element('.news__title').should(have.text('НОВОСТИ'))
            return self

    def valid_search(self,word):
        with allure.step('Check valid search'):
            browser.element('input.search__input').should(be.visible).set_value(word).press_enter()
            results = browser.all('a.news-card__title, div.news-card__text').with_(timeout=10)
            results.should(have.size_greater_than(0))
            texts = [el.get(query.text) for el in results]

            assert any(word.lower() in t.lower() for t in texts),f'Ничего не найдено'
            return self



news_page = NewsPage()