# Changelog

## release X

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

### feature user article list

* Refactorización de código y estructura.
* Listado de artículos de usuario básico.

### feature category articles

* Listado de artículos de una categoría
* Refactorización del código de las views de listado, las cuales comparten mismo funcionamiento

### feature article comments

* Modificada la clase ArticleDetailView en `articles/views/detail.py` para incluir comentarios del artículo en base a query string.
* Modificada plantilla HTML `articles/templates/articles/detail.html` incluyendo sección de comentarios.
* Cambiado campo creation_date del modelo Comment de DateField a DateTimeField, para poder realizar ordenación de comentarios desde el más reciente.
* Corregido bug en los href de `lists.html` para que sigan la ruta `/<str:username>/<str:slug>` definida en el PR de `fix/PUB_article_detail`
* Incluida paginación en los comentarios. El método se basa en lo ya creado para la paginación de articulos en `articles/views/list.py`.

### feature add new article comment

* Creación de la nueva vista CommentsView
* Añadir nuevo endpoint /comments/slug
* Modificar plantilla HTML para incluir el formulario de creacion nuevo comentario
* Creación formulario CommentForm
* Creación nuevo controlador CommentController

Respecto a la paginación, he creado en Trello una HU opcional para mejorar la paginación con JS + llamada al API. Creo que sería un método más eficiente, pero más laborioso, al menos para mí. De momento dejo cumplido el requisito con la implementación más sencilla.
