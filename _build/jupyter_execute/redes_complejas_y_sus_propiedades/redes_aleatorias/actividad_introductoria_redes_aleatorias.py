#!/usr/bin/env python
# coding: utf-8

# # Actividad introductoria a las redes aleatorias (notebook)
# En este notebook se introduce la noción de red aleatoria de Erdős-Rényi. Posteriormente se introducen dos métodos para generarlas como objetos de networkx y comenzar a analizar sus propiedades. Particularmente nos concentraremos en:
# - número de enlaces
# - valor esperado del grado
# - coeficiente de acumulación esperado
# - distribución de grado
# 
# ## Definiciones
# Una red aleatoria es aquella en la que la asignación de los enlaces se hace a partir de un mecanismo aleatorio. Hay dos tipos de definiciones posibles:
# - Modelo $G(N,L)$ en el que se fijan el número de nodos $N$ y el número de enlaces $L$. Los enlaces se asignan de forma aleatoria entre los nodos, esto es, se seleccionan aleatoriamente $L$ parejas de nodos, de entre las $\frac{N(N-1)}{2}$ parejas posibles.
# - Modelo $G(N,p)$ en el que la probabilidad de que entre dos nodos haya un enlace es igual a $p\le1$.
# En este notebook se usa esta última definición.
# 
# A continuación se proporcionan dos funciones. Una es para generar los enlaces aleatorios (las parejas) entre los $N$ nodos, dada la probabilidad $p$. La otra es para generar la red a partir de los nodos y los enlaces previamente generados.

# In[ ]:


import networkx as nx
import numpy as np
import matplotlib.pyplot as plt


# ## Definición según probabilidad de enlace
# La siguiente funcion ```enalces_aleatorios``` recibe como parámetros el número de nodos $N$ y la probabilidad de enlace entre pares $p$. Lo que hace es recorrer, mediante dos bucles anidados (uno dentro de otro) todas las parejas de nodos. Para cada pareja de nodos, genera un número aleatorio entre 0 y 1 mediante la función de numpy ```np.random.rand()``` y si este es menor que $p$, registra el enlace.
# 
# Deben poner atención a que en esta ocasión no se utiliza la instrucción ```return``` al final de la definición. En su lugar se utiliza la instrucción ```yield```, que es un generador que permite dar múltiples salidas a la función. Además tiene la ventaja de que la información que se genera no ocupa espacio en la memoria, aunque tiene la desventaja de que después de utilizar la información una vez, ya no se puede volver a utilizar. Para más información pueden googlearlo, aquí un ejemplo: https://www.geeksforgeeks.org/use-yield-keyword-instead-return-keyword-python/
# 
# En resumen, la función ```enlaces_aleatorios(N,p)``` es un generador de parejas de nodos, es decir de enlaces. Estas parejas serán utilizadas en la función ```red_aleatoria``` para generar una red de $N$ nodos enlazados según la probabilidad $p$. Lo único que hace esta última es generar el objeto ```nx.Graph()```, agregar los nodos y agregar los enlaces.

# In[ ]:


def enlaces_aleatorios(N, p):
  for i in range(N):
    for j in range(i):
      if np.random.rand() < p:
        yield i,j

def red_aleatoria(N, p):
  G = nx.Graph()
  G.add_nodes_from(range(N)) # agrega todos los nodos
  
  G.add_edges_from( enlaces_aleatorios(N, p) ) # agrega los enlaces obedeciendo la probabilidad p
  
  return G


# En la siguiente celda pueden jugar con el número de nodos y la probabilidad, para empezar a explorar visualmente las características cualitativas de la red: ¿está formada por una o más componentes?, ¿hay nodos aislados?
# 
# Pueden jugar con las funciones ```nx.draw()``` o sus derivadas ```nx.draw_circular()```, la kamada_kawai, etc.

# In[ ]:


N = 100
p = .2

nx.draw(red_aleatoria(N,p))


