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

now = datetime.today()

TIME_FOR_WAIT = 30

# Кликнуть на линк
def click_on_link(context, link):
    WebDriverWait(context.browser, TIME_FOR_WAIT).until(
        EC.element_to_be_clickable((By.XPATH, '//*[1][contains(text(), "%s")]' % link))
    )
    time.sleep(2)
    while True: 
        try:
            context.browser.find_element_by_xpath('//*[1][contains(text(), "%s")]' % link).click()
            break;
        except StaleElementReferenceException: 
            continue
            
def click_on_xpath(context, xpath):
    WebDriverWait(context.browser, TIME_FOR_WAIT).until(
        EC.element_to_be_clickable((By.XPATH, xpath))
    )
    element = context.browser.find_element_by_xpath(xpath)
  #  scroll_element_into_view(context.browser, element)
    element.click()            

        