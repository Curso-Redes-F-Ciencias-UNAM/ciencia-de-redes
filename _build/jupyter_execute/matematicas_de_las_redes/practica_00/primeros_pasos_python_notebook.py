#!/usr/bin/env python
# coding: utf-8

# # Práctica 0: primeros pasos con Python (notebook)

# ## Introducción
# En este curso utilizaremos python mediante el uso de **notebooks**. Éstos se pueden abrir en Google Colab o pueden ser archivos tipo `.ipynb` que se abren con [Jupyter](https://jupyter.org/). La forma más sencilla para installar Jupyter en sus computadoras es a travéz de Anaconda (una distribución de python). Para ello se recomienda visitar la [página oficial de Anaconda](https://www.anaconda.com/) y seguir las instrucciones.
#  
# En primer lugar, un notebook es una calculadora. Ahí se pueden realizar las operaciones suma, resta, multiplicación, división, potencia, etc. Basta con escribir la operación y "correr" la celda; para ello puedes presionar el botón correspondiente a la izquierda de la celda o puedes presionar `Shift + Enter`.
#  
# A continuación se presentan algunas operaciones "comentadas", es decir, antecedidas por el signo `#` (en python, todo lo que esté a la derecha de ese signo será ignorado), puedes borrar el signo `#` al inicio y correr la celda cada vez para obtener cada resultado. Nóta que cada celda puede ser corrida tantas veces como quieras. Es común que en alguna línea se ponga una explicación con el uso de otro signo `#`; aquí se hace para explicarle a las personas no familiarizadas con algunas operaciones matemáticas los nombres de éstas, pero puede ser un buen hábito comentar el código que generemos (como veremos más adelante).

# In[ ]:


#8*5  

#5+6+7

#8/2

#8**6   #potencia

#(5*8 + 6)**2/100

#13 // 5 #parte entera de la division

#13 % 5  #residuo de la division


# ## Importar paquetes
# Para utilizar otras funciones matemáticas será necesario importar una librería. Aquí utilizaremos la librería Numpy que viene por defecto en Anaconda. Esta librería tiene una cantidad inimaginable de funciones y objetos matemáticos de los que utilizaremos unos cuantos (para más información visita [la página oficial de numpy](https://numpy.org/)) 
# 
# Ahora se introduce una forma estándar para importar las librerías. La estructura es: `import <libreria> as <clave>`. La clave será la forma con la que "invocaremos" a la librería en nuestro código. Si bien la clave puede ser cualquier conjunto de letras, en foros, tutoriales y documentaciones suele haber convenciones que también utilizaremos aquí. En este caso, se suele importar a numpy con la clave `np`.
# 
# Después correr la siguiente celda, podrás utilizar todas las funciones y objetos de la librería durante la misma sesión. Esto significa que no hay que estar importando en todo momento la librería.

# In[ ]:


import numpy as np


# 
# Ya habiendo importado la librería, cualquier objeto o función de esa librería se invoca mediante `np.[funcion]`.
# 
# A continuación se introducen algunas funciones y constantes matemáticas cargadas en numpy para que empieces a utilizarlas. De nuevo, "descomenta" las líneas para obtener cada resultado.

# In[ ]:


## FUNCIONES

#np.cos(50) #coseno

#np.exp(5) #exponencial

#np.sqrt(10) #raiz cuadrada


# In[ ]:


## CONSTANTES

np.pi  #numero pi

#np.e   #constante de Euler


#np.cos(2*np.pi)


# ## Bucle `for`
# La estructura básica de python que hace falta dominar (al menos para toda la primera parte de este curso) es el bucle ```for``` que comprenderemos a partir del ejemplo de la siguiente celda:

# In[ ]:


for i in range(10):
    print(i)


# Como podrás ver, lo único que ocurrió es que se mostraron los números del 0 al 9. Los elementos importantes son:
# - ```range(N)``` es una estructura que genera una "iteración" de ```N``` números empezando por el cero.
# - ```print()``` es una función cuyo argumento se muestra en la pantalla
# 
# Así, la instrucción del bucle podría leerse entonces como "para cada elemento de la lista [0, ..., 9], muestra dicho elemento".
# 
# En general, el bucle ```for``` tiene la siguiente estructura:
# 
# ```
# for elemento in iterable:
#    función(elemento)
# ```
# Los dos puntos de la primera línea y la sangría de la instrucción son importantes (esta última se genera de forma automática en jupyter y casi cualquier editor de textos, pero puede ser causa de errores).
# Para familizarizarte con la lógica, juega con la siguientes celdas. Como antes, puedes "descomentar" y comentar cada línea para ver cómo cambia el resultado:

# In[ ]:


for i in range(10):
  #print(i)
  #print(i-1)
  #print(2*i)
  #print(i**2)
  #print(2**i)


