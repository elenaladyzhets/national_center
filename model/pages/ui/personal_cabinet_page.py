from selene import browser, have
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


personal_cabinet_page = PersonalCabinetPage()