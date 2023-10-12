# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 15:47:02 2023

@author: LENOVO
"""
#alt92 = \ #alt94 = ^    

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as st
import importlib
import os

# import our own files and reload
import random_variables
importlib.reload(random_variables)
import market_data
importlib.reload(market_data)

#inputs
ric = 'MA'

# computations
dist = market_data.distribution(ric)
dist.load_timeseries()
dist.plot_timeseries()
dist.compute_stats()
dist.plot_histogram()



# lop to check normalitu in real distributions
#directory = 'C:\\Users\\LENOVO\\.spyder-py3\\2024-1\\data\\' #hardcode#rics = []
#is_normals = []
#for file_name in os.listdir(directory):
 #   print('file name= ' + file_name)
  #  ric = file_name.split('.')[0]
   # if ric == 'datayfinance':
    #    continue
    #compute stats
  # dist = market_data.distribution(ric)
   #dist.load_timeseries()
#    dist.compute_stats()
    # generate lists
 #   rics.append(ric)
  #  is_normals.append(dist.is_normal)
#df = pd.DataFrame()
#df['ric'] = rics
#df['is_normal'] = is_normals
#f = df.sort_values(by = 'is_normal', ascending = False)




