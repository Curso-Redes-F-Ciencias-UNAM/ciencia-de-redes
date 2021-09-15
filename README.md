# Ciencia de Redes

Este es el repositorio donde se aloja la página del curso **Ciencia de Redes** que se imparte en la Facultad de Ciencias de la UNAM.

---

## Organización del repositorio

Este repositorio consta de 2 carpteras:

- `/src` : la cual contiene todos los archivos fuente del libro (aquí se deben realizar todas las modificaciones necesarias). El contenido de esta carpeta está ordenado de acuerdo a la estructura de un [Jupyter Book](https://jupyterbook.org/intro.html).
- `/_build` : la cual contiene todo el código html de la página (el contenido de esta carpeta no debe modificarse).

## Requisitos

Para construir este libro se requiere de jupyter book y ghp-import:

```
pip install -U jupyter-book
pip install ghp-import
```

## Uso

1. Clona este repositorio:

```
git clone "https://github.com/Curso-Redes-F-Ciencias-UNAM/ciencia-de-redes"
```
2. Realiza las modificaciones necesarias (archivos dentro de la carpeta `/src`).

3. Construye el libro (ejecutar desde `/ciencia-de-redes`):
```
jupyter-book build --path-output . src/
```
4. Agrega los cambios al repositorio:
```
git add .
git commit -m "<DESCRIPCIÓN DE LAS MODIFICACIONES REALIZADAS>
git push origin main
```
5. Publica los cambios a GitHub Pages (ejecutar desde `/ciencia-de-redes`):
```
ghp-import -n -p -f _build/html
```
