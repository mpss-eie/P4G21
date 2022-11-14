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

def autocovarianza():
    return 'Aquí está la autocovarianza.'