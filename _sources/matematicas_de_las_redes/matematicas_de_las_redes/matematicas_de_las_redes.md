# Matemáticas de las redes

## Introducción

Este capítulo contiene cinco videos y una lista de referencias para que cada quien adquiera las herramientas matemáticas mínimas necesarias para el análisis de redes y fenómenos que estudiaremos en las siguientes semanas del curso. Los contenidos están ordenados de la siguiente forma:

- [Tipos de redes y matriz de adyacencia](./tipos_de_redes_y_matriz_de_adyacencia.md) (video 20 min)
- [Definición de grado](./definicion_de_grado.md) (video 4 min)
- [Motivación y más tipos de redes](./motivacion_y_mas_tipos_de_redes.md) (lectura)
- [Matriz de adyacencia y sus propiedades](./matriz_de_adyacencia_y_sus_propiedades.md) (video 12 min)
- [Número de nodos y enlaces](./numero_de_enlaces_de_la_red.md) (video 10 min)
- [Caminos y distancia entre nodos](./caminos_y_distancia_entre_nodos.md) (video 11 min)


## Tipos de redes y matriz de adyacencia

En el siguiente video (20 min) presentamos la definición de matriz de adyacencia, una representación matemática de las redes que tendrá varias aplicaciones en el análisis de sus propiedades, y se introducen las caracterísiticas de cuatro tipos de redes: 

1. Redes simples
1. Resdes dirigidas
1. *Multiredes* o redes con multienlaces
1. Redes ponderadas o redes con pesos

<div class="iframe-container-out">
	<div class="iframe-container-in">
		<iframe src="https://www.youtube.com/embed/Qva6zeEppqU" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
	</div>
</div>

## Motivación y más tipos de redes

A continuación se listan algunos apartados breves del libro de Barabasi {cite}`barabasi_2016_network_science` para que ustedes lean por su cuenta y profundicen su comprensión de las redes y algunas propiedades de las redes reales. Aunque sería conveniente que revisaran todo el capítulo, algunos de los temas que omitimos en esta selección están contenidos en los videos o serán revisados en las siguientes semanas. Otros no son de tanta importancia para los análisis que haremos en este curso.

El cuestionario de esta semana estará basado en los ejercicios de este capítulo.

Contenidos para revisión individual:

- Motivación. [2.1 The Brideges of Königsberg](http://networksciencebook.com/chapter/2#bridges)
- Relación redes - gráficas. [2.2 Networks and Graphs](http://networksciencebook.com/chapter/2#networks-graphs)
- Redes poco densas. [2.5 Real Networks are Sparse](http://networksciencebook.com/chapter/2#real-networks)
- Redes bipartitas. [2.7 Bipartite Networks](http://networksciencebook.com/chapter/2#bipartite-networks)
- Conectividad o conexidad. [2.9 Connectedness](http://networksciencebook.com/chapter/2#connectedness)

Recuerda que cualquier duda que tengas puedes externarla en el foro de dudas. Eso seguro enriquecerá al grupo entero.

## Matríz de adyacencia y sus propiedades

En el siguiente video se analizan algunas propiedades de la matriz de adyacencia para de ella comprender algunas características de las redes de interés para el estudio de redes complejas y redes reales que haremos en las siguientes partes del curso. 

<div class="iframe-container-out">
	<div class="iframe-container-in">
		<iframe src="https://www.youtube.com/embed/qo7Ecy0fXAg" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
	</div>
</div>

## Número de enlaces de la red

A continuación se analizan alguna de las condiciones impuestas sobre el número de enlaces de una red, particularmente para una red simple. De ahí se extraen conclusiones en torno al grado promedio de la red, que intuitivamente se puede asociar con su densidad.


<div class="iframe-container-out">
	<div class="iframe-container-in">
		<iframe src="https://www.youtube.com/embed/6jAKmae-D6I" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
	</div>
</div>

:::{admonition} Material complementario
Si les interesa profundizar más en el tema aquí les dejamos unas [notas sobre redes tipo árbol y algunas de sus propiedades matemáticas](https://www.matem.unam.mx/~ilan/2011/1/graficas/Graficas20111-arboles.pdf).
:::

## Caminos y distancia entre nodos

A partir de las propiedades de la matriz de adyacencia, particularmente sus potencias, se pueden obtener el número de caminos y la distancia entre nodos. Eso se explica en el último video de este bloque.

<div class="iframe-container-out">
	<div class="iframe-container-in">
		<iframe src="https://www.youtube.com/embed/92SEew75HQw" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
	</div>
</div>

:::{admonition} Nota
Estas últimas propiedades de las potencias de la matriz de adyacencia también se generalizan sin cambios a las redes dirigidas.
:::