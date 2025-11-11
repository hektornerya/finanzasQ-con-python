# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 14:34:56 2024

@author: LENOVO
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as st
import importlib

# import our own files and reload
import capm2
importlib.reload(capm2)

#inputs
security = 'JPM' #y
factors = ['^SPX','IVW','IVE','QUAL','USMV','MTUM','SIZE',\
           'XLK','XLF','XLV','XLP','XLY','XLI','XLC','XLU']

# initialice class capm
df = capm2.dataframe_factors(security, factors)



# LAS CORRELACIONES NOS DICEN QUE FACTORES AFECTAN AL ACTIVO
# LOS BETAS NOS DICEN CUANTO AFECTA CADA FACTOR AL RENDIMIENTO DEL ACTIVO