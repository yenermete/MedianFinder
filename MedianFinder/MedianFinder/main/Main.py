'''
Created on 03 Aug 2014

@author: Yener
'''

from methods.ExternalSort import MergeSort 
from pip._vendor.distlib.compat import raw_input
from methods.QuickSelect import QuickSelect
import traceback

quickSelect = "1"
externalSort = "2"
while True :
    file_name = raw_input('Enter full path of the file that holds the numbers : ')
    if file_name and len(file_name) > 0 :
        break
while True :
    choice = raw_input("Type " + quickSelect + " for quicksselect, " + externalSort + " for external sorting : ")
    if choice and choice in [quickSelect, externalSort] :
        break
try :
    if choice == quickSelect :
        sortMethod = QuickSelect()
    else :
        sortMethod = MergeSort()
    medianValue = sortMethod.calculate_median(file_name)
    del sortMethod
    print("Median Value is : " + str(medianValue))
    del medianValue
except Exception as e :
    traceback.print_exc()
