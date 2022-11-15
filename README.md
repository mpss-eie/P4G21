### Universidad de Costa Rica
#### IE0405 - Modelos Probabilísticos de Señales y Sistemas
##### Proyecto 4: Procesos aleatorios (segundo ciclo del 2022)

- Daymer Alberto Vargas Vargas, C08286
- Fabricio Jose Arguijo Cantillo, B70645
- Jafet Soto Arrieta, B77543

# Paquete `proceso`

> Este paquete se encarga de suministrar una serie de funciones con las cuales se logra obtener una secuencia aleatoria de un conjunto de datos de consumo de energía anual,
graficar las funciones de densidad de cada hora del día, y obtener la ocurrencia de
un evento en un rango de tiempo y potencia determinadas.

## Módulo `proceso`

> Este modulo se encarga de suministrar una serie de funciones con las cuales se logra obtener una secuencia aleatoria de un conjunto de datos de consumo de energía anual a partir de un dataFrame,
graficar las funciones de densidad de probabilidad (pdf) de cada hora del día, y obtener la ocurrencia de
un evento en un rango de tiempo y potencia determinadas.

### Funciones

#### Demanda(inicio,final)
> La funcion demanda se encarga de retorna un dataFrame con los datos de consumo de potencia entre fechas especificas. Recibe como parámetros la fecha de inicio y fecha final.

#### densidad(DataFrame)
> La funcion retorna 3 variables, C, log y scale para construir la secuencia aleatoria P(t) mostrada en los resultados
estas variables contienen el polinomio de orden 7 necesario para construir la P(t). DIcha funcion necesita recibir una dataFrame con el consumo anual.

#### grafica(datos_df)
> Recibe un dataFrame de consumo anual y grafica las pdf de cada una de las horas del día.

#### probabilidad(datos_df, hora_1, hora_2, potencia_1, potencia_2)
> Obtiene la probabilidad de ocurrencia en un rango de horas determinados y rango de potencia determinado. Sus entradas son el dataFrame, seguido de la hora inicial, hora final , potencia inicial y potencia final.
> El ejemplo expuesto en resultados tiene la forma: probabilidad(A0,0,23,1000,1500), quiere decir que A0 es el dataframe, 0,23 es que vaya de las o horas a las 23 horas y 1000,1500 es que tome ese rango de potencia.

### Resultados `proceso`

#### densidad(DataFrame)
> C(t) = 4.57199340e-08*t^7 - 5.00399491e-06*t^6 + 2.09913189e-04*t^5 - 4.32940873e-03*t^4 +  4.60710835e-02*t^3 - 2.33562409e-01*t^2 + 3.68052322e-01*t + 6.52281140e-01 MODE LATEX: 4.57199340*10^{-8}*t^7 - 5.00399491*10^{-6}*t^6 + 2.09913189*10^{-4}*t^5 - 4.32940873*10^{-3}*t^4 + 4.60710835*10^{-2}*t^3 - 2.33562409*10^{-1}*t^2 + 3.68052322*10^{-1}*t + 6.52281140*10^{-1}

> log(t) = 2.85391745e-05*t^7 - 2.39480688e-03*t^6 + 7.39492808e-02*t^5 - 9.84120610e-01*t^4 +
  3.91618298e+00 *t^3 + 2.19374917e+01*t^2 - 1.03908708e+02*t + 1.03447704e+03

> scale(t) = -1.32009676e-06*t^7 + 7.54402041e-05*t^6 - 1.40668876e-03*t^5 + 6.56674366e-03*t^4 + 7.82871767e-02*t^3 - 8.31609677e-01*t^2 + 1.26876083e+00*t + 2.33549419e+01

> La secuencia aleatoria para los datos suministrados es de:

> P(t) = (4.57199340*10^{-8}*t^7 - 5.00399491*10^{-6}*t^6 + 2.09913189*10^{-4}*t^5 - 4.32940873*10^{-3}*t^4 + 4.60710835*10^{-2}*t^3 - 2.33562409*10^{-1}*t^2 + 3.68052322*10^{-1}*t + 6.52281140*10^{-1})*\frac{exp(-t)}{(1+exp(-t)^{4.57199340*10^{-8}*t^7 - 5.00399491*10^{-6}*t^6 + 2.09913189*10^{-4}*t^5 - 4.32940873*10^{-3}*t^4 + 4.60710835*10^{-2}*t^3 - 2.33562409*10^{-1}*t^2 + 3.68052322*10^{-1}*t + 6.52281140*10^{-1}+1}})

#### probabilidad(datos_df, hora_1, hora_2, potencia_1, potencia_2)
> El ejemplo expuesto en resultados tiene la forma: probabilidad(A0,0,23,1000,1500).
la probabilidad de que el consumo de potencia esté entre 1000 y 1500 a todo el día es de 0.5875250420977342.

(Descripción y análisis de resultados)
