
from proceso import proceso, momentos, estacionaridad, espectro

#----------Importamos las bibliotecas necesarias:----------
import requests
import json
import pandas as pd
import csv
import numpy as np
import matplotlib.pyplot as plt

from fitter import HistFit
from pylab import hist
from fitter import Fitter
from datetime import time
from scipy import stats
from scipy.stats import pearsonr
#----------------------------------------------------------
#=================Carga de Datos diários:==================
#----------------------------------------------------------
#--------Función para importar los datos del CENCE:--------
def datos_demanda(inicio, fin):
    '''
    ==========
    Parameters
    ----------
    api_url             : str
        URL de la información para el proyecto
    datos_demanda_df    : .jason
        Archivo de .json con la informacion solicitada.
    ==========
    Returns
    ----------
    datos_demanda_df : data frame
        Data frame de los datos solicitados en el periodo de tiempo correspondiente.
    ==========
    '''
    api_url = f'https://apps.grupoice.com/CenceWeb/data/sen/json/DemandaMW?inicio={inicio}&fin={fin}'    #Modificamos la URL.
    print('Se extraen los datos para:\nInicio:',inicio,'Fin:',fin)      #Imprimimos la direccion URL.

    datos_demanda_jason = requests.get(api_url).json()                     #Variable para los datos extraídos del URL.
    datos_demanda_df = pd.DataFrame(datos_demanda_jason['data'])           #Generamos el Dataframe de los datos.
    dayDemanda_datos_df = pd.DataFrame(datos_demanda_jason['data'])
    datos_demanda_df['fechaHora'] = pd.to_datetime(datos_demanda_df['fechaHora'])
    datos_demanda_df = datos_demanda_df.sort_values(by='fechaHora')
    datos_demanda_df.to_csv('Datos_Demanda.csv', index=False)           #Almacenamos los resultados en un archivo .csv.

    print('--------Data Frame generado con exito.--------')
    return datos_demanda_df ,dayDemanda_datos_df                                      #Se retornar los datos en un data frame.

#----------------------------------------------------------
#==========================================================
#=================Ejecución del programa:==================
'''
---En caso de que desee solicitar fechas al usuario     ---
---aplique el siguiente codigo:                         ---
-----------------------------------------------------------
fecha_inicio = input('Fecha inicio (YYYYMMDD):)                         #Solicitamos la fecha de inicio.
fecha_fin = input('Fecha final  (YYYYMMDD):)                            #Solicitamos la fecha de fin.
'''
#------------------Variables de inicio---------------------
fecha_inicio = f'20190101'                                              #Fecha de incio para solicitud de datos.
fecha_fin = f'20200101'                                                 #Fecha final para solicitud de datos.

#----------------------------------------------------------
#===========Se almacenan los datos para analizar===========
datos_demanda_df,dayDemanda_datos_df = datos_demanda(fecha_inicio , fecha_fin)               #Llamada a la funcion datos_demanda. Generamos el df.
DF_demanda_hora = pd.read_csv('Datos_Demanda.csv')                       #Caragamos el Data Frame generado por datos_demanda.
#----------------------------------------------------------

#print (DF_demanda_hora)


# SECCIÓN A: Procesos

# 0. Datos de demanda de potencia
A0 = proceso.demanda()
#print(A0)

# 1. Función de densidad del proceso aleatorio
c , log ,scale = proceso.densidad(A0)
print("#########################################################")
print(f"Polinomio para C:{c}")
print(f"Polinomio para log:{log}")
print(f"Polinomio para scale:{scale}")
print("#########################################################")

# 2. Gráfica de la secuencia aleatoria
A2 = proceso.grafica(A0)

# 3. Probabilidad de tener un consumo p1 < P < p2 en t1 < T < t2
# datas a ingresar(dataframe, hora Inicial, hora Final, potencia Inicial, potencia Final)
A3 = proceso.probabilidad(A0,0,23,1000,1500)
print("#########################################################")
print("La probabilidad de ocurrencia para los rangos especificados es de:")
print(f"{A3}")
print("#########################################################")


# SECCIÓN B: Momentos

# 4. Autocorrelación
B4 = momentos.autocorrelacion()
print(B4)

# 5. Autocovarianza
B5 = momentos.autocovarianza()
print(B5)

# SECCIÓN C: Estacionaridad

# 6. Estacionaridad en sentido amplio
C6 = estacionaridad.wss(datos_demanda_df)
print(C6)

# 7. Promedio temporal
C7 = estacionaridad.prom_temporal()
print(C7)

# 8. Ergodicidad
C8 = estacionaridad.ergodicidad()
print(C8)

# SECCIÓN D: Características espectrales

# 9. Función de densidad espectral de potencia
D9 = espectro.psd()
print(D9)
