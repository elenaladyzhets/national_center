import allure

from model.pages.ui.events_page import events_page
from model.pages.ui.main_page import main_page
from model.pages.ui.header import header_page
from model.pages.ui.personal_cabinet_page import personal_cabinet_page


@allure.epic('UI. Events page')
@allure.label('owner', 'Elena Ladyzhets')
@allure.feature('Registration')
@allure.tag('ui')
@allure.severity('normal')
def test_registration():
    main_page.open()
    header_page.log_in_from_header()
    personal_cabinet_page.opened_cabinet_page()
    events_page.open_events_page()
    events_page.open_event_page()
    events_page.valid_individual_registration_without_guests()
    events_page.select_region()
    events_page.submit_registration()
    events_page.confirm_registration_popup()
    personal_cabinet_page.open_registration_page()
    personal_cabinet_page.should_have_event_with_status("Интерактивная экскурсия «Путешествие по России»","Подтверждена")

@allure.epic('UI. Events page')
@allure.label('owner', 'Elena Ladyzhets')
@allure.feature('Cansel registration')
@allure.tag('ui')
@allure.severity('normal')
def test_cancel_registration():
    main_page.open()
    header_page.log_in_from_header()
    personal_cabinet_page.opened_cabinet_page()
    personal_cabinet_page.open_registration_page()
    personal_cabinet_page.cancel_event("Интерактивная экскурсия «Путешествие по России»")