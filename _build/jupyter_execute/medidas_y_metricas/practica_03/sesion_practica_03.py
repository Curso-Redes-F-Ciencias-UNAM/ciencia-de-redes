#!/usr/bin/env python
# coding: utf-8

# # Práctica 3 (notebook)

# <!-- esta celda no se renderizará en jupyter -->
# 
# ```{admonition} Ejecuta el notebook
# Para ejecutar este notebook da click en <i class="fas fa-download"></i> y descarga el archivo `.ipynb` para correrolo localmente en tu computadora o da click en <i class="fas fa-rocket"></i> para correlo en Binder o Google Colab.
# ```

# En este notebook se aplican los siguientes conceptos:
# - Medidas de grupos de nodos
#   - Coeficiente de agrupamiento (clustering): https://youtu.be/zH5oMNKtVoA
#   - Detección de comunidades: https://www.youtube.com/watch?v=pG5XKZqyFmk&t
# - Propiedades globales: https://youtu.be/FBu3yA0CdwY
#   - Componentes y máxima componente
#   - Medidas promedio
#   - Modularidad: https://www.youtube.com/watch?v=jlAZJqAqlTA&t
#   - Distribución de grado: https://youtu.be/nUi203c53lA
# 
# 
# La única función nueva que se importar para esta práctica es greedy_modularity_communities, se se encuentra en networkx.algorithms.community y es para la detección de comunidades según el algoritmo de Newman, Clauset y Moore (ver [documentación](https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.community.modularity_max.greedy_modularity_communities.html#networkx.algorithms.community.modularity_max.greedy_modularity_communities))

# In[ ]:


import networkx as nx
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from google.colab import files #solo para trabajar en Colaboratory

from networkx.algorithms.community import greedy_modularity_communities # para detección de comunidades


# ## Medidas de grupos de nodos
# 
# Para este notebook se utilizarán datos de redes reales. La importación de datos reales en un notebook se discute en la [práctica 2](https://www.youtube.com/playlist?list=PLCTzelSlkHdP2NZ-zKVwPqSbnw61b9eY7).
# 

# In[ ]:


files.upload()


# Aquí se utiliza una red de coautoría en trabajos de redes obtenida de www.networkrepository.com

# In[ ]:


ruta = 'ca-netscience.mtx'

datos = pd.read_csv(ruta,
            #nrows = 10,
            skiprows = 2,
            header = None,
            sep = ' ')
datos.columns = ['Nodo1', 'Nodo2']

G = nx.from_pandas_edgelist(datos, source = 'Nodo1', target = 'Nodo2')


# ### Clustering (coeficiente de agrupamiento o acumulación)

# En forma completamente análoga a las centralidades analizadas en la práctica 2, la función ```nx.clustering(G)``` arroja un diccionario que asigna a cada nodo un valor de agrupamiento (acumulación). Siguiendo el mismo procedimiento para visualizarlo, a continuación se convierte el diccionario en un arreglo y se introduce como argumento para la función ```nx.draw()```. Para esta red, el layout "Kamada kawai" ofrece una visualización adecuada; ustedes pueden explorar distintos diseños (ver [documentación](https://networkx.org/documentation/stable/reference/drawing.html) correspondiente)

# In[ ]:


diccionario = nx.clustering(G)
clus = np.array([ diccionario[i] for i in G ])


# In[ ]:


plt.figure(figsize = [8,8])
nx.draw_kamada_kawai(G,
                     node_color = clus,
                     node_size = 50,
                     cmap = 'plasma')


# Como se dice en la parte práctica, el coeficiente de clustering es una medida de cuánto se acumulan enlaces en grupos de nodos, o lo que es lo mismo, cuántos enlaces hay entre los nodos vecinos de un nodo. En esta imagen se utiliza el mapeo de color (```cmap```) plasma, que recorre del azul para valores pequeños al amarillo para valores grandes. A partir de ello se pueden identificar zonas de "alta densidad" de enlaces en amarillo y nodos azules, más bien aislados (relativamente).
# 
# Se recomienda explorar los distintos cmap disponibles para matplotlib: https://matplotlib.org/stable/tutorials/colors/colormaps.html

# ### Comunidades

