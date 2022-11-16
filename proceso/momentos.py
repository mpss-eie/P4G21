import numpy as np

def autocorrelacion(datos_df,t1,t2):
    '''Función autocorrelacions().

    Esta función se encarga de obtener la autocorrelación entre dos arreglo
    de datos, estos datos es la potencia consumida a dos horas distintas
    del dia, esta se hace utilizando una función de numpy.

    Parameters
    ----------
    datos_t1 : array
        Contendrá los datos de consumo a una hora en especifico.
    datos_t2 : array
        Contendrá los datos de consumo a una hora en especifico distinta.

    Returns
    -------
    correlacion : float
        Almacena la correlación entre las dos horas de consumo.
    '''

    #Se obtiene el consumo a la primera hora específica.
    datos_t1 = []
    for i in range(t1, len(datos_df.index), 24):
        datos_t1.append(float(datos_df.MW[i]))

    #Se obtiene el consumo a la segunda hora específica.
    datos_t2 = []
    for j in range(t2, len(datos_df.index), 24):
        datos_t2.append(float(datos_df.MW[j]))

    #Se obtiene la autocorrelación mediante la funcion corrcoef de numpy.
    correlacion = np.corrcoef(datos_t1,datos_t2)

    return correlacion

def autocovarianza(datos_df,t1,t2):
    '''Función autocovarianza().

    Esta función se encarga de obtener la Autocovarianza entre dos arreglo
    de datos, estos datos es la potencia consumida a dos horas distintas
    del dia, esta se hace utilizando una función de numpy.

    Parameters
    ----------
    datos_t1 : array
        Contendrá los datos de consumo a una hora en especifico.
    datos_t2 : array
        Contendrá los datos de consumo a una hora en especifico distinta.

    Returns
    -------
    covarianza : float
        Almacena la covarianza entre las dos horas de consumo.
    '''

    #Se obtiene el consumo a la primera hora específica.
    datos_t1 = []
    for i in range(t1, len(datos_df.index), 24):
        datos_t1.append(float(datos_df.MW[i]))

    #Se obtiene el consumo a la segunda hora específica.
    datos_t2 = []
    for j in range(t2, len(datos_df.index), 24):
        datos_t2.append(float(datos_df.MW[j]))

    #Se obtiene la autocovarianza mediante la funcion cov de numpy.
    covarianza = np.cov(datos_t1,datos_t2)

    return covarianza
