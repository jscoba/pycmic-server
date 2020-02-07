# Pycmic-server - Documentación Hito 3

## Construcción del microservicio

En este hito hemos terminado de desarrollar nuestro microservicio. En este caso hemos completado la programación de las rutas que teníamos diseñadas a partir de las historias de usuario del sistema.

Además hemos generado la documentación de cada función y de cada test, explicando en el caso de las rutas que hacen y que devuelven y en el caso de los tests que está testando cada uno.

Hemos seguido un desarrollo basado en test, por lo que por cada ruta de la aplicación hemos escrito el test correspondiente (que claramente fallaba al ser la función un simple `pass`) y luego la función que hacía cumplir dicho test.



Con este trabajo hecho ya tenemos un microservicio funcional que puede ser desplegado en un servidor, ya sea como aplicación standalone, en un PaaS, a través de contenedores en la nube o donde se quiera.



## Herramienta de construcción

Para manejar la instalación, el arranque y el testeo del servicio vamos a utilizar objetivos de `make` Para esto utilizamos un fichero `Makefile` en la raíz de nuestro directorio en el que añadimos los siguientes objetivos:

- `install`: Instala las dependencias y genera la base de datos inicial (con las tablas).
- `start`: Arranca el servicio utilizando el servidor de aplicaciones `werkzeug` integrado de forma predeterminada en `Flask`
- `start_heroku`: Arranca el servicio utilizando el servidor `gunicorn`, mejor preparado que el predeterminado para entornos de producción
- `build_docker`: Construye la imagen de docker a partir del Dockerfile
- `test`: Ejecuta los tests de la aplicación. Este objetivo es el usado por Travis y CircleCI para ejecutar los procesos de integración continua.

El uso de una herramienta como make nos permite centralizar la gestión de la aplicación en una única herramienta y no tener que recordar exactamente cada comando a ejecutar para cada operación que tengamos que hacer repetidas veces con la aplicación.