# Como se explicó en el video correspondiente, algunos algoritmos de detección de comunidades utilizan el método de maximización de la modularidad. El empleado a continuación se basa en el método de Newman, Clauset y Moore proporcionado en la parte teórica. El método desarrollado por Blondel que se explicó con más detalle también está implementado en networkx y se les recomienda explorarlo e implementarlo. En su [documentación](https://python-louvain.readthedocs.io/en/latest/) viene un ejemplo que pueden copiar y pegar, introduciendo su red de trabajo.
# 
# Su implementación es inmediata, como se importó directamente, únicamente hay que aplicar la función a la red. Lo que arroja es una lista de objetos ```frozenset``` que agrupan a los nodos y cuya naturaleza no nos importa mucho aquí.

# In[ ]:


comunidades = greedy_modularity_communities(G)


# In[ ]:


comunidades


# Imitando los procedimientos anteriores en los que partimos de un diccionario y lo convertimos en arreglos, a continuación generamos un diccionario al que a cada nodo le asignará un valor numérico en función de a qué comunidad pertenece. Los pasos son los siguientes:
# - Se genera un diccionario vacío
# - Se hace un ```for``` sobre el objeto ```enumerate(comunidades)```; este objeto le asocia a cada elemento del iterable ```comunidades``` un índice, por eso en el ```for``` hay que introducir dos objetos.
# - Como cada elemento de ```comunidades``` es una "lista" de nodos, hacemos un ```for``` que los recorra y a cada uno se le asocia el índice que ```enumerate``` le asoció a su grupo.
# - Ya con ese diccionario, se puede generar el arreglo como se ha hecho hasta ahora.

# In[ ]:


diccionario = {}

for i, comunidad in enumerate(comunidades): #visita cada comunidad
  for nodo in comunidad: #visita cada nodo de la comunidad
    diccionario[nodo] = i 
    
diccionario


# In[ ]:


colors = np.array([diccionario[i] for i in G ])


# In[ ]:


plt.figure(figsize = [6,6])

nx.draw_kamada_kawai(G, node_color = colors, node_size = 50,
                     cmap = 'nipy_spectral')


# Para esta gráfica se utilizó un cmap que genera altos contrastes, en este caso no es tan conveniente usar los que generan un gradiente uniforme (a la percepción) pues buscamos que las comunidades se distingan. Ver de nuevo los mapeos de color [disponibles](https://matplotlib.org/stable/tutorials/colors/colormaps.html).
# 
# En este caso, como se explica en la parte teórica, se han detectado grupos de nodos que maximizan la modularidad; estos grupos son tales que la modularidad de la red es elevada. El significado de estas comunidades es labor del análisis de las propiedades de los elementos y puede ser una ruta de investigación del fenómeno en cuestión. En este caso (coautorías), si las comunidades corresponden a grupos de trabajo de universidades, publicaciones de áreas de conocimiento específicas, comunidades culturales o lingüísticas de los autores o regiones geográficas (por poner ejemplos) se revelará en un análisis de las propiedades de los autores que son representados por nodos.
# 
# En cada res particular, las comunidades pueden motivar estas reflexiones dependiendo del fenómeno del que se trate.
# 
# En la siguiente celda se prueba que tal partición de los nodos efectivamente arroja una modularidad alta; recordar que una modularidad mayor a 0.3 ya puede considerarse significativa, y que el 1 es una cota superior. La documentación de la función ```modularity``` también está [disponible](https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.community.quality.modularity.html#networkx.algorithms.community.quality.modularity).

# In[ ]:


nx.algorithms.community.modularity(G, comunidades)


# ## Propiedades globales

# ### Componentes
# Como se menciona en el video correspondiente a propiedades globales, es común que las redes estén formadas por varias componentes no conectadas entre sí. Esto es especialmente común en redes biológicas como la que se usa en este ejemplo (de tortugas). Muchas veces, como veremos con las redes aleatorias, el análisis del número y tamaño de las componentes es importante para la comprensión de los fenómenos. 
# 
# En otras ocasiones, algunas de las propiedades de las redes que hemos estudiado hasta ahora no están definidas para redes disconexas (por ejemplo, la centralidad de cercanía), y la solución puede ser analizar sólo la componente más grande.
# 
# A continuación se hace esto para el conjunto de datos 'reptilia-tortoise-network-fi' disponible en networkrepository.
# 

