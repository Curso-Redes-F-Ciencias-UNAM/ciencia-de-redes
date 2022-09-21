# Número de enlaces

Como la definición de la red aleatoria está relacionada con procesos probabilísticos, para estudiar sus propiedades debemos hacer un análisis estadístico. Para ello tenemos que considerar las propiedades, no de una red, sino de un conjunto de redes (ensemble) del que analizaremos las propiedades promedio.

La primer propiedad a considerar es el número de enlaces que se espera que tenga una red dados su tamaño $N$ y la probabilidad de enlace entre dos nodos $p$. Para ello se puede hacer un análisis computacional, como el de la [introducción](./actividad_introductoria_redes_aleatorias), aunque también se puede resolver analíticamente como se hace en le siguiente video. 

<div class="iframe-container-out">
	<div class="iframe-container-in">
		<iframe src="https://www.youtube.com/embed/iVbz1DTxhto" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
	</div>
</div>

En resumen, el número esperado de los enlaces que tendrá la red $G(N,p)$ es

$$\left< L  \right> = p \frac{N(N-1)}{2}$$

y la distribución de probabilidad del número de enlaces, $P_L$ del ensemble de redes aleatorias es una distribución binomial

$$P_L = \left(\begin{array}{c} \frac{N(N-1)}{2} \\ L \end{array}\right) p^L (1-p)^{\frac{N(N-1)}{2} -L}$$

Las implicaciones cualitativas de esta distribución de probabilidad se exploran en la introducción a las redes aleatorias.