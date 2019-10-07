# check_distribution
Python package that compares input data to common distributions.

1) Install the package
2) Specify the distribution that you want to check your data against and the file name of the input data. The classes are named 
   after the distribution of interest. 

   E.g., Gaussian('example.txt') would help you to assess to what extent the input data in the "example.txt" file, is deviating 
   from a Gaussian distribution. 
   
Currently supported distributions (version 0.1 of the package):
- Gaussian()
- Lognormal()

Currently supported input data:
 - txt files with one non-negative number (float or integer) per line

