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
from settings import settings_test as settings
from selenium.webdriver.common.action_chains import ActionChains
from generators import *

now = datetime.today()

TIME_FOR_WAIT = 30

SERVER = settings['server']
LOGIN = settings['login']
PASSWORD = settings['password']
STAND = settings['stand_number']


# Кликнуть на линк
def click_on_link(context, link):
    WebDriverWait(context.browser, TIME_FOR_WAIT).until(
        EC.element_to_be_clickable((By.XPATH, '//*[1][contains(text(), "%s")]' % link))
    )
    time.sleep(2)
    while True: 
        try:
            context.browser.find_element_by_xpath('//*[1][contains(text(), "%s")]' % link).click()
            break
        except StaleElementReferenceException:
            continue

# Then scroll to end of the page
def open_main_page(context, server=SERVER):
    '''
    Функция для перехода на Главную, там где нет кнопки в шапке
    '''
    context.browser.get(server)              
            
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

def moveAndClick(context, move_to, button):
    time.sleep(4)
    moveTo = context.browser.find_element_by_xpath(move_to)
    click_button = context.browser.find_element_by_xpath(button)
    action = webdriver.ActionChains(context.browser)
    action.move_to_element(moveTo)
    action.perform()
    time.sleep(4)
    click_button.click()

# Кликнуть на кнопку
def click_on_button(context, button):
    """

    :rtype: object
    """
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

# Кликнуть на кнопку, найденой с помощью названия кнопки
def click_on_button_findByName(context, name):
    WebDriverWait(context.browser, TIME_FOR_WAIT).until(
        EC.element_to_be_clickable((By.XPATH, '//button[contains(., "%s")]' % name))
    )
    time.sleep(2)
    while True:
        try:
            context.browser.find_element_by_xpath('//button[contains(., "%s")]' % name).click()
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
тестовые функции
     
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

# тестовая фунция

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

# Найти поле и ввести в него текст
def input_text(context, text, field):
	context.browser.find_element_by_xpath('//*[@id="%s"]' % field).click()
	context.browser.find_element_by_xpath('//*[@id="%s"]' % field).send_keys(text)

# Найти поле по xpath и ввести в него текст
def inputText(context, text, xpath):
    context.browser.find_element_by_xpath(xpath).click()
    context.browser.find_element_by_xpath(xpath).clear()
    context.browser.find_element_by_xpath(xpath).send_keys(text)

# Возвращаеться на превидущую страницу
def back_to_previous_page(context):
    context.browser.back()

# происходит логин
def login(context, login=LOGIN, password=PASSWORD):
    context.browser.find_element_by_id("RegisterForm_email").clear()
    context.browser.find_element_by_id("RegisterForm_email").send_keys(login)
    context.browser.find_element_by_id("RegisterForm_password").clear()
    context.browser.find_element_by_id("RegisterForm_password").send_keys(password)
    context.browser.find_element_by_name("yt0").click()

    time.sleep(2)

# проверяет, что элемент отсутствует.
def absent_element(context, xpath):
    time.sleep(4)
    try:
        context.browser.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return True
    return False

# проверяет, что элемент отсутствует.
def dragAndDrop(context, element, moveto):
    source = context.browser.find_element_by_xpath(element)
    target = context.browser.find_element_by_xpath(moveto)
    action = webdriver.ActionChains(context.browser)
    action.drag_and_drop(source, target)
    action.perform()

# Возвращае колличество єлементов
def countOfElements(context, xpath):
    count = 0
    elementNumber = 1
    while True:
        try:
            print (str(count))
            context.browser.find_element_by_xpath(xpath % elementNumber)
            count += 1
            elementNumber += 1
        except NoSuchElementException:
            print (str(count) + ' - number of elements')
            break
    return count

# Кликает на все найденные элементы
def clickAll(context, xpath):
    count = countOfElements(context, xpath)
    while count > 0:
        print (str(count))
        context.browser.find_element_by_xpath(xpath % count).click()
        count -= 1

# Кликает на все найденные элементы и потом еще кликает на кнопку
def clickAllAndButtons(context, xpathFirst, xpathSecond):
    count = countOfElements(context, xpathFirst)
    while count > 0:
        print (str(count))
        context.browser.find_element_by_xpath(xpathFirst % count).click()
        time.sleep(3)
        context.browser.find_element_by_xpath(xpathSecond).click()
        count -= 1

#context.browser.find_element_by_xpath(xpath % count).click()
# пока не пашет    
# def pedro_search(context, xpath):
    # WebDriverWait(context.browser, TIME_FOR_WAIT).until(
        # #EC.element_to_be_clickable((By.XPATH, xpath)).click()
        # EC.find_element_by_xpath((By.XPATH, xpath)).send_keys("Minecraft")
        
    # )
    # time.sleep(2)
    # context.browser.find_element_by_xpath(xpath).clear()
    # context.browser.find_element_by_xpath(xpath).send_keys("Minecraft")
    # time.sleep(2)
    # while True: 
        # try:
            # context.browser.find_element_by_xpath(xpath)
            # break
        # except StaleElementReferenceException: 
            # continue    