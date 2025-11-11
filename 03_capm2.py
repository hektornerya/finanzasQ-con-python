# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 12:15:52 2024

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
benchmark = '^SPX' #x
security = 'TDG' #y

# initialice class capm
model = capm2.model(benchmark, security)
model.synchronise_timeseries()
model.plot_timeseries()
model.compute_linear_regression()
model.plot_linear_regression()



# FACTORES DE CRECIMIENTO
# PRIMER CIRTERIO  CORRELACION
# CORREL ES EL POTENCIAL DE CRECIMIENTO (IVW) QUE ACTIVO DE VALOR (IVE)
# SEGUND CRITERIO  BETA (el beta es una corelacion pondearada por volatilidad)
# EL BETA DE UN ACTIVO ES UN PROXY DE SU NIVEL DE RIESGO
# BETA MAYOR QUE UNO amplifica las ganancias
# BETA MENOR QUE UNO disminuye las gnancias pero amortiguan las perdidas
# MIENTRAS MAS GRANDE SERA EL BETA MAYORES SERAN EL RIESGO Y EL RENDIMIENTO