# ## Definición con matriz de adyacencia aleatoria
# A continuación se les propone otra implementación, esta vez basada en la matriz de adyacencia. Básicamente se genera una matriz con las propiedades de una matriz de adyacencia (formada por ceros y unos, diagonal igual a cero, simétrica) en la que la entrada correspondiente a cada enlace tiene valor 1 con probabilidad $p$, y 0 con probabilidad $p-1$. Después se utiliza la función ```nx.from_numpy_array()``` para convertir esa matriz de adyacencia en su representación como red.
# 
# Para la implementación se utilizan las siguientes funciones:
# - ```np.ones((N,N))```: genera un arreglo de numpy de dimensión $N\times N$ de puros 1's.
# - ```np.triu()```: a partir de un arreglo de numpy, genera su matriz triangular superior (upper triangular). El parámetro ```k``` que recibe indica a partir de cuál diagonal generar la matriz triangular. ```k = 0``` respeta la diagonal principal, aquí necesitamos que la diagonal principal sea de ceros, por lo que utilizamos ```k = 1```
# - ```np.random.rand(N,N)```: genera un arreglo de numpy de dimensión $N\times N$ de números aleatorios entre 0 y 1.
# - Nota: observen cómo se puede aplicar el comparador $<$ al arreglo de numpy, lo cual tendrá como resultado una matriz de valores booleanos (True / False) que después puede multiplicarse por la matriz triangular superior. La multiplicación que se realiza es ```A*B```, no es una multiplicación matricial sino una multiplicación elemento a elemento. En este caso, el valor True toma el valor 1 y False el valor 0.
# 
# Ya que se generó la matriz triangular superior, se genera la matriz de adyacencia sumando la triangular y su transpuesta, que sería una triangular inferior.
# 
# En la siguiente celda pueden variar los valores de $N$ y $p$ y visualizar el resultado

# In[ ]:


N = 100
p = .1

A = np.triu(np.ones((N,N)), k = 1)*(np.random.rand(N,N) < p)
A = A.T + A

plt.imshow(A)


# ### Ejercicio 1
# Utilicen el código anterior para crear la matriz de adyacencia para generar una función que tome los parámetros $N$ y $p$ y regrese (```return```) la red aleatoria correspondiente

# In[ ]:


def red_aleatoria(N,p):
    ### aqui debes definir la matriz de adyacencia como se hizo antes
    
    
    ### aqui debes utilizar la funcion nx.from_numpy_array()
    ### para gererar la red. Usa el nombre G


    ###
    return G


# ## Número esperado de enlaces
# A partir de cualquiera de las dos definiciones utilizadas hasta ahora, se pueden estudiar las propiedades de la red aleatoria. Empezaremos con el estudio de el número de enlaces.
# 
# Algo a tomar en cuenta es que al tratarse de una red de carácter aleatorio, cada vez que generemos una debemos considerarla una realización. Cada realización tendrá propiedades distintas: distinto número de enlaces, distinta distribución de grado, distinto grado promedio, coeficiente de acumulación, etc. Para estudiar las propiedades de la red aleatoria en abstracto, debemos considerar cada realización como parte de un conjunto (o un ensemble) de redes aleatorias de las que estudiaremos sus propiedades estadísticas. 
# 
# Particularmente, el número esperado de enlaces se estudiará generando muchas redes aleatorias, contando el número de enlaces de cada una y promediando sobre todas las redes (realizaciones).
# 
# Recordar que cada red tiene la propiedad ```.edges``` que es la lista de todos sus enlaces. Con esa propiedad y la funcion ```len()``` sabremos cuántos enlaces tiene cada red. En la siguiente celda puedes jugar con el número de nodos y la probabilidad $p$ para contar el número de enlaces. Corre varias veces la celda con los mismos parámetros para verificar que cada realización tiene distinto número de enlaces:

# In[ ]:


N = 100
p = .1
G = red_aleatoria(N,p)

len(G.edges)


# ### Ejercicio 2
# Mediante un ```for``` genera muchas realizaciones (corridas) y guarda el número de enlaces $L$ de cada una en una lista. Mediante la función de numpy ```np.mean()``` puedes obtener el promedio sobre todas las corridas, es decir, el valor esperado del número de enlaces.

# In[ ]:


# elige los valores para N, p y el numero de corridas
N = 
p = 
corridas = 

lista_L = []  # esta linea define una lista sin elementos a la que se iran agregando los valores de L
for i in range(corridas):
    
    #####
    ##### inician campos a rellenar:
    #En la siguiente linea genera una red aleatoria con los parametros indicados
    G = 
    
    #Ahora calcula el numero de enlaces de la red generada
    L = 
    
    ##### terminan campos a rellenar
    #####
    
    
    lista_L.append(L) #aqui se agrega el valor de L a la lista


print('El valor esperado de L es ', np.mean(lista_L))


