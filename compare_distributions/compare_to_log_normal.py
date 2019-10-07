# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 12:23:10 2019

@author: marti
"""

from .compare_to_normal import Gaussian
import math
import numpy as np
from matplotlib import pyplot as plt

class Lognormal(Gaussian):
    
    def __init__(self, file_name = 'example.txt'):
            Gaussian.__init__(self, file_name)
            self.distribution = 'Log Normal'
            
    
    
    def read_data_file(self, file_name):
        
        """Function to read in data from a txt file. The txt file should have
        one number (float) per line. The numbers are stored in the data attribute.

        Args:
            file_name (string): name of a file to read from

        Returns:
            None

        """

        with open(file_name) as file:
            data_list = []
            line = file.readline()
            while line:
                data_list.append(float(line))
                line = file.readline()
            file.close()

        self.data = [np.log(x) for x in data_list]
        
        return self.data     

        