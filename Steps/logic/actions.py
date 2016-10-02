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




class Page(object):
    def __init__(self, context):
        self.browser = context.browser



class ClickActions(Page):
    # Кликнуть на линк
    def click_on_link(self, link):
        WebDriverWait(self.browser, TIME_FOR_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, '//*[1][contains(text(), "%s")]' % link))
        )
        time.sleep(2)
        while True:
            try:
                self.browser.find_element_by_xpath('//*[1][contains(text(), "%s")]' % link).click()
                break
            except StaleElementReferenceException:
                continue

    # кликнуть на элемент по xpath
    def click_on_xpath(self, xpath):
        WebDriverWait(self.browser, TIME_FOR_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, xpath))
        )
        element = self.browser.find_element_by_xpath(xpath)
        self.movementActions = MovementActions(self)
        self.movementActions.scroll_element_into_view(element)
        element.click()

    def moveAndClick(self, move_to, button):
        time.sleep(4)
        moveTo = self.browser.find_element_by_xpath(move_to)
        click_button = self.browser.find_element_by_xpath(button)
        action = webdriver.ActionChains(self.browser)
        action.move_to_element(moveTo)
        action.perform()
        time.sleep(4)
        click_button.click()

    # Кликнуть на кнопку
    def click_on_button(self, button):
        """
        :rtype: object
        """
        WebDriverWait(self.browser, TIME_FOR_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, '//button[.="%s"]' % button))
        )
        time.sleep(2)
        while True:
            try:
                self.browser.find_element_by_xpath('//button[.="%s"]' % button).click()
                break
            except StaleElementReferenceException:
                continue

    # Кликнуть на кнопку, найденой с помощью названия кнопки
    def click_on_button_findByName(self, name):
        WebDriverWait(self.browser, TIME_FOR_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, '//button[contains(., "%s")]' % name))
        )
        time.sleep(2)
        while True:
            try:
                self.browser.find_element_by_xpath('//button[contains(., "%s")]' % name).click()
                break
            except StaleElementReferenceException:
                continue

    # Кликнуть на вкладку
    def click_on_unactive_tab(self, tab):
        WebDriverWait(self.browser, TIME_FOR_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@class="%s"]' % tab))
        )
        time.sleep(2)
        while True:
            try:
                self.browser.find_element_by_xpath('//*[@class="%s"]' % tab).click()
                break
            except StaleElementReferenceException:
                continue

    # Кликнуть на кнопку Создать коллекцию
    def click_on_create(self, create):
        WebDriverWait(self.browser, TIME_FOR_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@class="%s"]' % create))
        )
        time.sleep(2)
        while True:
            try:
                self.browser.find_element_by_xpath('//*[@class="%s"]' % create).click()
                break
            except StaleElementReferenceException:
                continue

    # Кликает на все найденные элементы
    def clickAll(self, xpath):
        self.locateActions = LocateActions(self)
        count = self.locateActions.countOfElements(xpath)
        while count > 0:
            print (str(count))
            self.browser.find_element_by_xpath(xpath % count).click()
            count -= 1

    # Кликает на все найденные элементы и потом еще кликает на кнопку
    def clickAllAndButtons(self, xpathFirst, xpathSecond):
        self.locateActions = LocateActions(self)
        count = self.locateActions.countOfElements(xpathFirst)
        while count > 0:
            print (str(count))
            self.browser.find_element_by_xpath(xpathFirst % count).click()
            time.sleep(3)
            self.browser.find_element_by_xpath(xpathSecond).click()
            count -= 1












class LocateActions(Page):
    # Найти видимиый текст
    def locate_text(self, text, time_for_search=TIME_FOR_WAIT):
        WebDriverWait(self.browser, time_for_search).until(
            EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "%s")]' % text))
        )
        assert self.browser.find_element_by_xpath('//*[contains(text(), "%s")]' % text)

        # Найти видимиый элемент по xpath

    def locate_element(self, xpath, time_for_search=TIME_FOR_WAIT):
        WebDriverWait(self.browser, time_for_search).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )
        element = self.browser.find_element_by_xpath(xpath)
        self.movementActions = MovementActions(self)
        self.movementActions.scroll_element_into_view(element)
        assert self.browser.find_element_by_xpath(xpath)

    # проверяет, что элемент отсутствует.
    def absent_element(self, xpath):
        time.sleep(4)
        try:
            self.browser.find_element_by_xpath(xpath)
        except NoSuchElementException:
            return True
        return False

    # Возвращае колличество єлементов
    def countOfElements(self, xpath):
        count = 0
        elementNumber = 1
        while True:
            try:
                print (str(count))
                self.browser.find_element_by_xpath(xpath % elementNumber)
                count += 1
                elementNumber += 1
            except NoSuchElementException:
                print (str(count) + ' - number of elements')
                break
        return count

    # Try click xpath > then click xpath > then find another xpath
    def tryFindClickFind(self, try_find, click, find_second):
        try:
            self.browser.find_element_by_xpath(try_find)
            self.clickActions = ClickActions(self)
            self.clickActions.click_on_xpath(click)
            self.locateActions = LocateActions(self)
            self.locateActions.locate_element(find_second)
        except NoSuchElementException:
            pass












class MovementActions(Page):
    # скроллинг до элемента
    def scroll_element_into_view(self, element):
        """Scroll element into view"""
        y = element.location['y']
        # От верхненего края на 250 пикселей
        y = y - 250
        self.browser.execute_script('window.scrollTo(0, {0})'.format(y))

    # Прокрутить вниз страницы
    # Then scroll to end of the page
    def scroll_down(self):
        ##    context.browser.execute_script("window.scrollTo(0,250)", "")
        self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")  ## - old version

    # Прокрутить в вверх страницы
    # Then scroll to begin of the page
    def scroll_up(self):
        self.browser.execute_script("window.scrollTo(0,window.screen.availHeight);")

    # проверяет, что элемент отсутствует.
    def dragAndDrop(self, element, moveto):
        source = self.browser.find_element_by_xpath(element)
        target = self.browser.find_element_by_xpath(moveto)
        action = webdriver.ActionChains(self.browser)
        action.drag_and_drop(source, target)
        action.perform()












class TextActions(Page):
    # Найти поле и ввести в него текст
    def input_text(self, text, field):
        self.browser.find_element_by_xpath('//*[@id="%s"]' % field).click()
        self.browser.find_element_by_xpath('//*[@id="%s"]' % field).send_keys(text)

    # Найти поле по xpath и ввести в него текст
    def inputText(self, text, xpath):
        self.browser.find_element_by_xpath(xpath).click()
        self.browser.find_element_by_xpath(xpath).clear()
        self.browser.find_element_by_xpath(xpath).send_keys(text)












class PageActions(Page):
    # Then scroll to end of the page
    def open_main_page(self, server=SERVER):
        '''
        Функция для перехода на Главную, там где нет кнопки в шапке
        '''
        self.browser.get(server)

    # Возвращаеться на превидущую страницу
    def back_to_previous_page(self):
        self.browser.back()

    # происходит логин
    def login(self, login=LOGIN, password=PASSWORD):
        self.browser.find_element_by_id("RegisterForm_email").clear()
        self.browser.find_element_by_id("RegisterForm_email").send_keys(login)
        self.browser.find_element_by_id("RegisterForm_password").clear()
        self.browser.find_element_by_id("RegisterForm_password").send_keys(password)
        self.browser.find_element_by_name("yt0").click()

        time.sleep(2)


"""
def upload(context, uploadTo, pathToFile):
    context.browser.find_element_by_xpath(uploadTo).click().send_keys(pathToFile)
"""