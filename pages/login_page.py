from selenium import webdriver
from .base_page import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    #def should_be_login_url(self):
    #    URL = self.browser.find_element(By.CSS_SELECTOR, "#login_link")
     #   URL.click()
     #   get_url = self.browser.current_url
     #   print(get_url)
        # assert ('login' in get_url) ,  \
        # f"in URL don't have Login! '{get_url}'"
      #  URL2 = self.browser.find_element(By.XPATH, "/html/body/div[2]/div/ul/li[1]/a")
     #   URL2.click()
     #   get_url2 = self.browser.current_url
      #  print(get_url2)

    