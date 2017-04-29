# -*- coding: utf-8 -*-

from selenium import webdriver
import time
from settings import settings_test as settings
from selenium.webdriver.common.action_chains import ActionChains
from generators import RandomGenerate

SERVER = settings['server']
LOGIN = settings['login']
PASSWORD = settings['password']
STAND = settings['stand_number']


class Page(object):
    """Задает context как browser, унаследуеться всеми классами"""


    def __init__(self, context):
        self.browser = context.browser


class MovementActions(Page):
    """Скролы, передвижения курсора и другие движения"""


    def scroll_element_into_view(self, element):
        """Scroll element into view"""
        y = element.location['y']
        # От верхненего края на 250 пикселей
        y = y - 250
        self.browser.execute_script('window.scrollTo(0, {0})'.format(y))

    def scroll_down(self):
        """Прокрутить вниз страницы"""
        ##    context.browser.execute_script("window.scrollTo(0,250)", "")
        self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def scroll_up(self):
        """Прокрутить в вверх страницы"""
        self.browser.execute_script("window.scrollTo(0,window.screen.availHeight);")

    def dragAndDrop(self, element, moveto):
        """Проверяет, что элемент отсутствует."""
        source = self.browser.find_element_by_xpath(element)
        target = self.browser.find_element_by_xpath(moveto)
        action = webdriver.ActionChains(self.browser)
        action.drag_and_drop(source, target)
        action.perform()

    def move_mouse(self, element_to):
        """Перемещает мышь та элемент"""
        if element_to == 'right bar':
            xpath = '''//*[@i8-scroll-commander="vm.scrollCommander"]'''
        element = self.browser.find_element_by_xpath(xpath)
        action = webdriver.ActionChains(self.browser)
        action.move_to_element(element)
        action.perform()


class TextActions(Page):
    """Манипуляции с текстом"""


    def input_text(self, text, field):
        """Найти поле и ввести в него текст"""
        self.browser.find_element_by_xpath('//*[@id="%s"]' % field).click()
        self.browser.find_element_by_xpath('//*[@id="%s"]' % field).send_keys(text)

    def inputText(self, text, xpath):
        """Найти поле по xpath и ввести в него текст"""
        self.browser.find_element_by_xpath(xpath).click()
        self.browser.find_element_by_xpath(xpath).clear()
        self.browser.find_element_by_xpath(xpath).send_keys(text)

    def addTextToField(self, TextType, FieldName):
        """Добавляет текст в поле."""
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
            xpath = './/input[@ng-init="vm.newCollName = vm.IconsCollsModel.current.name"]'
            text = 'Collection %s' % Random_generate.random_text(6)
        self.textActions = TextActions(self)
        self.textActions.inputText(text, xpath)


class PageActions(Page):
    """Действия на странице и со страницами"""


    def open_main_page(self, server=SERVER):
        """Then scroll to end of the page"""
        self.browser.get(server)

    def back_to_previous_page(self):
        """Возвращаеться на превидущую страницу"""
        self.browser.back()

    def login(self, login=LOGIN, password=PASSWORD):
        """Login"""
        self.browser.find_element_by_id("RegisterForm_email").clear()
        self.browser.find_element_by_id("RegisterForm_email").send_keys(login)
        self.browser.find_element_by_id("RegisterForm_password").clear()
        self.browser.find_element_by_id("RegisterForm_password").send_keys(password)
        self.browser.find_element_by_name("yt0").click()

        time.sleep(2)


class Helpers(Page):
    """Вспомогательные методы, который нельзя отдельно выделить"""


    def sleepTime(self, seconds):
        """Спит N секунд"""
        x = float(seconds)
        time.sleep(x)
