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

# import our own files and reload
import random_variables
importlib.reload(random_variables)

#inputs
ric = 'BTC-USD'

directory = 'C:\\Users\\LENOVO\\.spyder-py3\\2024-1\\data\\' #hardcode
path = directory + ric + '.csv'
raw_data = pd.read_csv(path)
t = pd.DataFrame()
t['date'] = pd.to_datetime(raw_data['Date'], dayfirst=True)
t['close'] = raw_data['Close']
t.sort_values(by='date', ascending=True)
t['close_previous'] = t['close'].shift(1)
t['return_close'] = t['close']/t['close_previous'] - 1
t= t.dropna()
t = t.reset_index(drop=True)

inputs = random_variables.simulation_inputs()
inputs.rv_type = ric + ' | real time' 
#options : standard_normal normal student uniform exponential chi-squared
inputs.decimals = 5

# computations
sim = random_variables.simulator(inputs)
sim.vector = t['return_close'].values
sim.inputs.size = len(sim.vector)
sim.str_title = sim.inputs.rv_type
sim.compute_stats()
sim.plot()
x = sim.vector




