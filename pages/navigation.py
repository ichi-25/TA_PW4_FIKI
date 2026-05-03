import allure
from playwright.sync_api import expect
from locators.login import Loc

class Navigation:
    def __init__(self, driver):
        self.driver = driver
    
    def check_url_page(self, url_page):    
        with allure.step('Check URL'):
            expect(self.driver).to_have_url(url_page)
    
    def check_error_msg(self, error_msg):
        with allure.step('Check error message'):
            self.driver.wait_for_selector(Loc.login_error)
            expect(self.driver.locator(Loc.login_error)).to_have_text(error_msg)