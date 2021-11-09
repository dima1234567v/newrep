from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import MainPageLocators
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasketPage(BasePage):
    def go_to_basket(self):
       basket = self.browser.find_element(By.XPATH, "/html/body/header/div[1]/div/div[2]/span/a")
       basket.click()

    def is_not_element_present(self, how, what, timeout=4):
       try:
           WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
       except TimeoutException:
           return True

       return False

    def is_not_need(self):
       assert self.is_not_element_present(By.XPATH, "/html/body/div[2]/div/div[3]/div[2]/p/text()"), \
          "message is presented"  
 
    