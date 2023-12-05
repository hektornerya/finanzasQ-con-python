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
import market_data
importlib.reload(market_data)
import options
importlib.reload(options)

inputs = options.inputs()
inputs.price = 36820 # S
inputs.time = 0 # t
inputs.maturity = 1 # T
inputs.strike = 30000 # K
inputs.interest_rate = .0453 # r (BONO USA 10Y)
inputs.volatility = 0.556 # sigma
inputs.type = 'call'

option_mgr = options.manager(inputs)
option_mgr.compute_black_scholes_price()
option_mgr.compute_monte_carlo_price()