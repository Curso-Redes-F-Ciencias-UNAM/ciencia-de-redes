# Distribución de grado tipo ley de potencia 

En esta sección se implementan las funciones para verificar si la distribución de grado de una red real satisface una ley de potencia y, si es el caso, se calcula el parámetro α obtenido del ajuste de los datos.

Estos videos mezclan las explicaciones teóricas con la implementación computacional. La idea es que ustedes reproduzcan la implementación con la red que eligieron y que produzca un [notebook como el que se construye en los videos](https://colab.research.google.com/drive/1oGSWm6w661Pt7fwhz75hHDPvbiscs63S?usp=sharing).

## Importar redes pesadas

Lo primero que se hace es mejorar todavía más el procedimiento para importar los datos del grado, que es lo que nos importa en esta parte, optimizando los recursos con los que disponemos.

<div class="iframe-container-out">
	<div class="iframe-container-in">
		<iframe src="https://www.youtube.com/embed/Yti5CVRpoeQ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
	</div>
</div>

## Inspección y PDF

<div class="iframe-container-out">
	<div class="iframe-container-in">
		<iframe src="https://www.youtube.com/embed/Yt24plMYQTQ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
	</div>
</div>

## CCDF: función de distribución complementaria acumulada

<div class="iframe-container-out">
	<div class="iframe-container-in">
		<iframe src="https://www.youtube.com/embed/rfpt_Tn5Xc4" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
	</div>
</div>

## Estimación por máxima verosimilitud

<div class="iframe-container-out">
	<div class="iframe-container-in">
		<iframe src="https://www.youtube.com/embed/He3zAbTdirQ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
	</div>
</div>

:::{admonition} Nota

Para profundizar más en el tema se recomienda revisar {cite:t}`Clauset_2009`.

:::

## Implementación de la estimación

<div class="iframe-container-out">
	<div class="iframe-container-in">
		<iframe src="https://www.youtube.com/embed/q4UjNbrcdr0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
	</div>
</div>

## Paquetería powerlaw

<div class="iframe-container-out">
	<div class="iframe-container-in">
		<iframe src="https://www.youtube.com/embed/8h2TqIBnLvo" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
	</div>
</div>

:::{admonition} Nota

Para profundizar en el tema se recomienda consultar {cite:t}`Alstott_2014` y la [documentación oficial de `powerlaw`](https://pypi.org/project/powerlaw/)
:::