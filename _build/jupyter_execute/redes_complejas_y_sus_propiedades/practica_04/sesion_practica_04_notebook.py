#!/usr/bin/env python
# coding: utf-8

# # Práctica 4 (notebook)
# En este notebook se coninúa el análisis de las redes aleatoria de Erdős-Rényi conocidas como $G(N,p)$. Se termina con el análisis de algunas propiedades sobre las que se profundizará en algunos videos esta semana, particularmente:
# - la distribución de grado de una red aleatoria satisface una distribución binomial
# - la distribución de grado de una red aleatoria cuando $\frac{\left< k\right>}{N} \ll 1 $ (condición satisfecha en general por las redes reales) tiende a una distribución de Poisson
# 
# Con esto en mente, aplicaremos este primer modelo analítico a la descripción de una red real. La conclusión que podemos adelantar es que casi ninguna de las redes reales de interés son bien modeladas por las redes aleatorias.

# In[ ]:


import networkx as nx
import numpy as np
import matplotlib.pyplot as plt


# Se utilizará la primera definición de red aleatoria que se propuso en la práctica anterior, es decir, a partir de la probabilidad de enlace:

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


# ## Distribución (de probabilidad) de grado
# Lo último que se hizo la práctica pasada fue el histograma de grados, o distribución de grados, como función de $N$ y $p$. A continuación se recupera la celda de la práctica anterior con la que se obtuvo $N_k$, es decir, el número de nodos que tienen grado $k$
# 

# In[ ]:


N = 101
p = .5
corridas = 100


Y = np.zeros(N-1)

for i in range(corridas):
    G = red_aleatoria(N,p)
    y, x = np.histogram([dict(G.degree)[i] for i in G], bins = range(N))
    Y += y
Y = Y/corridas

plt.figure(figsize = [10,5])
plt.bar(x[:-1],Y)
plt.xlabel('k', size = 10)
plt.ylabel('Nk', size = 10)
plt.title('Red aleatoria, N = %i, p = %1.2f' %(N,p), size = 20)


# La única modificación que se hará a partir de ahora es aquella referente a pasar de $N_k$ a $P_k$, es decir, pasar del histograma a la distribución de probabilidad mediante $P_k = N_k / N$. Esto se puede hacer directamente utilizando el parámetro ```density``` de la función ```np.histogram```. 
# 
# Como se verá en los videos, la distribución de probabilidad de grado de la red aleatoria es una distribución binomial, por lo que la importaremos a continuación. De este modo, a la distribución de grado se puede incorporar la binomial correspondiente. Consideraciones:
# - la variable ```x```, que se crea con la función ```histogram```, es un arreglo correspondiente al dominio, es decir, los número naturales hasta $N-1$. Por ser un arreglo se le puede aplicar también una función.
# - la función que se le aplica es la función ```binom.pmf()```, que dentro del conjunto de funciones que importamos con ```binom```, es la que proporciona la *probability mass function*, es decir, la distribución de probabilidad que nos interesa. Esa es la que graficamos en rojo. Para más información: https://docs.scipy.org/doc/scipy-0.14.0/reference/generated/scipy.stats.binom.html
# 
# 
# Jueguen nuevamente con $N$ y $p$ para ver cómo se relacionan con la distribución de probabilidad. También jueguen con el número de corridas para ver cómo aumentan o disminuyen las fluctuaciones respecto a la línea base; no perder de vista que estamos frente a un experimento estocástico.

# In[ ]:


from scipy.stats import binom 


# In[ ]:


# Se definen los parámetros
N = 101
p = .5
corridas = 500

# Y es el arreglo en el que se acumularán las observaciones para luego promediarlas
Y = np.zeros(N-1)

for i in range(corridas):
    G = red_aleatoria(N,p)
    y, x = np.histogram([dict(G.degree)[i] for i in G], bins = range(N), density = True)
    Y += y

# Se obtiene el promedio sobre todas las corridas
Y = Y/corridas


# Se genera la gráfica
plt.figure(figsize = [10,5])
# La distribución de probabilidad como gráfica de barras
plt.bar(x[:-1],Y, label = 'Pk') 

# La distribución binomial como una línea roja. Se grafica la función binomial de x, contra x.
plt.plot(x[:-1], binom.pmf(x[:-1],N-1,p), 'r', label = 'Binomial')

# Se ponen los títulos de los ejes y la gráfica
plt.xlabel('k', size = 20)
plt.title('Red aleatoria, N = %i, p = %1.2f' %(N,p), size = 20)
plt.legend()


