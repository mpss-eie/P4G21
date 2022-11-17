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

def psd(datos_df, hora):
   
    # Protección contra errores
    if (hora < 0) or (hora > 23):
        error = 'El programa está trabajando con valores inválidos de tiempo.'
        return error
    else:
        # Crea un dataframe para una hora especifica con los datos brindados
        def datos_hora(hora):
            if hora > 9:
                hora = '{}:00:00.0'.format(hora)
            else:
                hora = '0{}:00:00.0'.format(hora)
            consumo_pot = datos_df[datos_df['fechaHora'].str.contains(hora)]
            del consumo_pot['MW_P']
            return consumo_pot
        # En esta parte se crea una función muestra para una hora determinada que representa la
        # densidad espectral de potencia
        muestra = datos_hora(hora).assign(Index=
                        range(len(datos_hora(hora)))).set_index('Index')['MW']
        # Se grafica la funcion muestra con 800 puntos
        plt.psd(muestra, 800, 1./0.01)
        plt.xlabel('Frecuencia')
        plt.ylabel('Densidad Espectral')
        plt.show()
        return 'Se muestra la gráfica de la densidad espectral'
    
    