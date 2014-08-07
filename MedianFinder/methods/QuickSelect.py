'''
Created on 03 Aug 2014

@author: Yener
'''
from statistics import median
from math import ceil
from MedianFinder.util import FileUtil

class QuickSelect(object):
    '''
    This class will pick a pivot value from the given input file and then partition the file into two files as smallerThanPivot
    and greaterThanPivot. Median index is calculated before this operation so that it is known where the median is after this 
    phase. This phase is repeated afterwards till median is the pivot or the greatest value of the smallerThanPivot file, depending
    on the number of integers in the input file. Then the median is calculated.
    '''
    def __init__(self):
        self._SMALLER_FILE_NAME = "s"
        self._GREATER_FILE_NAME = "l"
        self._RESULT = None
        self._LESS_THAN_PIVOT = "lessThanPivot"
        self._LESS_THAN_PIVOT_LENGTH = "lessThanPivotLength"
        self._GREATER_THAN_PIVOT = "greaterThanPivot"
        self._GREATER_THAN_PIVOT_LENGTH = "greaterThanPivotLength"
        self._MEDIAN_INDEX = "indexToLookFor"
        self._FILE_LENGTH = "fileLength"
        self._TWO_MEDIANS = "checkTwoValues"
        self._SUFFIX = "1"
          
    def _calculate_median_with_partitioning(self, input_file_name, index_of_median, two_median_values, file_length):
        """   This method looks for the indexToLookForth element in the file, without sorting the file. It will partition
              the file into two files, where one file will contain values smaller than the pivot and other file will contain
              values equal to or bigger than the pivot. If the pivot is at the median position, the appropriate median is
              returned. Otherwise, next median index, next file name, next file length and median search strategy is returned.
              Args :
                input_file_name : Name of the file that will be partitioned.
                index_of_median : Median index
                two_median_values :  Boolean value, true if original file had an even amount of lines
                file_length : Number of lines in the input file.
            Returns :
                A dictionary which contains two file names that were created, their lengths, the new index of the median.
          """
        with open(input_file_name, "r") as input_file :
            pivot = median(self._get_pivot(input_file, file_length))
            less_than_pivot_file = open(self._SMALLER_FILE_NAME + FileUtil.TXT_SUFFIX, "w")
            greater_than_pivot_file = open(self._GREATER_FILE_NAME + FileUtil.TXT_SUFFIX, "w")
            less_than_pivot_length = 0
            greater_than_pivot_length = 0
            pivot_added = False
            line = input_file.readline()
            while line:
                number = int(line)
                if number < pivot :
                    less_than_pivot_length += 1
                    less_than_pivot_file.write(line)
                else:
                    if not pivot_added and number == pivot:                   # pivot is not added to any of the files
                        pivot_added = True
                    else :
                        greater_than_pivot_file.write(line)
                        greater_than_pivot_length += 1
                line = input_file.readline()
    
        self._change_file_names()
        if less_than_pivot_length == index_of_median :
            FileUtil.remove_file(greater_than_pivot_file)
            lastLessThanValue = self._get_max_or_min_in_file(less_than_pivot_file, False)
            FileUtil.remove_file(less_than_pivot_file)
            if two_median_values :
                return {self._RESULT : (lastLessThanValue + pivot) / 2}
            else :
                return {self._RESULT : lastLessThanValue}
        elif less_than_pivot_length == index_of_median - 1 :
            FileUtil.remove_file(less_than_pivot_file)
            if two_median_values :
                firstGreaterThanValue = self._get_max_or_min_in_file(greater_than_pivot_file, True)
                FileUtil.remove_file(greater_than_pivot_file)
                return {self._RESULT : (firstGreaterThanValue + pivot) / 2}
            else :
                FileUtil.remove_file(greater_than_pivot_file)
                return {self._RESULT : pivot}
        else :
            return {self._MEDIAN_INDEX : index_of_median, self._GREATER_THAN_PIVOT : greater_than_pivot_file, self._GREATER_THAN_PIVOT_LENGTH : greater_than_pivot_length,
                    self._LESS_THAN_PIVOT : less_than_pivot_file, self._LESS_THAN_PIVOT_LENGTH : less_than_pivot_length}
    
    def calculate_median(self, inputFileName):
        """ This method will call _calculate_median_with_partitioning until the median is found. If it is not found, the file in which the median
            does not exist is deleted. The search is repeated with the other file with recalculated values. When the median is found, both files
            are deleted.
        """
        file_length = FileUtil.get_file_length(inputFileName)
        two_medians = file_length % 2 == 0
        if(two_medians) :
            index_of_median = int(file_length / 2)
        else :
            index_of_median = ceil(file_length / 2)
        result_map = self._calculate_median_with_partitioning(inputFileName, index_of_median, two_medians, file_length)
        result = result_map.get(self._RESULT)
        while(result is None) :
            less_than_pivot_length = result_map.get(self._LESS_THAN_PIVOT_LENGTH)
            lessThanPivot = result_map.get(self._LESS_THAN_PIVOT)
            greaterThanPivot = result_map.get(self._GREATER_THAN_PIVOT)
            greaterThanPivotLength = result_map.get(self._GREATER_THAN_PIVOT_LENGTH)
            index_of_median = result_map.get(self._MEDIAN_INDEX)
            if less_than_pivot_length < index_of_median :
                FileUtil.remove_file(lessThanPivot)
                greaterThanPivot.close()
                index_of_median = index_of_median - less_than_pivot_length - 1
                result_map = self._calculate_median_with_partitioning(greaterThanPivot.name, index_of_median, two_medians, greaterThanPivotLength)
                FileUtil.remove_file(greaterThanPivot)
            else :
                FileUtil.remove_file(greaterThanPivot)
                lessThanPivot.close()
                result_map = self._calculate_median_with_partitioning(lessThanPivot.name, index_of_median, two_medians, less_than_pivot_length)
                FileUtil.remove_file(lessThanPivot)
            result = result_map.get(self._RESULT)
        else :
            return result
    
    def _get_max_or_min_in_file(self, file, minRequired):
        "This method will get the min or max number in the file according to the parameter 'minRequired' == true or not"
        file.close()
        file = open(file.name, "r")
        line = file.readline()
        returnValue = int(line)
        while line :
            number = int(line)
            if minRequired :
                if number < returnValue :
                    returnValue = number
            else :
                if number > returnValue :
                    returnValue = number
            del number
            line = file.readline()
        return returnValue
        
    def _change_file_names(self):
        "This method will change the generated fileNames from l and s to l1 and s1 and vice versa during the partitioning phase"
        if self._SMALLER_FILE_NAME.endswith(self._SUFFIX) :
            self._SMALLER_FILE_NAME = self._SMALLER_FILE_NAME.replace(self._SUFFIX, "")
            self._GREATER_FILE_NAME = self._GREATER_FILE_NAME.replace(self._SUFFIX, "")
        else :
            self._SMALLER_FILE_NAME += self._SUFFIX
            self._GREATER_FILE_NAME += self._SUFFIX
    
    def _get_pivot(self, inputFile, file_length):
        """This method will get the pivot from the given inputFile, as the median of first, middle and last elements. It will default 
            to initial number if there are just two numbers. This method can be changed to take the first number as a pivot, which will
            increase the performance a lot, especially in large files, at the cost of picking a possible bad pivot value. """
        middle_index = file_length // 2
        i = 1
        pivot_chooser = []
        file_length -= 1         # 0 based index
        line = inputFile.readline()
        while line :
            if i == 1 :
                pivot_chooser.append(int(line))
            elif i == middle_index :
                pivot_chooser.append(int(line))
            elif i == file_length :
                pivot_chooser.append(int(line))
            line = inputFile.readline()
            i += 1
        length = len(pivot_chooser)
        if length == 2 :
            del pivot_chooser[1]
        elif length == 0 :
            raise Exception(FileUtil.EMPTY_FILE)
        inputFile.seek(0)
        return pivot_chooser
    