# Ahora se utilizará la expresión que encontraron en la práctica pasada que relaciona al valor esperado del grado promedio* $\left< k \right>$ con $N$ y $p$, $$\left< k \right> = p(N-1)$$ para fijar $\left< k \right>$ y variar el tamaño de la red. Lo que queremos es una forma de comparar las distribuciones de probabilidad de redes distintas y la mejor forma de hacerlo es obligarlas a tener el centro (el valor esperado) en el mismo punto. 
# 
# *Notar que estamos hablando de dos tipos de promedios: $\left< k \right>$ es el promedio sobre el conjunto de nodos, se toma el grado para cada nodo y se promedia, para cada red. Por otro lado, se está tomando el promedio de esa cantidad sobre un conjunto de corridas o, lo que es lo mismo, un conjunto (ensemble) de redes aleatorias. Por eso hablamos de valor esperado del grado promedio. Se podría usar la notación $E[\left< k \right>]$ para referirnos a ese valor esperado, pero en los libros de consulta no lo hacen así que llamamos a advertir la diferencia y evitar confusiones.
# 
# Juega con $\left< k \right>$, el número de corridas y los tamaños de la red para ver cuál es el efecto sobre la distribución:

# In[ ]:


k = 50 # se fija el valor para el grado promedio. La única condición es que debe ser menor que N. 


corridas = 10 # se puede variar el número de corridas. Si es demasiado alto puede tardar mucho para redes grandes


plt.figure(figsize = [10,5])
for N in [100, 500, 1000]: #se tomarán tres redes distintas, para N igual a 100, 500 y 1000. Pueden agregar más grandes pero es posible que tarde mucho
    p = k/(N-1)
    
    Y = np.zeros(100-1)

    for i in range(corridas):
        G = red_aleatoria(N,p)
        y, x = np.histogram([dict(G.degree)[i] for i in G], bins = range(100), density = True)
        Y += y
    Y = Y/corridas



    

    plt.plot(x[:-1],Y, 'o', label = 'N = '+str(N))
    plt.plot(x[:-1],binom.pmf(x[:-1],N-1,p))

plt.xlim([0,100])
plt.legend()


# Ya que se verifica que la distribución de probabilidad es una binomial (además se demuestra con todo detalle en uno de los videos) verificaremos que si $N$ y $\left< k \right>$ satisfacen cierta condición podemos trabajar con una distribución de Poisson. Esto se hace ya no con las redes, sino con las correspondientes distibuciones, ya que generar redes aleatorias con más de 10000 nodos puede requerir mucha memoria.
# 
# Lo que se hace a continuación es, nuevamente, fijar la $\left< k \right>$ y tomar las distribuciones para redes de cuatro órdenes de magnitud. Todas se comparan con la distribución de Poisson correspondiente, para eso importamos ```poisson``` y usamos ```poisson.pmf()```:

# In[ ]:


from scipy.stats import poisson


# In[ ]:


plt.figure(figsize = [10,5])

k = 50
x = np.arange(100)

# Se utilizan cuatro N's en cuatro órdenes:
for N in [10**2, 10**3, 10**4, 10**5]:
    p = k/(N-1)

    plt.plot(x[:-1],binom.pmf(x[:-1], N-1, p), label = 'N = '+str(N))

    

plt.xlim([0,100])

plt.plot(x[:-1], poisson.pmf(x[:-1], 50), 'k--', label = 'Poisson')

plt.legend()
plt.title('Distribuciones binomiales <k> = 50', size = 20)
plt.xlabel('k', size = 20)
plt.ylabel('pmf(k)', size = 20)

#plt.xlim([45, 55])
#plt.ylim([0.05, 0.06])


# Se puede ver que para $N = 10^4$, más o menos dos órdenes de magnitud mayor a $\left< k\right> = 50$, la distribución binomial es indistinguible de la de Poisson. Para revisar la deducción analítica de este límite, pueden ver los temas avanzados del capítulo 3 del libro de Barabasi : http://networksciencebook.com/chapter/3#advanced-a

# ## Coeficiente de acumulación (agrupamiento) de los nodos
# En la práctica pasada se vio cómo el coeficiente de acumulación promedio de la red aleatoria coincide con la probabilidad de enlace $p$. Sin embargo, esta es una propiedad no sólo del promedio, sino que es equivalente para el mismo coeficiente en cada uno de los nodos. Para verificar eso, a continuación se grafica el coeficiente para cada nodo y se compara con los valores de $p$ y $\left< C \right>$
# 
# De nuevo, jugando con los valores de $N$ y $p$ pueden generar la intuición de que es una propiedad general, aunque se revisará analíticamente en los videos de la semana.

# In[ ]:


N = 100
p = .7



