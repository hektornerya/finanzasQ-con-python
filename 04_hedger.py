# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 10:19:18 2023

@author: LENOVO
"""

#alt92 = \ #alt94 = ^  #at124 = |  

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as st
import importlib
import scipy.optimize as op

# import our own files and reload
import capm
importlib.reload(capm)

#inputs
position_security = 'NVDA'
position_delta_usd = 10 # in mn USD
benchmark = 'NVDA'
#hedge_universe = ['AAPL','MSFT','NVDA','AMZN','GOOG','META','NFLX','SPY','XLK','XLF']
hedge_universe = ['NVDA','^SPX','XLK','XLF','XLV','XLP','XLY','XLE','XLI']
regularisation = 0.0

# compuet correlations
df = capm.dataframe_correl_beta(benchmark, position_security, hedge_universe)

# computations
hedge_securities = ['MA','SPY']
hedger = capm.hedger(position_security, position_delta_usd, benchmark, hedge_securities)
hedger.compute_betas()
hedger.compute_hedge_weights(regularisation)

# variables
hedge_weights = hedger.hedge_weights
hedge_delta_usd = hedger.hedge_delta_usd
hedge_beta_usd = hedger.hedge_beta_usd


