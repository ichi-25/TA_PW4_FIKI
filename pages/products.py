import allure
from playwright.sync_api import expect, Dialog
from locators.products import Loc

def dialog_confirmation(dialog: Dialog):
    dialog.accept()

class Products:
    def __init__(self, driver):
        self.driver = driver
    
    def check_username(self, name):    
        with allure.step('Check Username'):
            user = self.driver.locator(Loc.txt_usrnm)
            expect(user).to_have_text(name)
    
    def click_add(self):
        with allure.step('Click Add Product Button'):
            self.driver.locator(Loc.add_product_btn).click()
    
    def add_product(self, p_name, p_price, p_stock, p_cat, p_desc):
        with allure.step('Add New Product'):
            self.driver.locator(Loc.add_product_name).fill(p_name)
            self.driver.locator(Loc.add_product_price).fill(p_price)
            self.driver.locator(Loc.add_product_stock).fill(p_stock)
            self.driver.locator(Loc.add_product_cat).select_option(p_cat)
            self.driver.locator(Loc.add_product_desc).fill(p_desc)
        
    def submit_product(self):
        with allure.step('Submit New Product'):
            self.driver.locator(Loc.submit_product_btn).click()
    
    def check_product_name(self, p_name):
        with allure.step('Check Product by Name'):
            return self.driver.get_by_text(p_name, exact=True)

    def delete_product(self, p_name):
        with allure.step('Get Row by Product Name'):
            row = self.driver.locator(Loc.product_row).filter(has_text=p_name)
            target_button = row.locator(Loc.del_product_btn)

        with allure.step('Delete Product by Name'):
            self.driver.on("dialog", dialog_confirmation)
            target_button.click()
            expect(row).to_be_hidden()