# librerías
import json
import requests
import pandas as pd
from pandas import json_normalize
from fitter import Fitter
import numpy as np
from scipy import stats
from scipy.stats import gamma
import matplotlib.pyplot as plt

# Se crea un dataframe para una hora específica con los datos brindados


def datos_hora(datos_df, hora):
    """Función datos_hora.

    Esta función se encarga de obtener los datos de consumo de
    una determinada hora.

    Parameters:
    ----------
    datos_df : dataFrame
         Se consideran los datos de consumo de energía
    hora : ingreso manual de la hora a analizar
         Se consideran los datos de consumo de energía
         de una hora específica.
    """
    # Se obtiene el consumo de la primera hora específica.
    datos_t1 = []
    for i in range(hora, len(datos_df.index), 24):
        datos_t1.append(float(datos_df.MW[i]))

    return datos_t1


def psd(datos_df, hora):
    """Función psd.

    Esta función se encarga de obtener la densidad espectral de
    potencia para una función muestra en una secuencia aleatoria.

    Parameters:
    ----------
    datos_df : dataFrame
         Se consideran los datos de consumo de energía
    hora : ingreso manual de la hora a analizar
         Se consideran los datos de consumo de energía
         de una hora específica.
    """
    # Protección contra errores
    if (hora < 0) or (hora > 23):
        error = 'El programa presenta valores inválidos de tiempo '
        return error
    else:
        # En esta parte se crea una función muestra para una hora
        # determinada que representa la
        # densidad espectral de potencia
        muestra = datos_hora(datos_df, hora)
        # Se grafica la función muestra con 800 puntos
        plt.psd(muestra, 800, 1./0.01)
        plt.title('Densidad Espectral de Potencia')
        plt.xlabel('Frecuencia (Hz)')
        plt.ylabel('Densidad Espectral')
        plt.show()
        return 'Se muestra la gráfica de la densidad espectral'
