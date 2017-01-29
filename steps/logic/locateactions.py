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
from actions import *


now = datetime.today()

TIME_FOR_WAIT = 30

SERVER = settings['server']
LOGIN = settings['login']
PASSWORD = settings['password']
STAND = settings['stand_number']




# Проверки на присутствия
class LocateActions(Page):

    # Найти видимиый текст что содержит в себе
    def locate_text(self, text, time_for_search=TIME_FOR_WAIT):
        WebDriverWait(self.browser, time_for_search).until(
            EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "%s")]' % text))
        )
        assert self.browser.find_element_by_xpath('//*[contains(text(), "%s")]' % text)

    # Найти видимиый текст
    def locate_concrete_text(self, text, time_for_search=TIME_FOR_WAIT):
        WebDriverWait(self.browser, time_for_search).until(
            EC.presence_of_element_located((By.XPATH, '//*[text()="%s"]' % text))
        )
        assert self.browser.find_element_by_xpath('//*[text()="%s"]' % text)


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
        # Тут импорт, чтобы не было циклического импорта с clickactions.py
        from clickactions import ClickActions
        try:
            self.browser.find_element_by_xpath(try_find)
            self.clickActions = ClickActions(self)
            self.clickActions.click_on_xpath(click)
            self.locateActions = LocateActions(self)
            self.locateActions.locate_element(find_second)
        except NoSuchElementException:
            pass

    # Найти элемент по уникальному xpath
    def locateElement(self, elementName):
        Value_generate = ValueGenerate()
        if elementName == 'icons result':
            xpath = '//*[@class="icons-set"]/descendant::span[%s]' % Value_generate.values_in_range(1, 5)
        elif elementName == 'icons in result':
            xpath = '//div[@class="b-subcategory-wrapper"][1]/descendant::a[%s]' % Value_generate.values_in_range(1, 3)
        elif elementName == 'created first collection':
            xpath = '//*[@class="b-collections-container"]/div[1]'
        elif elementName == 'created second collection':
            xpath = '//*[@class="b-collections-container"]/div[2]'
        elif elementName == 'first icon in collection':
            xpath = './/*[@class="icons-set__icon"]'
        elif elementName == 'Get Font pop-up':
            xpath = '//*[@stop-events="click"]'
        elif elementName == 'Public Link':
            xpath = '//*[@ng-model="colSharing.url"]'
        elif elementName == 'icon category':
            xpath = '//*[@class="c-breadcrumbs"]/*[%s]' % Value_generate.values_in_range(1, 3)
        elif elementName == 'icon text':
            xpath = '//*[@ng-bind-html="mainSubtitleText"]'
        elif elementName == 'Icon':
            xpath = '//*[@class="col-md-4 m-full-width b-main-icon m-main-icon"]/*'
        elif elementName == 'Download button':
            xpath = '//button[contains(text(), "Download")]'
        elif elementName == 'icon download sizes':
            xpath = '//ul[@class="c-list m-nooverflow"]/*[%s]' % Value_generate.values_in_range(1, 4)
        elif elementName == 'icon download format':
            xpath = '//*[@class="c-list m-nooverflow b-format"]/*[%s]' % Value_generate.values_in_range(1, 6)
        elif elementName == 'Category Title':
            xpath = '//*[@ng-bind-html="vm.category.title"]'
        elif elementName == 'simple list':
            xpath = './/*[@class="c-icon-list"]'
        elif elementName == 'list with names':
            xpath = './/*[@class="c-icon-list m-with-name"]'
        elif elementName == 'table list':
            xpath = '''.//*[@ng-if="vm.gridState.state == 'table'"]'''
        self.locateActions = LocateActions(self)
        self.locateActions.locate_element(xpath)


