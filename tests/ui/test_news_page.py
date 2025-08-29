import allure

from model.pages.ui.news_page import news_page

@allure.epic('UI. News page')
@allure.label('owner', 'Elena Ladyzhets')
@allure.feature('Search')
@allure.tag('ui')
@allure.severity('normal')
def test_search(search_word):
    news_page.open_news_page()
    news_page.valid_search(search_word)

#@allure.epic('UI. News page')
#@allure.label('owner', 'Elena Ladyzhets')
#@allure.feature('Sort date')
#@allure.tag('ui')
#@allure.severity('normal')
#def test_sort_date():
 #   news_page.open_news_page()
  #  news_page.select_date("2024-11-05")
