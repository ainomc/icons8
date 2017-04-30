# -*- coding: utf-8 -*-

from selenium.common.exceptions import NoSuchElementException
from actions import Page
from locators import locators_dict


class LocateActions(Page):
    """Проверки на присутствия"""

    def locate_text(self, text):
        """Найти видимиый текст что содержит в себе"""
        self.browser.find_element_by_xpath('//*[contains(text(), "%s")]' % text)

    def locate_concrete_text(self, text):
        """Найти видимиый текст"""
        self.browser.find_element_by_xpath('//*[text()="%s"]' % text)

    def locate_element(self, xpath):
        """Найти видимиый элемент по xpath"""
        self.browser.find_element_by_xpath(xpath)

    def absent_element(self, xpath):
        """Проверяет, что элемент отсутствует."""
        try:
            self.browser.find_element_by_xpath(xpath)
        except NoSuchElementException:
            return True
        return False

    def countOfElements(self, xpath):
        """Возвращае колличество єлементов"""
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

    def tryFindClickFind(self, try_find, click, find_second):
        """Try click xpath > then click xpath > then find another xpath"""
        from clickactions import ClickActions
        try:
            self.browser.find_element_by_xpath(try_find)
            self.clickActions = ClickActions(self)
            self.clickActions.click_on_xpath(click)
            self.locateActions = LocateActions(self)
            self.locateActions.locate_element(find_second)
        except NoSuchElementException:
            pass


    def locateElement(self, elementName):
        """Найти элемент по уникальному xpath"""
        self.locateActions = LocateActions(self)
        self.locateActions.locate_element(locators_dict.get(elementName))