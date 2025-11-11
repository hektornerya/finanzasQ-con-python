# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 18:14:58 2024

@author: LENOVO
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as st
import importlib
import scipy.optimize as op

# import our own files and reload
import capm2
importlib.reload(capm2)

#inputs
position_security = 'PG'
position_delta_usd = 10 # in mn USD
benchmark = 'PG'
#hedge_securities = ['AAPL','MSFT']
#hedge_universe = ['AAPL','MSFT','NVDA','AMZN','GOOG','META','NFLX','SPY','XLK','XLF']
#hedge_universe = ['BRK-B','JPM','V','MA','BAC','MS','GS','BLK','SPY','XLF']
hedge_universe = ['PG','^SPX','XLK','XLV','XLP','XLY','XLE','XLI','XLF']
regularisation = 0.0

# compuet correlations
df = capm2.dataframe_correl_beta(benchmark, position_security, hedge_universe)

# computations
hedge_securities = ['MA','SPY']
hedger = capm2.hedger(position_security, position_delta_usd, benchmark, hedge_securities)
hedger.compute_betas()
hedger.compute_hedge_weights(regularisation)

# variables
hedge_weights = hedger.hedge_weights
hedge_delta_usd = hedger.hedge_delta_usd
hedge_beta_usd = hedger.hedge_beta_usd





