# Introducción al modelo Watts-Strogatz

En resumen, el modelo de Erdős–Rényi nos sirvió para ejercitar nuestro análisis de redes, sin embargo falla en la mayoría de las propiedades de las redes reales. En la década de 1990, a raíz de la popularización  del internet y el inicio de la digitalización de muchos aspectos de la vida (sumado al cada vez mayor uso de computadoras para estudios en ciencias sociales y naturales), comenzaron a estar disponibles muchos datos relacionados con redes (de telecomunicación, tecnológicas, de internet, biológicas, sociales, etc.). Con el crecimiento de las redes disponibles para el análisis se generó un ambiente de búsqueda de modelos que pudieran dar cuenta de sus propiedades. 

En 1998 aparece un artículo de Watts y Strogatz que pretendía aportar un modelo que pudiera dar cuenta de dos de las propiedades que muchas de las redes reales tienen; propiedades que, dicho sea de paso, ya han sido probadas en la mayoría de los ejemplos reales trabajados por ustedes: el alto coeficiente de clustering y la propiedad de mundo pequeño.

La información de los dos modelos mencionados hasta ahora, en relación con las redes reales, se expone en el siguiente video.

<div class="iframe-container-out">
	<div class="iframe-container-in">
		<iframe src="https://www.youtube.com/embed/lerf221gOF8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
	</div>
</div>

Resulta ilustrativo revisar el abstract del artículo de Watts y Strogatz, publicado en Nature y titulado <a href="http://worrydream.com/refs/Watts-CollectiveDynamicsOfSmallWorldNetworks.pdf" target="_blank"><i>Collective dynamics of ‘small-world’ networks</i></a>:

> Networks of coupled dynamical systems have been used to model biological oscillators, Josephson junction arrays, excitable media, neural networks, spatial games, genetic controlnetworks and many other self-organizing systems. Ordinarily, the connection topology is assumed to be either completely regular or completely random. But many biological, technological and social networks lie somewhere between these two extremes. Here we explore simple models of networks that can be tuned through this middle ground: regular networks ‘rewired’ to introduce increasing amounts of disorder. We find that these systems can be highly clustered, like regular lattices, yet have small characteristic path lengths, like random graphs. We call them‘small-world’  networks,  by  analogy  with  the  small-worldphenomenon (popularly known as six degrees of separation). The neural network of the worm Caenorhabditis  elegans, the power grid of the western United States, and the collaboration graph of film actors are shown to be small-world networks. Models of dynamical systems with small-world coupling display enhanced signal-propagation speed, computational power, and synchronizability. In particular, infectious diseases spread more easily in small-world networks than in regular lattices.

En el siguiente apartado les proporcionamos un notebook para que generen intuición en torno a la propuesta de Watts-Strogatz para construir redes de mundo pequeño. Con las funciones generadas ustedes reproducirán, al final de esta semana, el principal resultado de su artículo.