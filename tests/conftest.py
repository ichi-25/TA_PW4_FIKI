from playwright.sync_api import sync_playwright, expect
import allure
import pytest
import os
from dotenv import load_dotenv

load_dotenv()

url = os.getenv('URL')

@pytest.fixture
def setup():
    with sync_playwright() as p:
        with allure.step('Buka Browser Chromium'):
            browser = p.chromium.launch(headless=False)
            page = browser.new_page(viewport={ 'width': 1280, 'height': 1024 })
            
        with allure.step('Buka aplikasi test Kelas Otomesyen'):
            page.goto(url)
            
        yield page
    
        with allure.step('Tutup browser'):
            browser.close()