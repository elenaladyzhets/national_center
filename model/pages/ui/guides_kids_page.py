from selene import browser, have
import allure

class GuidesKidsPage:
    def open_guides_kids_page(self):
        with allure.step('Open guides kids page'):
            browser.open('https://guides.kids.russia.ru/')
            return self

    def opened_guides_kids_page(self):
        with allure.step ('Check open guides kids page'):
            browser.element('#rec1235608691 .tn-elem__12356086911755806524608 .tn-atom') \
                .should(have.text('ШКОЛА ЮНОГО ЭКСКУРСОВОДА РОССИИ'))
            return self



guides_kids_page = GuidesKidsPage()