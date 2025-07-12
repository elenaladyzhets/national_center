from selene import browser, have
import allure

class ContactsPage:
    def open_contacts_page(self):
        with allure.step('Open contacts page'):
            browser.open('/contacts')
            return self

    def opened_contacts_page(self):
        with allure.step ('Check open contacts page'):
            browser.element('.default-section__title').should(have.text('КОНТАКТЫ'))
            return self



contacts_page = ContactsPage()