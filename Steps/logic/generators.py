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
	my_file = open(file, "r+")
	my_file.write(save_text + "\n")

# Открывает файл и возвращает первую строку
def read_file(file):
	my_file = open(file, "r+")
	fileText = my_file.readline()
	print ("%s" + " idea created!!!") % fileText
	my_file.close()
	return fileText

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
	write_in_file("steps\logic\ideas.txt", idea)
	return idea

# Генерирует рандомное имейл из 6 значений из списка и + '@gmail.com'
def random_email():
	email = ''
	for x in range(6):
		email = email + random.choice(list('qwertyuiopasdfghjklzxcvbnm'))
	return email + '@gmail.com'

# Генерирует значения промежуточные значения между first_value и second_value
def values_in_range(first_value, second_value):
	for values in range(first_value, second_value):
		return values












