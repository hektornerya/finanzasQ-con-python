# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 17:17:21 2023

@author: LENOVO
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as st
import importlib

import market_data
importlib.reload(market_data)  
  
def compute_beta(benchmark, security):
    m = model(benchmark, security)
    m.synchronise_timeseries()
    m.compute_linear_regression()
    return m.beta


class model:
    
    # constructor
    def __init__ (self, benchmark, security, decimals = 6):
        self.benchmark = benchmark
        self.security = security
        self.decimals = decimals
        self.timeseries = None
        self.x = None
        self.y = None
        self.alpha = None
        self.beta = None
        self.p_value = None
        self.null_hypothesis = None
        self.correlation = None
        self.r_squared = None
        self.predictor_linreg = None
        
    def synchronise_timeseries(self):
        self.timeseries = market_data.synchronise_timeseries(self.benchmark, self.security)
        
    def plot_timeseries(self):
        plt.figure(figsize=(12,5))
        plt.title('Timeseries of close price')
        plt.xlabel('Time')
        plt.ylabel('Prices')
        ax = plt.gca()
        ax1 = self.timeseries.plot(kind='line', x='date', y='close_x', ax=ax, grid=True, \
                              color='blue', label=self.benchmark)
        ax2 = self.timeseries.plot(kind='line', x='date', y='close_y', ax=ax, grid=True, \
                                  color='red', secondary_y=True, label=self.security)
        ax1.legend(loc=2)
        ax2.legend(loc=1)
        plt.show()
        
    def compute_linear_regression(self):
        self.x = self.timeseries['return_x'].values
        self.y = self.timeseries['return_y'].values
        slope, intercept, r_value, p_value, std_err = st.linregress(self.x, self.y)
        self.alpha = np.round(intercept, self.decimals)
        self.beta = np.round(slope, self.decimals)
        self.p_value = np.round(p_value, self.decimals)
        self.null_hypothesis = p_value > 0.05 # p_value < 0.05 --> reject null hypothesis
        self.correlation = np.round(r_value, self.decimals) # correlation coefficient
        self.r_squared = np.round(r_value**2, self.decimals) # 
        self.predictor_linreg = intercept + slope*self.x

    def plot_linear_regression(self):
        # plot linear regression
        self.x = self.timeseries['return_x'].values
        self.y = self.timeseries['return_y'].values
        str_self = 'Linear regression | security ' + self.security\
            +' | benchmark ' + self.benchmark + '\n'\
            +'alpha (intercept) ' + str(self.alpha)\
            +' | beta (slope) ' + str(self.beta) + '\n'\
            +'p-value ' + str(self.p_value)\
            +' | null hypothesis ' + str(self.null_hypothesis) + '\n'\
            +'correl (r-value ' + str(self.correlation)\
            +' | r-squared ' + str(self.r_squared)
        str_title = 'Scater plot of returns' + '\n' + str_self
        plt.figure()
        plt.title(str_title)
        plt.scatter(self.x, self.y)
        plt.plot(self.x, self.predictor_linreg, color='green')            
        plt.ylabel(self.security)
        plt.xlabel(self.benchmark)
        plt.grid()
        plt.show()
        
class hedger:
    
    def __init__(self, position_security, position_delta_usd, benchmark, hedge_securities, decimals = 6):
        self.position_security = position_security
        self.position_delta_usd = position_delta_usd
        self.position_beta = None
        self.position_beta_usd = None
        self.benchmark = benchmark
        self.decimals = decimals
        self.hedge_securities = hedge_securities
        self.hedge_betas = []
        self.hedge_weights = None
        self.hedge_delta_usd = None
        self.hedge_beta_usd = None
        
    def compute_betas(self):
        self.position_beta = compute_beta(self.benchmark, self.position_security)   
        self.position_beta_usd = self.position_beta * self.position_delta_usd
        for security in self.hedge_securities:
            beta = compute_beta(self.benchmark, security)
            self.hedge_betas.append(beta)
    
    def compute_hedge_weights(self):
        # exact solution using matrix algebra
        dimensions = len(self.hedge_securities)
        if dimensions != 2:
            print('------')
            print('Cannot compute exact solution because dimensions: ' + str(dimensions) + ' =')
            return
        deltas = np.ones([dimensions])
        mtx = np.transpose(np.column_stack((deltas, self.hedge_betas)))        
        targets = -np.array([[self.position_delta_usd],[self.position_beta_usd]])
        self.hedge_weights = np.linalg.inv(mtx).dot(targets)
        self.hedge_delta_usd = np.sum(self.hedge_weights)
        self.hedge_beta_usd = np.transpose(self.hedge_betas).dot(self.hedge_weights).item()
    
        
        