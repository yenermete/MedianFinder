'''
Created on 6 Aug 2014

@author: Yener
'''
import unittest
from methods.ExternalSort import MergeSort
from methods.QuickSelect import QuickSelect
from _decimal import Decimal
from MedianFinder.util import FileUtil


class Test(unittest.TestCase):

    def setUp(self):
        self._QUICK_SELECT = "q"
        self._EXTERNAL_SORT = "e"

    def test_median_with_externalSort(self):
        file_name = FileUtil.FILE_PATH + "6248111_28114.txt"
        method = self._EXTERNAL_SORT
        assert self._get_median_from_fileName(file_name) == self._get_calculated_median(method, file_name)


    def test_median_with_quickSelect(self):
        file_name = FileUtil.FILE_PATH + "6248111_28114.txt"
        method = self._QUICK_SELECT
        assert self._get_median_from_fileName(file_name) == self._get_calculated_median(method, file_name)
    
    def _get_calculated_median(self, method, fileName):
        if(method == self._QUICK_SELECT):
            sort_method = QuickSelect()
        elif method == self._EXTERNAL_SORT :
            sort_method = MergeSort()
        else :
            raise Exception("Method name wrong")
        real_median = sort_method.calculate_median(fileName)
        del sort_method
        return real_median; 
    
    def _get_median_from_fileName(self, fileName):
        "This method will return the median acquired from the file name"
        return Decimal(fileName.split("_")[1].replace(".txt", ""))