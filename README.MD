# Proyecto API con FastAPI conectado a una BD Postgres

Este proyecto utiliza FastAPI para gestionar una base de datos de películas en Postgres.

## Requisitos

- Docker

## Instrucciones para ejecutar la base de datos

Para levantar el contenedor de PostgreSQL, ejecuta el siguiente comando:

```bash
sudo docker run --name db -e POSTGRES_PASSWORD=mysecretpassword -p 5432:5432 -d postgres


## Instrucciones para ejecutar la aplicacion

#Construir la imagen de Docker para nuestra aplicación

docker build -t movie-api .

#Ejecutar el contenedor de la API:

docker run -d --name movie-api -p 8000:8000 movie-api


