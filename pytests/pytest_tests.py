# -*- coding: utf-8 -*-
from selenium import webdriver
import pytest
import os
from environment import *
from steps.logic.actions import *
from pytest_settings import *

# python -m pytest -v pytest_tests.py -s     --   runner

# Main Test class
class Tests(MainTestClassSettings):
    def test_ofTests(self):
        self.clickActions = ClickActions(self)
        self.clickActions.click_on_xpath('html/body/nav/div/div/ul/li[2]/a/span')
        print ("First Test Done")
