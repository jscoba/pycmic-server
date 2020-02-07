FROM python:3.7-alpine

# Etiqueta de responsable de la imagen
LABEL MANTAINER="jscoba"

#Instalamos make
RUN apk add --update make

#Copiar la aplicación al contenedor
COPY . /app
WORKDIR /app

#Variable de entorno para el puerto
ENV PORT 8000

#Instalar dependencias
RUN make install

#Ejecutar gunicorn
CMD ["make", "start_heroku"]