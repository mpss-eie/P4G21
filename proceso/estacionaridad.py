import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import adfuller


def wss(A0):
    '''Función wss().

    Esta funcion determina la estacionaridad en sentido amplio
    de una secuencia aleatorea, manteniedo los valores validos
    en un factor del 5% de diferencia

    Parameters:
    ----------
    A0                  : DataFrame
        Datos de consumo de potencia.
    DF_DICKEYFULLER     : Dta frame
        Valores de prueba de DickeyFuller para estacionaridad.
    DF_SALIDA           : Data frame
        Contiene los valores finales de las pruebas.
    '''
    print("============Modulo Estacionaridad :=============")
    print("=======Estacionaridad en sentido amplio:========")
    print("----------Resultados de Dickey-fuller:----------")
    DF_DICKEYFULLER = adfuller(A0, autolag='AIC')
    DF_SALIDA = pd.Series(DF_DICKEYFULLER[0:4], index=[
                          'Test Statistic', 'p-value', '#lags used', 'number of observations used'])
    for key, value in DF_DICKEYFULLER[4].items():
        DF_SALIDA['critical value (%s)' % key] = value

    if (DF_SALIDA[5] < DF_SALIDA[0]):
        print('Serie temporal no estacionaria en setido amplio.\n\tTest estático:\t',
              DF_SALIDA[0], '\n\t5%:\t\t', DF_SALIDA[5])
    else:
        print('Serie temporal estacionaria en setido amplio.')
    return '------------------------------------------------'


def prom_temporal(C, A0):
    '''Función prom_temporal().

    Esta funcion determina el promedio temporal para los valores
    de consumo MW, se calcula tanto el vcalor numerico sujeto a 
    la funcion 'C' como el vector de promedio temporal para el
    data frame de las horas.

    Parameters:
    ----------
    C                   : list
        Secuencia aleatoria de consumo de MW.
    A0                  : DataFrame
        Datos de consumo de potencia.
    PROMEDIO_TEMPORAL_ADD: Dta frame
        Almacena los valores para el nuevo vector de A0.
    PROMEDIO_TEMPORAL   : float
        Valor numérico del promedio temporal para la funcion 'C.
    '''
    print("===============Promedio temporal:===============")
    A0['fechaHora'] = pd.to_datetime(A0['fechaHora'])
    A0 = A0.sort_values(by='fechaHora')
    PROMEDIO_TEMPORAL_ADD = A0['MW'].rolling(7).mean()
    A0['Promedio_Temporal'] = PROMEDIO_TEMPORAL_ADD

    PROMEDIO_TEMPORAL = np.convolve(C, np.ones(8), 'valid')/8

    return float(PROMEDIO_TEMPORAL), A0


def ergodicidad(A0, PROMEDIO_TEMPORAL):
    '''Función ergodicidad().

    Esta funcion determina la ergodicidad de la secuencia aleatoria 
    del consumo de MW que está en A0, utiliza el promedio temporal 
    calculado anteriormente y mantiene los valores validos dentro
    del 5% de error.

    Parameters:
    ----------
    A0                  : DataFrame
        Datos de consumo de potencia.
    PROMEDIO_TEMPORAL   : DataFrame
        Data frame con los valor calculados para el promedio temporal,
        almacenados en PROMEDIO_TEMPORAL['Promedio_Temporal'].
    PROMEDIO_TEMPORAL_MEAN: int
        Valor promedio del vector PROMEDIO_TEMPORAL['Promedio_Temporal'].
    MEDIA_ESTADAR       : int
        ALmacena el valor de la media estandar para comprar el error con
        el promedio temporal.
    PORCENTAJE_ERROR    : int
        Valor del porcentaje de error, que debe ser menor a 5%.
    '''
    print("====================Ergodicidad:================")
    # Calcular el promedio estadístico:
    MEDIA_ESTANDAR = np.mean(A0['MW'])

    PROMEDIO_TEMPORAL_MEAN = PROMEDIO_TEMPORAL['Promedio_Temporal'].mean()

    # Porcentaje de error:
    PORCENTAJE_ERROR = abs(MEDIA_ESTANDAR-PROMEDIO_TEMPORAL_MEAN)
    print(PORCENTAJE_ERROR)
    if PORCENTAJE_ERROR < 0.5:
        print('-------------El proceo es ergódico-------------')
    else:
        print('------------El proceso no es ergódico----------')
    return '------------------------------------------------'
