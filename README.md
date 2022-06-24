# Proyecto Final de Grado

Tenía que ser un reto, algo diferente, tecnologías no descubiertas, frameworks refrescantes después de un duro curso...
Nuestra ambición y objetivos comunes nos llevó a desarrollar un servicio web que recoge valoraciones y opiniones acerca de múltiples productos o servicios.
Partíamos de cero en cuanto al desarrollo web, JavaScript y Python.
Sin conocimientos de desarrollo en estos lenguajes y frameworks como Django, este es el resultado :)

## Empecemos

Este proyecto muestra a la perfección lo que queríamos plasmar en un principio. Antes que eso, aprendimos y nos formamos al máximo en los lenguajes y tecnologías adecuadas, esa también fue una parte importante del proyecto.

El servicio web permitirá a cualquier usuario comentar, valorar u opinar sobre un tema/producto/servicio que es expuesto por una empresa.
Hablando de empresas, estas son las encargadas de subir productos a la web para "exponerlos" a crítica. De esta manera, encontramos centralizado en un servicio web una lista infinita de productos con comentarios totalmente objetivos. Las empresas disponen de un panel informativo para recibir información concreta acerca de sus productos.
Por parte de la administración y moderación de la web tenemos un apartado de administrador o una especie de cuadro de mandos donde podremos gestionar toda la web.

#### ¿Qué diferencia a un cliente de una empresa?
El inicio en la web es el mismo, ambos cuentan con un registro y un inicio de sesión. Tanto cliente como empresa empiezan igual, para adquirir permisos de empresa se debe gestionar administrativamente la validación para que desde administración se incluya en grupos y permisos de organización.

La interfaz también cambia. Los clientes acceden a una vista básica orientada a dar su opinión. Donde podrá encotrar todos los productos ordenados por los mejores valorados o ver los productos por categorías. Por otra parte, las empresas abren en su menu superior la opcion de "crear producto". Esto les permitirá registrar un producto y subirlo a la web desde el panel oficial de "staff".

#### ¿Diferencias para los administradores?
Los administradores disponen de la totalidad de permisos. Pueden visualizar el servicio desde cualquier perfil cliente/empresa y además se les abre la posibilidad de gestionar y acceder al control de datos desde el menú superior.

También son los encargados de "moderar" en medida de lo posible la web, para hacerla lo mas objetiva y válida posible. Tienen el deber de gestionar permisos y personalización del panel de control para empresas dependiendo de los requisitos de dicha empresa. Esta personalización será tanto visual como enfocada a lo que quieren ver en su tablón.


## Prerequisitos

Necesitarás contar con Python 3.10 o superior. Recomendamos crear un entorno virtual para la instalación de paquetes.
Recomendación de PyCharm para una mejor gestion de paquetes y dependencias.
Django 4.0

## Desarrollo y funcionamiento

Los comandos que nos facilita Django para la gestion de la BBDD y modelos con sus migraciones facilitarán el desarrollo.
En terminos generales, si has conseguido clonar el proyecto e instalar sus paquetes/dependencias, ejecuta el siguiente comando para correrlo:
```
python manage.py runserver
```
Puedes desarrollar tus propias modificaciones e incluso contribuir en el proyecto. Puedes hacerlo en un sistema de integración continua.
¡Ánimo!

Puedes empezar por crear un super-usuario para ver la vista de administrador y poder ver todas las funcionalidades.
```
python manage.py createsuperuser
```

## Despliegue

En desarrollo, trabajo a futuro para desplegarlo con HEROKU.

## Built With

* [Django](https://www.djangoproject.com/) - Framework usado.
* [Django REST](https://www.django-rest-framework.org/) - Fundamentos de la API.
* [Swagger](https://swagger.io/) - [ReDoc](https://redocly.com/) - Documentación de la API.

## Control de versiones

Actualizaciones en GitHub. Estamos abiertos a trabajo futuro y seguir desarrollando este proyecto o cualquier otro con Django y tecnologías similares.

## Autores

* **Javier Gonzalez** - *BackEnd & FrontEnd* - [javiergmun](https://github.com/javiergmun)
* **Daniel Castellote** - *BackEnd & FrontEnd* - [DanielCastellote](https://github.com/DanielCastellote)

¡Estamos abiertos a nuevas contribuciones!

## Licencia

This project is licensed under the MIT License.

