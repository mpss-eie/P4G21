from fitter import Fitter
import numpy as np
from scipy import stats
from scipy.stats import genlogistic
import matplotlib.pyplot as plt
import json
import pandas as pd

def demanda():
    with open('datos.json') as file:
        datos = json.load(file)
    df = pd.DataFrame(datos['data'])
    return df

def demandaConURL(inicio, fin):
    '''Función datos_demanda(inicio,fin).

    Esta función se encarga de retornar un dataFrame con
    los datos de consumo de potencia en un rango determinado
    de tiempo como parámetro de entrada, se encarga de acceder
    a la base de datos del grupoice obtener los datos en formato
    JSON, para posterior seleccionar solo los datos deseados y
    almacenarlos en un dataFrame para su posterior análisis.
    En el data DataFrame almacena fecha/hora y potencia

    Parameters
    ----------
    inicio : str
    fin : str
    api_url : str
        Una variable que construye el URL de la página a visitar.
    respuesta : str
        variable que almacena los datos obtenidos de la base de dato del
        grupoice.
    datos : JSON
        Convierte la información extraída en formato JSON.

    Returns
    -------
    dataFrame : dataFrame
        Retorna los datos obtenidos de la base de datos en un dataFrame
        de pandas.
    '''
    # Modificamos la URL.
    api_url = f'https://apps.grupoice.com/CenceWeb/data/sen/json/DemandaMW?inicio={inicio}&fin={fin}'

    # Imprimimos el rango de fechas
    print('Se extraen los datos para:\nInicio:', inicio, 'Fin:', fin)

    # Variable para los datos extraídos del URL.
    datos_demanda_jason = requests.get(api_url).json()
    # Generamos el Dataframe de los datos.
    datos_demanda_df = pd.DataFrame(datos_demanda_jason['data'])
    datos_demanda_df['fechaHora'] = pd.to_datetime(
        datos_demanda_df['fechaHora'])
    datos_demanda_df = datos_demanda_df.sort_values(by='fechaHora')

    print('--------Data Frame generado con exito.--------')
    return datos_demanda_df  # Se retornar los datos en un data frame.

def densidad(datos_df):
    '''Función densidad().

    Esta función encarga de retornar el polinomio de orden 7 de los parámetros de la distribución
    genlogistic c, log y scale, tomando en cuenta todas las horas del día, a partir de DataFrame
    de la función demanda(), se extrae la potencia para cada hora del día, con Fitter se obtiene los
    parámetros c, log y scale para la hora especifica, los cuales son almacenados, para
    posterior ingresarlos en la función polyfit de numpy y obtener el polinomio de orden 7,
    con el cual se construye P(t).

    Parameters
    ----------
    hora : int
        Variable con la hora deseada.
    datos_hora : array
        Contiene los datos de consumo a una hora especifica de forma temporal.
    modelo : string
        Almacena el nombre de la distribución utilizada.
    datos_df : DataFrame
        Una variable global que contiene los datos anuales de potencia.
    mejorAjuste_Horas : fitter
        Contiene información de los parámetros del modelo.
    param : diccionario
        contiene los parámetros c, log, scale a utiliar.
    c : array
        Variable con los párametros de la distribución para c con todas las horas del día.
    log : array
        Variable con los párametros de la distribución para log con todas las horas del día.
    scale : array
        Variable con los párametros de la distribución para scale con todas las horas del día.

    Returns
    -------
    c_t : array
        Variable con el polinomio de orden 7 para c.
    log_t : array
        Variable con con el polinomio de orden 7 para log.
    scale_t : array
        Variable con con el polinomio de orden 7 para scale.
    '''

    # Arreglos para almacenar los datos de las distribuciones.
    c = []
    log = []
    scale = []

    # Ciclo para obtener la información y parámetros c, log y scale de todas las horas.
    for hora in range(0, 24):
        datos_hora = []
        # Ciclo para recorrer todo el dataFrame en búsqueda de las hora especificada
        for i in range(hora, len(datos_df.index), 24):
            # El dato de una hora especifica aparecerá cada 24 filas, por las 24 horas del días.
            # Almacena la potencia en la hora especifica
            datos_hora.append(float(datos_df.MW[i]))

        # Selección del modelo.
        modelo = 'genlogistic'

        # Parámetros para la hora especifica.
        mejorAjuste_Horas = Fitter(datos_hora, distributions=[modelo])
        mejorAjuste_Horas.fit()

        # Parámetros de la distribución.
        params = mejorAjuste_Horas.fitted_param

        # Guardar los datos en los arreglos, su posición indica su hora.
        c.append(params[modelo][0])
        log.append(params[modelo][1])
        scale.append(params[modelo][2])

    # Vector de horas
    f = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,
         13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]

    # ----------------------------------------------------------
    # ===========Encontrar c(t)===========
    c_t = np.polyfit(f, c, 7)
    # print(c_t)

    # ----------------------------------------------------------
    # ===========Encontrar log(t)===========
    log_t = np.polyfit(f, log, 7)
    # print(log_t)

    # ----------------------------------------------------------
    # ===========Encontrar scale(t)===========
    scale_t = np.polyfit(f, scale, 7)
    # print(scale_t)

    return c_t, log_t, scale_t

