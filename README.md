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

### Funciones de `proceso`

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
> De la función de densidad se obtienen los parámetros para construir la secuencia aleatoria, estos son:

```math
c(t) = 4.57199340*10^{-8}*t^7 - 5.00399491*10^{-6}*t^6 + 2.09913189*10^{-4}*t^5 - 4.32940873*10^{-3}*t^4 + 4.60710835*10^{-2}*t^3 - 2.33562409*10^{-1}*t^2 + 3.68052322*10^{-1}*t + 6.52281140*10^{-1}
```
```math
log(t) = 2.85391745*10^{-5}*t^7 - 2.39480688*10^{-3}*t^6 + 7.39492808*10^{-2}*t^5 - 9.84120610*10^{-1}*t^4 +
  3.91618298*t^3 + 2.19374917*10^{1}*t^2 - 1.03908708*10^{2}*t + 1.03447704*10^{3}
```
```math
scale(t) = -1.32009676*10^{-6}*t^7 + 7.54402041*10^{-5}*t^6 - 1.40668876*10^{-3}*t^5 + 6.56674366*10^{-3}*t^4 + 7.82871767*10^{-2}*t^3 - 8.31609677*10^{-1}*t^2 + 1.26876083*t + 2.33549419*10^{1}
```

> La secuencia aleatoria para los datos suministrados p(t) es:

```math
P(t) = c*\frac{exp(-x)}{(1+exp(-x)^{c+1})}
```
> donde:

```math
c = 4.57199340*10^{-8}*t^7 - 5.00399491*10^{-6}*t^6 + 2.09913189*10^{-4}*t^5 - 4.32940873*10^{-3}*t^4 + 4.60710835*10^{-2}*t^3 - 2.33562409*10^{-1}*t^2 + 3.68052322*10^{-1}*t + 6.52281140*10^{-1}
```

```math
x = \frac{(p-log(t))}{scale(t)}
```

#### probabilidad(datos_df, hora_1, hora_2, potencia_1, potencia_2)
> El ejemplo expuesto en resultados tiene la forma: probabilidad(A0,0,23,1000,1500).
la probabilidad de que el consumo de potencia esté entre 1000 y 1500 a todo el día es de 0.5875250420977342.

(Descripción y análisis de resultados)

## Módulo `estacionaridad`
>El objetivo de este módulo es ser capaz de determinar si una secuencia aleatorea es estacionaria en sentido amplio, para luedo determinar su promedio temporal y finalmente determinar si la secuecia es ergodica o no.

### Funciones de `estacionaridad`
#### WSS(A0)
>Esta funcion determina la estacionaridad en sentido amplio de una secuencia aleatorea, manteniedo los valores validos en un factor del 5% de diferencia.

#### prom_temporal(c,A0)
>Esta funcion determina el promedio temporal para los valores
de consumo MW, se calcula tanto el vcalor numerico sujeto a
la funcion 'C' como el vector de promedio temporal para el
data frame de las horas.

#### ergodicidad(A0)
>Esta funcion determina la ergodicidad de la secuencia aleatoria
del consumo de MW que está en A0, utiliza el promedio temporal
calculado anteriormente y mantiene los valores validos dentro
del 5% de error.

## Resultados `estacionaridad`
#### WSS(A0)
>Serie temporal estacionaria en setido amplio.
#### prom_temporal(c,A0)
>0.10358971035885703
#### ergodicidad(A0,C71)
> '------------El proceso no es ergódico----------'

# Paquete `Momentos' 

En este paquete se implementan dos funciones: autocorrelación y autocovarianza. En el caso de la primera función, se desea encontrar la correlación entre variables aleatorias por lo cual se considera t1 y t2. El procedimiento consiste en brindar como parámetros dos horas determinadas, además se guardan los datos de consumo en las variables establecidas. 

Para el caso de la segunda función, se desea encontrar la covarianza entre variables aleatorias por lo cual se considera t1 y t2. Al igual que la función mencionada anteriormente, se toman en cuenta como parámetros dos horas determinadas, para obtener los datos correspondientes.

## Resultados `Momentos'


# Paquete `Espectro'

En el caso de este paquete la función psd se encarga de calcular la densidad espectral de potencia de un proceso aleatorio. Para esto se considera como parámetros el dataFrame de consumo de energía, la hora inicial y la hora final. También esta función se encarga de generar la lista de datos como muestra con una cantidad definida de puntos en este caso 800. Con estos puntos se logra crear una gráfica que represente la densidad espectral de potencia para los datos que fueron seleccionados.

## Resultados `Espectro'