G = red_aleatoria(N,p)
C = nx.average_clustering(G)
print('El coeficiente de acumulación promedio es:\n', C)
print('La probabilidad de enlace p es:\n', p)

diccionario = nx.clustering(G)
Y = [diccionario[i] for i in G]

plt.figure(figsize = [15,5])
plt.plot(Y, 'o', label = 'C_i')
plt.plot([0,N], [p,p], 'r--', linewidth = 2, label = 'p')
plt.plot([0,N], [C,C], 'k--', label = 'C (prom)')
plt.ylim([0,1])

plt.legend()
plt.xlabel


# Esta propiedad es relevante para cuando queramos aplicar el modelo de redes aleatorias a redes reales, como se hará a continuación.

# ## Comparación del modelo de red aleatoria con redes reales
# El modelo de red aleatoria ha resultado muy útil para aplicar los conceptos matemáticos que hemos venido estudiando hasta ahora. Ahora corresponderá utilizar este modelo para intentar describir el comportamiento de redes reales. La suposición principal detrás de esto sería pensar que las interacciones entre los elementos del sistema están dadas de forma aleatoria. Eso tendría consecuencias particularmente en propiedades como su grado promedio, su distribución de grado y el coeficiente de clustering de los nodos. Esas mismas propiedades son las que analizaremos en las redes reales.
# 
# En la siguiente celda deben seleccionar el archivo de los datos que hayan elegido. Recuerden que si están trabajando en colab, deben utilizar ```files``` para subir el archivo (líneas comentadas). También recuerden el procedimiento para preparar los datos, descrito en la práctica 2 https://www.youtube.com/watch?v=tD7-9yM-xLA
# 

# In[ ]:


import pandas as pd

from google.colab import files
archivo = files.upload()



# In[ ]:


ruta = ''

datos = pd.read_csv(ruta,
            nrows = 10,
            #skiprows = 0,
            #header = None,
            #sep = ' ',
            #usecols = [0,1]
            )
datos


# In[ ]:


G = nx.from_pandas_edgelist(datos, source = 0, target = 1)


# Ya que se creó la red como objeto de networkx, vamos a encontrar sus propiedades generales (número de nodos, número de enlaces, grado promedio y coeficiente de clustering promedio). Además, a la red le asociaremos la probabilidad de enlace $p$ **que le correspondería *si fuera* una red aleatoria**, es decir: 
# 
# $$p = \frac{\left< k \right>}{N-1}$$ 
# 
# a partir de sus propiedades empíricas $N$ y $\left<k\right>$. 
# 
# La intención de esto es, a partir de esa $p$ que junto con $N$ caracteriza a una red aleatoria $G(N,p)$, determinar las propiedades de la red aleatoria equivalente. En otras palabras, calcularemos las propiedades de la red aleatoria (el modelo) que tiene el mismo tamaño y el mismo grado promedio que nuestra red real, para luego compararlas con las propiedades de nuestra red real. Así, podremos ver si el modelo de red aleatoria se ajusta a nuestra red real.  Las propiedades que usaremos para la comparación son:
# - Coeficiente de clustering promedio
# - Distribución de grado
# - Coeficiente de clustering por nodo, en distintas representaciones.
# 

# ### Coeficiente de clustering promedio
# Recordemos que el coeficiente de clustering promedio de una red aleatoria es exactamente igual a $p$. Compararemos el coeficiente de clustering promedio de la red y lo compararemos con la $p$ correspondiente:

# In[ ]:


N = len(G)
L = len(G.edges)
k = 2*L/N
C = nx.average_clustering(G)

p = k / (N-1)
print('Propiedades generales de tu red:')
print('- El número de nodos es:\t', N)
print('- El número de enlaces es:\t', L)
print('- El grado promedio es:\t\t', k)

print('\n\nEl coeficiente de clustering promedio de la red es:\n', C)
print('\nEl coeficiente de clustering que tendría la red si fuera aleatoria (es decir p) es:\n', p)


# **Pregunta 1**
# Hablando de la primera propiedad a comparar, el coeficiente de clustering promedio:
# 
# ¿consideras que el modelo de red aleatoria se ajusta a la red real que estás utilizando?

