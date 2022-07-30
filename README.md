# Habbi

# Servicio Consulta de Inmuebles

Tabla de contenido
- [Servicio Consulta de Inmuebles](#servicio-consulta-de-inmuebles)
  - [Tecnologias del proyecto](#tecnologias-del-proyecto)
  - [Estructura General](#estructura-general)
  - [Descripcion del Microservicio](#descripcion-del-microservicio)
  - [Diagrama Entidad-Relacion para el Servicio](#diagrama-entidad-relacion-para-el-servicio)
  - [Como ejecutar los test?](#como-ejecutar-los-test)
  - [Como ejecutar el servicio?](#como-ejecutar-el-servicio)
  - [Funcionalidades](#funcionalidades)
    - [Consulta de inmuebles por estado](#consulta-de-inmuebles-por-estado)
    - [Consulta de inmuebles por los datos del mismo](#consulta-de-inmuebles-por-los-datos-del-mismo)
  - [Servicio “Me gusta”](#servicio-me-gusta)


## Tecnologias del proyecto

Este servicio se encuentra desarrollado con las siguientes herramientas

- `Python 3.9` (librerias Core)
    - `http.server`: Servidor Http
    - `unnittest:` Pruebas unitarias
- `SQLAlchemy`:  Solo como driver para conexion a la base de datos
- `MySQL`: Motor de base de datos
- `Docker`: Crear el contenedor del microservicio.

## Estructura General

El proyecto presenta la siguiente estructura

## Descripcion del Microservicio

Esta herramienta permite que los usuarios puedan consultar los inmuebles disponibles para venta, el endpoint principal expone a los usuarios una respuesta en formato json que puede ser consumida por el front-end de Habbi, permite a los usuarios ver tanto los inmuebles que se encuentran en la base de datos, los usuarios pueden ver la siguiente información del inmueble: ***Dirección, Ciudad, Estado, Precio de venta y Descripción***.

La ruta principal se encuentra documentada como:

```python
localhost/api/vi/properties
```

La cual genera una respuesta de tipo json como la siguiente

```python
aqui la respuesta del endpoint para documentar al frontend
```

## Diagrama Entidad-Relacion para el Servicio





## Como ejecutar los test?

```python
coverage run -m unittest
```

## Como ejecutar el servicio?

Este proyecto puede ejecutarse de dos formas, la primera correrlo desde tu maquina local con el siguiente comando:

```python
python3 main.py
```

Este comando despliega el servidor al cual podras realizarle peticiones http para los endpoints descritos mas adelante, a manera de ejemplo puedes visitar la siguiente URL

`(escribir url)`

La segunda opcion es crear un contenedor mediante el siguiente comando

```python

```

Esto crea una imagen a partir del archivo Dockerfile, y posteriormente el servicio dockerizado para consumirlo mediante la misma url anteriormente descrita.

## Funcionalidades

### Consulta de inmuebles por estado

Los usuarios pueden consultar los inmuebles por estatus (”pre-venta”, “en venta” y “vendido”) con los siguientes endpoints

- Preventa: retorna todos los inmuebles en pre-venta

```python

```

- En venta: retorna todos los inmuebles en venta

```python

```

- Vendido: retorna todos los inmuebles vendidos

```python

```

### Consulta de inmuebles por los datos del mismo

Adicionalmente los usuarios pueden filtar estos inmuebles mediante `query parameters` utilizando los siguientes criterios:

- Año de construcción

```python

```

- Ciudad

```python

```

- Estado

```python

```

Ejemplo aplicando los 3 filtros a una misma consulta.

```python

```

Esta funcionalidad esta disponible tanto para la ULR principal, tanto como para las colecciones por estatus.

```python

```

## Servicio “Me gusta”

Proximo a documentar