# ### Ejercicios `for`
# Mediante el uso de las estructuras ```for``` y ```range()```, genera un bucle que produzca los siguientes resultados:
# 1. Imprimir todos los números del 0 al 15
# 2. Imprimir todos los números del 1 al 15
# 3. Imprimir los números pares menores que 20
# 4. Imprimir los números impares menores e iguales a 25. 

# In[ ]:


# Ejercicio 1


# In[ ]:


# Ejercicio 2


# In[ ]:


# Ejercicio 3


# In[ ]:


# Ejercicio 4


# ## Listas
# Otra estructura de python que utilizaremos son las listas. Las listas se construyen con corchetes y sus elementos se separan con comas. Las listas pueden contener números enteros, números flotantes (con punto decimal), cadenas alfanuméricas o cualquier otra estructura de python, inclusive listas.
# 
# En los primeros ejercicios de este curso las utilizaremos para hacer listas de nodos y luego emplearlas para construir enlaces de forma ordenada.
# 
# A continuación se detallan algunos aspectos sobre el empleo de listas en python.

# In[ ]:


# se construye una lista de diez elementos
lista = [1,5,9,4,8,7,2,6,3,0]


# Para acceder a cualquier elemento de la lista se puede escribir su nombre y, entre corchetes, indicar la entrada (el índice) que quieres extraer. 
# 
# Nota: en python, cuando se habla de índices se inicia a contar desde el cero, esto es, el 0 indica el primer elemento, el 1 el segundo, y así sucesivmente.
# 
# En la siguiente celda descomenta los distintos renglones para ver el resultado, y compáralo con la lista creada más arriba.

# In[ ]:


lista[0]
#lista[1]
#lista[8]
#lista[10]


# Como habrás notado, y por lo dicho antes, la lista tiene diez elementos, pero sus índices llegan hasta el 9 por haber iniciado en 0. Si introduces un índice mayor al tamaño de la lista obtendras un error.
# 
# Uno de los aspectos de las listas que nos resultarán más útiles en la primera práctica es la posibilidad de acceder a sus elementos mediante índices negativos. El -1 corresponde al último, el -2 al penúltimo, y así el resto.
# 
# En la siguiente celda vuelve a hacer lo mismo:

# In[ ]:


lista[-1]
#lista[-8]
#lista[-10]
#lista[-11]


# Utilizando los mismos índices, es posible extraer "subconjuntos# de la lista mediante el uso de el símbolo ":" y la estructura 
# 
# ```[limite inferior:limite superior]```
# 
# Observa que el subconjunto siempre **contiene** al límite inferior y **no contiene** al superior:
# 

# In[ ]:


lista[2:6]
#lista[6:9]
#lista[:5]
#lista[-4:]


# Nota: Como puedes ver en los últimos dos ejemplos, no indicar el límite inferior o el límite superior se entiende como "todos los elementos a la izquierda que", o "a la derecha que", respectivamente.

# Las listas, por contener elementos "iterables", se puede utilizar dentro de la estructura ```for``` para realizar las operaciones dentro del bucle. A continuación se ponen dos ejemplos, uno de con números y otro con cadenas. Notar la flexibilidad de la estructura ```for``` que permite elegir el nombre del iterable  (no es necesario que sea ```i``` como hasta ahora hemos hecho).
# También se muestra cómo imprimir varias cosas en una misma línea, introduciendo varios argumentos separados por comas.

# In[ ]:


for numero in lista:
  print('El elemento es', numero, 'y su cuadrado es', numero**2)


# In[ ]:


lista2 = ['Esta', 'es', 'una', 'lista', 'de', 'cadenas', 'las', 'cadenas', 'deben', 'ir', 'entre', 'comillas.']

for cadena in lista2:
  print(cadena)
  #print(2*cadena)


# Nota la diferencia entre multiplicar números y multiplicar números por cadenas.

# La función en python para agregar nuevos elementos a una lista antes creada es **append()**
# 
# A continuación se muestra su uso:

# In[ ]:


A = []  # se crea una lista vacía, sin elementos
print(A)
A.append(5)
print(A)


# In[ ]:


for i in range(5):
  A.append(i)

print(A)


# Para finalizar con las listas, observemos qué resulta al sumar listas o al multiplicarlas por un éntero:

# In[ ]:


lista + lista2
#lista+lista
#2*lista2
#2*A+lista


# ### Ejercicios de listas
# 1. Define dos listas vacías, una llamada pares y otra impares

# In[ ]:


#Ejercicio 1


# 2. Mediante el uso de ```for``` y la función ```append```, agrega a la lista ```pares``` el cero y los números pares **menores** que 20

# In[ ]:


# Ejercicio 2


# 3. Igual que el inciso anterior, agrega a la lista ```impares``` los números impares **menores o iguales** que 21.

# In[ ]:


#Ejercicio 3


# ## Arreglos de numpy

