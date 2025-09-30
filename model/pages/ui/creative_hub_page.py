from selene import browser, have
import allure

class CreativeHubPage:
    def open_creative_hub_page(self):
        with allure.step('Open creative hub page'):
            browser.open('/creative_hub')
            return self

    def opened_creative_hub_page(self):
        with allure.step ('Check open creative_hub page'):
            browser.element('.creative-hub__title').should(have.text('КРЕАТИВНЫЙ ХАБ'))
            return self

    def opened_creative_hub_gallery_page(self):
        with allure.step ('Check open creative_hub page'):
            browser.element('.creative-hub-gallery__title').should(have.text('РАБОТЫ УЧАСТНИКОВ КОНКУРСА «КРЕАТИВНЫЙ ХАБ»'))
            return self



creative_hub_page = CreativeHubPage()