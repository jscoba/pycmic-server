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

## Docker

Esta aplicación está preparada para ser ejecutada utilizando contenedores docker.

Puedes descargar la imagen desde el Docker Hub aquí: https://hub.docker.com/r/jscoba/pycmic-server o puedes construirla en local ejecutando `make build_docker`

## Vagrant

Esta aplicación puede ejecutarse como máquina virtual usando `vagrant` . Para ello puedes seguir las instrucciones desde VagrantCloud (https://app.vagrantup.com/jscoba/boxes/pycmic-server) o desde el apartado de releases de este repositorio (https://github.com/jscoba/pycmic-server/releases/tag/v1.0)

También puedes crear tu propia imagen ejecutando `make start_vm` desde la raiz de este repositorio. Esto creará la máquina virtual y la configurará de forma automática. Tendrás que tener instalado `vagrant` y `ansible` en tu máquina local.

## Despliegue en Azure

La aplicación incluye en la carpeta `despliegue/` ficheros para desplegar de forma automática la aplicación como una máquina virtual de Azure. Puedes seguir las instrucciones que se encuentran en el último link de [aquí](docs/) para configurar tus credenciales de azure y luego ejecutar `make azure_up` para desplegar la máquina virtual.

## Documentación para IV
La descripción de las tareas realizadas puede encontrarse [aquí](docs).

buildtool: Makefile

Despliegue: https://pycmic-server.herokuapp.com/

Contenedor: https://pycmic-server.azurewebsites.net/

Provision: provision/playbook.yml

Despliegue final: 104.42.190.206

Se puede acceder a la aplicación mediante el puerto 5000 de la IP arriba indicada


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
