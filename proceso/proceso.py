from fitter import Fitter
import numpy as np
from scipy import stats
def demanda(dayDemanda_datos_df):
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

    f = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]

    #----------------------------------------------------------
    #===========Encontrar c(t)===========
    c_t = np.polyfit(f,c,7)
    print(c_t)

    #----------------------------------------------------------
    #===========Encontrar log(t)===========
    log_t = np.polyfit(f,log,7)
    #print(log_t)

    #----------------------------------------------------------
    #===========Encontrar scale(t)===========
    scale_t = np.polyfit(f,scale,7)
    #print(scale_t)

    #X = float(c_t[0])*x^7 + float(c_t[1])*x^6 + float(c_t[2])*x^5 + float(c_t[3])*x^4 + float(c_t[4])*x^3 + float(c_t[5])*x^2 + float(c_t[6])*x + float(c_t[7])
    X = c_t
    return X

def densidad(pol):
    pdf = stats.norm.pdf(pol)
    return pdf

def grafica():
    return 'Aquí está la gráfica.'

def probabilidad():
    return 'Aquí está la probabilidad.'
