import allure
from playwright.sync_api import expect
from locators.login import Loc

class Login_failed:
    def __init__(self, driver):
        self.driver = driver        
    
    def check_error_msg(self, email):    
        with allure.step('Error Message'):    
            expect(self.driver.locator(Loc.login_error)).to_have_text(error_message)
