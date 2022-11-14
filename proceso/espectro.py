from fitter import Fitter
import numpy as np
import pandas as pd 
from pandas import json_normalize
from scipy import stats
from scipy.stats import genlogistic
import matplotlib.pyplot as plt

# Se obtendrá el espectro de potencia para una hora determinada
# en todos los días del año, por lo cual es necesario definir un array
# (psd) para todas las potencias posibles en el intervalo de tiempo establecido (hora determinada).

hora_determinada= int(input("Hora empleada como muestra: "))
if hora_determinada < 10: # Se implementa un if-else para que el usuario pueda establecer una hora en punto como muestra
    hora_determinada = "%02d" % (hora_determinada,)
else:
      hora_determinada= str(hora_determinada)
      
# Se prosigue a crear un array con los datos de la hora determinada, para tomar en cuenta todas las potencias posibles.
mw_hora = [] 
print("El espectro de potencia para la hora determinada es", hora_determinada)

# Se utiliza un for para considerar todas las potencias de los datos y pasar por cada uno.
for i in range(len(datos["data"])): 
    
    # Se considera la posición (10:14), debido a que representa en espacio donde se especifica la hora establecida de los datos.
      horas = datos["data"][i]["fecha_Hora"][10:14] 
      
# Se aplica un if, en caso de que se de la coincidencia en la cual: la hora determinada por el usuario sea igual a la hora de los datos dado por el data.
if hora_determinada== horas: 
    mw2= datos["data"][i]["MW"]
mw_hora.append(mw2)

# Obtención de la densidad de potencia espectral con base a la hora establecida
     dt= 0.01
plt.psd (mw_hora, 512, 1./dt, color = "Blue")
plt.xlabel('Frequency')
plt.ylabel('Psd (db)')
plt.suptitle('Densidad de Potencia Espectral para una determinada hora', fontweight = "bold")
plt.show()
