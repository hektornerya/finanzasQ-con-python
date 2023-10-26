# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 17:12:00 2023

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

# create offline instances of pca model
notional = 10 # in mn USD
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


#rics = ['^MXX','^SPX','BTC-USD','MXNUSD=USD',\
#        'XLK','XLF','XLV','XLP','XLY','XLE','XLI']
#rics = ['^MXX','^SPX','^IXIC','^STOXX','^GDAXI','^FCHI','^VIX',\
#        'BTC-USD','ETH-USD','SOL-USD','USDC-USD','USDT-USD','DAI-USD']
#rics = ['AAPL','MSFT','NVDA','AMZN','GOOG','META','NFLX',\
#        'BRK-B','JPM','V','MA','BAC','MS','GS','BLK',\
 #       'LLY','JNJ','PG','MRK','ABBV','PFE']
# amos, militares, 5big
#rics = ['^MXX','^SPX','^IXIC','^STOXX','^GDAXI','^FCHI','^VIX',\
#        'AAPL','MSFT','AMZN','GOOG','MCD',\
#        'VTI','JPM','MS','STT','BLK',\
#        'NOC','LMT','GD','RTX'] 
#rics = ['BTC-USD','ETH-USD','SOL-USD','USDC-USD','USDT-USD','DAI-USD']
#rics = ['^SPX','IVW','IVE','QUAL','MTUM','SIZE','USMV',\
#        'XLK','XLF','XLV','XLP','XLY','XLE','XLI']  


df = market_data.synchronise_returns(rics)
mtx = df.drop(columns=['date'])
mtx_var_covar = np.cov(mtx, rowvar=False) * 252
mtx_correl = np.corrcoef(mtx, rowvar=False)

#min-var with eigenvectors
eigenvalues, eigenvectors = np.linalg.eigh(mtx_var_covar)
min_var_vector = eigenvectors[:,0]

#unit test for variance function
variance_1 = np.matmul(np.transpose(min_var_vector), np.matmul(mtx_var_covar,min_var_vector))

###########################################################
# min-var with eigenvectors
###########################################################

np.matmul(eigenvectors, np.transpose(eigenvectors))


# initial condition
def portfolio_variance(x, mtx_var_covar):
    variance = np.matmul(np.transpose(x), np.matmul(mtx_var_covar,x))
    return variance

#variance_2 = portfolio_variance(min_var_vector, mtx_var_covar)

# compute optimisation
x0 = [notional / len(rics)] * len(rics)
l2_norm = [{"type": "eq", "fun": lambda x: sum(x**2) - 1}]   # unitary in norm L2
l1_norm = [{"type": "eq", "fun": lambda x: sum(abs(x)) - 1}]   # unitary in norm L1
optimal_result = op.minimize(fun=portfolio_variance, x0=x0,\
                             args=(mtx_var_covar),\
                                 constraints=l2_norm)
optimize_vector = optimal_result.x
variance_2 = optimal_result.fun

df_weights = pd.DataFrame()
df_weights['rics'] = rics
df_weights['min_var_vector'] = min_var_vector
df_weights['optimize_vector'] = optimize_vector


