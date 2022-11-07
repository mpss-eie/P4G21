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

#------Función para obtener los datos por horas:--------
def parametros_horas():
    '''Función distribucion_horas().

    Esta función encarga de retornar los parametros de la distribucion
    genlogistic a todas las horas del dia, a partir de DataFrame
    de la función datos_demanda(), extrae específicamente la potencia a
    a la hora específica, para obtener los parametros c,log,scale y retornarlos.

    Parameters
    ----------
    hora : int
        Variable con la hora deseada.
    datos_hora : array
        Contiene los datos de consumo a una hora especifica.
    modelo : string
        Almacena el nombre de la distribucion utilizada.
    dayDemanda_datos_df : DataFrame
        Una variable global que contiene los datos anuales de potencia.
    mejorAjuste_Horas : fitter
        Contiene información de los parametros del modelo.
    param : dicccionario
        contiene los parametros c, log, scale a utiliar.

    Returns
    -------
    c : array
        Variable con los parametros de la distribucion para c.
    log : array
        Variable con los parametros de la distribucion para log.
    scale : array
        Variable con los parametros de la distribucion para scale.
    '''
    #Arreglos para almacenar los datos de las distribuciones.
    c = []
    log = []
    scale = []

    #Ciclo para obtener la informacion y parametros de todas las horas.
    for hora in range(0,24):
        datos_hora = []
        # Ciclo para recorrer todo el dataFrame en busqueda de las hora especificada
        for i in range(hora, len(dayDemanda_datos_df.index), 24):
            # El dato de una hora especifica aparecerá cada 24 filas, por las 24 horas del días.
            # Almacena la potencia en la hora especifica
            datos_hora.append(float(dayDemanda_datos_df.MW[i]))

        #Seleccion del modelo.
        modelo = 'genlogistic'

        # Parametros para la hora especifica.
        mejorAjuste_Horas = Fitter(datos_hora,distributions=[modelo])
        mejorAjuste_Horas.fit()

        #Parametros de la distribucion.
        params = mejorAjuste_Horas.fitted_param

        #Guardar los datosen los arreglos, su posicion indica su hora.
        c.append(params[modelo][0])
        log.append(params[modelo][1])
        scale.append(params[modelo][2])

    return c , log , scale
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

#----------------------------------------------------------
#===========Obtencion del los parametros por horas===========
c,log,scale = parametros_horas()
x = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]

#----------------------------------------------------------
#===========Encontrar c(t)===========
c_t = np.polyfit(x,c,7)
print(c_t)

#----------------------------------------------------------
#===========Encontrar log(t)===========
log_t = np.polyfit(x,log,7)
print(log_t)

#----------------------------------------------------------
#===========Encontrar scale(t)===========
scale_t = np.polyfit(x,scale,7)
print(scale_t)
#----------------------------------------------------------

# SECCIÓN A: Función de densidad de probabilidad

# 0. Datos de demanda de potencia
A0 = proceso.demanda()
print(A0)

# 1. Función de densidad del proceso aleatorio
A1 = proceso.densidad()
print(A1)

# 2. Gráfica de la secuencia aleatoria
A2 = proceso.grafica()
print(A2)

# 3. Probabilidad de tener un consumo p1 < P < p2 en t1 < T < t2
A3 = proceso.probabilidad()
print(A3)

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
