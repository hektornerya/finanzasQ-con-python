# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 11:39:55 2024

@author: LENOVO
"""

import yfinance as yf
import pandas as pd
import os
from datetime import datetime, timedelta
import time  # Importa la librería time

# Lista de tickers de las empresas
#tickers = ['AAPL', 'MSFT', 'GOOG','NVDA','META','NFLX','TSLA','AMZN']  # Puedes agregar más tickers a esta lista
#tickers = ['^MXX','^SPX','^IXIC','^STOXX','^GDAXI','^FCHI','^VIX']
#tickers = ['XLK','XLF','XLV','XLP','XLY','XLE','XLI','XLB','XLRE','XLU','XLC']
#tickers = ['LLY','JNJ','PG','MRK','ABBV','PFE','UNH','TMO','ABT','AMGN','DHR','BMY'] #healthcare
#tickers = ['BTC-USD','ETH-USD','SOL-USD','USDC-USD','USDT-USD','DAI-USD']
#tickers = ['EURUSD=X','GBPUSD=X','CHFUSD=X','SEKUSD=X','NOKUSD=X','JPYUSD=X','MXNUSD=X']
#tickers = ['BRK-B','JPM','V','MA','BAC','MS','GS','BLK'] #financieros
#tickers = ['VTI','BLK','STT','MS','JPM'] #amos del mundo
#tickers = ['SPY','EWW','RSP'] #ETF trackers
#tickers = ['IVW','IVE','QUAL','USMV','MTUM','SIZE'] #ETF factors blackrock
#tickers = ['000001.SS','^N225','^HSI','^NSEI','^KS11','^DJI','^NYA'] #indices especiales
#tickers = ['WWD','NOC','LHX','HWM','LMT','HEI','BA','GD','RTX','TDG'] #aerospacedefense
#tickers = ['ORCL','AMAT','INTC','TSLA','AAPL','GOOG','NVDA','META','MSFT','AMZN'] #10 Ai stock upside potential
#tickers = ['LMT','IBM','TXN','ADP','AMT','PEP','KO','PM','VZ','TGT','HD','NEE','JNJ','XOM','SPGI'] #best stock for dividends
#tickers = ['PLTR','DDD','EXPE','IBM'] individuales
#tickers = ['PXLW','BWEN','CARM','BLNK'] #Top Undervalued Nasdaq Stock
#tickers = ['^MXX','^SPX','^IXIC','^STOXX','^GDAXI','^FCHI','^VIX',\
#tickers =['XLK','XLF','XLV','XLP','XLY','XLE','XLI','XLB','XLRE','XLU','XLC',\
#            'SPY','EWW','RSP',\
#            'IVW','IVE','QUAL','MTUM','SIZE','USMV',\
#            'AAPL','MSFT','NVDA','AMZN','GOOG','META','NFLX','TSLA',\
#            'BRK-B','JPM','V','MA','BAC','MS','GS','BLK',\
#            'LLY','JNJ','PG','MRK','ABBV','PFE','UNH','TMO','ABT','AMGN','DHR','BMY',\
#            'BTC-USD','ETH-USD','SOL-USD','USDC-USD','USDT-USD','DAI-USD',\
#            'EURUSD=X','GBPUSD=X','CHFUSD=X','SEKUSD=X','NOKUSD=X','JPYUSD=X','MXNUSD=X']
#tickers = ['MTDR','PR','MUR','CIVI','CHRD','CLMT','AR','EQT','CTRA','MRO','SWN',\
 #           'CHK','FANG','HES','DVN','EOG','OXY','COP','CVX']
tickers = ['AA','AIG','AXP','BA','C','CAT','DD','DIS','GE','GM','HD','HON',\
          'HPQ','IBM','NTC','JNJ','JPM','KO','MCD','MMM','MO','MRK','MSFT',\
            'PFE','PG','T','UTX','VZ','WMT','XOM']  #CAPMfinancialmodelingSB

# Ruta del directorio donde se guardarán los archivos CSV
#directorio = r"C:\Users\LENOVO\.spyder-py3\2024-1\data2"
# Ruta del directorio donde se guardarán los archivos CSV MONTHLY*****
directorio = r"C:\Users\LENOVO\.spyder-py3\2024-1\data25"

# Crear el directorio si no existe
if not os.path.exists(directorio):
    os.makedirs(directorio)

# Fecha de inicio y fecha de ayer
#fecha_inicio = "2014-05-01"
fecha_inicio = "2021-01-01"
fecha_fin = (datetime.now() - timedelta(1)).strftime("%Y-%m-%d")

# Función para descargar datos históricos y guardarlos en un archivo CSV
def descargar_y_guardar_datos(ticker, directorio,delay_success=5, delay_fail=30):    ## Añadimos un retraso de 2 segundos por defecto
    print(f"Intentando descargar datos para {ticker}...")
# Descargar datos históricos diarios
    #datos = yf.download(ticker, start=fecha_inicio, end=fecha_fin)
# Descargar datos históricos MONTHLY*****
    datos = yf.download(ticker, start=fecha_inicio, end=fecha_fin, interval="1mo")
# Descargar datos históricos YEARLY*****
    #datos = yf.download(ticker, start=fecha_inicio, end=fecha_fin, interval="1y")
    if not datos.empty:
    # Aplanar el MultiIndex de las columnas    
        datos.columns=[f'{col[0]}_{col[1]}' for col in datos.columns]
        # Renombrar las columnas para que sean más limpias
        rename_dict = {
            f'Adj Close_{ticker}': 'Adj Close',
            f'Close_{ticker}': 'Close',
            f'High_{ticker}': 'High',
            f'Low_{ticker}': 'Low',
            f'Open_{ticker}': 'Open',
            f'Volume_{ticker}': 'Volume'
        }
        datos = datos.rename(columns=rename_dict)
        datos = datos.reset_index()  # Convertir la fecha a una columna
        # Guardar en un archivo CSV en el directorio especificado
        archivo_csv = os.path.join(directorio, f"{ticker}.csv")
        datos.to_csv(archivo_csv, index=False)
        print(f"Datos guardados en {archivo_csv}")
    else:
        print(f"No se pudieron descargar datos para {ticker}.")

# Descargar y guardar datos para cada ticker en la lista
for ticker in tickers:
    descargar_y_guardar_datos(ticker, directorio)
    
    

# La media te dice el valor promedio de tu conjunto de datos. 

#En estadística y finanzas, la "volatility" (volatilidad) se refiere a la medida de la variabilidad o dispersión de los retornos de un activo financiero. En términos simples, la volatilidad indica cuánto varían los precios de un activo en un período de tiempo determinado.
#Alta volatilidad: Significa que los precios del activo pueden fluctuar significativamente en un corto período de tiempo, lo cual implica mayor riesgo. Los activos con alta volatilidad pueden ofrecer mayores oportunidades de ganancias, pero también mayores riesgos de pérdidas.
#Baja volatilidad: Indica que los precios del activo cambian de manera más gradual y menos pronunciada. Los activos con baja volatilidad se consideran más seguros, pero generalmente ofrecen menores oportunidades de ganancias rápidas.

#el "skewness" (sesgo o asimetría) mide la asimetría de la distribución de los datos alrededor de su media. Indica si los datos están más concentrados en un lado de la media que en el otro.
#Skewness positivo (asimetría positiva): La cola derecha (valores altos) es más larga o más pronunciada que la cola izquierda (valores bajos). Esto significa que hay una mayor cantidad de valores más bajos y unos pocos valores extremadamente altos. La media será mayor que la mediana.
#Skewness negativo (asimetría negativa): La cola izquierda (valores bajos) es más larga o más pronunciada que la cola derecha (valores altos). Esto significa que hay una mayor cantidad de valores más altos y unos pocos valores extremadamente bajos. La media será menor que la mediana.
#Skewness cero: La distribución es simétrica, lo que significa que las colas a ambos lados de la media son aproximadamente iguales. En este caso, la media, la mediana y la moda son iguales.

#la "kurtosis" es una medida que describe la forma de la distribución de los datos, específicamente la "agudeza" de la curva de la distribución de probabilidad. La kurtosis mide las colas de la distribución en comparación con una distribución normal.
#Kurtosis positiva (leptokúrtica):
#Colas pesadas: Distribuciones con colas más largas y agudas en comparación con una distribución normal.
#Pico alto y estrecho: Indica una mayor concentración de valores cerca de la media y más valores extremos (lejos de la media).
#Kurtosis > 3 (cuando se usa el exceso de kurtosis, entonces > 0).
#Kurtosis negativa (platicúrtica):
#Colas ligeras: Distribuciones con colas más cortas y menos agudas en comparación con una distribución normal.
#Pico bajo y ancho: Indica una menor concentración de valores cerca de la media y menos valores extremos.
#Kurtosis < 3 (cuando se usa el exceso de kurtosis, entonces < 0)
#Kurtosis normal (mesokúrtica):
#Distribución normal: La kurtosis de una distribución normal estándar es 3.
#Colas medianas: Las colas y el pico son "promedio" en comparación con otras distribuciones.
#Kurtosis = 3 (cuando se usa el exceso de kurtosis, entonces = 0).

#El test de Jarque-Bera es una prueba estadística que se utiliza para comprobar si una muestra de datos sigue una distribución normal. La prueba se basa en el análisis de la skewness (asimetría) y la kurtosis (curtosis) de los datos. La idea es comparar la asimetría y la curtosis de los datos con las de una distribución normal, que tiene una skewness de 0 y una kurtosis de 3
#Interpretación
#Valor de JB cercano a 0: Indica que la distribución de los datos es similar a una distribución normal.
#Valor de JB alto: Indica que la distribución de los datos se desvía significativamente de una distribución normal.
#Hipótesis
#Hipótesis nula (H0): Los datos siguen una distribución normal.
#Hipótesis alternativa (H1): Los datos no siguen una distribución normal.
#Procedimiento
#Calcular la skewness y la kurtosis de los datos.
#Calcular el estadístico JB usando la fórmula.
#Comparar el estadístico JB con un valor crítico de la distribución 𝜒2 con 2 grados de libertad, o utilizar el p-valor correspondiente.
#Si el estadístico JB es mayor que el valor crítico o el p-valor es menor que el nivel de significancia (por ejemplo, 0.05), se rechaza la hipótesis nula, indicando que los datos no siguen una distribución normal.
#El test de Jarque-Bera es ampliamente utilizado en análisis de datos y econometría para verificar la normalidad de los datos antes de aplicar modelos estadísticos que asumen normalidad. Es particularmente útil porque se basa en la skewness y la kurtosis, que son características clave de la distribución.
#En resumen, el test de Jarque-Bera es una herramienta eficaz para evaluar la normalidad de una distribución de datos, proporcionando información valiosa sobre la asimetría y la curtosis en comparación con una distribución normal.

#El p-value (valor p) es una medida que se utiliza en la estadística para ayudar a determinar la significancia de los resultados de una prueba de hipótesis. Específicamente, el valor p indica la probabilidad de obtener un resultado tan extremo o más extremo que el observado, suponiendo que la hipótesis nula (𝐻0) sea verdadera.
#interpretación del p-value
#Valor p pequeño (generalmente ≤ 0.05): Indica evidencia en contra de la hipótesis nula, sugiriendo que es poco probable que los resultados observados hayan ocurrido por azar. En este caso, se rechaza la hipótesis nula.
#Valor p grande (> 0.05): Indica evidencia insuficiente en contra de la hipótesis nula, sugiriendo que los resultados observados pueden ser consistentes con el azar. En este caso, no se rechaza la hipótesis nula.
#Ejemplo de Prueba de Hipótesis
#Definir las hipótesis:
#Hipótesis nula (H0): No hay efecto o diferencia (por ejemplo, la media de un grupo es igual a la media de otro grupo).
#Hipótesis alternativa (𝐻1): Hay un efecto o diferencia (por ejemplo, la media de un grupo es diferente a la media de otro grupo).
#Seleccionar un nivel de significancia (𝛼):
#Comúnmente usado 𝛼 es 0.05, lo que significa que hay un 5% de riesgo de rechazar la hipótesis nula cuando es verdadera.
#Realizar la prueba estadística:
#Calcular el estadístico de prueba y el p-value correspondiente.
#Tomar una decisión:
#Si el p-value ≤ 𝛼, rechazar 𝐻0.
#Si el p-value > 𝛼, no rechazar 𝐻0.

#El Sharpe Ratio es una medida utilizada en finanzas para evaluar el rendimiento ajustado por riesgo de una inversión o de una cartera de inversiones. Fue desarrollado por William F. Sharpe y se utiliza ampliamente para comparar la eficiencia de diferentes inversiones.
#Cálculo del Sharpe Ratio
#El Sharpe Ratio se calcula utilizando la siguiente fórmula:
#Sharpe Ratio =(𝑅𝑝−𝑅𝑓)/𝜎𝑝
#Donde:
#𝑅𝑝 es el rendimiento esperado de la cartera o inversión.
#𝑅𝑓 es la tasa libre de riesgo, que es el rendimiento de una inversión considerada libre de riesgo (como los bonos del Tesoro de EE.UU.).
#𝜎𝑝 es la desviación estándar del exceso de rendimiento de la cartera o inversión, que mide la volatilidad o el riesgo.
#Interpretación del Sharpe Ratio
#Valor Positivo Alto: Un Sharpe Ratio alto indica que la inversión ha generado un alto rendimiento ajustado por riesgo. En general, un Sharpe Ratio mayor a 1 es considerado bueno, mayor a 2 es muy bueno, y mayor a 3 es excelente.
#Valor Cercano a Cero: Un Sharpe Ratio cercano a 0 sugiere que la inversión tiene un rendimiento ajustado por riesgo similar al de la tasa libre de riesgo. Esto significa que no hay una ventaja significativa en términos de rendimiento por asumir el riesgo adicional.
#Valor Negativo: Un Sharpe Ratio negativo indica que la inversión ha tenido un rendimiento inferior al de la tasa libre de riesgo. Esto significa que asumir el riesgo adicional de la inversión no ha sido recompensado con rendimientos adecuados.

#El VaR (Value at Risk), o Valor en Riesgo, es una medida estadística utilizada en la gestión de riesgos financieros para estimar la pérdida potencial máxima en el valor de una cartera de inversiones durante un período específico con un nivel de confianza determinado. El VaR al 95% (VaR_95) es un tipo específico de VaR que indica la cantidad máxima que se espera perder con una probabilidad del 95% en un horizonte temporal determinado.
#Cálculo del VaR_95
#El cálculo del VaR puede realizarse utilizando varios métodos, incluyendo el método histórico, el método paramétrico (o de la varianza-covarianza), y el método de simulación de Monte Carlo. Aquí te explico el método paramétrico como ejemplo:
#Método Paramétrico:
#Media (𝜇): Rendimiento promedio de la cartera.
#Desviación Estándar (σ): Volatilidad o riesgo de la cartera.
#Nivel de Confianza (95%): Utilizamos el valor crítico de la distribución normal estándar para el 95%, que es aproximadamente 1.65.
#VaR95 = 𝜇−(1.65⋅𝜎)
#Este cálculo asume que los rendimientos siguen una distribución normal.
#Interpretación del VaR_95
#Definición: El VaR_95 de una cartera es la pérdida máxima que se espera no ser superada con un 95% de confianza durante el horizonte temporal especificado.
#Ejemplo:
#Supongamos que tienes una cartera con un rendimiento promedio diario (𝜇) del 0.1% y una desviación estándar diaria (𝜎) del 2%. El cálculo del VaR_95 diario sería:
#VaR95 = 0.001−(1.65⋅0.02)=0.001−0.033=−0.032
#Esto significa que con un 95% de confianza, la pérdida máxima esperada en un día es del 3.2%.
#Uso Práctico:
#Gestión de Riesgos: Ayuda a los gestores de riesgos a comprender y limitar las pérdidas potenciales.
#Regulaciones: Muchas instituciones financieras están obligadas por regulaciones a mantener suficiente capital para cubrir sus VaR.
#Toma de Decisiones: Permite a los inversores y gestores tomar decisiones informadas sobre la asunción de riesgos.
#Limitaciones del VaR
#Suposiciones de Normalidad: El VaR asume que los rendimientos siguen una distribución normal, lo cual no siempre es cierto, especialmente en eventos extremos.
#No Captura el Riesgo Más Allá del Umbral: El VaR no proporciona información sobre la magnitud de las pérdidas que superen el nivel de confianza.
#Sensibilidad al Horizonte Temporal: El VaR puede variar significativamente dependiendo del horizonte temporal considerado.
#Resumen
#El VaR_95 es una herramienta clave en la gestión de riesgos financieros que proporciona una estimación de la pérdida máxima esperada con un 95% de confianza. Aunque es una medida útil, debe ser complementada con otras herramientas y análisis para una gestión de riesgos completa y precisa.

#El CAPM (Capital Asset Pricing Model) es un modelo financiero utilizado para calcular el rendimiento esperado de un activo financiero, como una acción o un portafolio, basado en el riesgo sistemático o no diversificable que posee. Aquí te explico cómo interpretarlo:
#Componentes del CAPM:
        #Rendimiento Libre de Riesgo (Rf): Es el rendimiento que se obtendría si se invirtiera en un activo libre de riesgo, como bonos del gobierno.
        #Prima de Riesgo del Mercado (Rm - Rf): Es la diferencia entre el rendimiento esperado del mercado y el rendimiento libre de riesgo. Refleja el rendimiento adicional que los inversionistas esperan recibir por asumir el riesgo del mercado.
        #Beta (β): Mide la sensibilidad de un activo en relación con los movimientos del mercado en general. Un beta de 1 implica que el activo se mueve en línea con el mercado. Un beta mayor que 1 indica mayor volatilidad en comparación con el mercado, mientras que un beta menor que 1 indica menor volatilidad.
#Fórmula del CAPM:
    #Rendimiento esperado=Rf+β×(Rm−Rf)Rendimiento esperado=Rf+β×(Rm−Rf)
    #Esta fórmula muestra que el rendimiento esperado de un activo depende del rendimiento libre de riesgo, ajustado por la prima de riesgo del mercado multiplicada por el beta del activo.
#Interpretación del CAPM:
        #Rendimiento Libre de Riesgo (Rf): Es el punto de partida seguro para los inversionistas. Cuanto mayor sea el Rf, mayores serán los rendimientos esperados de todos los activos.
        #Prima de Riesgo del Mercado (Rm - Rf): Refleja el retorno adicional que los inversionistas deben esperar por asumir el riesgo del mercado. Si la economía es incierta, esta prima puede ser más alta.
        #Beta (β): Indica cómo se mueve un activo en relación con el mercado en general. Un beta más alto significa que el activo es más volátil y probablemente tenga mayores retornos esperados.
#Uso práctico:
        #Los inversionistas y gestores de carteras utilizan el CAPM para evaluar si un activo está ofreciendo un rendimiento adecuado dado su riesgo.
        #También se utiliza para calcular el costo de capital de una empresa, necesario para valoraciones y decisiones de inversión.
#En resumen, el CAPM es una herramienta fundamental en las finanzas para estimar el rendimiento esperado de un activo, considerando su riesgo relativo al mercado. Interpretarlo implica comprender cómo cada componente (Rf, Rm - Rf, β) contribuye al cálculo del rendimiento esperado y cómo estos factores afectan las decisiones de inversión.

#La regresión lineal es una técnica estadística que se utiliza para modelar la relación entre una variable dependiente y una o más variables independientes. Aquí te explico cómo se interpreta una regresión lineal:
#Coeficiente de regresión (𝛽): Cada coeficiente de regresión representa el cambio esperado en la variable dependiente por cada unidad de cambio en la variable independiente correspondiente, manteniendo constantes todas las demás variables.
#𝛽0(Intercepto): Este es el valor de la variable dependiente cuando todas las variables independientes son iguales a cero.
#𝛽1,𝛽2,…,𝛽𝑛(Pendientes): Estos son los coeficientes de las variables independientes. Por ejemplo, si 𝛽1=2, significa que por cada unidad adicional en la variable independiente correspondiente, la variable dependiente aumenta en promedio en 2 unidades.
#Valor p (p-value): El valor p de cada coeficiente prueba la hipótesis nula de que el coeficiente es igual a cero (sin efecto). Un valor p bajo (generalmente < 0.05) indica que puedes rechazar la hipótesis nula, sugiriendo que la variable independiente tiene un efecto significativo en la variable dependiente.
#𝑅2(Coeficiente de determinación): Mide la proporción de la varianza en la variable dependiente que puede ser explicada por las variables independientes. Un R2 cercano a 1 indica que el modelo explica bien los datos, mientras que un R2 cercano a 0 indica lo contrario.
#Signo de los coeficientes:
#Positivo: Si el coeficiente es positivo, la variable dependiente aumenta cuando la variable independiente aumenta.
#Negativo: Si el coeficiente es negativo, la variable dependiente disminuye cuando la variable independiente aumenta.
#Errores estándar: Indican la variabilidad de los coeficientes de regresión. Coeficientes con errores estándar pequeños son más precisos.





