# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 16:10:42 2023

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
import market_data2
importlib.reload(market_data2)
import capm2
importlib.reload(capm2)
import portfolio2
importlib.reload(portfolio2)

# inputs
notional = 15 # in mn USD
universe = ['^MXX','^SPX','^IXIC','^STOXX','^GDAXI','^FCHI','^VIX',\
            'XLK','XLF','XLV','XLP','XLY','XLE','XLI','XLB','XLRE','XLU',\
            'SPY','EWW',\
            'IVW','IVE','QUAL','MTUM','SIZE','USMV',\
            'AAPL','MSFT','NVDA','AMZN','GOOG','META','NFLX',\
            'BRK-B','JPM','V','MA','BAC','MS','GS','BLK',\
            'LLY','JNJ','PG','MRK','ABBV','PFE',\
            'BTC-USD','ETH-USD','SOL-USD','USDC-USD','USDT-USD','DAI-USD',\
            'EURUSD=X','GBPUSD=X','CHFUSD=X','SEKUSD=X','NOKUSD=X','JPYUSD=X','MXNUSD=X']
rics = random.sample(universe, 10)

#rics = ['^MXX','^SPX','^IXIC','^STOXX','^GDAXI']
#rics = ['XLK','XLF','XLV','XLP','XLY','XLE','XLI','XLB','XLRE','XLU']
#rics = ['IVW','IVE','QUAL','MTUM','SIZE','USMV']
#rics = ['AAPL','MSFT','NVDA','AMZN','GOOG','META','NFLX']
#rics = ['BRK-B','JPM','V','MA','BAC','MS','GS','BLK']
#rics = ['LLY','JNJ','PG','MRK','PFE']
#rics = ['BTC-USD','ETH-USD','SOL-USD','USDC-USD','USDT-USD','DAI-USD']
#rics = ['BTC-USD','ETH-USD','SOL-USD']
#rics = ['USDC-USD','USDT-USD','DAI-USD']
#rics = ['AAPL','MSFT','NVDA','AMZN','GOOG','META','NFLX',\
#        'BRK-B','JPM','V','MA','BAC','MS','GS','BLK',\
#        'LLY','JNJ','PG','MRK','ABBV','PFE']
rics = ['XLC','XLU','QUAL','BTC-USD','XLY','NOKUSD=X','XLB','^GDAXI','GOOG','CHFUSD=X']
#rics = universe
#rics = ['ADBE','LLY','HD','TSM','AMD','ASML','CRM','NVDA','AMZN','GOOG','MSFT','AAPL']   # Ken Fisher Portfolio


# efficient frontier
target_return = 0.075 # 0.075 or None
include_min_variance = True #False or True
dict_portfolios = portfolio2.compute_efficient_frontier(rics, notional, target_return, include_min_variance)
print(rics)

dict_portfolios['markowitz_target'].plot_histogram()



