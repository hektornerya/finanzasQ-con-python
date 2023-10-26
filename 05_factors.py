# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 16:07:21 2023

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
security = 'HLF' #y
factors = ['^SPX','IVW','IVE','QUAL','USMV','MTUM','SIZE',\
           'XLK','XLF','XLV','XLP','XLY','XLI','XLC','XLU']

# initialice class capm
df = capm.dataframe_factors(security, factors)
