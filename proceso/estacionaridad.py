import pandas as pd
from statsmodels.tsa.stattools import adfuller

def wss(DF):
    print("============Modulo Estacionaridad :=============")
    print("=======Estacionaridad en sentido amplio:========")
    print("----------Resultados de Dickey-fuller:----------")
    DF_DICKEYFULLER = adfuller(DF['MW'], autolag='AIC')
    DF_SALIDA = pd.Series(DF_DICKEYFULLER[0:4], index = ['Test Statistic','p-value','#lags used','number of observations used'])
    for key, value in DF_DICKEYFULLER[4].items():
        DF_SALIDA['critical value (%s)'%key]= value
    
    if (DF_SALIDA[5] < DF_SALIDA[0]):
        print('Serie temporal no estacionaria en setido amplio.\n\tTest estático:\t',DF_SALIDA[0],'\n\t5%:\t\t',DF_SALIDA[5])
    else:
        print('Serie temporal estacionaria en setido amplio.')
    return '------------------------------------------------'

def prom_temporal():
    return 'Aquí está el promedio temporal.'

def ergodicidad():
    return 'Aquí está la ergodicidad.'