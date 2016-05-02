# -*- coding: utf-8 -*-
from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, TimeoutException, StaleElementReferenceException
from datetime import datetime, timedelta
import selenium.webdriver.common.action_chains as AC
import time
import os
from logic.actions import *

TIME_FOR_WAIT = 30

@given('we have behave installed')
def step_impl(context):
    pass
  
# Then push link 'link text'
@then("push link '{link}'")
def step(context, link):
    click_on_link(context, link)               

# Then go to Main page
@then("go to Main page")
def step(context):
    open_main_page(context)    
    
# Then push link in header 'link text'
@then("push link in header '{text_link}'")
def step(context, text_link):
    xpath = "//span[contains(text(), '%s')]" % text_link
    click_on_xpath(context, xpath)    
   
# Then push 'button' in Request icons
@then("push '{button}' in Request icons")
def step(context, button):
    xpath = "//*[contains(text(), '%s')]" % button
    click_on_xpath(context, xpath) 
   
# Then locate image 'address'
@then("locate image '{link}'")    
def step(context, link):
    xpath = "//img[@src='%s']" % link
    locate_element(context, xpath)      
  
# Then locate category 'name'
@then("locate category '{name}'")    
def step(context, name):
    xpath = "//a[@ng-href='%s']" % name
    locate_element(context, xpath)     

# Then push link request icons
@then("push link Request icons")
def step(context):
    xpath = "//a[@class='c-pretty-link']"
    click_on_xpath(context, xpath)  

# Then close popup
@then("close popup")
def step(context):
    xpath = "(//div[@class='ng-modal-close'])[last()]"
    click_on_xpath(context, xpath)      
      
# Then locate image 'text image'
@then("locate image text '{text_image}'")
def step(context, text_image):
     xpath = "//img[@alt='%s']" % text_image
     locate_element(context, xpath)      

# Then locate element in popup
@then("locate element in popup")
def step(context):
     xpath = "//span[@class='hljs-doctype']"
     locate_element(context, xpath)     
     
# Then push button 'button text'
@then("push button '{button}'")
def step(context, button):
    click_on_button(context, button)

# Then push unactive tab 'Collections'
@then("push unactive tab")
def step(context):
    tab = 'b-tab'
    click_on_unactive_tab(context, tab)

#Then push button 'Create'    
@then("Then push 'Create'")
def step(context):
    create = 'b-collection-preview-create'
    click_on_create(context, create)
    
## xpath for new name of collection 
##//input[@ng-model='collsControl.newCollName']

# Прокрутить вниз страницы
# Then scroll to end of the page
@then("scroll to end of the page")
def step(context):
    scroll_down(context)
    
# Прокрутить в вверх страницы
# Then scroll to begin of the page
@then("scroll to begin of the page")
def step(context):
    scroll_up(context)

# Then locate text 'text'
@then("locate text '{text}'")
def step(context, text):
    locate_text(context, text)
   
# Then pedro search
@then("pedro search")
def step(context):
     xpath = "//input[@placeholder='Find an icon']"
     locate_element(context, xpath)       