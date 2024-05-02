# tadb_202410_ex04

# Importante
Este proyecto se realizó utilizando el lenguaje de programación Python y el Motor de Base de datos MongoDB
- Con python se utilizaron librerías como FastAPI para la creación de la API, sqlalchemy para la interacción con la base de datos de manera programática y orientada a objetos (ORM).

# Estructura de Carpetas del Proyecto

- **project/app/**
  - **context/**: Contiene la clase Session, define la configuración y la gestión del contexto de la aplicación, incluida la conexión a la base de datos.
  - **Controller/**: Contiene los controladores de la aplicación, que manejan las rutas y las solicitudes HTTP.
  - **model/**: Contiene las definiciones de los modelos de datos de la aplicación.
    - **model/reactor_schema.py**: Son los modelos con los cuales van a retornar las consultas que realice el usuario.
    - **model/reacto.py**: Es la definición del ORM para realizar el mapeo de las tablas.
  - **repositories/**: Contiene los repositorios que interactúan con la base de datos.
  - **service/**: Contiene los servicios que implementan la lógica de negocio de la aplicación.
  - **context.py**: Define la configuración y la gestión del contexto de la aplicación, incluida la conexión a la base de datos.
- **README.md**: Archivo de documentación que proporciona información sobre el proyecto, cómo configurarlo, ejecutarlo y usarlo.
- **.gitignore**: Archivo que especifica qué archivos y directorios deben ser ignorados por Git durante el versionado del proyecto.

## **.env**

Archivo que contiene variables de entorno para la configuración local del proyecto, como claves secretas, configuraciones de la base de datos, etc.
En este caso se almaceno una variable de entorno llamada **uri** que tiene la siguiente estructura

```python
uri = "mongodb+srv://<username>:<password>@cluster0.3l35xwi.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
```

## Conexion a MongoDB

Antes se debe verificar que este instalado el siguiente paquete.

```python
python -m pip install "pymongo[srv]"
```

De la siguiente forma se implementa la conexion a la bd

```python

import os
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri='uri'
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
```

## Datos
1. **Crear Uuarios**

Esto se hace con el fin de mantener lo mayormente seguro el entorno de desarrollo
  ![alt text](Usuarios.png)

2. **Crear la Base de datos y a su vez las colecciones**
  ![alt text](Colleciones_en_Mongodb.png)

  1. coleccion paises
  ![alt text](Collecion_Paises.png)

  2.  coleccion estados
  ![alt text](Collecion_estados.png)

  3. coleccion reactores
  ![alt text](Reactores.png)

  4. coleccion de las ubicaciones
  ![alt text](Ubicacion.png)

## Conexion usando MongoDB Compass

Para conectarse localmente, seleccionamos la opcion Compass que se habilita al dar click en la opcion Conectar. 
Despues de modificar el string proporcionado con el **admin** y **pasword** habilitados se ve de la siguiente manera al conectarse.
  ![alt text](Compass.png)

# Creacion de la coleccion y validaciones

En este apartado se dara el codigo para replicar lo deseado

```json
// Conexión a MongoDB
use Reactores_bd

// Crear las colecciones correspondientes
db.createCollection("estados")
db.createCollection("paises")
db.createCollection("ubicacion")
db.createCollection("tipos_reactor")
db.createCollection("reactores")

```


# Ejecucion PY

Tener en cuenta la instalación de python y sus complementos

1. Crear el entorno virtual:
- instalar pipenv: pip install pipenv
- python -m pipenv shell o pipenv shell

2. Importar las siguientes librerías en el entorno virtual:

  ```python

  ```
  
3. Ejecutar la app:


# Resultados
Se deja el archivo de word "Evidencias de los resultados.docx" el cual se puedes descargar y evidenciar capturas de los resultados