from fitter import Fitter
import numpy as np
from scipy import stats
from scipy.stats import genlogistic
import matplotlib.pyplot as plt

def demanda():
    return 'Aquí está la demanda.'

def densidad(dayDemanda_datos_df):
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
    #print(c_t)

    #----------------------------------------------------------
    #===========Encontrar log(t)===========
    log_t = np.polyfit(f,log,7)
    #print(log_t)

    #----------------------------------------------------------
    #===========Encontrar scale(t)===========
    scale_t = np.polyfit(f,scale,7)
    #print(scale_t)

    A = [c_t, log_t, scale_t]

    return A

def grafica(dayDemanda_datos_df):

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

    x = np.arange(1000,1800)

    fig,(ax0,ax1,ax2,ax3,ax4,ax5,ax6,ax7,ax8,ax9,ax10,ax11) = plt.subplots(12,1,sharex=True)
    fig2, (ax12,ax13,ax14,ax15,ax16,ax17,ax18,ax19,ax20,ax21,ax22,ax23) = plt.subplots(12,1,sharex=True)

    ax0.plot(x,genlogistic.pdf(x,c[0],log[0],scale[0]))
    ax0.set_ylabel("00:00")

    ax1.plot(x,genlogistic.pdf(x,c[1],log[1],scale[1]))
    ax1.set_ylabel("01:00")

    ax2.plot(x,genlogistic.pdf(x,c[2],log[2],scale[2]))
    ax2.set_ylabel("02:00")

    ax3.plot(x,genlogistic.pdf(x,c[3],log[3],scale[3]))
    ax3.set_ylabel("03:00")

    ax4.plot(x,genlogistic.pdf(x,c[4],log[4],scale[4]))
    ax4.set_ylabel("04:00")

    ax5.plot(x,genlogistic.pdf(x,c[5],log[5],scale[5]))
    ax5.set_ylabel("05:00")

    ax6.plot(x,genlogistic.pdf(x,c[6],log[6],scale[6]))
    ax6.set_ylabel("06:00")

    ax7.plot(x,genlogistic.pdf(x,c[7],log[7],scale[7]))
    ax7.set_ylabel("07:00")

    ax8.plot(x,genlogistic.pdf(x,c[8],log[8],scale[8]))
    ax8.set_ylabel("08:00")

    ax9.plot(x,genlogistic.pdf(x,c[9],log[9],scale[9]))
    ax9.set_ylabel("09:00")

    ax10.plot(x,genlogistic.pdf(x,c[10],log[10],scale[10]))
    ax10.set_ylabel("10:00")

    ax11.plot(x,genlogistic.pdf(x,c[11],log[11],scale[11]))
    ax11.set_ylabel("11:00")

    ax12.plot(x,genlogistic.pdf(x,c[12],log[12],scale[12]))
    ax12.set_ylabel("12:00")

    ax13.plot(x,genlogistic.pdf(x,c[13],log[13],scale[13]))
    ax13.set_ylabel("13:00")

    ax14.plot(x,genlogistic.pdf(x,c[14],log[14],scale[14]))
    ax14.set_ylabel("14:00")

    ax15.plot(x,genlogistic.pdf(x,c[15],log[15],scale[15]))
    ax15.set_ylabel("15:00")

    ax16.plot(x,genlogistic.pdf(x,c[16],log[16],scale[16]))
    ax16.set_ylabel("16:00")

    ax17.plot(x,genlogistic.pdf(x,c[17],log[17],scale[17]))
    ax17.set_ylabel("17:00")

    ax18.plot(x,genlogistic.pdf(x,c[18],log[18],scale[18]))
    ax18.set_ylabel("18:00")

    ax19.plot(x,genlogistic.pdf(x,c[19],log[19],scale[19]))
    ax19.set_ylabel("19:00")

    ax20.plot(x,genlogistic.pdf(x,c[20],log[20],scale[20]))
    ax20.set_ylabel("20:00")

    ax21.plot(x,genlogistic.pdf(x,c[21],log[21],scale[21]))
    ax21.set_ylabel("21:00")

    ax22.plot(x,genlogistic.pdf(x,c[22],log[22],scale[22]))
    ax22.set_ylabel("22:00")

    ax23.plot(x,genlogistic.pdf(x,c[23],log[23],scale[23]))
    ax23.set_ylabel("23:00")
    ax23.set_xlabel("Potencia")

    plt.show()

def probabilidad(dayDemanda_datos_df,t1,t2,p1,p2):
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

    pt = 0
    times = 0

    for i in range(t1,t2):
        pt = pt + (genlogistic.cdf(p2,c[i],log[i],scale[i]) - genlogistic.cdf(p1,c[i],log[i],scale[i]))
        times = times + 1

    p_total = pt/times

    return p_total
