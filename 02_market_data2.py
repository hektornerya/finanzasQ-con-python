# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 17:21:57 2024

@author: LENOVO
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as st
import importlib

#import our own files and reload
import random_variables2
importlib.reload(random_variables2)
import market_data2
importlib.reload(market_data2)

# inputs
directory = 'C:\\Users\\LENOVO\\.spyder-py3\\2024-1\\data2\\' #hardcode
ric = '^MXX'

# computations
dist = market_data2.distribution(ric)
dist.load_timeseries()
dist.plot_timeseries()
dist.compute_stats()
dist.plot_histogram()



#['^MXX','^SPX','^IXIC','^STOXX','^GDAXI','^FCHI','^VIX',\
#'XLK','XLF','XLV','XLP','XLY','XLE','XLI','XLB','XLRE','XLU','XLC',\
 #'SPY','EWW','RSP',\
  #'IVW','IVE','QUAL','MTUM','SIZE','USMV',\
   #'AAPL','MSFT','NVDA','AMZN','GOOG','META','NFLX','TSLA',\
    #'BRK-B','JPM','V','MA','BAC','MS','GS','BLK',\
     #'LLY','JNJ','PG','MRK','ABBV','PFE','UNH','TMO','ABT','AMGN','DHR','BMY',\
      #'EURUSD=X','GBPUSD=X','CHFUSD=X','SEKUSD=X','NOKUSD=X','JPYUSD=X','MXNUSD=X']