# ¿Puedes encontrar una expresión del valor esperado de $L$ que relacione a $N$ y $p$? (Redondea el valor esperado para muchas corridas, digamos 1000)
# 
# #### Distribución de probabilidad de L
# Ahora se generará un histograma de frecuencias de los valores de $L$ para ver cómo se comportan.
# Para ello utilizaremos la función ```np.histogram()``` que recibe una lista o arreglo y regresa el histograma. Los parámetros que utilizamos son:
# - ```bins = range(N*(N-1)/2)```: los bins son las "cajitas" dentro de las cuales se agrupará y contará a los valores. Al dar esta instrucción estamos diciendo que tome cajas uniformes, con los valores desde 0 hasta N(N-1)/2 (el máximo valor posible para L, tal y como vimos la primera semana)
# 
# Lo que regresa la función ```histogram``` es primero las cuentas de los valores para cada intervalo y luego los extremos de los intervalos en sí. Por ello debemos guardar ambas cantidades como $y$ y $x$, respectivamente. 

# In[ ]:


y, x = np.histogram(lista_L, bins = range(int(N*(N-1)/2)))


# A continuación se puede visualizar el histograma. Como el arreglo $x$ representa los valores extremos de los intervalos, tiene un valor extra, por eso debemos excluirlo al momento de graficar (por eso se indica ```x[:-1]```, que equivale a todos los elementos menos el último)
# 
# Como podrás ver, los valores de $L$ están muy concentrados. Mediante la asignación de valores ```xmin``` y ```xmax``` puedes utilizar la instrucción ```plt.xlim()``` para acotar tu gráfica en el dominio donde veas que se concentran los valores. Así puedes analizar la estructura de la distribución con más detalle.
# **Debes descomentar esas líneas y asignar los valores xmin y xmax**

# In[ ]:


plt.plot(x[:-1], y)

#xmin =
#xmax = 
#plt.xlim([xmin, xmax])


# ## Grado promedio esperado
# ### Ejercicio 3

# Ya que tienes el valor esperado del número de enlaces se puede calcular el valor esperado del grado promedio, mediante la expresión que obtuvimos la primera semana:
# $$\left<k\right> = \frac{2L}{N}$$
# 
# Con esto, ¿podrías encontrar una expresión para $\left<k\right>$ que relacione a $N$ y $p$? 

# ## Coeficiente de acumulación promedio
# ### Ejercicio 4
# Genera redes aleatorias para distintos valores de $N$ y $p$. Para cada una calcula su coeficiente de acumulación promedio (varias veces para cada uno, a ver si encuentras una regularidad).
# 
# ¿Podrías encontrar una expresión para $\left<C\right>$ (coeficiente de acumulación promedio) en términos de $N$ o $p$?

# In[ ]:


N = 
p = 

G = red_aleatoria(N,p)
print('El coeficiente de acumulación promedio es:\n', nx.average_clustering(G))


# ## Distribución de grado
# Finalmente, realizaremos un análisis de la distribución de grado de las redes. Para ello, mediante un bucle ```for``` generaremos redes aleatorias y obtendremos, para cada una, el histograma de grados. Cada histograma lo agregaremos a un histograma acumulado (sobre todas las corridas) con el que podremos obtener el promedio de la distribución de grado para todas las corridas. Algunas consideraciones:
# - Vamos a generar histogramas como ya se hizo antes, pero ahora los grados sólo pueden ir de 0 a $N-1$, por lo que le damos un ```bins = range(N)```
# - Antes del ```for```, generamos un arreglo de puros ceros, con longitud $N-1$. Ahí se van a sumar los histogramas de cada realización para luego dividirlo entre el número de corridas y nos dará la distribución promedio sobre todas las corridas.
# - El histograma lo hacemos bajo la misma lógica que cuando hicimos la distribución de grado en la sesión práctica 4 (https://www.youtube.com/watch?v=FFq40_AXhSM) pero ahora utilizando la función ```histogram```.
# 
# 
# ### Ejercicio 5
# Juega con distintos valores de $N$, $p$ y el número de corridas para observar cómo se modifica el histograma. ¿Podrías encontrar una relación entre $N$, $p$ y el comportamiento cualitativo del histograma? (su centro, su anchura, su altura, etc.)
# 

# In[ ]:


N = 
p =
corridas =


Y = np.zeros(N-1)

for i in range(corridas):
    G = red_aleatoria(N,p)
    y, x = np.histogram([dict(G.degree)[i] for i in G], bins = range(N))
    Y += y
Y = Y/corridas

plt.figure(figsize = [10,5])
plt.bar(x[:-1],Y)

