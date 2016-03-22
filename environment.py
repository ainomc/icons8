# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from settings import settings_test as settings
from os import getcwd
from api_method import delete_data
from sys import platform
import time

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


def delete_saved_document(context):
    '''
    Фунцкия готовит список УД из context.list_ud для метода, который дернет api arm-oms,
    и удалит их. 
    '''
    # список для ID
    list_ud_for_delete = list()
    # Взять id из окружения с припиской ID, и убрать приписку.
    # Напримеh, было "UD 1334124", станет "1334124"
    # Это необходимо, т.к. id  подают в список с припиской 'УД ', необходимо отбросить первые три символа.
    for item in context.list_ud:
        list_ud_for_delete.append(item[3:])
    try:
        delete_data(list_ud_for_delete)
    except:
        print ('cant decode date... UD didnt removed')
    context.list_ud = list()

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
    Функция для логина в CAS.
    Ввести логин и пароль, нажать "войти"
    '''
    # явные ожидания
    # context.browser.implicitly_wait(120)
    print ('I get access to the arm-oms...')
    server = 'http://{0}/arm-oms/'.format(server)
    context.browser.get("http://10.0.33.19:8081/arm-oms/")
    WebDriverWait(context.browser, 1000).until(
        EC.presence_of_element_located((By.NAME, 'username'))
    )
    context.browser.find_element_by_name("username").send_keys(login)
    context.browser.find_element_by_name("password").send_keys(password)
    context.browser.find_element_by_class_name("btn-submit").click()
    text = 'ГБУЗ ГП № 46'.decode('utf-8')
    WebDriverWait(context.browser, 1000).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='s2id_autogen1_search']"))
    )
    time.sleep(2)
    context.browser.find_element_by_xpath("//*[@id='s2id_autogen1_search']").click()
    context.browser.find_element_by_xpath("//*[@id='s2id_autogen1_search']").send_keys(text)
    WebDriverWait(context.browser, 1000).until(
        EC.presence_of_element_located((By.XPATH, '//*/li//*[contains(text(), "%s")]' % text))
    )
    context.browser.find_element_by_xpath('//*/li//*[contains(text(), "%s")]' % text).click()
    print ('DONE!')
    WebDriverWait(context.browser, 1000).until(
        EC.presence_of_element_located((By.XPATH, '//*/li//*[contains(text(), "Регистрация услуг")]'))
    )

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
    profile.native_events_enabled = False
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
    delete_saved_document(context)
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

