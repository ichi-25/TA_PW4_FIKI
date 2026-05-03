import allure
import pytest
import os
from pages.login import Login
from pages.navigation import Navigation
from dotenv import load_dotenv

load_dotenv()

url_login = os.getenv('URL_LOGIN')
url_prod = os.getenv('URL_PRODUCT')
eml1 = os.getenv('EMAIL_TEST1')
eml2 = os.getenv('EMAIL_TEST2')
eml3 = os.getenv('EMAIL_TEST3')
pss1 = os.getenv('PASS_TEST1')
pss2 = os.getenv('PASS_TEST2')
error_message = 'Invalid login credentials'

data_login = [(eml1, pss1, url_prod, None),
              ('', pss1 , url_login, None),
              (eml1, '', url_login, None),
              ('', '', url_login, None),
              (eml2, pss1, url_login, None),
              (eml1, pss2, None, error_message),
              (eml3, pss2, None, error_message)]

@allure.title('Tugas Akhir')
@allure.description('Skenario login otomesyen versi POM')
@allure.severity(allure.severity_level.CRITICAL)
@allure.tag("NewUI", "Essentials", "Authentication")

@pytest.mark.parametrize('email, password, check_url, error_message', data_login)

def test_login(setup, email, password, check_url, error_message):
    login = Login(setup)
    
    login.input_email(email)
    login.input_password(password)
    login.click_submit()

    navigate = Navigation(setup)
    
    if check_url:
        navigate.check_url_page(check_url)
    else:
        navigate.check_error_msg(error_message)