# Distribución de grado

La distribución de grado de una red aleatoria también es una binomial:

$$P_k = \left( \begin{array}{c}N-1 \\ k \end{array}\right) p^{k}(1-p)^{N-1-k}$$

En el siguiente video se deduce este resultado:

<div class="iframe-container-out">
	<div class="iframe-container-in">
		<iframe src="https://www.youtube.com/embed/x8BCsk7BZy8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
	</div>
</div>

```{admonition} Corrección
:class: danger

En el minuto 4:20 se habla con cierta soltura de la anchura de la distribución. Se comete un error al hablar del segundo momento de la distribución $⟨k^2⟩$. La expresión $np(1−p)$ corresponde a la varianza, es decir $⟨k^2⟩−⟨k⟩^2$.
```