# La estructura básica de numpy que utilizaremos es ```array()``` (arreglo) que recoge muchas de las propiedades de los vectores y las matrices.
# 
# En primer lugar, cualquier lista puede usarse para definir un arreglo y cambiar sus propiedades, particularmente en lo que se refiere a la multiplicación y la suma:

# In[ ]:


arreglo = np.array(lista)


# In[ ]:


2*arreglo #notar la diferencia con el caso de 2*lista


# Si dos arreglos tienen el mismo tamaño, su suma y su resta tienen un sentido vectorial:

# In[ ]:


arreglo1 = np.array([1,2,3,4,5,6])
arreglo2 = np.array([2,4,6,8,10,12])


# In[ ]:


arreglo1 + arreglo2
#arreglo1 - arreglo2
#arreglo1 * arreglo2
#arreglo1**2


# Analizando los últimos dos ejemplos, ¿qué interpretación tiene2 la multiplicación de dos arreglos o el cuadrado de un arreglo?
# 
# Si se quiere recoger el sentido del producto (interno) de vectores se puede usar la función ```np.dot()``` o la función 
# 

# In[ ]:


np.dot(arreglo1, arreglo2)


# Como se dijo antes, una lista puede tener listas como elementos. Si una estructura así se convierte en un arreglo se obtiene algo como una matriz:

# In[ ]:


Lista2d = [[1,2,3],[6,5,4], [7,8,9]] #una lista de tres listas, cada una con tres elementos

Arreglo2d = np.array(Lista2d) #matriz de tres por tres

Arreglo2d


# In[ ]:


2*Arreglo2d
#-1*Arreglo2d
#Arreglo2d**2


# Algunos arreglos de interés vienen como funciones de numpy, particularmente 
# - ```np.zeros([n,m])``` (arreglo de $n\times m$ hecho de puros ceros)
# -  ```np.ones([n,m])``` (arreglo hecho de puros unos)
# - ```np.random.rand(n,m)``` arreglo de números aleatorios entre 0 y 1
# 
# para más información, visitar https://numpy.org/

# In[ ]:


np.zeros([2,4])


# In[ ]:


np.ones([2,3])


# In[ ]:


np.random.rand(5,4)


# Mediante la misma estructura de índices que en las listas, se pueden acceder a los elementos de un arreglo con la ventaja de que para arreglos de dimensión 2 y mayores, se puede utilizar la notación que usamos para matrices. A continuación un ejemplo:

# In[ ]:


R = np.random.rand(4,4)
print(R)


# Descomentando cada línea, verifica qué resultado se obtiene con los distintos índices de la matriz generada:

# In[ ]:


R[0]
#R[1]
#R[2]
#R[1,3]
#R[3,1]


# Mediante el uso de los índices se puede sustituir el valor de una de las entradas de un arreglo. Como ejemplo, a continuación se modifica un elemento del arrelgo ```R``` antes creado:

# In[ ]:


print(R)

R[1,1] = 10


# In[ ]:


print(R)


# ### Ejercicios de arreglos
# 1. Genera los arreglos ```arreglo_pares``` y ```arreglo_impares``` convirtiendo las listas generadas en los ejercicios anteriores en arreglos.
# 2. Suma, resta, multiplica y **divide** ambos arreglos.
# 3. Contesta: ¿qué significado tiene la división de arreglos de numpy?

# In[ ]:


# Ejercicio 1


# In[ ]:


# Ejercicio 2


# In[ ]:


# Ejercicio 3


# 4. Genera un arreglo cuya entrada ```[i,j]``` sea la multiplicación de la entrada ```[i]``` del arreglo ```arreglo_pares``` y la entrada ```[j]``` del arreglo ```arreglo_impares```.
# Recomendación:
#   - Identifica la longitud de los arreglos y llámalo ```L```
#   - Genera un arreglo de puros ceros de dimensión $L \times L$ y llámalo ```A```
#   - Mediante un for dentro de otro for, sustituye los elementos de ```A``` por los productos de las entradas de los arreglos (este último paso se pone a continuación, tú debes hacer los primeros dos pasos):

# In[ ]:


## haz los primeros pasos


## a continuacion se proporciona el tercer paso
for i in range(L):
  for j in range(L):
    A[i,j] = arreglo_pares[i]*arreglo_pares[j]


# ## Importar NetworkX y Matplotlib

# En la primera parte de este curso, además de Numpy, serán fundamentales otras dos librerías que ya están integradas en anaconda: en NetworkX están definidos todos los objetos y funciones de redes que usaremos y en Pyplot hay muchas funciones para visualizar información. Pyplot está contenida en otra librería llamada Matplotlib.
# Más información en https://matplotlib.org/ y https://networkx.org/
# 
# En la siguiente celda se importan ambas librerías con sus claves convencionales:

# In[ ]:


import networkx as nx
import matplotlib.pyplot as plt


# En los siguientes notebooks y videos se explican las funciones más importantes relacionadas con las redes que utilizaremos.
