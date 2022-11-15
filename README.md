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

## Funciones

### Demanda(inicio,final)
> La funcion demanda se encarga de retorna un dataFrame con los datos de consumo de potencia entre fechas especificas. Recibe como parámetros la fecha de inicio y fecha final.

### densidad(DataFrame)
> La funcion retorna 3 variables, C, log y scale para construir la secuencia aleatoria P(t)
estas variables contienen el polinomio de orden 7 necesario.

### grafica(datos_df)
> Recibe un dataFrame de consumo anual y grafica las pdf de cada una de las horas del día.

### probabilidad(datos_df, hora_1, hora_2, potencia_1, potencia_2)
> Obtiene la probabilidad de ocurrencia en un rango de horas determinados y rango de potencia determinado. Sus entradas son el dataFrame, seguido de la hora inicial, hora final , potencia inicial y potencia final

## Resultados

(Descripción y análisis de resultados)
