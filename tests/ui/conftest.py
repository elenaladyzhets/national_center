import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selene import browser
from utils import attach
from dotenv import load_dotenv


@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(scope='function', autouse=True)
def setting_browser():
    browser.config.base_url = 'https://russia.ru/'
    browser.config.window_height = 1080
    browser.config.window_width = 1920

    options = Options()
    options.add_argument('--start-maximized')
    # options.add_argument('--headless')  # Если нужен headless, раскомментируй

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    browser.config.driver = driver

    yield

    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    browser.quit()