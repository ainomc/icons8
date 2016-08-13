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
# открывает файл, записывает данные. Значение file должно быть в скобках  "some.txt"
def write_in_file(file, save_text):
	my_file = open(file, "a")
	my_file.write(save_text + "\n")

# Возвращает случайное значение в диапазоне first_value, last_value
def random_betweenValue(first_value, last_value):
	return random.randint(first_value, last_value)

# Возвращает случайное значение из списка
def random_listValue(list):
	return random.choice(list)

# Генерирует рандомное идею из 6 значений из списка и сохраняет его в файл
def random_idea_name():
	idea = ''
	for x in range(6):
		idea = idea + random.choice(list('qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
	write_in_file("Steps\logic\ideas.txt", idea)
	return idea