def grafica(datos_df):
    '''Función grafica().

    Esta función encarga de almacenar los parámetros c, log y scale para posterior
    utilizarlos para generar la función pdf que permite la visualización de todas
    las graficas a distintas horas del día, donde la potencia es su común denominador.

    Parameters
    ----------
    hora : int
        Variable con la hora deseada.
    datos_hora : array
        Contiene los datos de consumo a una hora especifica de forma temporal.
    modelo : string
        Almacena el nombre de la distribución utilizada.
    datos_df : DataFrame
        Una variable global que contiene los datos anuales de potencia.
    mejorAjuste_Horas : fitter
        Contiene información de los parámetros del modelo.
    param : diccionario
        contiene los parámetros c, log, scale a utilizar.
    c : array
        Variable con los parámetros de la distribución para c con todas las horas del día.
    log : array
        Variable con los parámetros de la distribución para log con todas las horas del día.
    scale : array
        Variable con los parámetros de la distribución para scale con todas las horas del día.
    '''

    # Arreglos para almacenar los datos de las distribuciones.
    c = []
    log = []
    scale = []

    # Ciclo para obtener la información y parámetros c, log y scale de todas las horas.
    for hora in range(0, 24):
        datos_hora = []
        # Ciclo para recorrer todo el dataFrame en búsqueda de las hora especificada
        for i in range(hora, len(datos_df.index), 24):
            # El dato de una hora especifica aparecerá cada 24 filas, por las 24 horas del días.
            # Almacena la potencia en la hora especifica
            datos_hora.append(float(datos_df.MW[i]))

        # Selección del modelo.
        modelo = 'genlogistic'

        # Parámetros para la hora especifica.
        mejorAjuste_Horas = Fitter(datos_hora, distributions=[modelo])
        mejorAjuste_Horas.fit()

        # Parámetros de la distribución.
        params = mejorAjuste_Horas.fitted_param

        # Guardar los datos en los arreglos, su posición indica su hora.
        c.append(params[modelo][0])
        log.append(params[modelo][1])
        scale.append(params[modelo][2])

    #Vector de potencia.
    x = np.arange(800, 1800)

    #Configuración para mostrar las 24 pdf juntas.
    fig, (ax0, ax1, ax2, ax3, ax4, ax5, ax6, ax7, ax8, ax9,
          ax10, ax11) = plt.subplots(12, 1, sharex=True)
    fig2, (ax12, ax13, ax14, ax15, ax16, ax17, ax18, ax19, ax20,
           ax21, ax22, ax23) = plt.subplots(12, 1, sharex=True)

    #Asignación de parámetros para las graficas mostrar
    ax0.plot(x, genlogistic.pdf(x, c[0], log[0], scale[0]))
    ax0.set_ylabel("00:00")

    ax1.plot(x, genlogistic.pdf(x, c[1], log[1], scale[1]))
    ax1.set_ylabel("01:00")

    ax2.plot(x, genlogistic.pdf(x, c[2], log[2], scale[2]))
    ax2.set_ylabel("02:00")

    ax3.plot(x, genlogistic.pdf(x, c[3], log[3], scale[3]))
    ax3.set_ylabel("03:00")

    ax4.plot(x, genlogistic.pdf(x, c[4], log[4], scale[4]))
    ax4.set_ylabel("04:00")

    ax5.plot(x, genlogistic.pdf(x, c[5], log[5], scale[5]))
    ax5.set_ylabel("05:00")

    ax6.plot(x, genlogistic.pdf(x, c[6], log[6], scale[6]))
    ax6.set_ylabel("06:00")

    ax7.plot(x, genlogistic.pdf(x, c[7], log[7], scale[7]))
    ax7.set_ylabel("07:00")

    ax8.plot(x, genlogistic.pdf(x, c[8], log[8], scale[8]))
    ax8.set_ylabel("08:00")

    ax9.plot(x, genlogistic.pdf(x, c[9], log[9], scale[9]))
    ax9.set_ylabel("09:00")

    ax10.plot(x, genlogistic.pdf(x, c[10], log[10], scale[10]))
    ax10.set_ylabel("10:00")

    ax11.plot(x, genlogistic.pdf(x, c[11], log[11], scale[11]))
    ax11.set_ylabel("11:00")

    ax12.plot(x, genlogistic.pdf(x, c[12], log[12], scale[12]))
    ax12.set_ylabel("12:00")

    ax13.plot(x, genlogistic.pdf(x, c[13], log[13], scale[13]))
    ax13.set_ylabel("13:00")

    ax14.plot(x, genlogistic.pdf(x, c[14], log[14], scale[14]))
    ax14.set_ylabel("14:00")

    ax15.plot(x, genlogistic.pdf(x, c[15], log[15], scale[15]))
    ax15.set_ylabel("15:00")

    ax16.plot(x, genlogistic.pdf(x, c[16], log[16], scale[16]))
    ax16.set_ylabel("16:00")

    ax17.plot(x, genlogistic.pdf(x, c[17], log[17], scale[17]))
    ax17.set_ylabel("17:00")

    ax18.plot(x, genlogistic.pdf(x, c[18], log[18], scale[18]))
    ax18.set_ylabel("18:00")

    ax19.plot(x, genlogistic.pdf(x, c[19], log[19], scale[19]))
    ax19.set_ylabel("19:00")

    ax20.plot(x, genlogistic.pdf(x, c[20], log[20], scale[20]))
    ax20.set_ylabel("20:00")

    ax21.plot(x, genlogistic.pdf(x, c[21], log[21], scale[21]))
    ax21.set_ylabel("21:00")

    ax22.plot(x, genlogistic.pdf(x, c[22], log[22], scale[22]))
    ax22.set_ylabel("22:00")

    ax23.plot(x, genlogistic.pdf(x, c[23], log[23], scale[23]))
    ax23.set_ylabel("23:00")
    ax23.set_xlabel("Potencia")

    plt.show()

