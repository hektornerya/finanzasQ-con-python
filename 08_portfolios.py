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
rics = random.sample(universe, 5)

# initialice de instance of the class
port_mgr = portfolio.manager(rics, notional)

# compute correlation and variance-covariance matrix
port_mgr.compute_covariance()

# compute the desired portfolio: output class = portfolio.output
port_min_variance_l1 = port_mgr.compute_portfolio('min_variance_l1')
port_min_variance_l2 = port_mgr.compute_portfolio('min_variance_l2')
port_equi_weight = port_mgr.compute_portfolio('equi_weight')



