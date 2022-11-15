import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import adfuller

def wss(A0):
    print("============Modulo Estacionaridad :=============")
    print("=======Estacionaridad en sentido amplio:========")
    print("----------Resultados de Dickey-fuller:----------")
    DF_DICKEYFULLER = adfuller(A0, autolag='AIC')
    DF_SALIDA = pd.Series(DF_DICKEYFULLER[0:4], index = ['Test Statistic','p-value','#lags used','number of observations used'])
    for key, value in DF_DICKEYFULLER[4].items():
        DF_SALIDA['critical value (%s)'%key]= value
    
    if (DF_SALIDA[5] < DF_SALIDA[0]):
        print('Serie temporal no estacionaria en setido amplio.\n\tTest estático:\t',DF_SALIDA[0],'\n\t5%:\t\t',DF_SALIDA[5])
    else:
        print('Serie temporal estacionaria en setido amplio.')
    return '------------------------------------------------'

def prom_temporal(C,A0):
    print("===============Promedio temporal:===============")
    A0['fechaHora'] = pd.to_datetime(A0['fechaHora'])
    A0 = A0.sort_values(by='fechaHora')
    PROMEDIO_TEMPORAL_ADD = A0['MW'].rolling(7).mean()
    A0['Promedio_Temporal'] = PROMEDIO_TEMPORAL_ADD

    PROMEDIO_TEMPORAL = np.convolve(C, np.ones(8), 'valid')/8

    return float(PROMEDIO_TEMPORAL), A0

def ergodicidad(A0):
    print(A0.head())
  
    return '------------------------------------------------'