def probabilidad(datos_df, hora_1, hora_2, potencia_1, potencia_2):
    '''Función grafica().

    Esta función encarga de obtener la probabilidad de ocurrencia donde un evento
    tenga una potencia entre dos rangos (potencia_1 y potencia_2), entre ciertas horas especificas
    (hora_1,hora_2). Esto lo hace mediante la cdf de cada una de las horas del día, tomando
    las horas específicas y sumando la probabilidad entre los rangos de potencia, para finalmente
    obtener el la probabilidad de ocurrencia.

    Parameters
    ----------
    hora : int
        Variable con la hora deseada.
    datos_hora : array
        Contiene los datos de consumo a una hora especifica de forma temporal.
    modelo : string
        Almacena el nombre de la distribución utilizada.
    datos_df : DataFrame
        Una variable global que contiene los datos anuales de potencia.
    mejorAjuste_Horas : fitter
        Contiene información de los parámetros del modelo.
    param : diccionario
        contiene los parámetros c, log, scale a utiliar.
    c : array
        Variable con los parámetros de la distribución para c con todas las horas del día.
    log : array
        Variable con los parámetros de la distribución para log con todas las horas del día.
    scale : array
        Variable con los parámetros de la distribución para scale con todas las horas del día.
    '''
    # Arreglos para almacenar los datos de las distribuciones.
    c = []
    log = []
    scale = []

    # Ciclo para obtener la información y parámetros c, log y scale de todas las horas.
    for hora in range(0, 24):
        datos_hora = []
        # Ciclo para recorrer todo el dataFrame en búsqueda de las hora especificada
        for i in range(hora, len(datos_df.index), 24):
            # El dato de una hora especifica aparecerá cada 24 filas, por las 24 horas del días.
            # Almacena la potencia en la hora especifica
            datos_hora.append(float(datos_df.MW[i]))

        # Selección del modelo.
        modelo = 'genlogistic'

        # Parámetros para la hora especifica.
        mejorAjuste_Horas = Fitter(datos_hora, distributions=[modelo])
        mejorAjuste_Horas.fit()

        # Parámetros de la distribución.
        params = mejorAjuste_Horas.fitted_param

        # Guardar los datos en los arreglos, su posición indica su hora.
        c.append(params[modelo][0])
        log.append(params[modelo][1])
        scale.append(params[modelo][2])

    #Sumatoria de probabilidades del rango de horas.
    sumatoria_horas = 0
    #Cantidad de horas sumadas
    repeticion_horas = 0

    #Ciclo para recorrer el rango de horas, y extraer la probabilidad de cada una
    #de ellas al rango de potencia especificado.
    for i in range(hora_1, hora_2):
        sumatoria_horas = sumatoria_horas + (genlogistic.cdf(potencia_2, c[i], log[i], scale[i]) -
                   genlogistic.cdf(potencia_1, c[i], log[i], scale[i]))
        repeticion_horas = repeticion_horas + 1

    #Se divide la sumatoria de las horas entre la cantidad de horas sumadas.
    ocurrencia_total = sumatoria_horas/repeticion_horas

    return ocurrencia_total
