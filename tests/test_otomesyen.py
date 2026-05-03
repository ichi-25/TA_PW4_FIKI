import allure
import pytest
import os
from pages.login import Login
from pages.navigation import Navigation
from pages.products import Products
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
product_name = os.getenv('PRODUCT_TEST_NAME')
product_price = os.getenv('PRODUCT_TEST_PRICE')
product_stock = os.getenv('PRODUCT_TEST_STOCK')
product_cat = os.getenv('PRODUCT_TEST_CAT')
product_desc = os.getenv('PRODUCT_TEST_DESC')

data_login = [(eml1, pss1, url_prod, None),
              ('', pss1 , url_login, None),
              (eml1, '', url_login, None),
              ('', '', url_login, None),
              (eml2, pss1, url_login, None),
              (eml1, pss2, None, error_message),
              (eml3, pss2, None, error_message)]

@allure.title('LOGIN TEST')
@allure.description('Tes login versi POM')
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

@allure.title('PRODUCT TEST')
@allure.description('Tes product versi POM')

def test_product(setup):
    login = Login(setup)
    
    login.input_email(eml1)
    login.input_password(pss1)
    login.click_submit()

    navigate = Navigation(setup)

    navigate.check_url_page(url_prod)

    products = Products(setup)

    products.check_username('uno')
    products.click_add()
    products.add_product(product_name, product_price, product_stock, product_cat, product_desc)
    products.submit_product()
    products.check_product_name(product_name)
    products.delete_product(product_name)