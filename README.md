### Universidad de Costa Rica
#### IE0405 - Modelos Probabilísticos de Señales y Sistemas
##### Proyecto 4: Procesos aleatorios (segundo ciclo del 2022)

- Daymer Alberto Vargas Vargas, C08286
- Fabricio Jose Arguijo Cantillo, B70645
- Jafet Soto Arrieta, B77543

# Paquete `proceso`

> Este paquete se encarga de suministrar una serie de funciones con las cuales se logra obtener una secuencia aleatoria de un conjunto de datos de consumo de energía anual, graficar las funciones de densidad de cada hora del día, obtener la ocurrencia de
un evento en un rango de tiempo y potencia determinadas, obtener la autocovarianza y autocorrelación, brindar aspectos importantes de la función y realizar un análisis espectral de los datos.



## Módulo `proceso`

> Este módulo se encarga de suministrar una serie de funciones con las cuales se logra obtener una secuencia aleatoria de un conjunto de datos de consumo de energía anual a partir de un dataFrame,
graficar las funciones de densidad de probabilidad (pdf) de cada hora del día, y obtener la ocurrencia de
un evento en un rango de tiempo y potencia determinadas.

### Funciones de `proceso`

#### Demanda(inicio,final)
> La función demanda se encarga de retornar un dataFrame con los datos de consumo de potencia entre fechas específicas. Recibe como parámetros la fecha de inicio y fecha final.

#### densidad(DataFrame)
> La función retorna 3 variables, C, log y scale para construir la secuencia aleatoria P(t) mostrada en los resultados
estas variables contienen el polinomio de orden 7 necesario para construir la P(t). DIcha función necesita recibir una dataFrame con el consumo anual.

#### grafica(datos_df)
> Recibe un dataFrame de consumo anual y grafica las pdf de cada una de las horas del día.

#### probabilidad(datos_df, hora_1, hora_2, potencia_1, potencia_2)
> Obtiene la probabilidad de ocurrencia en un rango de horas determinadas y rango de potencia determinado. Sus entradas son el dataFrame, seguido de la hora inicial, hora final , potencia inicial y potencia final.
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

#### probabilidad(datos_df, hora_1, hora_2, p_1, p_2)
> El ejemplo expuesto en resultados tiene la forma: probabilidad(A0,0,23,1000,1500).
la probabilidad de que el consumo de potencia esté entre 1000 y 1500 a todo el día es de 0.5875250420977342.

(Descripción y análisis de resultados)

## Módulo `estacionaridad`
>El objetivo de este módulo es ser capaz de determinar si una secuencia aleatoria es estacionaria en sentido amplio, para luego determinar su promedio temporal y finalmente determinar si la secuencia es ergódica o no.

### Funciones de `estacionaridad`
#### WSS(A0)
>Esta funcion determina la estacionaridad en sentido amplio de una secuencia aleatorea, manteniedo los valores válidos en un factor del 5% de diferencia.

#### prom_temporal(c,A0)
>Esta función determina el promedio temporal para los valores
de consumo MW, se calcula tanto el valor numérico sujeto a
la función 'C' como el vector de promedio temporal para el
data frame de las horas.

#### ergodicidad(A0)
>Esta función determina la ergodicidad de la secuencia aleatoria
del consumo de MW que está en A0, utiliza el promedio temporal
calculado anteriormente y mantiene los valores validos dentro
del 5% de error.

## Resultados `estacionaridad`
#### WSS(A0)
>Al ingresar los valores del parámetro A0 se evalúa la media no puede cambiar más del
 5% para ser considerada "constante" y la autocorrelación será "igual" si no cambia
 más de un 5%.
Para determinar que un proceso es estacionario en sentido amplio se debe cumplir:
```math
E\left [ X(t)) \right ]=\overline{X} (constante)
```
```math
E\left [ X(t) X(t+\tau )\right ]=R_{xx}(\tau)
```
>Resultados generados:
Serie temporal estacionaria en sentido amplio.
#### prom_temporal(c,A0)
>Esta función debe calcular el promedio temporal para una función muestra de la secuencia aleatoria.
>La función del promedio temporal se define como:

```math
A\left [ * \right ]=\lim_{T\rightarrow\infty}\int_{-T}^{T}* dt
```
>Y para los parámetros evaluados la función retorna el valor de:
0.10358971035885703
#### ergodicidad(A0,C71)
>La función de ergodicidad determina si el proceso analizado es ergódico o no.
Utilizando el promedio temporal del proceso. Para que un proceso se considere ergódico debe cumplir que
>Resultados generados:  
> '------------El proceso no es ergódico----------'

## Módulo `Momentos`

>En este paquete se implementan dos funciones: autocorrelación y autocovarianza. En el caso de la primera función, se desea encontrar la correlación entre variables aleatorias por lo cual se considera t1 y t2. El procedimiento consiste en brindar como parámetros dos horas determinadas, además se guardan los datos de consumo en las variables establecidas.

>Para el caso de la segunda función, se desea encontrar la covarianza entre variables aleatorias por lo cual se considera t1 y t2. Al igual que la función mencionada anteriormente, se toman en cuenta como parámetros dos horas determinadas, para obtener los datos correspondientes.

>Por teoría, se conoce que la correlación entre dos variables X y Y esta dada de la siguiente manera:

```math
  R_{XY} = E[XY]
```

> donde:

```math
    R_{XY}= \int_{-\infty}^{\infty}\int_{-\infty}^{\infty} xy f_X,_Y(x,y) dxdy
```
 >Por otro lado, la covarianza entre dos variables X y Y esta dada de la siguiente manera:

```math
  C_{XY}= R_{XY} - E[X]E[Y]
```
> donde:

```math
    C_{XY} = \int_{-\infty}^{\infty}\int_{-\infty}^{\infty} (x-X)(y-Y) f_X,_Y(x,y) dxdy
```

## Resultados `Momentos`
>Con las funciones empleadas, se obtuvo el valor de la autocorrelación y autocovarianza, para las horas entre 3 y 12. Los resultados obtenidos con acordes a lo esperado según la teoría estudiada en el curso de MPSS.

#### Autocorrelación
>La autocorrelación entre las horas 3 y 12:
0.4733539038703084.

#### Autocovarianza
>La Autocovarianza entre las horas 3 y 12:
1957.7249063051345.

## Módulo `Espectro`

>En el caso de este paquete la función psd se encarga de calcular la densidad espectral de potencia de un proceso aleatorio. Para esto se considera como parámetros el dataFrame de consumo de energía, la hora inicial y la hora final. También esta función se encarga de generar la lista de datos como muestra con una cantidad definida de puntos en este caso 800. Con estos puntos se logra crear una gráfica que represente la densidad espectral de potencia para los datos que fueron seleccionados.

El espectro de densidad de potencia se define de la siguiente manera:

```math
    S_{xx}(f) = \lim_{T \to \infty} \frac{E[ X_T(\omega)^{2}]}{2T}

```
Donde P_{xx} puede ser calculado mediante la siguiente integral en el dominio de la frecuencia:

```math
    P_{XX}=\frac{1}{2\pi}\int_{-\infty}^{\infty} S_{XX}(\omega) d\omega
```

## Resultados `Espectro`

>Se obtuvo una gráfica que muestra la densidad espectral de potencia, la cual presenta un comportamiento acorde a los esperado. Se realizó la prueba en la terminal con el dato de 17 h.
La gráfica obtenida fue bastante precisa, ya que se puede observar que la densidad espectral de potencia se encuentra en un rango acorde según la teoría estudiada en el curso de MPSS. Además la frecuencia se mantuvo entre un rango de 0-50 Hz.
