# Ciencia de Redes

Este es el repositorio donde se aloja la página del curso **Ciencia de Redes** que se imparte en la Facultad de Ciencias de la UNAM.

---

## Organización del repositorio

Este repositorio consta de 2 carpteras:

- `/src` : la cual contiene todos los archivos fuente del libro (aquí se deben realizar todas las modificaciones necesarias). El contenido de esta carpeta está ordenado de acuerdo a la estructura de un [Jupyter Book](https://jupyterbook.org/intro.html).
- `/_build` : la cual contiene todo el código html de la página (el contenido de esta carpeta no debe modificarse).

## Requisitos

Instalar [ghp-import](https://pypi.org/project/ghp-import/):
```
python -m pip install ghp-import
```

Para evitar conflictos se recomienda trabajar en un [ambiente virtual](https://docs.python.org/3/tutorial/venv.html).

Crear ambiente virtual:
```
python -m venv .venv
source .venv/bin/activate
```
Instalar paquetes de python requeridos:
```
python -m install -r requirements.txt
```

## Edición de página

1. Clona este repositorio:
```
git clone "https://github.com/Curso-Redes-F-Ciencias-UNAM/ciencia-de-redes"
```
2. Realiza las modificaciones necesarias (en la carpeta `/src`).
3. Construye el libro:
```
source .venv/bin/activate # activar ambiente virtual
cd ../ciencia-de-redes # ubicarse en directorio ciencia-de-redes
jupyter-book build --path-output . src/ # crear libro
```
4. Visualizar cambios localmente:
```
cd ./_build/html/
python -m http.server # inicializa un servidor en localhost:8000
```

## Desplegar

1. Agrega los cambios al repositorio:
```
git add .
git commit -m "DESCRIPCIÓN DE LAS MODIFICACIONES REALIZADAS"
git push origin main
```
2. Publica los cambios a GitHub Pages:
```
cd ciencia-de-redes
ghp-import -n -p -f _build/html
```
