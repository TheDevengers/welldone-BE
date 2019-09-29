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

Respecto a la paginación, he creado en Trello una HU opcional para mejorar la paginación con JS + llamada al API. Creo que sería un método más eficiente, pero más laborioso, al menos para mí. De momento dejo cumplido el requisito con la implementación más sencilla.

### feature list create article

* Añadido endpoint de consulta de listado de artículos. Devuelve todos los artículos del usuario autenticado.
* Modificado endpoint de creación de artículo. Se le han añadido los mismos permisos que al listado y el autor se vincula al usuario autenticado.
* Documentación de la API en README.

### feature add new article comment

* Creación de la nueva vista CommentsView
* Añadir nuevo endpoint /comments/slug
* Modificar plantilla HTML para incluir el formulario de creacion nuevo comentario
* Creación formulario CommentForm
* Creación nuevo controlador CommentController

### feature search articles

* Modificado el controller `articles.py` para filtrar articulos por búsqueda si la URL incluye el parámetro `search`, el cual se genera al realizar el usar el buscador del header. Se busca en los campos `title`, `ìntroduction` y `body`, y se limitan los resultados a máximo 20 artículos por defecto.
* Modificado la plantilla `list.html`para mostrar un mensaje de que no se encuentran resultados de búsqueda en caso de que el objeto `articles_list` tenga 0 elementos.

La búsqueda es case insensitive, pero busca las palabras con acentos, lo cual no es muy bueno de cara a la UX. Incluiré en Trello una HU opcional para mejorar la búsqueda, quizás usando el operador __iregex.
https://docs.djangoproject.com/en/2.2/ref/models/querysets/#iregex

### feature shown comments number

* Modificado detail.html para mostrar el número de comentarios del artículo arriba junto a la fecha de publicación y abajo justo antes de los comentarios.
* El contador superior de comentarios está dentro de una etiqueta anchor que dirige a la sección inferior de comentarios.
* Añadido formato condicional para usar el singular 'comentario' si sólo hay un comentario.

### feature article API post & delete method

* Añadida varible de entorno para modificar la duración de ACCESS_TOKEN.
* Adaptación a las vistas de API genéricas.
* Modificación en la creación de slug: solo funciona cuando se crea un artículo. Si se edita ha de indicarse expresamente el nuevo slug.
* Serializador de actualización de artículo:
    * Si algún valor no es indicado, dejará los valores previos.
    * Si se indica una categoría inexistente, no se tendrá en cuenta.
* Refactorización de la paginación a un único lugar. Ha de ser incluido cuando quiera usarse, y cargarse sus propios estilos css.

### feature docker

* Añadidas variables de entorno a dockerfile.
* Refactorización del código.
* Añadidos permisos de ejecución a run.sh.