'''
Created on 5 Aug 2014

@author: Yener
'''
from _decimal import Decimal
from methods.ExternalSort import MergeSort
from methods.QuickSelect import QuickSelect
from MedianFinder.util import FileUtil

"""    This script will make all the files available to be tested. Files should have the median as part of their names.
        They are assumed to be in the folder FileUtil.FILE_PATH
"""

file_names = ["10000_0.0.txt","10000_382.5.txt","10000_74.5.txt","10001_-1.txt","10001_-73.txt","10001_1.txt","10001_264.txt","102309_84.txt",
            "123451_0.txt","123498_3.0.txt","124987_143.txt","124988_-137.5.txt","125001_0.txt","125001_1112.txt","125001_6533.txt","125048_-78.0.txt",
            "125147_-147.txt","1300_-81.0.txt","1300_0.0.txt","1300_206.5.txt","149999_-1.txt","149999_0.txt","149999_116.txt","149999_38.txt",
            "150000_-1.0.txt","150000_-3508.5.txt","150000_0.0.txt","150000_1116.5.txt","19987_466.txt","20006_166.5.txt","2499_-1514.txt","2499_-3.txt",
            "2499_-360.txt","2499_4.txt","2500_-133.5.txt","2500_-217.5.txt","2500_0.0.txt","2501_-353.txt","2501_0.txt","2501_1.txt",
            "2501_354.txt","250_-109.0.txt","250_-364.0.txt","250_0.0.txt","33461_-808.txt","33461_0.txt","33544_-41.5.txt","33544_70.5.txt",
            "4_-0.5.txt","4_-84.5.txt","4_50.0.txt","5_-4.txt","5_0.txt","5_1.txt","5_4.txt","62499_0.txt",
            "62499_311.txt","62499_98.txt","62500_-46.0.txt","62500_0.0.txt","62500_167.0.txt","62501_0.txt","62501_194.txt","62501_40.txt",
            "64489_-3.txt","65000_-58.0.txt","65000_-81.5.txt","65062_-237.5.txt","65210_-131.0.txt","9999_0.txt","9999_158.txt","9999_331.txt",
            "a5_0.txt","b5_0.txt","c4_-0.5.txt","d250_0.0.txt","e2500_0.0.txt","f10000_0.0.txt","g125001_0.txt","h9999_0.txt",
            "i9999_0.txt","j1300_0.0.txt","k62500_0.0.txt","l62500_0.0.txt","m62501_0.txt","n62501_0.txt","o62499_0.txt","p62499_0.txt"];
for file_name in file_names :
    index = file_name.find("_")
    median = Decimal(file_name.split("_")[1].replace(".txt", ""))
    sortMethod = MergeSort()
    realMedian = sortMethod.calculate_median(FileUtil.FILE_PATH + file_name)
    print("Median of " + file_name + " with external sort is " + str(realMedian))
    assert median == realMedian
    sortMethod = QuickSelect()
    realMedian = sortMethod.calculate_median(FileUtil.FILE_PATH + file_name)
    print("Median of " + file_name + " with quickselect is " + str(realMedian))
    assert median == realMedian

    
    