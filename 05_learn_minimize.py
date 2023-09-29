# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 12:00:27 2023

@author: LENOVO
"""
#alt92 = \ #alt94 = ^  #at124 = |  

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as st
import scipy.optimize as op
import importlib

# define the function to minimise
#def cost_function(x):
#    f = (x[0] - 7.0)**2 + (x[1] + 5)**2 + (x[2] - 13)**2
#   return f

# initialize optimisation
#x0 = np.zeros([3,1])

# compute optimisation
#optimal_result = op.minimize(fun=cost_function, x0=x0)

#print
#print('------')
#print('Optimisation Result: ')
#print(optimal_result)


# define the function to minimise
def cost_function(x, roots, coeffs):
    f = 0
    for n in range(len(x)):
        f += coeffs[n]*(x[n] - roots[n])**2
    return f

# input parameters
dimensions = 5
roots = np.random.randint(low=-20, high=20, size=dimensions)
coeffs = np.ones([dimensions,1])

# initialize optimisation
x0 = np.zeros([dimensions,1])

# compute optimisation
optimal_result = op.minimize(fun=cost_function, x0=x0, args=(roots,coeffs))

#print
print('------')
print('Optimisation Result: ')
print(optimal_result)
print('------')
print('Roots: ')
print(roots)   
print('------')