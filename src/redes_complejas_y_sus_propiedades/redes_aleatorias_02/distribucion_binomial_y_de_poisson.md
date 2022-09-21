# Distribución biniomial y de Poisson

En la primera parte de la [práctica 4](../practica_04/sesion_practica_04_notebook) obtuvieron la distribución de grado y su ajuste mediante la distribución binomial de una red aleatoria. En el siguiente video se deduce formalmente este resultado:

<div class="iframe-container-out">
	<div class="iframe-container-in">
		<iframe src="https://www.youtube.com/embed/x8BCsk7BZy8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
	</div>
</div>

```{admonition} Corrección
:class: danger

En el minuto 4:20 se habla con cierta soltura de la anchura de la distribución. Se comete un error al hablar del segundo momento de la distribución $⟨k^2⟩$. La expresión $np(1−p)$ corresponde a la varianza, es decir $⟨k^2⟩−⟨k⟩^2$. En las imágenes ya está la corrección.
```
Como se ejemplificó, sin probar, en la práctica 4, si ocurre que el grado promedio (que depende de $p$ y $N$ como se explicó en la página anterior) y $N$ satisfacen que $\frac{⟨k⟩}{N}≪1$$ la distribución binomial se aproxima a una de Poisson.

$$P_k = e^{-\left< k \right>} {{\left< k \right>^{k}}\over{k!}}$$

Esto es de gran importancia porque para la mayoría de las redes reales de interés se satisface esta condición. Es de hecho la condición de "escasez" de enlaces en las redes reales. Esto facilitó la comparación entre las redes reales y la red aleatoria correspondiente (mismo tamaño $N$ y mismo grado promedio $\left< k \right>$).

La demostración de este hecho está desarrollada con todo detalle en el [material complementario del segundo capítulo del libro de Barabasi](http://networksciencebook.com/chapter/3#advanced-a).