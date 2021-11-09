from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
import pytest


link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"

#@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                       #          "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                       #           "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                       #           "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                       #           "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                       #           "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                       #           "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                        #           pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
                       #           "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                        #          "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
@pytest.mark.need_review
class TestLoginFromMainPage2():
   def test_guest_can_add_product_to_basket(self, browser):
      page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
      page.open()                      # открываем страницу
      page.go_to_login_page()          # выполняем метод страницы — переходим на страницу логина
      page.solve_quiz_and_get_code()


   def test_guest_should_see_login_link_on_product_page(self, browser):
      link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
      page = ProductPage(browser, link)
      page.open()
      page.should_be_login_link()

   def test_guest_can_go_to_login_page_from_product_page(self, browser):
       link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
       page = ProductPage(browser, link)
       page.open()
       page.go_to_login_page_2()


   def test_user_cant_see_product_in_basket_opened_from_product_page(self, browser):
       link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
       page = ProductPage(browser, link)
       page2 = BasketPage(browser, link)
       page.open()
       page.go_to_garb()
       page2.is_not_need()

    

    
