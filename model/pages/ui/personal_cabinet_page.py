from selene import browser, have, be, by
import allure
from dotenv import load_dotenv
import os


load_dotenv()

NAME= os.getenv("USER_NAME")

class PersonalCabinetPage:
    def open_cabinet_page(self):
        with allure.step('Open cabinet page'):
            browser.open('/personal/profile')
            return self

    def opened_cabinet_page(self):
        with allure.step('Check open profile page'):
            browser.element('.header-profile-dropdown-btn.authorized').should(have.text(NAME))
            return self

    def open_registration_page(self):
        with allure.step('Open registration page'):
            browser.open('/personal/simpleApplications')
            return self

    def should_have_event_with_status(self, title: str, status: str):
        with allure.step(f'Проверяем событие "{title}" со статусом "{status}"'):
            card = (browser.all('.show-card__content')
                    .filtered_by(have.text(title))
                    .filtered_by(have.text(status))
                    .with_(timeout=10)
                    .first)
            # доп. проверки внутри карточки (по желанию)
            card.element('.show-card__title').should(have.text(title))
            card.element('.show-card__accreditation-status').should(have.text(status))
        return self

    def cancel_event(self, title: str):
        with allure.step(f'Отменяем запись на событие "{title}"'):
            card = browser.element(by.xpath("//div[contains(@class,'show-card')]"
                "[.//a[contains(@class,'show-card__title') and contains(normalize-space(.), %s)]"
                " and .//div[contains(@class,'show-card__accreditation-status') and contains(., 'Подтверждена')]]"
                % repr(title)
            )).should(be.visible)
            card.element(".show-card__actions .js-delete-card-button").should(be.visible).should(be.clickable).click()
            browser.element(by.xpath("//div[contains(@class,'delete-ticket-block')]//button[contains(normalize-space(.),'Да, отменить')]")).should(be.visible).click()
            return self

personal_cabinet_page = PersonalCabinetPage()