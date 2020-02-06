# pycmic-server

[![Build Status](https://travis-ci.org/jscoba/pycmic-server.svg?branch=master)](https://travis-ci.org/jscoba/pycmic-server) [![CircleCI](https://circleci.com/gh/jscoba/pycmic-server.svg?style=svg)](https://circleci.com/gh/jscoba/pycmic-server) 

Servicio de contabilidad de fotocopias y autorización para fotocopiadoras de la gama MP C5503 de Ricoh

Este servicio se encarga de recoger información de la impresora sobre los usuarios del sistema, las copias que estos utilizan y las copias restantes de los mismos sin darles permisos de administración a la máquina.

Además puede usarse como servicio de autenticación para que solo los usuarios autorizados puedan imprimir en ordenadores públicos conectados a la impresora.

## Instalación

Para instalar la aplicación sigue los siguientes pasos:

1. Clona el repositorio
2. Si quieres puedes instalar un virtualenv de python para aislar el entorno de trabajo
3. `make install`
4. Cambia los valores de `instance/config.py` a los que se ajusten a tu [configuración](docs/Valores_de_configuración.md).
5. Ejecuta el servidor con `make start`

Si quieres configurar la aplicación para que corra en la nube (Heroku, Azure, Docker) sigue los pasos que encontrarás en la carpeta de documentación.

## Tests

Puedes ejecutar los test de la aplicación ejecutando `make test`

## Logs y depuración

La aplicación saca los registros por consola. Además guarda los registros en el directorio `instance` que se crea al instalar la aplicación y ejecutarla por primera vez. En ellos encontrarás información sobre los accesos realizados y posibles errores de ejecución. Si tienes que abrir un issue por algún problema no olvides adjuntar la parte del log necesaria para poder identificar el problema.

## Documentación para IV
La descripción de las tareas realizadas puede encontrarse [aquí](docs).


## Licencia

Copyright [2020] [Javier Sáez de la Coba]

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
