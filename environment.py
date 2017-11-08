# -*- coding: utf-8 -*-

"""
Файл environment.py устанавливает верхний слой окружения для behave.
Тут можно объявить переменные,
которые можно будет использовать на всех уровнях,
выполнения тестов. (Например, на уровне фичи, сценария, конкретного шага.)
Так же тут можно объявить функции,
которые будут выполняться после шагов,
сценариев, тэгов или фич.
Узнай больше на http://pythonhosted.org/behave/.
"""

import os
import time
from sys import platform
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from settings import settings_test as settings

# Choose download folder
path_to_download_folder = os.path.join(' ', 'download_tests')
path_to_test_folder = os.getcwd()
download_folder_path = path_to_test_folder + path_to_download_folder[1:]

# Обозначить переменные выполнения (сервер, логин и пароль)
SERVER = settings['server']
LOGIN = settings['login']
PASSWORD = settings['password']
STAND = settings['stand_number']


def login(context, server=SERVER, login=LOGIN, password=PASSWORD):
    """
    Функция для логина в аккаунте.
    Ввести логин и пароль, нажать "Login"
    """
    print ('I try to login into account...')

    # Open home page url
    context.browser.get(server + 'logout')

    # Login
    context.browser.find_element_by_link_text("Login").click()
    WebDriverWait(context.browser, 1000).until(
        EC.presence_of_element_located((By.ID, 'RegisterForm_email')))
    context.browser.find_element_by_id("RegisterForm_email").clear()
    context.browser.find_element_by_id("RegisterForm_email").send_keys(login)
    context.browser.find_element_by_id("RegisterForm_password").clear()
    context.browser.find_element_by_id(
        "RegisterForm_password").send_keys(password)
    context.browser.find_element_by_name("yt0").click()
    WebDriverWait(context.browser, 1000).until(
        EC.presence_of_element_located(
            (By.XPATH, "//*[@id='home-app']/div[2]/div/h2")))
    time.sleep(2)

    print ('DONE!')


def make_driver(context):
    """
    Создать объект-драйвер для взаимодействия с браузером.
    Можно вызывать в before_feature, если мы хотим каждый тест проводить,
    в отдельном браузере.
    P.S. в таком случае, не забыть в after_feature закрывать браузер.
    """

    # использовать конкретные бинарники
    print ('Opening browser now!')

    # Driver profile
    profile = FirefoxProfile()
    profile.set_preference("browser.download.folderList", 2)
    profile.set_preference("browser.download.manager.showWhenStarting", False)
    profile.set_preference("browser.download.dir", download_folder_path)
    profile.set_preference("browser.helperApps.neverAsk.saveToDisk",
                           '''application/x-msdos-program, 
                           application/octet-stream, image/png, 
                           image/svg+xml, application/postscript, 
                           application/eps, application/x-eps, 
                           image/eps, image/x-eps, text/plain, 
                           application/download, application/zip, 
                           application/unknown, text/html''')
    context.list_ud = list()
    context.stand = STAND

    # Choose profile
    if "win" in platform:
        context.browser = webdriver.Firefox(firefox_profile=profile)
    elif "linux" in platform:
        path_to_binary = "/usr/bin/firefox"
        binary = FirefoxBinary(path_to_binary)
        context.browser = webdriver.Firefox(
            firefox_profile=profile, firefox_binary=binary)
    else:
        path_to_binary = os.getcwd() + '/steps/data/firefox/firefox'
        binary = FirefoxBinary(path_to_binary)
        context.browser = webdriver.Firefox(
            firefox_profile=profile, firefox_binary=binary)
    context.browser.implicitly_wait(20)
    context.browser.maximize_window()

    # Login
    try:
        login(context)
    except:
        print ('cant login!!!')
        context.browser.quit()


def before_step(context, step):
    """
    Служебная функция behave с говорящим названием.
    Подробнее на http://pythonhosted.org/behave/.
    """
    time.sleep(0.1)


def before_all(context):
    """
    Служебная функция behave с говорящим названием.
    Подробнее на http://pythonhosted.org/behave/.
    """
    pass


def before_feature(context, feature):
    """
    Служебная функция behave с говорящим названием.
    Подробнее на http://pythonhosted.org/behave/.
    """
    # запустить браузер для теста
    make_driver(context)


def after_scenario(context, scenario):
    # getcwd()+'/screenshot_failed/'
    # +time.strftime('Date and time: %d/%m/%y %H:%M') + scenario.name +'.png'
    name_screenshot = 'error in scenario: ' + scenario.name + '.png'
    name_screenshot = name_screenshot.replace(" ", "_")
    if scenario.status != 'passed':
        context.browser.get_screenshot_as_file(name_screenshot)


def after_feature(context, feature):
    """
    Служебная функция behave с говорящим названием.
    Подробнее на http://pythonhosted.org/behave/.
    """

    try:
        context.browser.quit()
    except:
        print ('Already exit!st')
    # после выполнения теста закрыть браузера
    print ('Browser closes...')


def after_all(context):
    """
    Служебная функция behave с говорящим названием.
    Подробнее на http://pythonhosted.org/behave/.
    """
    pass
