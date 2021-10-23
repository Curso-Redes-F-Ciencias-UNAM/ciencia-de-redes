# Redes aleatorias y propiedad de mundo pequeño

Como pudieron ver en la [Práctica 4](../practica_04/sesion_practica_04_notebook.ipynb), el modelo de red aleatoria hace dos predicciones que fallan en la mayoría de las redes generadas a partir de datos reales; a decir un coeficiente de clustering constante (y relativamente bajo) y una distribución de probabilidad de grado tipo Poisson que, dicho sea de paso, subestima los nodos con grado bajo y prohíbe nodos con grados mucho mayores que el promedio. Prácticamente la totalidad de los ejemplos elegidos por ustedes no se ajustan al modelo de red aleatoria por las mismas razones.

Sin embargo, hay una propiedad de las redes aleatorias que sí parece describir una características de las redes reales: la propiedad de mundo pequeño. En pocas palabras, esta propiedad da cuenta de un [fenómeno conocido en ciencias sociales](https://en.wikipedia.org/wiki/Six_degrees_of_separation); aunque la población de un país, o del mundo entero, es muy grande, es fácil conectar a cualesquiera dos nodos con relativamente pocos enlaces. Es fácil conectar a cualesquiera dos personas en el mundo buscando entre los conocidos de sus conocidos, en menos de 10 pasos, que para una población de más de 6 mil millones de personas, son muy pocos. 

Las redes aleatorias tienen esa propiedad, cuando hacemos crecer mucho el tamaño de la red, la distancia entre cualesquiera dos nodos no crece de forma lineal. Además, como se puede ver en el siguiente video, la red aleatoria nos da un criterio para medir cuándo se puede afirmar que una red tiene la propiedad de mundo pequeño.

<div class="iframe-container-out">
	<div class="iframe-container-in">
		<iframe src="https://www.youtube.com/embed/AJHtyr3brD8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
	</div>
</div>

En resumen, se puede afirmar que una red tiene la propiedad de mundo pequeño si su distancia promedio $⟨d⟩$ y el número de nodos $N$ satisfacen

$$⟨d⟩ \sim \frac{\ln N }{\ln ⟨k⟩}$$

Para generar un poco de intuición al respecto de esta propiedad, en redes aleatorias, pueden jugar con la simulación alojada en este <a href="https://colab.research.google.com/drive/1HdTtz7tdSfO00pZDI18Ad_3CPJK3eWe9?usp=sharing" target="_blank">notebook</a>.


<!-- TODO: juntar esta página con su respectivo notebook -->