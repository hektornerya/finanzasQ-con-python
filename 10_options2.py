# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 17:15:34 2023

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
import options2
importlib.reload(options2)

inputs = options2.inputs()
inputs.price = 36820 # S
inputs.time = 0 # t
inputs.maturity = 1 # T
inputs.strike = 30000 # K
inputs.interest_rate = .0453 # r (BONO USA 10Y)
inputs.volatility = 0.556 # sigma
inputs.type = 'call'
inputs.monte_carlo_size = 10**6

option_mgr = options2.manager(inputs)
option_mgr.compute_black_scholes_price()
option_mgr.compute_monte_carlo_price()
option_mgr.plot_histogram()





    