# In[ ]:


files.upload()


# In[ ]:


ruta = 'reptilia-tortoise-network-fi.edges'

datos = pd.read_csv(ruta, 
            #nrows = 10,
            header = None,
            sep = ' ')

G = nx.from_pandas_edgelist(datos, source = 0, target = 1)
nx.draw(G, node_size = 50)


# La función ```nx.connected_components(G)``` devuelve las componentes de la red en un objeto de tipo generador de python. Para su tratamiento basta con convertirlo en una lista.
# 
# Con tal lista de componentes y utilizando la función ```.subgraph()``` de la clase ```nx.Graph()``` se puede analizar por separado cada componente. En este caso se hace un bucle sobre todas las componentes y se grafica cada una:

# In[ ]:


componentes = list(nx.connected_components(G))
print("El total de componentes de la red es:", len(componentes))
for i, componente in enumerate(componentes):
  print('Componente ', i)
  plt.figure(figsize=[2,2])
  Gs = G.subgraph(componente)
  nx.draw(Gs, node_size = 50)
  plt.show()


# Para concentrase en la máxima componente se puede aprovechar que la función ```max()``` de python admite un argument ```key``` que permite definir la función con la que se medirán los objetos de la lista. En este caso, al introducir la función ```len```, que devuelve la longitud de una lista, nos regresará el elemento más largo de la lista de componentes, esto es, la máxima componente:

# In[ ]:


max_comp = max(componentes, key = len ) #nodos de la máxima componente


print("La máxima componente contiene %i de los %i nodos" %(len(max_comp), len(G)))
Gm = G.subgraph(max_comp)

nx.draw_kamada_kawai(Gm, node_size = 50)


# ### Medidas promedio y otras medidas globales

# Como veremos en la segunda parte del curso, los promedios de las propiedades de los nodos dan mucha información relevante de la red. Algunos vienen implementados en networkx y otros requieren que los calculemos. A continuación algunos ejemplos tanto de medidas promedio como de otras propiedades globales mencionadas en la parte teórica:

# In[ ]:


N = nx.number_of_nodes(G)

print("El grado promedio de la red es %.3f" %(2*nx.number_of_edges(G)/N))

print("El clustering promedio de la red es %.3f" %nx.average_clustering(G))

print("La distancia promedio en la máxima componente es %.3f" %nx.average_shortest_path_length(Gm))

print("El diámetro de la máxima componente es %.3f" %max(nx.eccentricity(Gm).values()))

print("El radio de la máxima componente es %.3f" %min(nx.eccentricity(Gm).values()))


# Aprovechemos este cálculo para verificar la que distancia promedio de una red disconexa no está bien definida y marca error:

# In[ ]:


nx.average_shortest_path_length(G)


# ### Distribución de probabilidad de grado

# Finalmente, a partir de la función ```.degree()``` de la clase ```nx.Graph()``` que devuelve una estructura similar a un diccionario, podemos utilizar el método usual (listas por comprensión) para generar un histograma de los grados de los nodos de la red; contar el número de nodos que tienen cierto grado:

# In[ ]:


G.degree()


# In[ ]:


diccionario = dict(G.degree)
grados = [ diccionario[i] for i in G]


distribucion = {}

for i in grados: #este bucle únicamente genera las claves del diccionario, asignándoles un valor de 0
  distribucion[i] = 0

for i in grados: #este bucle recorre todos los grados y cada vez que un valor aparece, suma uno a la cuenta de ese valor
  distribucion[i] += 1

distribucion


# In[ ]:


X = distribucion.keys()
Y = distribucion.values()

plt.figure(figsize = [15, 5])

plt.bar(X,Y)

plt.xlabel('Grado', size = 20)
plt.ylabel('# nodos', size = 20)
plt.xticks(ticks = range(1,max(X)+1),labels = range(1,max(X)+1), size = 15)
plt.yticks(size = 15)
plt.show()


# De este histograma se puede extraer información de la red. Por ejemplo que la mayoría de los nodos tienen grado 1 y predominan nodos con pocos enlaces, mientras que hay unas pocos nodos que tienen 16 y 17 enlaces.
# Tomando en cuenta que se trata de tortugas, podemos sacar conclusiones respecto al comportamiento social de este animal.

# In[ ]:




