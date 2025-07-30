import allure

from model.pages.ui import search_page
from model.pages.ui.future_page import future_page
from model.pages.ui.gallery_page import gallery_page
from model.pages.ui.media_about_us_page import media_about_us_page
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
from model.pages.ui.main_page import main_page
from model.pages.ui.news_page import news_page
from model.pages.ui.events_page import events_page
from model.pages.ui.photobank_page import photobank_page
from model.pages.ui.pop_up_menu_page import pop_up_menu_page
from model.pages.ui.socials_page import socials_page
from model.pages.ui.victory_routes_page import victory_routes_page
from model.pages.ui.wedding_page import wedding_page
from model.pages.ui.dialog_page import dialog_page
from model.pages.ui.search_page import search_page


@allure.epic('UI. Pop up menu')
@allure.label('owner', 'Elena Ladyzhets')
@allure.feature('Open news page')
@allure.tag('ui')
@allure.severity('normal')
def test_open_news_page():
    main_page.open()
    main_page.open_pop_up_menu()
    pop_up_menu_page.open_news_page()
    news_page.opened_news_page()

@allure.epic('UI. Pop up menu')
@allure.label('owner', 'Elena Ladyzhets')
@allure.feature('Open events page')
@allure.tag('ui')
@allure.severity('normal')
def test_open_events_page():
    main_page.open()
    main_page.open_pop_up_menu()
    pop_up_menu_page.open_events_page()
    events_page.opened_events_page()

@allure.epic('UI. Pop up menu')
@allure.label('owner', 'Elena Ladyzhets')
@allure.feature('Open legacy page')
@allure.tag('ui')
@allure.severity('normal')
def test_open_legacy_page():
    main_page.open()
    main_page.open_pop_up_menu()
    pop_up_menu_page.open_legacy_page()
    legacy_page.opened_legacy_page()

@allure.epic('UI. Pop up menu')
@allure.label('owner', 'Elena Ladyzhets')
@allure.feature('Open architecture page')
@allure.tag('ui')
@allure.severity('normal')
def test_open_architecture_page_from_menu():
    main_page.open()
    main_page.open_pop_up_menu()
    pop_up_menu_page.open_architecture_page_from_menu()
    architecture_page.opened_architecture_page()

@allure.epic('UI. Pop up menu')
@allure.label('owner', 'Elena Ladyzhets')
@allure.feature('Open architecture page')
@allure.tag('ui')
@allure.severity('normal')
def test_open_architecture_page_from_menu_list():
    main_page.open()
    main_page.open_pop_up_menu()
    pop_up_menu_page.open_architecture_page_from_menu_list()
    architecture_page.opened_architecture_page()

@allure.epic('UI. Pop up menu')
@allure.label('owner', 'Elena Ladyzhets')
@allure.feature('Open creative hub page')
@allure.tag('ui')
@allure.severity('normal')
def test_open_creative_hub_page():
    main_page.open()
    main_page.open_pop_up_menu()
    pop_up_menu_page.open_creative_hub_page()
    creative_hub_page.opened_creative_hub_page()

@allure.epic('UI. Pop up menu')
@allure.label('owner', 'Elena Ladyzhets')
@allure.feature('Open photobank page')
@allure.tag('ui')
@allure.severity('normal')
def test_open_photobank_page_from_menu():
    main_page.open()
    main_page.open_pop_up_menu()
    pop_up_menu_page.open_photobank_page_from_menu()
    photobank_page.opened_photobank_page()

@allure.epic('UI. Pop up menu')
@allure.label('owner', 'Elena Ladyzhets')
@allure.feature('Open photobank page')
@allure.tag('ui')
@allure.severity('normal')
def test_open_photobank_page_from_menu_list():
    main_page.open()
    main_page.open_pop_up_menu()
    pop_up_menu_page.open_photobank_page_from_menu_list()
    photobank_page.opened_photobank_page()

