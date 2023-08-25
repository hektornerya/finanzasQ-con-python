# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import pandas as pd
import matplotlib as mpl
import scipy
import matplotlib.pyplot as plt

degrees_freedom = 5
size = 10**6
random_variable_type = 'student' # normal student variable

if random_variable_type == 'normal':
    x = np.random.standard_normal(size=size)
elif random_variable_type == 'student':
    x = np.random.standard_t(df=degrees_freedom, size=size)
#x = np.random.uniform(low=0.0, high=1.0, size=size)

mpl.pyplot.figure()
plt.hist(x, bins=100)
plt.title(random_variable_type)
plt.show()

