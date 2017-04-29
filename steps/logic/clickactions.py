# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
import time
import os
from settings import settings_test as settings
from selenium.webdriver.common.action_chains import ActionChains
from locateactions import Page, LocateActions
from generators import ValueGenerate


class ClickActions(Page):
    """Различные клики"""

    def click_on_link(self, link):
        """Click contains text"""
        try:
            WebDriverWait(self.browser, 1).until \
                (EC.element_to_be_clickable((By.XPATH, '//*[contains(text(), "%s")][1]' % link))).click()
        except:
            self.browser.find_element_by_xpath('//*[contains(text(), "%s")][1]' % link).click()

    def try_click_on_link(self, link):
        """Try contains text"""
        while True:
            try:
                self.browser.find_element_by_xpath('//*[contains(text(), "%s")][1]' % link).click()
                break
            except StaleElementReferenceException:
                continue

    def clickHeaderNavMenu(self, buttonName):
        """Наимает на кнопку в главном иеню в хедере.
        Типы вводных 'Icons', 'Download', 'Request', 'Buy', 'Resources'
        """
        Xpath = '//*[@class="b-menu"]/descendant::span[contains(text(), "%s")]' % buttonName
        self.clickActions = ClickActions(self)
        self.clickActions.click_on_xpath(Xpath)

    def clickButtonText(self, link):
        """Click text"""
        try:
            WebDriverWait(self.browser, 1).until \
                (EC.element_to_be_clickable((By.XPATH, '//*[text()="%s"]' % link))).click()
        except:
            self.browser.find_element_by_xpath('//*[text()="%s"]' % link).click()

    def click_text_with_div(self, link):
        """Click text with div"""
        try:
            WebDriverWait(self.browser, 1).until \
                (EC.element_to_be_clickable((By.XPATH, '//div[contains(text(), "%s")][1]' % link))).click()
        except:
            self.browser.find_element_by_xpath('//div[contains(text(), "%s")][1]' % link).click()

    def click_on_xpath(self, xpath):
        """Click xpath"""
        try:
            WebDriverWait(self.browser, 1).until \
                (EC.element_to_be_clickable((By.XPATH, xpath))).click()
        except:
            self.browser.find_element_by_xpath(xpath).click()

    def moveAndClick(self, move_to, button):
        """Передвигает курсор и кликает"""
        def logic():
            time.sleep(4)
            moveTo = self.browser.find_element_by_xpath(move_to)
            click_button = self.browser.find_element_by_xpath(button)
            action = webdriver.ActionChains(self.browser)
            action.move_to_element(moveTo)
            action.perform()
            time.sleep(7)
            click_button.click()
        try:
            logic()
        except:
            logic()

    def click_on_button(self, button):
        """Кликнуть на кнопку"""
        try:
            WebDriverWait(self.browser, 1).until \
                (EC.element_to_be_clickable((By.XPATH, '//button[.="%s"]' % button))).click()
        except:
            self.browser.find_element_by_xpath('//button[.="%s"]' % button).click()


    def click_on_button_findByName(self, name):
        """Кликнуть на кнопку, найденой с помощью названия кнопки"""
        try:
            WebDriverWait(self.browser, 1).until \
                (EC.element_to_be_clickable((By.XPATH, '//button[contains(., "%s")]' % name))).click()
        except:
            self.browser.find_element_by_xpath('//button[contains(., "%s")]' % name).click()

    def click_on_unactive_tab(self, tab):
        """Кликнуть на вкладку"""
        try:
            WebDriverWait(self.browser, 1).until \
                (EC.element_to_be_clickable((By.XPATH, '//*[@class="%s"]' % tab))).click()
        except:
            self.browser.find_element_by_xpath('//*[@class="%s"]' % tab).click()

    def click_on_create(self, create):
        """Кликнуть на кнопку Создать коллекцию"""
        try:
            WebDriverWait(self.browser, 1).until \
                (EC.element_to_be_clickable((By.XPATH, '//*[@class="%s"]' % create))).click()
        except:
            self.browser.find_element_by_xpath('//*[@class="%s"]' % create).click()

    def clickAll(self, xpath):
        """Кликает на все найденные элементы"""
        self.locateActions = LocateActions(self)
        count = self.locateActions.countOfElements(xpath)
        while count > 0:
            print (str(count))
            self.browser.find_element_by_xpath(xpath % count).click()
            count -= 1

    def clickAllAndButtons(self, xpathFirst, xpathSecond):
        """Кликает на все найденные элементы и потом еще кликает на кнопку"""
        self.locateActions = LocateActions(self)
        count = self.locateActions.countOfElements(xpathFirst)
        while count > 0:
            print (str(count))
            self.browser.find_element_by_xpath(xpathFirst % count).click()
            self.browser.find_element_by_xpath(xpathSecond).click()
            count -= 1

    def clickLogo(self):
        """Наимает на кнопку в хедере."""
        xpath = "//*[@class='b-logo']"
        self.clickActions = ClickActions(self)
        self.clickActions.click_on_xpath(xpath)

    def clickButton(self, buttonName):
        """Уликнуть на элемент по уникальному xpath"""
        Value_generate = ValueGenerate()
        if buttonName == 'search':
            xpath = '//*[@class="b-search-btn"]'
        elif buttonName == 'search platform filter':
            xpath = './/*[@class="b-bar-menus m-fix-c-list"]/*[1]/*[%s]' \
                    % Value_generate.values_in_range(2, 8)
        elif buttonName == 'first icon in result':
            xpath = '//div[@class="b-subcategory-wrapper"][1]/descendant::a[1]'
        elif buttonName == 'search category':
            xpath = './/*[@class="b-bar-menus-menu m-scrollable"]/descendant::a[%s]' % Value_generate.values_in_range(3, 50)
        elif buttonName == 'new icons search category':
            xpath = './/*[@class="b-bar-menus-menu m-scrollable"]/descendant::*[@class="c-list m-padding b-bar-menus-menu"][2]/a[1]'
        elif buttonName == 'Paypal':
            xpath = '''.//*[@id='page-app']/modals/descendant::*[@class="b-payment-description"]'''
        elif buttonName == 'Credit cards':
            xpath = '''.//*[@id='page-app']/modals/descendant::*[@class="b-payment-svg xxxx"]'''
        elif buttonName == 'Download for Windows':
            xpath = '//*[@click-need-register="//icons8.com/downloader/?pack=appWin"]'
        elif buttonName == 'Collections':
            xpath = '//span[contains(., "Collections")]'
        elif buttonName == 'Create collections':
            xpath = './/*[@ng-click="vm.createCollection();"]'
        elif buttonName == 'confirm name':
            xpath = './/*[@ng-if="vm.collectionRenaming"]/*[@ng-click="vm.renameCollection()"]/*'
        elif buttonName == 'delete collection menu':
            xpath = '''.//*[@ng-class="{'m-edit': collectionsEdit}"]'''
        elif buttonName == 'first icon in collection':
            xpath = './/*[@class="icons-set m-firefox"]/div[@draggable-type="fromLightBox"][1]'
        elif buttonName == 'delete icon in collection':
            xpath = '//span[@class="c-btn m-transparent"]'
        elif buttonName == 'Get Font':
            xpath = '''//*[@popup-target="'generate-font'"]'''
        elif buttonName == 'Get SVG Set':
            xpath = '''.//*[@class="b-bar-btns m-collections"]/div[3]'''
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
            xpath = './/*[@class="b-bar-btns m-icon"]/*[1]'
        elif buttonName == 'Download in icon bar esp':
            xpath = './/*[@class="b-bar-btns m-icon m-single-btn"]/*[1]'
        elif buttonName == 'Open download icon pop-up':
            xpath = './/*[@class="icon-format-item icon-format-dropdown off-click-dropdownsize m-center"]'
        elif buttonName == 'Edit name':
            xpath = './/div[@i8-simple-tooltip="Edit name"]'
        elif buttonName == 'Got it':
            xpath = './/div[@class="c-btn b-message-button"]'
        elif buttonName == 'Profile':
            xpath = '//a[contains(text(), "Profile")][1]'
        elif buttonName == 'API':
            xpath = '//a[contains(text(), "API")][1]'
        elif buttonName == 'delete icon':
            xpath = '//div[@class="c-btn modal__action-confirm modal__action"]'
        elif buttonName == 'Unlimited Plan buy':
            xpath = './/*[@class="b-license m-order-0"]/descendant::*[@class="c-btn m-pricing ng-binding ng-isolate-scope"]'
        elif buttonName == 'Free buy':
            xpath = './/*[@class="b-license m-order-1"]/descendant::*[@class="c-btn m-pricing ng-binding ng-isolate-scope"]'
        elif buttonName == 'Service Integration buy':
            xpath = './/*[@class="b-license m-order-2"]/descendant::*[@class="c-btn m-pricing ng-binding ng-isolate-scope"]'
        elif buttonName == 'icon8 app in download pop-up':
            xpath = './/*[@class="c-big-menu c-big-menu-narrow active"]/descendant::*[@href="/app"]'
        elif buttonName == 'Download menu':
            xpath = './/*[@for="big-menu-download"]'

        self.clickActions = ClickActions(self)
        self.clickActions.click_on_xpath(xpath)

    def try_click_button(self, buttonName):
        """Кликнуть на элемент по уникальному xpath"""
        if buttonName == 'got it':
            xpath = '''.//*[@ng-repeat="(title, action) in message.actions"]'''
        try:
            self.clickActions = ClickActions(self)
            self.clickActions.click_on_xpath(xpath)
        except:
            pass

    def clickFindByNg_if(self, ng_if_locator):
        """Кликает на элемент с ng-if"""
        xpath = '//*[@ng-if="%s"]' % ng_if_locator
        self.clickActions = ClickActions(self)
        self.clickActions.click_on_xpath(xpath)

    def click_download_icontype(self, icon_type):
        """Выбрать тип/формат скачиваемой иконки"""
        dict = {'PNG': 1, 'SVG': 2, 'EPS': 3,
                'PDF': 4, 'Font': 5, 'SVG set': 6}
        time.sleep(5)
        xpath = './/*[@class="c-list m-nooverflow b-format"]/*[%s]' % dict.get(icon_type)
        self.clickActions = ClickActions(self)
        self.clickActions.click_on_xpath(xpath)

    def click_download_iconsize(self, icon_size_button):
        """Выбрать размер скачиваемой иконки"""
        xpath = './/*[@class="b-bar-content m-icon-preview"]/descendant::*[@class="c-list m-nooverflow"]/*[%s]' % icon_size_button
        self.clickActions = ClickActions(self)
        self.clickActions.click_on_xpath(xpath)

    def try_gotit(self):
        """try 'got it'  c;ick"""

        try:
            self.browser.find_element_by_xpath('//*[@ng-click="action(message, icons8Messages.service, this)"]')
            self.browser.find_element_by_xpath('//*[@ng-click="action(message, icons8Messages.service, this)"]').click()
            time.sleep(1)
        except NoSuchElementException:
            pass

    def try_click_text(self, link):
        """try click text"""
        try:
            while True:
                try:
                    self.browser.find_element_by_xpath('//*[contains(text(), "%s")][1]' % link).click()
                    break
                except StaleElementReferenceException:
                    continue
        except:
            pass