@allure.epic('UI. Pop up menu')
@allure.label('owner', 'Elena Ladyzhets')
@allure.feature('Open photobank RIA page')
@allure.tag('ui')
@allure.severity('normal')
def test_open_photobank_RIA_page():
    main_page.open()
    main_page.open_pop_up_menu()
    pop_up_menu_page.open_photobank_RIA_page()
    photobank_ria_page.opened_photobank_ria_page()

@allure.epic('UI. Pop up menu')
@allure.label('owner', 'Elena Ladyzhets')
@allure.feature('Open photobank exhibition Russia page')
@allure.tag('ui')
@allure.severity('normal')
def test_open_photobank_exhibition_Russia_page():
    main_page.open()
    main_page.open_pop_up_menu()
    pop_up_menu_page.open_photobank_exhibitions_Russia_page()
    photobank_exhib_russia_page.opened_photobank_exhib_russia_page()

@allure.epic('UI. Pop up menu')
@allure.label('owner', 'Elena Ladyzhets')
@allure.feature('Open wedding page')
@allure.tag('ui')
@allure.severity('normal')
def test_open_wedding_page():
    main_page.open()
    main_page.open_pop_up_menu()
    pop_up_menu_page.open_wedding_page()
    wedding_page.opened_wedding_page()

@allure.epic('UI. Pop up menu')
@allure.label('owner', 'Elena Ladyzhets')
@allure.feature('Open broadcasts page')
@allure.tag('ui')
@allure.severity('normal')
def test_open_broadcasts_page():
    main_page.open()
    main_page.open_pop_up_menu()
    pop_up_menu_page.open_broadcasts_page()
    broadcasts_page.opened_broadcasts_page()

@allure.epic('UI. Pop up menu')
@allure.label('owner', 'Elena Ladyzhets')
@allure.feature('Open victory routes page')
@allure.tag('ui')
@allure.severity('normal')
def test_open_victory_routes_page():
    main_page.open()
    main_page.open_pop_up_menu()
    pop_up_menu_page.open_victory_routes_page()
    victory_routes_page.opened_victory_routes_page()

@allure.epic('UI. Pop up menu')
@allure.label('owner', 'Elena Ladyzhets')
@allure.feature('Open dialog page')
@allure.tag('ui')
@allure.severity('normal')
def test_open_dialog_page():
    main_page.open()
    main_page.open_pop_up_menu()
    pop_up_menu_page.open_dialog_page()
    dialog_page.opened_dialog_page()

@allure.epic('UI. Pop up menu')
@allure.label('owner', 'Elena Ladyzhets')
@allure.feature('Open for media page')
@allure.tag('ui')
@allure.severity('normal')
def test_open_for_media_page():
    main_page.open()
    main_page.open_pop_up_menu()
    pop_up_menu_page.open_for_media_page()
    for_media_page.opened_for_media_page()

@allure.epic('UI. Pop up menu')
@allure.label('owner', 'Elena Ladyzhets')
@allure.feature('Open for developer page')
@allure.tag('ui')
@allure.severity('normal')
def test_open_for_developer_page():
    main_page.open()
    main_page.open_pop_up_menu()
    pop_up_menu_page.open_for_developer_page()
    for_developer_page.opened_for_developer_page()

@allure.epic('UI. Pop up menu')
@allure.label('owner', 'Elena Ladyzhets')
@allure.feature('Open fair page')
@allure.tag('ui')
@allure.severity('normal')
def test_open_fair_page():
    main_page.open()
    main_page.open_pop_up_menu()
    pop_up_menu_page.open_fair_page()
    fair_page.opened_fair_page()

@allure.epic('UI. Pop up menu')
@allure.label('owner', 'Elena Ladyzhets')
@allure.feature('Open media about us page')
@allure.tag('ui')
@allure.severity('normal')
def test_open_media_bout_us_page():
    main_page.open()
    main_page.open_pop_up_menu()
    pop_up_menu_page.open_media_about_us_page()
    media_about_us_page.opened_media_about_us_page()

