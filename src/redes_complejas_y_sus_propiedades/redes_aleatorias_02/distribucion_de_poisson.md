# Distribución de Poisson

Como se ejemplificó en la [práctica 4](https://curso-redes-f-ciencias-unam.github.io/ciencia-de-redes/redes_complejas_y_sus_propiedades/practica_04/sesion_practica_04_notebook.html#distribucion-de-probabilidad-de-grado) cuando el grado promedio $⟨k⟩$ (que depende de $p$ y $N$ como se explicó en el [capítulo anterior](https://curso-redes-f-ciencias-unam.github.io/ciencia-de-redes/redes_complejas_y_sus_propiedades/redes_aleatorias_01/grado_promedio_distribucion_de_grado_y_clustering.html#grado-promedio-distribucion-de-grado-y-clustering)) y $N$ satisfacen que $\frac{⟨k⟩}{N}≪1$ entonces tenemos que la distribución binomial se aproxima a una distribución de Poisson:

$$P_k = e^{-\left< k \right>} {{\left< k \right>^{k}}\over{k!}}$$


La demostración de este hecho está desarrollada con todo detalle en el [material complementario del segundo capítulo del libro de Barabasi](http://networksciencebook.com/chapter/3#advanced-a).

Nótese que la condición $\frac{⟨k⟩}{N}≪1$ es equivalente a $⟨k⟩≪N$ la cual es la propiedad de "escasez" de enlaces (_sparce_). Como se ha mencionado previamente esta propiedad la satisfacen la mayoría de las redes reales. Por lo tanto, si queremos comparar redes reales con el modelo de redes aleatorias podemos usar esta última aproximación la cual es más sencilla y conveniente analíticamente ya que la distribución de Poisson tiene un solo parámetro (el grado promedio $\left< k \right>$). En cambio la distribución Binomial tiene dos parámetros.
