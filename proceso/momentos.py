import json
import requests
import pandas as pd 
from pandas import json_normalize
import numpy as np
from scipy import stats
from scipy.stats import genlogistic
import matplotlib.pyplot as plt

# Se define la función de autocorrelación

def autocorrelacion():
    
# Se consideran los datos de la primera hora asignada 
periodo1 = datos_hora(horas[0]).assign(Index =
range (len (datos_hora(horas[0])))).set_index('Index')['MW'] 

# Se consideran los datos de la segunda hora asignada
periodo2 = datos_hora(horas[1]).assign(Index =
range (len (datos_hora(horas[1])))).set_index ('Index')['MW']

# Se calcula la correlación mediante el uso de pandas

correlacion = periodo1.correlacion(periodo2, method = 'pearson') 
return correlacion, periodo1, periodo2

correlacion = autocorrelacion() 

print("El coeficiente obtenido de correlación de Pearson entre las horas "
+ str(horas[0]) + ":00 y " + str(horas[1]) + ":00 es de: \n", correlacion[0])

# Se define la función de autocovarianza

def autocovarianza():
    
# Se consideran los datos de la primera hora asignada 
periodo1 = datos_hora(horas[0]).assign(Index =
range (len (datos_hora(horas[0])))).set_index('Index')['MW'] 

# Se consideran los datos de la segunda hora asignada
periodo2 = datos_hora(horas[1]).assign(Index =
range (len (datos_hora(horas[1])))).set_index('Index')['MW']

# Es necesario guardar en una serie los dos periodos
consumoP1 = pd.Series(data=periodo1) 
consumoP2 = pd.Series(data=periodo2) 

# Se calcula la covarianza mediante el uso de pandas
covarianza= consumoP1.cov(consumoP2)
return covarianza

covarianza= autocovarianza()

print ("La covarianza obtenida entre la hora establecida " + str(horas[0]) + ":00 y la hora " + str(horas[1]) + ":00 es de " + str(covarianza))
