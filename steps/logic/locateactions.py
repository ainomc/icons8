# -*- coding: utf-8 -*-

from selenium.common.exceptions import NoSuchElementException
from actions import Page
from generators import ValueGenerate


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
        Value_generate = ValueGenerate()
        if elementName == 'icons result':
            xpath = '//div[@class="b-subcategory-wrapper"][1]/descendant::a[%s]' % Value_generate.values_in_range(1, 5)
        elif elementName == 'icons in result':
            xpath = '//div[@class="b-subcategory-wrapper"][1]/descendant::a[%s]' % Value_generate.values_in_range(1, 3)
        elif elementName == 'first icon in collection':
            xpath = './/*[@class="icons-set m-firefox"]/div[@draggable-type="fromLightBox"][1]'
        elif elementName == 'created first collection':
            xpath = '//*[@class="b-collections-container"]/div[1]'
        elif elementName == 'created second collection':
            xpath = '//*[@class="b-collections-container"]/div[2]'
        elif elementName == 'Get Font pop-up':
            xpath = '//*[@stop-events="click"]'
        elif elementName == 'Public Link':
            xpath = '//*[@ng-model="colSharing.url"]'
        elif elementName == 'icon category':
            xpath = '//*[@class="c-breadcrumbs"]/*[%s]' % Value_generate.values_in_range(1, 3)
        elif elementName == 'icon text':
            xpath = './/*[@ng-bind-html="vm.mainSubtitleText"]'
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

