# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 15:43:34 2024

@author: LENOVO
"""

import numpy as np
import matplotlib.pyplot as plt

# Configuración de simulación
np.random.seed(42)
n_assets = 4 #10
n_simulaciones = 5000 #10000

# Simulamos rendimientos esperados y matriz de covarianza
rendimientos_esperados = np.random.rand(n_assets) * 0.2   # rendimientos esperados entre 0% y 20%
cov_matrix = np.random.rand(n_assets, n_assets)
cov_matrix = np.dot(cov_matrix, cov_matrix.T)  # para hacerla simétrica y semi-definida positiva
#rendimientos_esperados = 0.05 + np.random.rand(n_assets) * 0.1  # rendimientos esperados entre 0% y 20%
#cov_matrix /= 100  # Reducimos los valores para simular menos volatilidad

# Simulación de portafolios
resultados = np.zeros((3, n_simulaciones))
pesos_portafolios = []

for i in range(n_simulaciones):
    # Generar pesos aleatorios para los activos
    pesos = np.random.random(n_assets)
    pesos /= np.sum(pesos)
    
    # Retorno esperado del portafolio
    retorno_portafolio = np.dot(pesos, rendimientos_esperados)
    
    # Riesgo (desviación estándar) del portafolio
    riesgo_portafolio = np.sqrt(np.dot(pesos.T, np.dot(cov_matrix, pesos)))
    
    # Guardar los resultados
    resultados[0, i] = retorno_portafolio
    resultados[1, i] = riesgo_portafolio
    resultados[2, i] = resultados[0, i] / resultados[1, i]  # Ratio de Sharpe (retorno/riesgo)
    pesos_portafolios.append(pesos)
    
# Frontera eficiente: portafolio con el mejor ratio de Sharpe
indice_mejor_sharpe = np.argmax(resultados[2])
mejor_ret, mejor_riesgo = resultados[0, indice_mejor_sharpe], resultados[1, indice_mejor_sharpe]
mejores_pesos = pesos_portafolios[indice_mejor_sharpe]

# Gráfico de la frontera eficiente
plt.figure(figsize=(10, 6))
plt.scatter(resultados[1, :], resultados[0, :], c=resultados[2, :], cmap='viridis', marker='o')
plt.colorbar(label='Ratio de Sharpe')
plt.scatter(mejor_riesgo, mejor_ret, color='red', marker='*', s=200, label='Mejor portafolio')
plt.title('Frontera Eficiente Simulada')
plt.xlabel('Riesgo (Desviación estándar)')
plt.ylabel('Retorno esperado')
plt.legend()
plt.show()

mejor_ret, mejor_riesgo, mejores_pesos


#Rendimiento esperado: Es la ganancia promedio que se espera obtener de un portafolio, basado en el rendimiento histórico o proyectado de los activos que lo componen
#Riesgo (desviación estándar o volatilidad): Representa la incertidumbre o variabilidad en el rendimiento de un portafolio. Un portafolio más arriesgado puede ofrecer rendimientos más altos, pero también es más impredecible.
#La frontera eficiente se representa gráficamente en un gráfico de riesgo-retorno, donde:
    #El eje X representa el riesgo (volatilidad).
    #El eje Y representa el rendimiento esperado.
#En este gráfico, la curva de la frontera eficiente está formada por aquellos portafolios que ofrecen el mejor rendimiento posible para cada nivel de riesgo. Cualquier portafolio que se encuentre por debajo de esta curva se considera ineficiente porque, para el mismo nivel de riesgo, hay otras combinaciones de activos que pueden ofrecer un mejor retorno.


#Aquí tienes el gráfico de la frontera eficiente simulada. La estrella roja representa el portafolio con el mejor ratio de Sharpe (es decir, el mejor retorno ajustado por riesgo).
    #Retorno esperado del mejor portafolio: 14.01%
    #Riesgo (desviación estándar): 81.85%
    #Pesos del mejor portafolio (distribución entre los 4 activos):
        #Activo 1: 1.54%
        #Activo 2: 8.08%
        #Activo 3: 57.55%
        #Activo 4: 32.83%