# -*- coding: utf-8 -*-
from behave import *
from selenium import webdriver
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
        EC.element_to_be_clickable((By.XPATH, '//*[1][contains(text(), "%s")]' % link)) ### '//*[1][contains(text(), "%s")] - old version
    )
    time.sleep(2)
    while True: 
        try:
            context.browser.find_element_by_xpath('//*[1][contains(text(), "%s")]' % link).click()
            break
        except StaleElementReferenceException: 
            continue

# скроллинг до элемента
def scroll_element_into_view(driver, element):
    """Scroll element into view"""
    y = element.location['y']
# От верхненего края на 250 пикселей
    y = y - 250 
    driver.execute_script('window.scrollTo(0, {0})'.format(y))            
 
# кликнуть на элемент по xpath
def click_on_xpath(context, xpath):
    WebDriverWait(context.browser, TIME_FOR_WAIT).until(
        EC.element_to_be_clickable((By.XPATH, xpath))
    )
    element = context.browser.find_element_by_xpath(xpath)
    scroll_element_into_view(context.browser, element)
    element.click()          

# Кликнуть на кнопку
def click_on_button(context, button):
    WebDriverWait(context.browser, TIME_FOR_WAIT).until(
        EC.element_to_be_clickable((By.XPATH, '//button[.="%s"]' % button))
    )
    time.sleep(2)
    while True:
        try:
            context.browser.find_element_by_xpath('//button[.="%s"]' % button).click()
            break
        except StaleElementReferenceException:
            continue

# Кликнуть на вкладку
def click_on_unactive_tab(context, tab):
    WebDriverWait(context.browser, TIME_FOR_WAIT).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@class="%s"]' % tab))                
    )
    time.sleep(2)
    while True:
        try:
            context.browser.find_element_by_xpath('//*[@class="%s"]' % tab).click()
            break
        except StaleElementReferenceException:
            continue        

# Кликнуть на кнопку Создать коллекцию            
def click_on_create(context, create):
    WebDriverWait(context.browser, TIME_FOR_WAIT).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@class="%s"]' % create))                
    )
    time.sleep(2)
    while True:
        try:
            context.browser.find_element_by_xpath('//*[@class="%s"]' % create).click()
            break
        except StaleElementReferenceException:
            continue

"""            
//input[@ng-model='collsControl.newCollName']


def login(context, server=SERVER, login=LOGIN, password=PASSWORD):
    '''
    Функция для логина в аккаунте.
    Ввести логин и пароль, нажать "Login"
    '''
    # неявные ожидания
    # context.browser.implicitly_wait(120)
    print ('I try to login into account...')
    
    context.browser.get(server)
    context.browser.find_element_by_link_text("Login").click()
    WebDriverWait(context.browser, 1000).until(
        EC.presence_of_element_located((By.ID, 'RegisterForm_email'))
    )
    context.browser.find_element_by_id("RegisterForm_email").clear()
    context.browser.find_element_by_id("RegisterForm_email").send_keys(login)
    context.browser.find_element_by_id("RegisterForm_password").clear()
    context.browser.find_element_by_id("RegisterForm_password").send_keys(password)
    context.browser.find_element_by_name("yt0").click()
       
    text = 'All the Icons You Need. Guaranteed.'.decode('utf-8')
    WebDriverWait(context.browser, 1000).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='home-app']/div[2]/div/h2"))
    )
    
    time.sleep(2)
    
    print ('DONE!')
"""    





# def login(context, server=SERVER, login=LOGIN, password=PASSWORD):
    # '''
    # Функция для логина в аккаунте.
    # Ввести логин и пароль, нажать "Login"
    # '''
    # # неявные ожидания
    # # context.browser.implicitly_wait(120)
    # print ('I try to login into account...')
    
    # context.browser.get(server)
    # context.browser.find_element_by_link_text("Login").click()
    # WebDriverWait(context.browser, 1000).until(
        # EC.presence_of_element_located((By.XPATH, '//input[@ng-model='collsControl.newCollName']'))
    # )
    # context.browser.find_element_by_id("RegisterForm_email").clear()
    # context.browser.find_element_by_id("RegisterForm_email").send_keys(login)
    # context.browser.find_element_by_id("RegisterForm_password").clear()
    # context.browser.find_element_by_id("RegisterForm_password").send_keys(password)
    # context.browser.find_element_by_name("yt0").click()
       
    # text = 'All the Icons You Need. Guaranteed.'.decode('utf-8')
    # WebDriverWait(context.browser, 1000).until(
        # EC.presence_of_element_located((By.XPATH, "//*[@id='home-app']/div[2]/div/h2"))
    # )
    
    # time.sleep(2)
    
    # print ('DONE!')
# # Кликнуть на кнопку Создать коллекцию            
# def click_on_create(context, create):
    # WebDriverWait(context.browser, TIME_FOR_WAIT).until(
        # EC.element_to_be_clickable((By.XPATH, '//*[@class="%s"]' % create))                
    # )
    # time.sleep(2)
    # while True:
        # try:
            # context.browser.find_element_by_xpath('//*[@class="%s"]' % create).click()
            # break
        # except StaleElementReferenceException:
            # continue
            
            
# Прокрутить вниз страницы
# Then scroll to end of the page
def scroll_down(context):
##    context.browser.execute_script("window.scrollTo(0,250)", "")
  context.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")## - old version
   
    
# Прокрутить в вверх страницы
# Then scroll to begin of the page
def scroll_up(context):
    context.browser.execute_script("window.scrollTo(0,window.screen.availHeight);")            
    
# Найти видимиый текст
def locate_text(context, text, time_for_search = TIME_FOR_WAIT):
    WebDriverWait(context.browser, time_for_search).until(
        EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "%s")]' % text))
    )
    assert context.browser.find_element_by_xpath('//*[contains(text(), "%s")]' % text)  
   
# Найти видимиый элемент по xpath
def locate_element(context, xpath, time_for_search = TIME_FOR_WAIT):
    WebDriverWait(context.browser, time_for_search).until(
        EC.presence_of_element_located((By.XPATH, xpath))
    )
    element = context.browser.find_element_by_xpath(xpath)
    scroll_element_into_view(context.browser, element)
    assert context.browser.find_element_by_xpath(xpath)  

# # кликнуть на элемент по xpath
# def click_on_xpath(context, xpath):
    # WebDriverWait(context.browser, TIME_FOR_WAIT).until(
        # EC.element_to_be_clickable((By.XPATH, xpath))
    # )
    # element = context.browser.find_element_by_xpath(xpath)
    # scroll_element_into_view(context.browser, element)
    # assert context.browser.find_element_by_xpath(xpath)

    # element.click()          

    
# # Найти видимиый текст новый
# def locate_text(context, text, time_for_search = TIME_FOR_WAIT):
    # WebDriverWait(context.browser, time_for_search).until(
        # EC.findElement((By.XPATH, '//*[contains(text(), "%s")]' % text))
    # )
    # assert context.browser.find_element_by_xpath('//*[contains(text(), "%s")]' % text)     