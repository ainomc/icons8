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
	 
# Then push button what named 'Name button text'
@then("push button what named '{name}'")
def step(context, name):
    click_on_button_findByName(context, name)

# Then add text to field
@then("add text to '{field}'")
def step(context, field):
	text = random_idea_name()
	input_text(context, text, field)

# Then add '{input_text}' text to '{id_field}' field
@then("add '{input_text}' text to '{locator_field}' field")
def step(context, input_text, locator_field):
    if input_text == 'email':
        xpath = '//input[@id="%s"]' % locator_field
        text = random_email()
    elif input_text == 'password':
        xpath = '//input[@id="%s"]' % locator_field
        text = random_idea_name()
    elif input_text == 'positive text':
        xpath = '//*[@placeholder="%s"]' % locator_field
        text = random_listValue(['google', 'facebook', 'space', 'ball', 'car', 'word'])
    elif input_text == 'negative text':
        xpath = '//*[@placeholder="%s"]' % locator_field
        text = 'kjhgfdsalkjjhggfd'
    inputText(context, text, xpath)

# Choose random style of request icon
# Then choose style of request icon
@then("choose style of request icon")
def step(context):
    xpath = '//*[@ng-repeat="platform in icCtrl.platforms"][%s]' % random_betweenValue(1,5)
    click_on_xpath(context, xpath)

# Clear similar ideas in Request icon pop-up
# Thaen clear similar ideas
@then("clear similar ideas")
def step(context):
    xpath = '//div[@ng-show="modal.template"]'
    click_on_xpath(context, xpath)

# Choose one type of ideas what alreade created by filter
# Then click '{filter}' filter of already created ideas
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
    xpath = '//a[@class="c-recently-icon"][%s]' % values_in_range(1, 5)
    locate_element(context, xpath)

# Then check ideas list
@then("check ideas list")
def step(context):
    xpath = '//div[@class="b-idea-table-row"][%s]' % values_in_range(1, 5)
    locate_element(context, xpath)

# Then locate search field
@then("locate search field")
def step(context):
     xpath = '//div[@class="b-col-1"]'
     locate_element(context, xpath)

# Then check locate '{element}' element
@then("check locate '{element}' element")
def step(context, element):
    if element == 'Search result':
        xpath = '//*[@single-icon="icon"][%s]' % values_in_range(1, 5)
    else:
        xpath = '//*[@single-icon="icon"][1]'
    locate_element(context, xpath)

# Choose click '{menu}' on request icon menu page
@then("click '{menu}' request icon menu")
def step(context, menu):
    if menu == 'Slow for Free':
        xpath = '//a[@ng-repeat="page in reqIcon.requestPages"][1]'
    elif menu == 'Fast for $199/year':
        xpath = '//a[@ng-repeat="page in reqIcon.requestPages"][2]'
    elif menu == 'Fastest for $50/icon':
        xpath = '//a[@ng-repeat="page in reqIcon.requestPages"][3]'
    click_on_xpath(context, xpath)

# Then back to previous page
@then("back to previous page")
def step(context):
    back_to_previous_page(context)

# Then locate '{placeholder}' field
@then("locate '{placeholder}' field")
def step(context, placeholder):
    xpath = '//*[@placeholder="%s"]' % placeholder
    locate_element(context, xpath)

# Then click '{placeholder}' field
@then("click '{placeholder}' field")
def step(context, placeholder):
    xpath = '//*[@placeholder="%s"]' % placeholder
    click_on_xpath(context, xpath)

# Then locate '{value}' element
@then("locate '{value}' element")
def step(context, value):
    xpath = '//*[@value="%s"]' % value
    locate_element(context, xpath)

# Then click '{value}' element
@then("click '{value}' element")
def step(context, value):
    xpath = '//*[@value="%s"]' % value
    click_on_xpath(context, xpath)

# Then click login button in register pop-up
@then("click login button in register pop-up")
def step(context):
    xpath = '//a[contains(., "Login")][@class]'
    click_on_xpath(context, xpath)

# Then login
@then("login")
def step(context):
    login(context)

# Then check last created idea
@then("check last created idea")
def step(context):
    file_read_text = read_file("steps\logic\ideas.txt")
    xpath = '//idea[1]/div/a[contains(., "%s")]' % file_read_text
    assert locate_element(context, xpath)

# Then click on '{button}' button
@then("click on '{button}' button")
def step(context, button):
    if button == 'search':
        xpath = '//*[@class="b-search-btn"]'
    click_on_xpath(context, xpath)



# Then absent '{element}' element
@then("absent '{element}' element")
def step(context, element):
    if element == 'search result':
        xpath = '//*[@single-icon="icon"]'
    assert absent_element(context, xpath)

"""
# Then click '{button}' on '{block}' block
@then("click")
def step(context):
    clickAndMove_on_xpath(context)

    if block == 'Free' and button == 'Get':
        xpath = '''//div[@ng-bind-html="'PAGE.BUY.PLANS.FREE.GET' | translate"]'''
        moveTo = '//*[@callback="goToWebApp()"]'
    elif block == 'All 32,200 Icons' and button == 'Buy':
        xpath = '//div[@ng-class="licenses.companies.updates.id"]'
        moveTo = '//*[@callback="buyHoverBlock(licenses.companies.updates)"]'
    elif block == 'Pay per Icon Buy' and button == 'Buy':
        xpath = '''//div[3]/div[%s]/div[4][@ng-bind-html="'PAGE.BUY.PLANS.BUY' | translate"]''' % 2 #values_in_range(1, 4)
        moveTo = '''//*[@ng-bind-html="'PAGE.BUY.PLANS.PER_ICON.SAVE' | translate:{percent:'17%'}"]'''
"""


