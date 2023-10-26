# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 15:59:42 2023

@author: LENOVO
"""
#alt92 = \ #alt94 = ^  #at124 = |  

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as st
import importlib

# import our own files and reload
import market_data
importlib.reload(market_data)
import capm
importlib.reload(capm)

#rics = ['^MXX','^SPX','BTC-USD','MXNUSD=USD',\
#        'XLK','XLF','XLV','XLP','XLY','XLE','XLI']
#rics = ['^MXX','^SPX','^IXIC','^STOXX','^GDAXI','^FCHI','^VIX',\
#        'BTC-USD','ETH-USD','SOL-USD','USDC-USD','USDT-USD','DAI-USD']
#rics = ['AAPL','MSFT','NVDA','AMZN','GOOG','META','NFLX',\
#        'BRK-B','JPM','V','MA','BAC','MS','GS','BLK',\
 #       'LLY','JNJ','PG','MRK','ABBV','PFE']
# amos, militares, 5big
rics = ['^MXX','^SPX','^IXIC','^STOXX','^GDAXI','^FCHI','^VIX',\
        'AAPL','MSFT','AMZN','GOOG','MCD',\
        'VTI','JPM','MS','STT','BLK',\
        'NOC','LMT','GD','RTX'] 
#rics = ['BTC-USD','ETH-USD','SOL-USD','USDC-USD','USDT-USD','DAI-USD']
#rics = ['^SPX','IVW','IVE','QUAL','MTUM','SIZE','USMV',\
#        'XLK','XLF','XLV','XLP','XLY','XLE','XLI']  

# SYNCHRONISE all the time series of returns
df = market_data.synchronise_returns(rics)

# compute the variance-covariance and correlation matrices
mtx = df.drop(columns=['date'])
mtx_var_covar = np.cov(mtx, rowvar=False) * 252
mtx_correl = np.corrcoef(mtx, rowvar=False)

# unitary test for correlation
#correl = capm.compute_correlation('XLK','XLF')

#compute eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eigh(mtx_var_covar)
variance_explained = eigenvalues / np.sum(eigenvalues)
prod = np.matmul(eigenvectors, np.transpose(eigenvectors))

######################################
#PCA for 2D visualisation
######################################

#compute min and max volatilities
volatility_min = np.sqrt(eigenvalues[0])
volatility_max = np.sqrt(eigenvalues[-1])

#compute PCA base for 2D visualisation
pca_vector_1 = eigenvectors[:,-1]
pca_vector_2 = eigenvectors[:,-2]
pca_eigenvalue_1 = eigenvalues[-1]
pca_eigenvalue_2 = eigenvalues[-2]
pca_variance_explained = variance_explained[-2:].sum()

#compute min variance portfolio
min_var_vector = eigenvectors[:,0]
min_var_eigenvalue = eigenvalues [0]
min_var_variance_explained = variance_explained[0]



#df = pd.DataFrame()
#dic_timeseries = {}
#timestamps = []
# get intersection of all timestamps
#for ric in rics:
#    t = market_data.load_timeseries(ric)
#    dic_timeseries[ric] = t
#    if len(timestamps) == 0:
#        timestamps = list(t['date'].values)
#    temp_timestamps = list(t['date'].values)
#    timestamps = list(set(timestamps) & set(temp_timestamps))
# SYNCHRONISE all the time series
#for ric in dic_timeseries:
#    t = dic_timeseries[ric]
#    t = t[t['date'].isin(timestamps)]
#   t = t.sort_values(by='date', ascending=True)
#    t = t.dropna()
#    t = t.reset_index(drop=True)
 #   dic_timeseries[ric] = t
#    if df.shape[1] == 0:
#        df['date'] = timestamps
#    df[ric] = t['return']
    
  
  

