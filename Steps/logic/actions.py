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
    # Наимает на кнопку в хедере. Типы вводных 'Icons', 'Download', 'Request', 'Buy', 'Resources'
    def clickHeaderButton(self, buttonName):
        Xpath = "//span[contains(text(), '%s')]" % buttonName
        self.clickActions = ClickActions(self)
        self.clickActions.click_on_xpath(Xpath)

    def clickButton(self, buttonName):
        Value_generate = ValueGenerate()
        if buttonName == 'search':
            xpath = '//*[@class="b-search-btn"]'
        elif buttonName == 'search platform filter':
            xpath = '//*[@ng-click="leftSideBar.platformClick(platform, $event)"][%s]' \
                    % Value_generate.values_in_range(2, 8)
        elif buttonName == 'search category':
            xpath = '//div[@class="b-bar-menus-menu m-scrollable"]/div[2]/a[%s]' % Value_generate.values_in_range(2, 50)
        elif buttonName == 'new icons search category':
            xpath = '//div[@class="b-bar-menus-menu m-scrollable"]/div[2]/a[1]'
        elif buttonName == 'Paypal':
            xpath = '//modals[2]/div/div/div[3]/div/div[2]'
        elif buttonName == 'Credit cards':
            xpath = '//modals[2]/div/div/div[3]/div/div[1]'
        elif buttonName == 'Download for Windows':
            xpath = '//*[@click-need-register="//icons8.com/downloader/?pack=appWin"]'
        elif buttonName == 'Collections':
            xpath = '//span[contains(., "Collections")]'
        elif buttonName == 'Create collections':
            xpath = '//*[@ng-click="collsControl.createCollection();"]'
        elif buttonName == 'confirm name':
            xpath = '//form/*[@ng-click="collsControl.renameCollection()"]'
        elif buttonName == 'delete collection menu':
            xpath = '//*[@ng-click="toggleCollectionsEdit()"]'
        elif buttonName == 'first icon in result':
            xpath = '//div[@class="b-subcategory-wrapper"][1]/descendant::a[1]'
        elif buttonName == 'first icon in collection':
            xpath = '//*[@ng-hide="collsControl.collectionCreating"]/*[1]/*[1]'
        elif buttonName == 'delete icon in collection':
            xpath = '//span[@class="c-btn m-transparent"]'
        elif buttonName == 'Get Font':
            xpath = '''//*[@popup-target="'generate-font'"]'''
        elif buttonName == 'Get SVG Set':
            xpath = '''//*[@ng-class="{'m-load': isDownloadSVGSet}"]'''
        elif buttonName == 'open public link pop-up':
            xpath = '//*[@class="c-tooltip m-no-border m-share-link-tooltip"]'
        elif buttonName == 'color palette':
            xpath = '//*[@class="colors"]/descendant::*[@ng-class="{active: showPicker}"]'
        elif buttonName == 'open color pop-up':
            xpath = '//*[@hide-color-picker="hideColorPicker"]/*[@ng-if="!hideColorPicker"]'
        elif buttonName == 'recommend':
            xpath = '//*[@class="infinario-block__poll"]/*[%s]' % Value_generate.values_in_range(1, 11)
        elif buttonName == 'icon name':
            xpath = '//*[@class="c-pretty-link m-inline"]'
        elif buttonName == 'tag':
            xpath = '//*[@class="b-tags-list"]/a[1]'
        elif buttonName == 'icon in tag page':
            xpath = '//span[@class="icons-set_element"][1]'
        elif buttonName == 'choose size of PNG':
            xpath = '//*[@class="icon-format-item icon-format-dropdown off-click-dropdownsize m-center"]'
        elif buttonName == 'icon category':
            xpath = '//*[@class="c-breadcrumbs"]/*[3]'
        self.clickActions = ClickActions(self)
        self.clickActions.click_on_xpath(xpath)










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

    def locateElement(self, elementName):
        Value_generate = ValueGenerate()
        if elementName == 'icons result':
            xpath = '//*[@class="icons-set"]/*[%s]' % Value_generate.values_in_range(1, 5)
        elif elementName == 'icons in result':
            xpath = '//div[@class="b-subcategory-wrapper"][1]/descendant::a[%s]' % Value_generate.values_in_range(1, 3)
        elif elementName == 'created first collection':
            xpath = '//*[@class="b-collections-container"]/div[1]'
        elif elementName == 'created second collection':
            xpath = '//*[@class="b-collections-container"]/div[2]'
        elif elementName == 'first icon in collection':
            xpath = '//*[@ng-hide="collsControl.collectionCreating"]/*[1]/*[1]'
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
            xpath = '//*[@ng-bind-html="category.title"]'
        self.locateActions = LocateActions(self)
        self.locateActions.locate_element(xpath)








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


"""
def upload(context, uploadTo, pathToFile):
    context.browser.find_element_by_xpath(uploadTo).click().send_keys(pathToFile)
"""