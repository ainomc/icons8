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
from locateactions import *


now = datetime.today()

TIME_FOR_WAIT = 30

SERVER = settings['server']
LOGIN = settings['login']
PASSWORD = settings['password']
STAND = settings['stand_number']




# Различные нклики
class ClickActions(Page):

    # Кликнуть на линк
    def click_on_link(self, link):
        WebDriverWait(self.browser, TIME_FOR_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, '//*[contains(text(), "%s")][1]' % link))
        )
        time.sleep(2)
        while True:
            try:
                self.browser.find_element_by_xpath('//*[contains(text(), "%s")][1]' % link).click()
                break
            except StaleElementReferenceException:
                continue

    # Наимает на кнопку в главном иеню в хедере. Типы вводных 'Icons', 'Download', 'Request', 'Buy', 'Resources'
    def clickHeaderNavMenu(self, buttonName):
        Xpath = '//*[@class="b-menu"]/descendant::span[contains(text(), "%s")]' % buttonName
        self.clickActions = ClickActions(self)
        self.clickActions.click_on_xpath(Xpath)

    # Кликнуть на линк
    def clickButtonText(self, link):
        WebDriverWait(self.browser, TIME_FOR_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, '//*[text()="%s"]' % link))
        )
        time.sleep(2)
        while True:
            try:
                self.browser.find_element_by_xpath('//*[text()="%s"]' % link).click()
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

    # Передвигает курсор и кликает
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

    # Наимает на кнопку в хедере.
    def clickLogo(self):
        xpath = "//*[@class='b-logo']"
        self.clickActions = ClickActions(self)
        self.clickActions.click_on_xpath(xpath)

    # Уликнуть на элемент по уникальному xpath
    def clickButton(self, buttonName):
        Value_generate = ValueGenerate()
        if buttonName == 'search':
            xpath = '//*[@class="b-search-btn"]'
        elif buttonName == 'search platform filter':
            xpath = '//*[@ng-click="leftSideBar.platformClick(platform, $event)"][%s]' \
                    % Value_generate.values_in_range(2, 8)
        elif buttonName == 'search category':
            xpath = './/*[@class="b-bar-menus-menu m-scrollable"]/descendant::a[%s]' % Value_generate.values_in_range(2, 50)
        elif buttonName == 'new icons search category':
            xpath = '//div[@class="b-bar-menus-menu m-scrollable"]/descendant::a[1]'
        elif buttonName == 'Paypal':
            xpath = '//modals[2]/descendant::*[contains(text(), "Paypal")][1]'
        elif buttonName == 'Credit cards':
            xpath = '//modals[2]/descendant::*[contains(text(), "Credit cards")][1]'
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
            xpath = '//*[@class="icons-set__icon"][1]'
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
        elif buttonName == 'Download for Windows':
            xpath = "//*[@id='home-app']/div[1]/div[2]/div/div/div[1]/div/a"  # test xpath
        elif buttonName == 'Download in icon bar':
            xpath = '//*[@class="b-bar-btns m-icon m-single-btn"]/*[1]'
        elif buttonName == 'Open download icon pop-up':
            xpath = '//*[@icon="selectedIcon.icon"]/div/*[1]'
        self.clickActions = ClickActions(self)
        self.clickActions.click_on_xpath(xpath)


    # Кликает на элемент с ng-if
    def clickFindByNg_if(self, ng_if_locator):
        xpath = '//*[@ng-if="%s"]' % ng_if_locator
        self.clickActions = ClickActions(self)
        self.clickActions.click_on_xpath(xpath)

    # Выбрать тип/формат скачиваемой иконки
    def click_download_icontype(self, icon_type):
        if icon_type == 'PNG':
            number = 1
        elif icon_type == 'SVG':
            number = 2
        elif icon_type == 'EPS':
            number = 3
        elif icon_type == 'PDF':
            number = 4
        elif icon_type == 'Font':
            number = 5
        elif icon_type == 'SVG set':
            number = 6
        xpath = '//div[@icon="selectedIcon.icon"]/descendant::li[%s]' % number
        self.clickActions = ClickActions(self)
        self.clickActions.click_on_xpath(xpath)

    # Выбрать размер скачиваемой иконки
    def click_download_iconsize(self, icon_size_button):
        xpath = '''//*[@ng-include="'/template-icon.html'"]/descendant::*[contains(text(), "%s")][1]''' % icon_size_button
        self.clickActions = ClickActions(self)
        self.clickActions.click_on_xpath(xpath)

    def try_gotit(self):
        try:
            self.browser.find_element_by_xpath('//*[@ng-click="action(message, icons8Messages.service, this)"]')
            self.browser.find_element_by_xpath('//*[@ng-click="action(message, icons8Messages.service, this)"]').click()
        except NoSuchElementException:
            pass



