# -*- coding: utf-8 -*-

import time
import os
from os import listdir
from environment import download_folder_path
import random


class FileActions(object):
    """Actions with files"""

    def write_in_file(self, file, save_text):
        """открывает файл, записывает данные. 
        Значение file должно быть в скобках  "some.txt"
        """
        my_file = open(file, "r+")
        my_file.write(save_text + "\n")

    def read_file(self, file):
        """Открывает файл и возвращает первую строку"""
        my_file = open(file, "r+")
        file_text = my_file.readline()
        my_file.close()
        return file_text

    def delete_file(self, file):
        """Удаляет файл по пути"""
        if file == 'icon8 app':
            setup_path = os.path.join(
                ' ', 'Icons8Setup.exe')
            file_path = download_folder_path + setup_path[1:]
            os.remove(file_path)
        else:
            pass

    def del_by_extension(self, extension):
        """Удаляет все файлы с окончание или расширением (extension)"""
        list_of_all_files = listdir(download_folder_path)
        print(str(list_of_all_files) + " << all files")
        elements_count = 0
        for item in list_of_all_files:
            if item.endswith(extension):
                elements_count += 1
                os.remove(os.path.join(download_folder_path, item))
        assert elements_count > 0

    def wait_presents_file(self, extension):
        """Ждёт пока не появиться файл"""
        loop = True
        time_count = 0
        while loop is True:
            assert time_count != 30, 'no download file'
            for item in listdir(download_folder_path):
                if item.endswith(extension):
                    loop = False
                    break
                else:
                    pass
            time.sleep(1)
            time_count += 1

    def downloading_file(self, extension):
        """Ждёт пока не исщезнит файл"""
        for item in listdir(download_folder_path):
            if item.endswith(extension):
                time_waited = 0
                download_end = False
                while download_end is False:
                    path = os.path.exists(
                        os.path.join(download_folder_path, item))
                    if path is True:
                        time.sleep(5)
                        time_waited += 5
                    elif time_waited == 240:
                        print ('download is to long')
                        break
                    elif path is False:
                        print ('Donwload file with ' +
                               extension + ' extension ended')
                        download_end = True
                print (str(time_waited) + "sec download")


class RandomGenerate(object):
    """Different randoms"""

    def random_between_values(self, first_value, last_value):
        """Return value between values"""
        return random.randint(first_value, last_value)

    def random_list_value(self, list):
        """Возвращает случайное значение из списка"""
        return random.choice(list)

    def random_idea_name(self):
        """Генерирует рандомное идею из 6 
        значений из списка и сохраняет его в файл
        """
        idea = ''
        symbols = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
        for x in range(6):
            idea = idea + \
                random.choice(
                    list(symbols))
        path_to_file = os.path.join('steps', 'logic', 'ideas.txt')
        print (path_to_file + "path to idea file")
        fileactions = FileActions()
        fileactions.write_in_file(path_to_file, idea)
        return idea

    def random_text(self, number_of_testitems):
        """Генерирует рандомный текст"""
        text = ''
        symbols = 'qwertyuiopasdfghjklzxcvbnm' \
                  'QWERTYUIOPASDFGHJKLZXCVBNM1234567890'
        for x in range(number_of_testitems):
            text = text + \
                random.choice(
                    list(symbols))
        return text

    def random_email(self):
        """Генерирует рандомное имейл из 6 
        значений из списка и + '@gmail.com'
        """
        email = ''
        for x in range(6):
            email = email + random.choice(list('qwertyuiopasdfghjklzxcvbnm'))
        return email + '@gmail.com'


class ValueGenerate(object):
    """Generators"""

    def values_in_range(self, first_value, second_value):
        """Генерирует значения промежуточные 
        значения между first_value и second_value
        """
        for values in range(first_value, second_value):
            return values
