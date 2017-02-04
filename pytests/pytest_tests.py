# -*- coding: utf-8 -*-
from selenium import webdriver
import pytest
import os
from environment import *
from pytest_settings import *
from steps.logic.actions import *
from steps.logic.locateactions import *
from steps.logic.generators import *
# python -m pytest -v pytest_tests.py -s     --   runner




# Main Test class
class Tests(MainTestClassSettings):

    # landing page icon
    def test_landingPageIcon(self):
        self.textActions.addTextToField('positive text', 'search')
        self.clickActions.clickButton('search')
        self.clickActions.clickButton('first icon in result')
        self.clickActions.clickButton('icon name')
        self.locateActions.locateElement('icon category')
        self.locateActions.locateElement('icon text')
        self.locateActions.locateElement('Icon')
        self.locateActions.locateElement('Download button')
        self.locateActions.locate_text('Generate HTML')
        self.clickActions.clickButton('choose size of PNG')
        self.locateActions.locateElement('icon download sizes')
        self.locateActions.locateElement('icon download format')
        self.locateActions.locate_text('Download multiple sizes')
        self.locateActions.locate_text('Browse by tags')

    # landing page tag
    def test_landingPageTag(self):
        self.textActions.addTextToField('positive text', 'search')
        self.clickActions.clickButton('search')
        self.clickActions.clickButton('first icon in result')
        self.clickActions.clickButton('icon name')
        self.locateActions.locate_text('Browse by tags')
        self.clickActions.clickButton('tag')
        self.locateActions.locate_text('This page contains')
        self.clickActions.clickButton('icon in tag page')
        self.locateActions.locate_text('Browse by tags')

    # landing page category
    def test_landingPageCategory(self):
        self.textActions.addTextToField('positive text', 'search')
        self.clickActions.clickButton('search')
        self.clickActions.clickButton('first icon in result')
        self.clickActions.clickButton('icon name')
        self.locateActions.locate_text('Browse by tags')
        self.clickActions.clickButton('icon category')
        self.locateActions.locateElement('icons result')
        self.locateActions.locateElement('icons in result')
        self.locateActions.locateElement('Category Title')



