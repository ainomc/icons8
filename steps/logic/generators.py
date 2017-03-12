# -*- coding: utf-8 -*-
from datetime import datetime
import time
import os
from os import listdir
from settings import settings_test as settings
from environment import download_folder_path
import random
now = datetime.today()

TIME_FOR_WAIT = 30

SERVER = settings['server']



# открывает файл, записывает данные.
# Значение file должно быть в скобках  "some.txt"
class FileActions(object):
    # открывает файл, записывает данные.
    # Значение file должно быть в скобках  "some.txt"
    def write_in_file(self, file, save_text):
        my_file = open(file, "r+")
        my_file.write(save_text + "\n")

    # Открывает файл и возвращает первую строку
    def read_file(self, file):
        my_file = open(file, "r+")
        fileText = my_file.readline()
        print ("%s" + " idea created!!!") % fileText
        my_file.close()
        return fileText

    # удаляет файл по пути
    def delete_file(self, file):
        if file == 'icon8 app':
            pathToSetup = os.path.join(
                ' ', 'Icons8Setup.exe')
            file_path = download_folder_path + pathToSetup[1:]
            os.remove(file_path)
        else:
            pass

    # Удаляет все файлы с окончание или расширением (extension)
    def del_by_extension(self, extension):
        list_of_all_files = listdir(download_folder_path)
        print(str(list_of_all_files) + " << all files")
        elements_count = 0
        for item in list_of_all_files:
            if item.endswith(extension):
                elements_count += 1
                os.remove(os.path.join(download_folder_path, item))
        assert elements_count > 0

    # Ждёт пока не исщезнит файл .part
    def downloading_file(self, extension):
        time.sleep(4)
        elements_count = 0
        for item in listdir(download_folder_path):
            if item.endswith(extension):
                time_waited = 0
                elements_count += 1
                download_end = False
                while download_end == False:
                    path = os.path.exists(os.path.join(download_folder_path, item))
                    if path == True:
                        time.sleep(5)
                        time_waited += 5
                    elif time_waited == 240:
                        print ('download is to long')
                        break
                    elif path == False:
                        print ('Donwload file with ' +
                               extension + ' extension ended')
                        download_end = True
                print (str(time_waited) + "sec download")
        assert elements_count > 0


class RandomGenerate(object):
    def random_betweenValue(self, first_value, last_value):
        return random.randint(first_value, last_value)

    # Возвращает случайное значение из списка
    def random_listValue(self, list):
        return random.choice(list)

    # Генерирует рандомное идею из 6 значений из списка и сохраняет его в файл
    def random_idea_name(self):
        idea = ''
        symbols = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
        for x in range(6):
            idea = idea + \
                random.choice(
                    list(symbols))
        pathToFile = os.path.join('steps', 'logic', 'ideas.txt')
        print (pathToFile + "path to idea file")
        Fileactions = FileActions()
        Fileactions.write_in_file(pathToFile, idea)
        return idea

    # Генерирует рандомный текст
    def random_text(self, number_of_testItems):
        text = ''
        symbols = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890'
        for x in range(number_of_testItems):
            text = text + \
                random.choice(
                    list(symbols))
        return text

    # Генерирует рандомное имейл из 6 значений из списка и + '@gmail.com'
    def random_email(self):
        email = ''
        for x in range(6):
            email = email + random.choice(list('qwertyuiopasdfghjklzxcvbnm'))
        return email + '@gmail.com'


class ValueGenerate(object):
    # Генерирует значения промежуточные значения
    # между first_value и second_value
    def values_in_range(self, first_value, second_value):
        for values in range(first_value, second_value):
            return values
