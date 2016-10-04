# -*- coding: utf-8 -*-
from selenium import webdriver
import pytest
import os
from environment import *
from steps.logic.actions import *


# init browser
class InitMain(object):
    def __init__(self, context):
        self.browser = context.browser
        print("Init browser")


# Fixture settings fo Tests class
class MainTestClassSettings(object):
    # Action before test
    def setup(self):
        self.browser.get("https://demo.icons8.com")
        print("Setup test")

    # Action after class
    def teardown(self):
        self.browser.get("https://demo.icons8.com")
        print("Teardown test")

    # Action before test
    def setup_class(cls):
        make_driver(cls)
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