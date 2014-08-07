'''
Created on 03 Aug 2014

@author: Yener
'''
from math import ceil
from MedianFinder.util import FileUtil

class MergeSort(object):
    """
    This class does external sorting. There is only one public method, 'calculate_median'. When this method is called, number of lines are counted. This value is divided to the THRESHOLD value, and files consisting of a maximum amount
    of THRESHOLD values are generated. Then these files are merged to new files, THRESHOLD of them each time. They are
    kept in an array of maximum THRESHOLD length. When this length is reached, they are also merged to new files.
    Eventually, a totally sorted file is achieved. Then, the median  is found by reading this sorted file   
    """
    def __init__(self):
        self.THRESHOLD = 50
        self.__MERGE_LABEL = "m"
        self._MIN_VALUE = "minValue"
        self._MIN_INDEX = "minIndex"
            
    def _write_chunk(self, chunk, file_name):
        "Writes a chunk of sorted numbers to a temporary file"
        with open(file_name, "w") as file:
            for number in chunk :
                file.write(str(number) + "\n")


    def _write_to_temp_files(self, file_name):
        "This method will write all the numbers in the inputFile to files of length THRESHOLD in a sorted way"
        with open(file_name, "r") as inputFile :
            temp_list=[]
            line_count = 0;
            next_file_name = 0
            line = inputFile.readline()
            while line:
                temp_list.append(int(line))
                line_count += 1
                if line_count % self.THRESHOLD == 0:
                    self._write_chunk(sorted(temp_list), str(next_file_name) + FileUtil.TXT_SUFFIX)
                    next_file_name += 1 
                    temp_list = []
                line = inputFile.readline()
            else:
                if temp_list:
                    self._write_chunk(sorted(temp_list), str(next_file_name) + FileUtil.TXT_SUFFIX)
        if line_count == 0 :
            raise Exception(FileUtil.EMPTY_FILE)
        return line_count
    
    def _merge_chunks(self, open_files, output_file):
        """This method will merge all open_files, which are already sorted, into one sorted file and returns the new fileName
        
            Args :
                open_files : The files that have been opened to be merged
                output_file : the file that has been opened and into which merged values will be written
            Returns :
                Name of the output_file
        """
        number_list = []
        [number_list.append(int(file_.readline())) for file_ in open_files]
        min_info = self._get_min_of_list(number_list)
        while min_info :
            index = min_info.get(self._MIN_INDEX)
            output_file.write(str(min_info.get(self._MIN_VALUE)) + "\n")
            line = open_files[index].readline()
            if line :
                number_list[index] = int(line)
            else :
                del number_list[index]
                FileUtil.remove_file(open_files[index])
                del open_files[index]
            min_info = self._get_min_of_list(number_list)
        del number_list
        [FileUtil.remove_file(file__) for file__ in open_files]
        output_file.close()
        return output_file.name
        
    def _merge_sorted_files(self, output_list, file_name):
        "This method will merge already sorted files to one sorted file when the amount of them exceeds the THRESHOLD."
        temp_file_list = []
        [temp_file_list.append(open(file__, "r")) for file__ in output_list]
        output_list = [self._merge_chunks(temp_file_list, open(file_name + FileUtil.TXT_SUFFIX, "w"))]
        del temp_file_list
        return output_list
        
    def _main_merge(self, total_lines):
        """    If total amount of files created are less than THRESHOLD value, they can be merged to one file and the operation
               is complete. Otherwise, files are opened and merged to a sorted file. These file names are kept in an array. When
               they reach the threshold value, they are also merged(as a merge of merges) and this array is reinitialized with the
               first element as the merge of merges.
        """
        open_files = []
        number_of_files = ceil(total_lines/self.THRESHOLD)
        if number_of_files <= self.THRESHOLD :
            [open_files.append(open(str(file_index_) + FileUtil.TXT_SUFFIX, "r")) for file_index_ in range(0, number_of_files)]
            return self._merge_chunks(open_files, open(self.__MERGE_LABEL + FileUtil.TXT_SUFFIX, "w"))
        else :
            output_file_list = []
            processed_file_counter = 0
            merge_counter = 0
            merge_of_merges_counter = 0
            for file_index_ in range(0, number_of_files) :
                open_files.append(open(str(file_index_) + FileUtil.TXT_SUFFIX, "r"))
                processed_file_counter += 1
                if processed_file_counter % self.THRESHOLD == 0 :
                    output_file_list.append(self._merge_chunks(open_files, open(self.__MERGE_LABEL + str(merge_counter) + FileUtil.TXT_SUFFIX, "w")))
                    merge_counter += 1
                    if merge_counter % self.THRESHOLD == 0 :
                        output_file_list = self._merge_sorted_files(output_file_list, self.__MERGE_LABEL * 2 + str(merge_of_merges_counter))
                        merge_of_merges_counter += 1
                    open_files = []
            if len(open_files) > 0 :
                output_file_list.append(self._merge_chunks(open_files, open(self.__MERGE_LABEL + str(merge_counter) + FileUtil.TXT_SUFFIX, "w")))
            open_files = []
            [open_files.append(open(file, "r")) for file in output_file_list]
            return self._merge_chunks(open_files, open(self.__MERGE_LABEL + FileUtil.TXT_SUFFIX, "w"))
        
    def calculate_median(self, file_name):
        total_lines = self._write_to_temp_files(file_name)
        median_index = total_lines//2 - 1
        output_file = open(self._main_merge(total_lines), "r")
        two_medians = (total_lines % 2 == 0)
        for i in range(0, median_index+1):
            line = output_file.readline()
            if i == median_index :
                medianValue = 0
                if two_medians :
                    medianValue = (int(line) + int(output_file.readline()))/2
                else :
                    medianValue = int(output_file.readline())
                FileUtil.remove_file(output_file)
                return medianValue

    def _get_min_of_list(self, input_list):
        "This method will return the minimum number of the input_list along with its index in the list. It will skip 'None' values"
        index_of_min = 0
        valid_values = False
        first_min_set = False
        min_value = None
        for i in range(0, len(input_list)):
            if input_list[i] is not None:
                valid_values = True
                if not first_min_set :
                    min_value = input_list[i]
                    first_min_set = True
                    continue
            if valid_values and input_list[i] < min_value:
                index_of_min = i
                min_value = input_list[i]
        if(valid_values) :
            return {self._MIN_INDEX : index_of_min, self._MIN_VALUE : min_value}
        else :
            return None