# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 14:45:31 2023

@author: LENOVO
"""
#alt92 = \ #alt94 = ^  #at124 = |  

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as st
import importlib

# import our own files and reload
import capm
importlib.reload(capm)

#inputs
benchmark = '^SPX' #x
security = 'GOOG' #y

# initialice class capm
model = capm.model(benchmark, security)
model.synchronise_timeseries()
#model.plot_timeseries()
model.compute_linear_regression()
model.plot_linear_regression()









