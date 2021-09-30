# Grado promedio, distribución de grado y clustering

A partir del número de enlaces esperado se puede obtener una expresión para el grado promedio (esperado) de la red aleatoria

$$\left< k \right> = p(N-1)$$

Sin embargo, el grado promedio también puede obtenerse a partir de las propiedades de la distribución binomial, que también describe a la distribución de grado de la red aleatoria. Se tiene entonces que la distribución de grado de la red es

$$P_k = \left( \begin{array}{c}N-1 \\ k \end{array}\right) p^{k}(1-p)^{N-1-k}$$

La derivación de esta distribución de grado está desarrollada en el siguiente video:

<div class="iframe-container-out">
	<div class="iframe-container-in">
		<iframe src="https://www.youtube.com/embed/8JMnTvABvAs" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
	</div>
</div>

Igualmente, el razonamiento introducido a partir de la probabilidad de enlace, nos permite derivar que el coeficiente de clustering de los nodos de una red aleatoria obedece $\left< C_i \right> = p$ como se deduce en el siguiente video:

<div class="iframe-container-out">
	<div class="iframe-container-in">
		<iframe src="https://www.youtube.com/embed/2rJG0f73F1w" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
	</div>
</div>