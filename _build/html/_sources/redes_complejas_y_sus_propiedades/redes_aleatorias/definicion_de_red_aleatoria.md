# Definición red aleatoria

<div class="iframe-container-out">
	<div class="iframe-container-in">
		<iframe src="https://www.youtube.com/embed/Nqv-lgi-xvo" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
	</div>
</div>

Una red aleatoria es aquella en la que la asignación de los enlaces se hace a partir de un mecanismo aleatorio. Hay dos tipos de definiciones posibles:

- **Modelo** $G(N,L)$ en el que se fijan el número de nodos $N$ y el número de enlaces $L$. Los enlaces se asignan de forma aleatoria entre los nodos, esto es, se seleccionan aleatoriamente $L$ parejas de nodos, de entre las $\frac{N(N-1)}{2}$ parejas posibles.
- **Modelo** $G(N,p)$ en el que la probabilidad de que entre dos nodos haya un enlace es igual a $p\le 1$.

En el notebook de la introducción a las redes aleatorias se usa esta última definición.
