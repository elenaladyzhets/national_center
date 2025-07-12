from selene import browser, have
import allure

class ArchitecturePage:
    def open_architecture_page(self):
        with allure.step('Open architecture page'):
            browser.open('/architecture')
            return self

    def opened_architecture_page(self):
        with allure.step ('Check open architecture page'):
            browser.element('.main-architecture-slider__title').should(have.text('РОЖДЕНИЕ МАСШТАБА'))
            return self



architecture_page = ArchitecturePage()