# Transición de fase en redes aleatorias

En la introducción a las redes aleatorias se lanzó la pregunta de qué condición deben cumplir $N$ y $p$ para que, con alta probabilidad, se tenga una red conectada. Resulta intuitivo que mientras mayor sea la probabilidad de enlace $p$ más probable es que la red tenga una sola componente; menos intuitivo, pero también es fácil ver que mientras mayor sea el tamaño de la red $N$ es más probable que ésta sea conexa.

Para hacer un análisis más cuantitativo, se proporciona un [notebook que introduce el análisis del tamaño de la máxima componente promedio para un _ensemble_ de redes aleatorias](https://colab.research.google.com/drive/1EI8Yjs5ZoH4HremySaDLcmSc3TgB7_NL?usp=sharing), confirmando el resultado obtenido por Erdős-Renyi y presentado por [Barabasi en la sección 3.6 de su libro](http://networksciencebook.com/chapter/3/#evolution-network). 

Aquí, se observa que la red aleatoria posee una componente gigante (cuyo tamaño es comparable con el número de nodos de la red) a partir de que $N$ y $p$ cumplen

$$1≤⟨k⟩=p(N−1)≃pN$$

teniendo, en el límite $N→∞$, una transición de fase en $⟨k⟩=1$, analizada por [Erdős y Renyi en su artículo de 1959](https://www.renyi.hu/~p_erdos/1959-11.pdf). Para un análisis más detallado de la transición de fase se recomienda el apartado 12.5 (Giant component) del [libro de Newman](https://www.dropbox.com/s/14xchb0u9hlbigz/Mark%20Newman-Networks_%20An%20%20Introduction-Oxford%20University%20Press%20%282010%29.pdf?dl=0). Estos análisis arrojan que el tamaño de la máxima componente es igual a $N$ con alta probabilidad cuando se cumple la condición $⟨k⟩≥\ln N$ que sería la respuesta a la pregunta del cuestionario introductorio.

En el notebook, para optimizar el tiempo de cálculo, se juega con el tamaño de los ensembles y el tamaño de la red pues para redes con muchos nodos, networkx tarda en correr los algoritmos de selección de componentes. En él encontrarán el comportamiento de las redes para $N$ en cinco órdenes de magnitud.
