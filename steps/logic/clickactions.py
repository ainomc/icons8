# -*- coding: utf-8 -*-

from locators import locators_dict
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import \
    StaleElementReferenceException, NoSuchElementException
import time
from locateactions import Page, LocateActions


class ClickActions(Page):
    """Различные клики"""

    def click_on_link(self, link):
        """Click contains text"""
        try:
            WebDriverWait(self.browser, 1).until(EC.element_to_be_clickable(
                (By.XPATH, '//*[contains(text(), "%s")][1]' % link))).click()
        except:
            self.browser.find_element_by_xpath(
                '//*[contains(text(), "%s")][1]' % link).click()

    def try_click_on_link(self, link):
        """Try contains text"""
        while True:
            try:
                self.browser.find_element_by_xpath(
                    '//*[contains(text(), "%s")][1]' % link).click()
                break
            except StaleElementReferenceException:
                continue

    def click_header_nav_menu(self, button_name):
        """Наимает на кнопку в главном иеню в хедере.
        Типы вводных 'Icons', 'Download', 'Request', 'Buy', 'Resources'
        """
        xpath = '//*[@class="b-menu"]/descendant::' \
                'span[contains(text(), "%s")]' % button_name
        self.clickActions = ClickActions(self)
        self.clickActions.click_on_xpath(xpath)

    def click_text(self, link):
        """Click text"""
        try:
            WebDriverWait(self.browser, 1).until(EC.element_to_be_clickable(
                (By.XPATH, '//*[text()="%s"]' % link))).click()
        except:
            self.browser.find_element_by_xpath('//*[text()="%s"]' % link).click()

    def click_text_with_div(self, link):
        """Click text with div"""
        try:
            WebDriverWait(self.browser, 3).until(EC.element_to_be_clickable(
                (By.XPATH, '//div[contains(text(), "%s")][1]' % link))).click()
        except:
            self.browser.find_element_by_xpath(
                '//div[contains(text(), "%s")][1]' % link).click()

    def click_on_xpath(self, xpath):
        """Click xpath"""
        try:
            WebDriverWait(self.browser, 1).until(
                EC.element_to_be_clickable((By.XPATH, xpath))).click()
        except:
            self.browser.find_element_by_xpath(xpath).click()

    def move_and_click(self, move_to, button):
        """Передвигает курсор и кликает"""
        def logic():
            time.sleep(4)
            move = self.browser.find_element_by_xpath(move_to)
            click_button = self.browser.find_element_by_xpath(button)
            action = webdriver.ActionChains(self.browser)
            action.move_to_element(move)
            action.perform()
            time.sleep(4)
            click_button.click()
        try:
            logic()
        except:
            logic()

    def click_on_button(self, button):
        """Кликнуть на кнопку"""
        try:
            WebDriverWait(self.browser, 1).until(EC.element_to_be_clickable(
                (By.XPATH, '//button[.="%s"]' % button))).click()
        except:
            self.browser.find_element_by_xpath(
                '//button[.="%s"]' % button).click()

    def click_button_with_text(self, name):
        """Кликнуть на кнопку, найденой с помощью названия кнопки"""
        try:
            WebDriverWait(self.browser, 1).until(EC.element_to_be_clickable(
                (By.XPATH, '//button[contains(., "%s")]' % name))).click()
        except:
            self.browser.find_element_by_xpath(
                '//button[contains(., "%s")]' % name).click()

    def click_on_unactive_tab(self, tab):
        """Кликнуть на вкладку"""
        try:
            WebDriverWait(self.browser, 1).until(EC.element_to_be_clickable(
                (By.XPATH, '//*[@class="%s"]' % tab))).click()
        except:
            self.browser.find_element_by_xpath(
                '//*[@class="%s"]' % tab).click()

    def click_on_create(self, create):
        """Кликнуть на кнопку Создать коллекцию"""
        try:
            WebDriverWait(self.browser, 1).until(EC.element_to_be_clickable(
                (By.XPATH, '//*[@class="%s"]' % create))).click()
        except:
            self.browser.find_element_by_xpath(
                '//*[@class="%s"]' % create).click()

    def click_all(self, xpath):
        """Кликает на все найденные элементы"""
        self.locateActions = LocateActions(self)
        count = self.locateActions.element_count(xpath)
        while count > 0:
            print (str(count))
            self.browser.find_element_by_xpath(xpath % count).click()
            count -= 1

    def click_all_and_click_button(self, all_xpath, button_xpath):
        """Кликает на все найденные элементы и потом еще кликает на кнопку"""
        self.locateActions = LocateActions(self)
        count = self.locateActions.element_count(all_xpath)
        while count > 0:
            print (str(count))
            self.browser.find_element_by_xpath(all_xpath % count).click()
            self.browser.find_element_by_xpath(button_xpath).click()
            count -= 1

    def click_logo(self):
        """Наимает на кнопку в хедере."""
        xpath = './/a[@class="b-logo"]/span[contains(text(), "Icons8")]'
        self.clickActions = ClickActions(self)
        self.clickActions.click_on_xpath(xpath)

    def click_button(self, button_name):
        """Уликнуть на элемент по уникальному xpath"""

        self.clickActions = ClickActions(self)
        self.clickActions.click_on_xpath(locators_dict.get(button_name))

    def try_click_button(self, button_name):
        """Кликнуть на элемент по уникальному xpath"""
        if button_name == 'got it':
            xpath = '''.//*[@ng-repeat="(title, action) in message.actions"]'''
        try:
            self.clickActions = ClickActions(self)
            self.clickActions.click_on_xpath(xpath)
        except:
            pass

    def click_ng_if_xpath(self, ng_if_locator):
        """Кликает на элемент с ng-if"""
        xpath = '//*[@ng-if="%s"]' % ng_if_locator
        self.clickActions = ClickActions(self)
        self.clickActions.click_on_xpath(xpath)

    def click_download_icontype(self, icon_type):
        """Выбрать тип/формат скачиваемой иконки"""
        dict = {'PNG': 1, 'SVG': 2, 'EPS': 3,
                'PDF': 4, 'Font': 5, 'SVG set': 6}
        time.sleep(5)
        xpath = './/*[@class="c-list m-nooverflow b-format"]/*[%s]' \
                % dict.get(icon_type)
        self.clickActions = ClickActions(self)
        self.clickActions.click_on_xpath(xpath)

    def click_download_iconsize(self, icon_size_button):
        """Выбрать размер скачиваемой иконки"""
        xpath = './/*[@class="b-size"]/ul/li[%s]' % icon_size_button
        self.clickActions = ClickActions(self)
        self.clickActions.click_on_xpath(xpath)

    def try_gotit(self):
        """try 'got it'  c;ick"""

        try:
            self.browser.find_element_by_xpath(
                '//*[@ng-click="action(message, '
                'icons8Messages.service, this)"]')
            self.browser.find_element_by_xpath(
                '//*[@ng-click="action(message, '
                'icons8Messages.service, this)"]').click()
            time.sleep(1)
        except NoSuchElementException:
            pass

    def try_click_text(self, link):
        """try click text"""
        try:
            while True:
                try:
                    self.browser.find_element_by_xpath(
                        '//*[contains(text(), "%s")][1]' % link).click()
                    break
                except StaleElementReferenceException:
                    continue
        except:
            pass
