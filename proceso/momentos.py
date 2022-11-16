import numpy as np

def autocorrelacion(datos_df,t1,t2):

    datos_t1 = []
    for i in range(t1, len(datos_df.index), 24):
        datos_t1.append(float(datos_df.MW[i]))

    datos_t2 = []
    for j in range(t2, len(datos_df.index), 24):
        datos_t2.append(float(datos_df.MW[j]))

    correlacion = np.corrcoef(datos_t1,datos_t2)

    return correlacion

def autocovarianza(datos_df,t1,t2):

    datos_t1 = []
    for i in range(t1, len(datos_df.index), 24):
        datos_t1.append(float(datos_df.MW[i]))

    datos_t2 = []
    for j in range(t2, len(datos_df.index), 24):
        datos_t2.append(float(datos_df.MW[j]))

    covarianza = np.cov(datos_t1,datos_t2)

    return covarianza
