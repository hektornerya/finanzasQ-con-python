# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 12:30:56 2023

@author: LENOVO
"""
#alt92 = \ #alt94 = ^  #at124 = |  

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as st
import importlib
import random
import scipy.optimize as op

# import our own files and reload
import market_data
importlib.reload(market_data)
import capm
importlib.reload(capm)
import portfolio
importlib.reload(portfolio)

# inputs
notional = 15 # in mn USD
universe = ['^MXX','^SPX','^IXIC','^STOXX','^GDAXI','^FCHI','^VIX',\
            'XLK','XLF','XLV','XLP','XLY','XLE','XLI',\
            'SPY','EWW',\
            'IVW','IVE','QUAL','MTUM','SIZE','USMV',\
            'AAPL','MSFT','NVDA','AMZN','GOOG','META','NFLX',\
            'BRK-B','JPM','V','MA','BAC','MS','GS','BLK',\
            'LLY','JNJ','PG','MRK','ABBV','PFE',\
            'BTC-USD','ETH-USD','SOL-USD','USDC-USD','USDT-USD','DAI-USD',\
            'EURUSD=X','GBPUSD=X','CHFUSD=X','SEKUSD=X','NOKUSD=X','JPYUSD=X','MXNUSD=X']
rics = random.sample(universe, 30)

print(rics)

# initialice de instance of the class
port_mgr = portfolio.manager(rics, notional)

# compute correlation and variance-covariance matrix
port_mgr.compute_covariance()

# compute the desired portfolio: output class = portfolio.output
port_min_variance_l1 = port_mgr.compute_portfolio('min-variance-l1')
port_min_variance_l2 = port_mgr.compute_portfolio('min-variance-l2')
port_equi_weight = port_mgr.compute_portfolio('equi-weight')
port_long_only = port_mgr.compute_portfolio('long-only')
port_markowitz = port_mgr.compute_portfolio('markowitz', target_return=None)

# plot the histograms of returns for teh desired portfolio
port_min_variance_l1.plot_histogram()
port_min_variance_l2.plot_histogram()
port_long_only.plot_histogram()
port_equi_weight.plot_histogram()
port_markowitz.plot_histogram()




# return target
#return_portfolio_long_only = np.round(port_mgr.returns.dot(port_long_only.weights),6)
#return_portfolio_equi_weight = np.round(port_mgr.returns.dot(port_equi_weight.weights),6)
#return_portfolio_markowitz = np.round(port_mgr.returns.dot(port_markowitz.weights),6)



#df = pd.DataFrame()
#df['rics'] = rics
#df['returns'] = port_mgr.returns
#df['volatilities'] = port_mgr.volatilities
#df['markowitz_weights'] = port_markowitz.weights
#df['markowitz_allocation'] = port_markowitz.allocation
#df['min_variance_weights'] = port_min_variance_l1.weights
#df['min_variance_allocation'] = port_min_variance_l1.allocation
#df['equi_weight_weights'] = port_equi_weight.weights
#df['equi_weight_allocation'] = port_equi_weight.allocation
#df['long_only_weights'] = port_long_only.weights
#df['long_only_allocation'] = port_long_only.allocation








