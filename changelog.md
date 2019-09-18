# Changelog

## release X

### feature user article list

* Refactorización de código y estructura.
* Listado de artículos de usuario básico.

### feature create article

* Creación endpoint GET /categories para que devuelva las categorías existentes ya que a la hora de crear un artículo, las categorías solo pueden ser la que estén ya creadas por defecto en bbdd
* Creación serializers para las Categorias y Articulo
* Modificación del endpoint POST /article para que crear un articulo y guardarlo en bbdd
* Modificación .gitignore para incluir el /venv (windows)

### feature article list

* Estructura de plantillas básica y separada.
* Listado de artículos básico con diseño básico y datos representativos.
* Inclusión de urls públicas para desarrollo.
* Instalación de librerias Django Sass
* Inclusión de fuente Roboto

### feature article detail

* Creada clase ArticleDetailView en articles/views/detail.py.
* Creada plantilla HTML básica en articles/templates/articles/detail.html.
* Corregido import de ArticleDetailView en urls.py.
* Comentado el path de articulos de usuario en urls.py hasta desarrollar la HU.
