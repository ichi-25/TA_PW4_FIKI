import allure
from locators.login import Loc

class Login:
    def __init__(self, driver):
        self.driver = driver        
    
    def input_email(self, email):    
        with allure.step('Input Email'):    
            self.driver.locator(Loc.input_email).fill(email)

    def input_password(self, password):
        with allure.step('Input Password'):
            self.driver.locator(Loc.input_pass).fill(password)

    def click_submit(self):
        with allure.step('Click Submit Button'):
            self.driver.locator(Loc.btn_submit).click()