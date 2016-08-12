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
import random
now = datetime.today()

TIME_FOR_WAIT = 30

SERVER = settings['server']
# Возвращает случайное значение в диапазоне first_value, last_value
def random_betweenValue(first_value, last_value):
	return randint(first_value, last_value)

# Возвращает случайное значение из списка
def random_listValue(list):
	return choice(list)

# Генерирует рандомное имя из 6 букв разных регистров
def random_name():
	psw = ''  # предварительно создаем переменную psw
	for x in range(12):
		psw = psw + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
	return psw