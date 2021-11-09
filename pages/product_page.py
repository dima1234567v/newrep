from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import MainPageLocators

class ProductPage(BasePage): 
    def go_to_login_page(self):
        login_link = self.browser.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div[2]/article/div[1]/div[2]/form/button")
        login_link.click()

    def go_to_login_page_2(self):
        login_link_2 = self.browser.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/ul/li/a")
        login_link_2.click() 
     
    def go_to_garb(self):
        garb = self.browser.find_element(By.XPATH, "/html/body/header/div[1]/div/div[2]/span/a")
        garb.click() 
