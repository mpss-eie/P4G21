
from proceso import  espectro, momentos, proceso, estacionaridad

# SECCIÓN A: Procesos

# 0. Datos de demanda de potencia
A0 = proceso.demanda()

# 1. Función de densidad del proceso aleatorio
c, log, scale = proceso.densidad(A0)
print("#########################################################")
print(f"Polinomio para C:{c}")
print(f"Polinomio para log:{log}")
print(f"Polinomio para scale:{scale}")
print("#########################################################")

# 2. Gráfica de la secuencia aleatoria
#A2 = proceso.grafica(A0)

# 3. Probabilidad de tener un consumo p1 < P < p2 en t1 < T < t2
# datas a ingresar(dataframe, hora Inicial, hora Final, potencia Inicial, potencia Final)
A3 = proceso.probabilidad(A0, 0, 23, 1000, 1500)
print("#########################################################")
print("La probabilidad de ocurrencia para los rangos especificados es de:")
print(f"{A3}")
print("#########################################################")

# SECCIÓN B: Momentos
# 4. Autocorrelación
t1 = 3
t2 = 12

B4 = momentos.autocorrelacion(A0,t1,t2)
print("#########################################################")
print(f"La autocorrelacion entre las horas {t1} y {t2}:")
print(f"{B4[0][1]}")
print("#########################################################")

# 5. Autocovarianza

B5 = momentos.autocovarianza(A0,t1,t2)
print("#########################################################")
print(f"La Autocovarianza entre las horas {t1} y {t2}:")
print(f"{B5[0][1]}")
print("#########################################################")

# SECCIÓN C: Estacionaridad
# 6. Estacionaridad en sentido amplio
C6 = estacionaridad.wss(c)
print(C6)
# 7. Promedio temporal
C7, C71 = estacionaridad.prom_temporal(c,A0)
print(C7)
# 8. Ergodicidad
C8 = estacionaridad.ergodicidad(A0, C71)
print(C8)

# SECCIÓN D: Características espectrales
# 9. Función de densidad espectral de potencia

D9 = espectro.psd(A0,17)
print(D9)