# ### Distribución de grado
# Para analizar las siguientes dos propiedades vamos a hacer una tabla con el grado y el clustering de cada nodo. Para ellos se utilizarán diccionarios y un objeto de ```pandas``` que se llama ```DataFrame``` que no es más que una tabla, pero con funciones muy útiles implementadas. El procedimiento es el siguiente:
# - se generan los diccionarios de las propiedades que nos interesan, en este caso el grado y el clustering, como ya lo hemos venido haciendo. Los grados los convertimos a diccionario aplicando ```dict()```, y el clustering (como casi todas las medidas de centralidad) ya es un diccionario.
# - Esos diccionarios se introducen, en una lista, como primer argumento de la funcion ```pd.DataFrame()``` que, como las claves de ambos diccionarios son los mismos nodos, generará una tabla en la que a cada nodo le asocia sus dos propiedades. 
# - En la tabla que se genera, las propiedades son los renglones y los nodos son las columnas. No es la forma más conveniente para trabajar, así que la transponemos mediante la instrucción ```.T```. Entonces, cada fila será un nodo y las columnas son las propiedades de interés.
# - Se definen los nombres de las columnas, en este caso Degree y Clustering.
# - Todo esto lo guardamos en una variable ```df``` (de dataframe)
# 

# In[ ]:


# se generan los diccionarios
grado_dict = dict(nx.degree(G))
clustering_dict = nx.clustering(G)


# In[ ]:


# se genera el dataframe (la tabla)
df = pd.DataFrame([grado_dict, clustering_dict]).T
df.columns = ['Degree', 'Clustering']
df


# Para analizar la distribución de grado utilizaremos la función histogram que ya hemos usado, pero ahora aplicada a la columna 'Degree' de nuestra tabla. Para acceder a una columna completa basta con escribir el nombre de la tabla (en este caso ```df```) y, seguido de un punto, el nombre de la columna. Sabemos que ```np.histogram``` toma como argumento un arreglo de numpy. Para convertir la columna de la tabla en un arreglo, basta con agregarle, seguida de un punto, la instrucción ```values```. A continuación puedes ver la columna de la tabla y, si descomentas el resto de la línea, puedes verla convertida en arreglo:

# In[ ]:


df.Degree#.values


# A las columnas de un dataframe también se les pueden aplicar funciones. A continuación le aplicamos la función ```.max()``` que arroja el grado máximo de la red que utilizaremos para hacer el histograma. Se guardará ese valor como ```K``` para usarlo después.

# In[ ]:


K = df.Degree.max()


# Esto ya se introduce en la función histogram. Notar que ahora el parámetro ```bins``` será un ```range``` aplicado a ```K + 1```, para que cuente el número de nodos que tienen grado desde 0 hasta $k_{max}$. No olvidar que ```bins``` son las "cajitas" dentro de las cuales cuenta el número de elementos y el ```+1``` corresponde a que en python suele omitirse el límite superior. Así, ```range(K+1)``` es la colección [0, 1, 2, ..., K].

# In[ ]:


y,x = np.histogram(df.Degree.values, bins = range(int(K)+1), density= True)


# Ya con el histograma, se grafican tanto la distribución de probabilidad empirica" de la red real, y la distribución de Poisson que correspondería al valor $p$ calculado. Ésta sería la distribución de probabilidad esperada si la red fuera una red aleatoria.

# In[ ]:


plt.figure(figsize = [15,5])
plt.bar(x[:-1], y, label = 'pk')
plt.plot(x[:-1], poisson.pmf(x[:-1], k), 'r--', label = 'poisson') 

plt.ylim([0.5*y[y>0].min(),1.1*y.max()])
plt.xlim([0,100])
plt.legend()
plt.title('Comparación de la red real con la red aleatoria equivalente\n(N = %i, p = %.4f)' %(N,p), size = 20)
plt.xlabel('k', size = 20)


# **Pregunta 2** 
# 
# ¿Consideras que la distribución de grado de la red aleatoria correspondiente se ajusta a la distribución de grado de la red real que estás analizando?
# 
# 
# Para algunas redes reales, sobre todo aquellas muy grandes, conviene graficar la distribución de grado en escala "log-log". Volveremos a ello más adelante en el curso, pero por lo pronto se realiza la gráfica en esa escala con algunos parámetros que hace adecuada la visualización:

# In[ ]:


plt.figure(figsize = [15,5])
plt.plot(x[:-1], y, '.', label = 'Pk')
plt.plot(x[:-1], poisson.pmf(x[:-1], k), 'r--', label = 'poisson')

#Se aplica escala logarítmica a ambos ejes
plt.xscale('log')
plt.yscale('log')

#parámetros adecuados para la visualización:
plt.ylim([0.5*y[y>0].min(),2*y.max()])
plt.legend()

plt.title('Comparación de la red real con la red aleatoria equivalente. Escala "log-log"\n(N = %i, p = %.4f)' %(N,p), size = 20)
plt.xlabel('k', size = 20)


