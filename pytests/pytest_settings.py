# -*- coding: utf-8 -*-
from selenium import webdriver
import pytest
import os
from settings import settings_test as settings
from environment import *
from steps.logic.actions import *

SERVER = settings['server']

# Fixture settings fo Tests class
class MainTestClassSettings(object):
    # Action before test
    def setup(self):
        self.browser.get(SERVER)
        print("Setup test")

    # Action after class
    def teardown(self):
        self.browser.get(SERVER)
        print("Teardown test")

    # Action before test
    def setup_class(cls):
        make_driver(cls)
        cls.textActions = TextActions(cls)
        cls.clickActions = ClickActions(cls)
        cls.locateActions = LocateActions(cls)
        print("Setup class")

    #  Action after class
    def teardown_class(cls):
        try:
            cls.browser.quit()
            print("Teardown class")
        except:
            print ('Already exit!st')
        # после выполнения теста закрыть браузера
        print ('Browser closes...')


"""
# init browser
class InitMain(object):
    def __init__(self, context):
        self.browser = context.browser
        print("Init browser")
"""