@allure.epic('UI. Pop up menu')
@allure.label('owner', 'Elena Ladyzhets')
@allure.feature('Open contacts page')
@allure.tag('ui')
@allure.severity('normal')
def test_open_contacts_page():
    main_page.open()
    main_page.open_pop_up_menu()
    pop_up_menu_page.open_contacts_page()
    contacts_page.opened_contacts_page()

@allure.epic('UI. Pop up menu')
@allure.label('owner', 'Elena Ladyzhets')
@allure.feature('Open future page')
@allure.tag('ui')
@allure.severity('normal')
def test_open_future_page():
    main_page.open()
    main_page.open_pop_up_menu()
    pop_up_menu_page.open_future_page()
    future_page.opened_future_page()

@allure.epic('UI. Pop up menu')
@allure.label('owner', 'Elena Ladyzhets')
@allure.feature('Open gallery page')
@allure.tag('ui')
@allure.severity('normal')
def test_open_gallery_page():
    main_page.open()
    main_page.open_pop_up_menu()
    pop_up_menu_page.open_gallery_page()
    gallery_page.opened_gallery_page()

@allure.epic('UI. Pop up menu')
@allure.label('owner', 'Elena Ladyzhets')
@allure.feature('Close pop up menu')
@allure.tag('ui')
@allure.severity('normal')
def test_close_pop_up_menu():
    main_page.open()
    main_page.open_pop_up_menu()
    pop_up_menu_page.close_pop_up_menu()
    main_page.opened()

@allure.epic('UI. Pop up menu')
@allure.label('owner', 'Elena Ladyzhets')
@allure.feature('Change language')
@allure.tag('ui')
@allure.severity('normal')
def test_change_language_ru_to_eng():
    main_page.open()
    main_page.open_pop_up_menu()
    pop_up_menu_page.change_language_ru_to_eng()
    main_page.change_language_ru_to_eng()

@allure.epic('UI. Pop up menu')
@allure.label('owner', 'Elena Ladyzhets')
@allure.feature('Change language')
@allure.tag('ui')
@allure.severity('normal')
def test_change_language_eng_to_ru():
    main_page.open()
    main_page.open_pop_up_menu()
    pop_up_menu_page.change_language_ru_to_eng()
    main_page.open_pop_up_menu()
    pop_up_menu_page.change_language_eng_to_ru()
    main_page.opened()

@allure.epic('UI. Pop up menu')
@allure.label('owner', 'Elena Ladyzhets')
@allure.feature('Search from pop up menu')
@allure.tag('ui')
@allure.severity('normal')
def test_search_available_result():
    main_page.open()
    main_page.open_pop_up_menu()
    pop_up_menu_page.search_from_pop_up_menu()
    search_page.opened_available_search_page()

@allure.epic('UI. Pop up menu')
@allure.label('owner', 'Elena Ladyzhets')
@allure.feature('Link to telegram')
@allure.tag('ui')
@allure.severity('normal')
def test_link_to_tg():
    main_page.open()
    main_page.open_pop_up_menu()
    pop_up_menu_page.link_to_telegram()
    socials_page.open_telegram_page()

@allure.epic('UI. Pop up menu')
@allure.label('owner', 'Elena Ladyzhets')
@allure.feature('Link to vk')
@allure.tag('ui')
@allure.severity('normal')
def test_link_to_vk():
    main_page.open()
    main_page.open_pop_up_menu()
    pop_up_menu_page.link_to_vk()
    socials_page.open_vk_page()

@allure.epic('UI. Pop up menu')
@allure.label('owner', 'Elena Ladyzhets')
@allure.feature('Link to ok')
@allure.tag('ui')
@allure.severity('normal')
def test_link_to_ok():
    main_page.open()
    main_page.open_pop_up_menu()
    pop_up_menu_page.link_to_ok()
    socials_page.open_ok_page()

@allure.epic('UI. Pop up menu')
@allure.label('owner', 'Elena Ladyzhets')
@allure.feature('Link to dzen')
@allure.tag('ui')
@allure.severity('normal')
def test_link_to_dzen():
    main_page.open()
    main_page.open_pop_up_menu()
    pop_up_menu_page.link_to_dzen()
    socials_page.open_dzen_page()
