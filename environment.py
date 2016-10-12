# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from settings import settings_test as settings
from os import getcwd
#from api_method import delete_data
from sys import platform
import time
import os
'''
Файл environment.py устанавливает верхний слой окружения для behave.
Тут можно объявить переменные, которые можно будет использовать на всех уровнях,
выполнения тестов. (Например, на уровне фичи, сценария, конкретного шага.)
Так же тут можно объявить функции, которые будут выполняться после шагов, сценариев, тэгов или фич.
Узнай больше на http://pythonhosted.org/behave/.
'''

# Обозначить переменные выполнения (сервер, логин и пароль)
SERVER = settings['server']
LOGIN = settings['login']
PASSWORD = settings['password']
STAND = settings['stand_number']

def sleep_while_show_text(context, text):
    '''
    Функция ставит выполнение на паузу, пока на экране есть указанный текст.
    Объвлена тут для использование в before_step(), after_step().
    Подробнее смотри в before_step().
    '''
    while True:
        try:
           context.browser.find_element_by_xpath('//*[contains(text(), "%s")]')
        except:
            # print ('Блок загрузки не найден!')
            return 1
        time.sleep(1)

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
     
    
def make_driver(context):
    '''
    Создать объект-драйвер для взаимодействия с браузером.
    Можно вызывать в before_feature, если мы хотим каждый тест проводить, 
    в отдельном браузере. 
    P.S. в таком случае, не забыть в after_feature закрывать браузер.
    '''
    # использовать конкретные бинарники
    print ('Opening browser now!')
    path_to_binary = getcwd() + '/steps/data/firefox/firefox'
    binary = FirefoxBinary(path_to_binary)
    profile = FirefoxProfile()
    #profile.native_events_enabled = True
    profile.set_preference("browser.download.folderList", 2)
    profile.set_preference("browser.download.manager.showWhenStarting", False)
    profile.set_preference("browser.download.dir", os.getcwd())
    print (os.getcwd())
    profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/x-msdos-program, application/octet-stream")
    context.list_ud = list()
    context.stand = STAND
    # выбор профиля
    if "win" in platform:
        context.browser = webdriver.Firefox(firefox_profile=profile)
    else:
        context.browser = webdriver.Firefox(firefox_profile=profile, firefox_binary=binary)
    context.browser.maximize_window()
    # вызываем логин-фичу
    try:
        login(context)
    except:
        print ('cant login!!!')
        context.browser.quit()

def before_step(context, step):
    '''
    Служебная функция behave с говорящим названием.
    Подробнее на http://pythonhosted.org/behave/. 
    '''
    time.sleep(0.5)
    # текст, который показан, когда на странице есть блок загрузки.
    load_page_text = 'Загрузка'
    sleep_while_show_text(context, load_page_text)
    # текст, который показан, когда на странице есть блок сохранения.
    load_page_text = 'Сохранение'
    sleep_while_show_text(context, load_page_text)

def before_all(context):
    '''
    Служебная функция behave с говорящим названием.
    Подробнее на http://pythonhosted.org/behave/. 
    '''
    pass

def before_feature(context, feature):
    '''
    Служебная функция behave с говорящим названием.
    Подробнее на http://pythonhosted.org/behave/. 
    '''
    # запустить браузер для теста
    make_driver(context)


def after_scenario(context, scenario):        
    # getcwd()+'/screenshot_failed/'+time.strftime('Date and time: %d/%m/%y %H:%M') + scenario.name +'.png'
    name_screenshot = 'error in scenario: '+scenario.name+'.png'
    name_screenshot = name_screenshot.replace(" ", "_")
    if scenario.status != 'passed': context.browser.get_screenshot_as_file(name_screenshot)

def after_feature(context, feature):
    '''
    Служебная функция behave с говорящим названием.
    Подробнее на http://pythonhosted.org/behave/. 
    '''
    # Вызвать функцию для подготовки данных, которая вызовет api-metod для удаление УД.
  #  delete_saved_document(context)
    try:
        context.browser.quit()
    except: 
        print ('Already exit!st')
    # после выполнения теста закрыть браузера
    print ('Browser closes...')


def after_all(context):
    '''
    Служебная функция behave с говорящим названием.
    Подробнее на http://pythonhosted.org/behave/. 
    '''
    pass
 #   context.browser.quit()

