'''
Created on 03 Aug 2014

@author: Yener
'''
import os

TXT_SUFFIX = ".txt"                         # This value can be changed if file extensions are required to be different
FILE_PATH = "d:/median/smallfiles/"         # This value can be changed if input files are kept at a different folder
INVALID_INTEGER = "Invalid integer value!"
EMPTY_FILE = "File is empty!"

def get_file_length(file_name):
    return sum(1 for line in open(file_name))

def remove_file(file):
    file.close()
    os.remove(file.name)