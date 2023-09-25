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

# import our own files and reload
import capm
importlib.reload(capm)

#inputs
position_security = 'GOOG'
position_delta_usd = 15 # in mn USD
benchmark = '^SPX'
hedge_securities = ['AAPL', 'MSFT']

hedger = capm.hedger(position_security, position_delta_usd, benchmark, hedge_securities)
hedger.compute_betas()
hedger.compute_hedge_weights()
