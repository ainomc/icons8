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
    
