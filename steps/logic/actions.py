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


# Задает context как browser, унаследуеться всеми классами
class Page(object):
    def __init__(self, context):
        self.browser = context.browser




# Скролы, передвижения курсора и другие движения
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

    # Перемещает мышь та элемент
    def move_mouse(self, element_to):
        if element_to == 'right bar':
            xpath = '''//*[@ng-include="'/template-icon.html'"]/descendant::*[@class="b-collections-container"]'''
        element = self.browser.find_element_by_xpath(xpath)
        action = webdriver.ActionChains(self.browser)
        action.move_to_element(element)
        action.perform()





# Манипуляции с текстом
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

    # Добавляет текст в поле.
    def addTextToField(self, TextType, FieldName):
        Random_generate = RandomGenerate()
        if TextType == 'email':
            xpath = '//input[@id="%s"]' % FieldName
            text = Random_generate.random_email()
        elif TextType == 'password':
            xpath = '//input[@id="%s"]' % FieldName
            text = Random_generate.random_idea_name()
        elif TextType == 'positive text':
            xpath = '//*[@placeholder="%s"]' % FieldName
            text = Random_generate.random_listValue(['google', 'facebook', 'space', 'ball', 'car', 'word'])
        elif TextType == 'negative text':
            xpath = '//*[@placeholder="%s"]' % FieldName
            text = 'kjhgfdsalkjjhggfd'
        elif TextType == 'collection name':
            xpath = '//input[@ng-model="collsControl.%s"]' % FieldName
            text = 'Collection %s' % Random_generate.random_text(6)
        self.textActions = TextActions(self)
        self.textActions.inputText(text, xpath)




# Действия на странице и со страницами
class PageActions(Page):
    # Then scroll to end of the page
    def open_main_page(self, server=SERVER):
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




# Вспомогательные методы, который нельзя отдельно выделить
class Helpers(Page):
    # Спит N секунд
    def sleepTime(self, seconds):
        x = float(seconds)
        time.sleep(x)
