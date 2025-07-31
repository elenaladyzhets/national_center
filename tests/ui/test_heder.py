import allure

from model.pages.ui.photobank_exhibitions_Russia_page import photobank_exhib_russia_page
from model.pages.ui.contacts_page import contacts_page
from model.pages.ui.fair_page import fair_page
from model.pages.ui.for_developer_page import for_developer_page
from model.pages.ui.for_media_page import for_media_page
from model.pages.ui.photobank_RIA_page import photobank_ria_page
from model.pages.ui.architecture_page import architecture_page
from model.pages.ui.broadcasts_page import broadcasts_page
from model.pages.ui.creative_hub_page import creative_hub_page
from model.pages.ui.legacy_page import legacy_page
from model.pages.ui.header import header_page
from model.pages.ui.news_page import news_page
from model.pages.ui.events_page import events_page
from model.pages.ui.photobank_page import photobank_page
from model.pages.ui.search_page import search_page
from model.pages.ui.victory_routes_page import victory_routes_page
from model.pages.ui.wedding_page import wedding_page
from model.pages.ui.main_page import main_page
from model.pages.ui.personal_cabinet_page import personal_cabinet_page




@allure.epic('UI. Header')
@allure.label('owner', 'Elena Ladyzhets')
@allure.feature('Open news page')
@allure.tag('ui')
@allure.severity('normal')
def test_open_news_page():
    main_page.open()
    header_page.open_news_page_from_header()
    news_page.opened_news_page()


@allure.epic('UI. Header')
@allure.label('owner', 'Elena Ladyzhets')
@allure.feature('Open events page')
@allure.tag('ui')
@allure.severity('normal')
def test_open_events_page():
    main_page.open()
    header_page.open_events_page_from_header()
    events_page.opened_events_page()

@allure.epic('UI. Header')
@allure.label('owner', 'Elena Ladyzhets')
@allure.feature('Open legacy page')
@allure.tag('ui')
@allure.severity('normal')
def test_open_legacy_page():
    main_page.open()
    header_page.open_legacy_page_from_header()
    legacy_page.opened_legacy_page()

@allure.epic('UI. Header')
@allure.label('owner', 'Elena Ladyzhets')
@allure.feature('Open wedding page')
@allure.tag('ui')
@allure.severity('normal')
def test_open_wedding_page():
    main_page.open()
    header_page.open_wedding_page_from_header()
    wedding_page.opened_wedding_page()

@allure.epic('UI. Header')
@allure.label('owner', 'Elena Ladyzhets')
@allure.feature('Open victory routes page')
@allure.tag('ui')
@allure.severity('normal')
def test_open_victory_routes_page():
    main_page.open()
    header_page.open_victory_routes_page_from_header()
    victory_routes_page.opened_victory_routes_page()

@allure.epic('UI. Header')
@allure.label('owner', 'Elena Ladyzhets')
@allure.feature('Open architecture page')
@allure.tag('ui')
@allure.severity('normal')
def test_open_architecture_page():
    main_page.open()
    header_page.open_architecture_page_from_header()
    architecture_page.opened_architecture_page()

@allure.epic('UI. Header')
@allure.label('owner', 'Elena Ladyzhets')
@allure.feature('Open creative hub page')
@allure.tag('ui')
@allure.severity('normal')
def test_open_creative_hub_page():
    main_page.open()
    header_page.open_creative_hub_page_from_header()
    creative_hub_page.opened_creative_hub_page()

@allure.epic('UI. Header')
@allure.label('owner', 'Elena Ladyzhets')
@allure.feature('Open broadcasts page')
@allure.tag('ui')
@allure.severity('normal')
def test_open_broadcasts_page():
    main_page.open()
    header_page.open_broadcasts_page_from_header()
    broadcasts_page.opened_broadcasts_page()


@allure.epic('UI. Header')
@allure.label('owner', 'Elena Ladyzhets')
@allure.feature('Open  photobank page')
@allure.tag('ui')
@allure.severity('normal')
def test_open_photobank_page():
    main_page.open()
    header_page.open_photobank_page_from_header()
    photobank_page.opened_photobank_page()

@allure.epic('UI. Header')
@allure.label('owner', 'Elena Ladyzhets')
@allure.feature('Open  photobank directorate page')
@allure.tag('ui')
@allure.severity('normal')
def test_open_photobank_directorate_page():
    main_page.open()
    header_page.open_photobank_directorate_page_from_header()
    photobank_page.opened_photobank_page()

@allure.epic('UI. Header')
@allure.label('owner', 'Elena Ladyzhets')
@allure.feature('Open  photobank RIA page')
@allure.tag('ui')
@allure.severity('normal')
def test_open_photobank_ria_page():
    main_page.open()
    header_page.open_photobank_RIA_page_from_header()
    photobank_ria_page.opened_photobank_ria_page()

@allure.epic('UI. Header')
@allure.label('owner', 'Elena Ladyzhets')
@allure.feature('Open  photobank exhibitions Russia page')
@allure.tag('ui')
@allure.severity('normal')
def test_open_photobank_exhibitions_russia_page():
    main_page.open()
    header_page.open_photobank_exhibitions_Russia_page_from_header()
    photobank_exhib_russia_page.opened_photobank_exhib_russia_page()

@allure.epic('UI. Header')
@allure.label('owner', 'Elena Ladyzhets')
@allure.feature('Open  for media page')
@allure.tag('ui')
@allure.severity('normal')
def test_open_for_media_page():
    main_page.open()
    header_page.open_for_media_page_from_header()
    for_media_page.opened_for_media_page()

@allure.epic('UI. Header')
@allure.label('owner', 'Elena Ladyzhets')
@allure.feature('Open  fair page')
@allure.tag('ui')
@allure.severity('normal')
def test_open_fair_page():
    main_page.open()
    header_page.open_fair_page_from_header()
    fair_page.opened_fair_page()

@allure.epic('UI. Header')
@allure.label('owner', 'Elena Ladyzhets')
@allure.feature('Open  for developer page')
@allure.tag('ui')
@allure.severity('normal')
def test_open_for_developer_page():
    main_page.open()
    header_page.open_for_developer_page_from_header()
    for_developer_page.opened_for_developer_page()

@allure.epic('UI. Header')
@allure.label('owner', 'Elena Ladyzhets')
@allure.feature('Open  contacts page')
@allure.tag('ui')
@allure.severity('normal')
def test_open_contacts_page():
    main_page.open()
    header_page.open_contacts_page_from_header()
    contacts_page.opened_contscts_page()

@allure.epic('UI. Header')
@allure.label('owner', 'Elena Ladyzhets')
@allure.feature('Search from pop up menu')
@allure.tag('ui')
@allure.severity('normal')
def test_search_available_result():
    main_page.open()
    header_page.search_available_from_heder()
    search_page.opened_available_search_page()

@allure.epic('UI. Header')
@allure.label('owner', 'Elena Ladyzhets')
@allure.feature('Search from pop up menu')
@allure.tag('ui')
@allure.severity('normal')
def test_search_unavailable_result():
    main_page.open()
    header_page.search_unavailable_from_heder()
    search_page.opened_unavailable_search_page()

@allure.epic('UI. Header')
@allure.label('owner', 'Elena Ladyzhets')
@allure.feature('Log in')
@allure.tag('ui')
@allure.severity('normal')
def test_log_in_from_header():
    main_page.open()
    header_page.log_in_from_header()
    personal_cabinet_page.opened_cabinet_page()