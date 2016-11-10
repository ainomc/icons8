# -*- coding: utf-8 -*-
import os
import sys
from os import listdir
from os.path import join
'''
Настройки стенда.
Сервер, логин, пароль.
'''
settings_test = {
'login':'ainomc@gmail.com',
'password':'123',
'server':'https://demo.icons8.com/',
'stand_number':'demo'
}

"""
Путь к папке загрузок всех файлов
"""
path_to_download_folder = os.path.join(' ', 'download_tests')
path_to_test_folder = os.getcwd()
download_folder_path = path_to_test_folder + path_to_download_folder[1:]