# ### Clustering de los nodos
# Finalmente, compararemos el clustering de los nodos medido para nuestra red real con el equivalente para la red aleatoria equivalente. Ya sabemos que para una red aleatoria, el coeficiente de clustering es igual (salvo fluctuaciones) a la probabilidad de enlace $p$. A continuación se hace la comparación para tres representaciones distintas del coeficiente de clustering de los nodos.
# 
# 
# #### Representación 1
# Primero se grafica el coeficiente de clustering de los nodos ordenándolos según su etiqueta. Sabemos que la etiqueta de los nodos es prácticamente arbitraria, por lo que podemos afirmar que no hay un orden en su aparición. Para esta gráfica se utiliza la columna 'Clustering' de la tabla antes creada, mediante ```df.Clustering``` y se le aplica la función ```.plot()``` con algunos parámetros para su visualización. En la misma gráfica es muestran el valor que predice el modelo de red aleatoria $\left<C'\right> = p$ y el valor de $\left<C\right>$ empírico.

# In[ ]:


plt.figure(figsize = [15,5])
df.Clustering.plot(style = 'b.', alpha = .4)

plt.plot([0,N], [p,p], 'r--', linewidth = 3, label = 'p = %.4f' %p)
plt.plot([0,N], [C,C], 'k--', linewidth = 3, label = '<C> = %.4f' %C)

plt.xlabel('nodo i', size = 20)
plt.ylabel('C(i)', size = 20)
plt.legend()


# **Pregunta 3** ¿El coeficiente de clustering que el modelo predice para cada nodo, se ajusta al coeficiente de clustering de los nodos de tu red?
# 
# #### Representación 2
# A continuación se hace lo mismo, pero ordenando los nodos según su grado. Esto se hace ordenando los elementos de la tabla ```df``` según el valor de la columna 'Degree' (```.sort_values('Degree')```), reasignando los índices según este nuevo orden (```.reset_index()```), tomando la columna 'Clustering' (```.Clustering```) y graficándola (```.plot()```). Nuevamente se compara con los valores del promedio y el modelo.
# 
# Esta representación permitiría observar si hay alguna correlación entre el grado del nodo y su coeficiente de clustering.

# In[ ]:


plt.figure(figsize = [15,5])
df.sort_values('Degree').reset_index().Clustering.plot(style = 'b.', alpha = .4)

plt.plot([0,N], [p,p], 'r--', linewidth = 3, label = 'p = %.4f' %p)
plt.plot([0,N], [C,C], 'k--', linewidth = 3, label = '<C> = %.4f' %C)

plt.xlabel('nodo i', size = 20)
plt.ylabel('C(i)', size = 20)
plt.legend()


# **Pregunta 4** ¿Detectas alguna correlación o patrón interesante entre el grado y el clustering de los nodos?
# 
# 
# #### Representación 3
# Finalmente, bajo la misma lógica que la anterior, se representan el clustering promedio de los nodos, agrupados según su grado. Esto limpia un poco el ruido de la representación anterior y revelaría de forma más clara si hubiera alguna correlación entre las magnitudes del grado y el clustering de los nodos. Se utiliza otra función muy poderosa de ```pandas``` llamada ```groupby```. Sin entrar en la complejidad de esta función, se explica cada parte del código a continuación por si quieren usarlo en problemas similares:
# - se agrupan los elementos de la tabla ```df``` (i.e. los nodos) según el valor del grado: ```.groupby('Degree')```
# - de la tabla agrupada, se considera sólo la columna 'Clustering': ```['Clustering']```
# - de la propiedad 'Clustering' de los datos ya agrupados, se calcula el promedio: ```.mean()```
# - ahora se forman los arreglos correspondientes al grado y al promedio del clustering aplicando tres funciones seguidas: ```.reset_index().values.T```
# - estos arreglos se guardan como X y Y, respectivamente, para graficarlos
# 

# In[ ]:


X, Y = df.groupby('Degree')['Clustering'].mean().reset_index().values.T


# Así, se grafican entonces el coeficiente de clustering promedio del grupo de nodos con grado $k$, que denotamos como $C(k)$. De nuevo, se indican los valores del promedio empírico y el predicho por el modelo de red aleatoria para sacar conclusiones:

# In[ ]:


plt.figure(figsize=[15,5])
plt.plot(X, Y, '.')

plt.plot([0,K], [p,p], 'r--', label = 'p = %.4f' %p)
plt.plot([0,K], [C,C], 'k--', label = '<C> = %.4f' %C)

plt.xlabel('k', size = 20)
plt.ylabel('C(k)', size = 20)
plt.legend()


# **Pregunta 5** En esta representación, ¿encuentras alguna correlación o patrón interesante entre los valores de $k$ y $C$?
