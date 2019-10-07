# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 11:01:12 2019

@author: marti
"""

import math
import numpy as np
from matplotlib import pyplot as plt


class Gaussian:
    
    def __init__(self, file_name = 'example.txt'):
        
        self.data = self.read_data_file(file_name)
        self.mean = self.calculate_mean()
        self.stdev = self.calculate_stdev()
        self.distribution = 'Gaussian'
        self.plot_histogram_pdf()
        
        
        
        
    def calculate_mean(self):
		
        """Function to calculate the mean of the data set.
		
		Args: 
			None
		
		Returns: 
			float: mean of the data set
	
		"""
					
        avg = 1.0 * sum(self.data) / len(self.data)
		
        self.mean = avg
        
        return self.mean



    def calculate_stdev(self):
        """Function to calculate the standard deviation of the data set.
		Args: 
			sample (bool): whether the data represents a sample or population
		Returns: 
			float: standard deviation of the data set
		"""

        return np.array(self.data).std()
        
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

        self.data = data_list
        
        return self.data 
            
            
		
    def pdf(self, x):
    		"""Probability density function calculator for the gaussian distribution.
    		
    		Args:
    			x (float): point for calculating the probability density function
    			
    		
    		Returns:
    			float: probability density function output
    		"""
    		
    		return (1.0 / (self.stdev * math.sqrt(2*math.pi))) * math.exp(-0.5*((x - self.mean) / self.stdev) ** 2)
		

    def plot_histogram_pdf(self, n_spaces = 100):

    		"""Function to plot the normalized histogram of the data and a plot of the 
    		probability density function along the same range
    		
    		Args:
    			n_spaces (int): number of data points 
    		
    		Returns:
    			list: x values for the pdf plot
    			list: y values for the pdf plot
        """
        
        
    
    		min_range = min(self.data)
    		max_range = max(self.data)
    		
    		 # calculates the interval between x values
    		interval = 1.0 * (max_range - min_range) / n_spaces
    
    		x = []
    		y = []
    		
    		# calculate the x values to visualize
    		for i in range(n_spaces):
    			tmp = min_range + interval*i
    			x.append(tmp)
    			y.append(self.pdf(tmp))
    
    		# make the plots
    		fig = plt.figure(figsize = (12, 6))

    		plt.hist(self.data, density=True, color = 'grey')
    		plt.title('Data historgram vs '+ str(self.distribution) + ' distribution', fontsize = 14)
    		plt.ylabel('Density')
    		plt.plot(x, y, color = 'red')        


    		plt.ylabel('Density')
    		plt.show()
    
    		return x, y
		
		
    def __repr__(self):
	
    		"""Function to output the characteristics of the Gaussian instance
    		
    		Args:
    			None
    		
    		Returns:
    			string: characteristics of the Gaussian
    		
    		"""
    		
    		return "mean {}, standard deviation {}".format(self.mean, self.stdev)