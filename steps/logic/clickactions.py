# -*- coding: utf-8 -*-

from locators import locators_dict
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
import time
import os
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

        self.clickActions = ClickActions(self)
        self.clickActions.click_on_xpath(locators_dict.get(buttonName))


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




