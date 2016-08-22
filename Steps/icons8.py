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
from logic.generators import *
from behave import *


TIME_FOR_WAIT = 30

@given('we have behave installed')
def step_impl(context):
    pass
  
# Then push link 'link text'
@then("push link '{link}'")
def step(context, link):
    click_on_link(context, link)               

# Then push second link 'link text'
@then("push second link '{link}'")
def step(context, link):
    xpath = "(//*[1][contains(text(), '%s')])[2]" % link
    click_on_xpath(context, xpath) 
    
# Then go to Main page
@then("go to Main page")
def step(context):
    open_main_page(context)    
    
# Then push link in header 'link text'
@then("push link in header '{text_link}'")
def step(context, text_link):
    xpath = "//span[contains(text(), '%s')]" % text_link
    click_on_xpath(context, xpath)    
   
# Then push 'button' from tabs
@then("push '{button}' from tabs")
def step(context, button):
    xpath = "//*[contains(text(), '%s')]" % button
    click_on_xpath(context, xpath) 
   
# Then push link Logout
@then("push link Logout")
def step(context):
    xpath = "//*[@href='/logout/']"
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
	 
# Then push button what named 'Name buton text'
@then("push button what named '{name}'")
def step(context, name):
    click_on_button_findByName(context, name)

# Then add text to field
@then("add text to '{field}'")
def step(context, field):
	text = random_idea_name()
	input_text(context, text, field)

# Choose random style of request icon
@then("choose style of request icon")
def step(context):
    xpath = '//*[@class="ng-pristine ng-untouched ng-valid ng-scope ng-isolate-scope"][%s]' % random_betweenValue(1,5)
    click_on_xpath(context, xpath)

# Clear similar ideas in Request icon pop-up
@then("clear similar ideas")
def step(context):
    xpath = '//div[@class="modal__content ng-scope"]'
    click_on_xpath(context, xpath)

# Choose one type of ideas what alreade created by filter
@then("click '{filter}' filter of already created ideas")
def step(context, filter):
    if filter == 'Hot ideas':
        xpath = '//*[@ng-repeat="filter in reqIcon.iconFilters"][1]'
    elif filter == 'Latest ideas':
        xpath = '//*[@ng-repeat="filter in reqIcon.iconFilters"][2]'
    elif filter == 'Popular ideas':
        xpath = '//*[@ng-repeat="filter in reqIcon.iconFilters"][3]'
    click_on_xpath(context, xpath)

# Then check ideas list in filter
@then("check ideas list in filter")
def step(context):
    xpath = '//*[@ng-model="idea"][%s]' % values_in_range(1, 5)
    locate_element(context, xpath)

# Then check recently created icons
@then("check recently created icons")
def step(context):
    xpath = '//a[@class="c-recently-icon ng-binding ng-scope"][%s]' % values_in_range(1, 5)
    locate_element(context, xpath)