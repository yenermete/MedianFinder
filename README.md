MedianFinder
============
This project was written with Python 3.4.1. It takes a file name as input from the user. The file should contain only
integers. It finds the median of the input file list according to the choice of the user. It will either use quick select
or external sorting to find the median value. External sorting has the limit of holding maximum fifty numbers in the memory.
Naturally, quick select is not affected from this constraint.

There is also a java source file which generates files that can be used to test the correctness of the program.
This java source creates files with the following naming format : "line_count_median_value.txt". All files can be given to
the TestAllFiles.py script to be checked with both methods, or either unit tests or main module can be run to check the
correctness.
