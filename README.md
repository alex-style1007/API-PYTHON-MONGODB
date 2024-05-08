# tadb_202410_ex04

# Importante
Este proyecto se realizó utilizando el lenguaje de programación Python y el Motor de Base de datos MongoDB
- Con python se utilizaron librerías como FastAPI para la creación de la API, pymongo para la interacción con la base de datos Mongodb.

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

## **.env** y Conexion a MongoDB

Archivo que contiene variables de entorno para la configuración local del proyecto, como claves secretas, configuraciones de la base de datos, etc.
En este caso se almaceno una variable de entorno llamada **uri** que tiene la siguiente estructura

```python
uri = "mongodb+srv://<username>:<password>@cluster0.3l35xwi.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
```

## Datos
1. **Crear Uuarios**

Esto se hace con el fin de mantener lo mayormente seguro el entorno de desarrollo
  ![alt text](Usuarios.png)

2. **Crear la Base de datos y a su vez las colecciones**

  1. coleccion ubicaciones


  2.  coleccion tipos


  3. coleccion reactores





## Conexion usando MongoDB Compass

Para conectarse localmente, seleccionamos la opcion Compass que se habilita al dar click en la opcion Conectar. 
Despues de modificar el string proporcionado con el **admin** y **pasword** habilitados se ve de la siguiente manera al conectarse.
  ![alt text](Compass.png)

# Creacion de la coleccion y validaciones

En este apartado se dara el codigo para replicar lo deseado

```java
// Conexión a MongoDB
use Reactores_bd

// Crear las colecciones correspondientes
db.createCollection("estados")
db.createCollection("paises")
db.createCollection("ubicacion")
db.createCollection("tipos_reactor")
db.createCollection("reactores")

```
Ahora para realizar las validaciones

1. **estados**

```java
{
    "$jsonSchema": {
      "bsonType": "object",
      "required": ["_id", "estados"],
      "properties": {
        "_id": {
          "bsonType": "objectId",
          "description": "Identificador único del documento"
        },
        "estados": {
          "bsonType": "array",
          "minItems": 1,
          "items": {
            "bsonType": "object",
            "required": ["id", "estado"],
            "properties": {
              "id": {
                "bsonType": "int",
                "description": "ID del estado"
              },
              "estado": {
                "bsonType": "string",
                "description": "Descripción del estado"
              }
            }
          },
          "uniqueItems": true
        }
      }
    }
  }
  
```
2. **paises**

```java
{
    "$jsonSchema": {
      "bsonType": "object",
      "required": ["_id", "paises"],
      "properties": {
        "_id": {
          "bsonType": "objectId",
          "description": "Identificador único del documento"
        },
        "paises": {
          "bsonType": "array",
          "minItems": 1,
          "uniqueItems": true,
          "items": {
            "bsonType": "object",
            "required": ["id", "pais"],
            "properties": {
              "id": {
                "bsonType": "int",
                "description": "ID del país"
              },
              "pais": {
                "bsonType": "string",
                "description": "Nombre del país"
              }
            }
          }
        }
      }
    }
  }
  
```
3. **reactores**

```java
{
    "$jsonSchema": {
      "bsonType": "object",
      "required": ["_id", "reactores"],
      "properties": {
        "_id": {
          "bsonType": "objectId",
          "description": "Identificador único del documento"
        },
        "reactores": {
          "bsonType": "array",
          "minItems": 1,
          "items": {
            "bsonType": "object",
            "required": ["id", "nombre", "potencia_termica", "primera_fecha_reaccion", "id_tipo_reactor", "id_ubicacion", "id_estado"],
            "properties": {
              "id": {
                "bsonType": "int",
                "description": "ID del reactor"
              },
              "nombre": {
                "bsonType": "string",
                "description": "Nombre del reactor"
              },
              "potencia_termica": {
                "bsonType": "int",
                "minimum": 0,
                "description": "Potencia térmica del reactor"
              },
              "primera_fecha_reaccion": {
                "bsonType": "date",
                "description": "Fecha de la primera reacción del reactor"
              },
              "id_tipo_reactor": {
                "bsonType": "int",
                "description": "ID del tipo de reactor"
              },
              "id_ubicacion": {
                "bsonType": "int",
                "description": "ID de la ubicación del reactor"
              },
              "id_estado": {
                "bsonType": "int",
                "description": "ID del estado del reactor"
              }
            }
          }
        }
      }
    }
  }


```
4. **tipos_reactor**

```java
{
    "$jsonSchema": {
      "bsonType": "object",
      "required": ["_id", "tipos_reactor"],
      "properties": {
        "_id": {
          "bsonType": "objectId",
          "description": "Identificador único del documento"
        },
        "tipos_reactor": {
          "bsonType": "array",
          "minItems": 1,
          "uniqueItems": true,
          "items": {
            "bsonType": "object",
            "required": ["id", "tipo"],
            "properties": {
              "id": {
                "bsonType": "int",
                "description": "ID del tipo de reactor"
              },
              "tipo": {
                "bsonType": "string",
                "description": "Nombre del tipo de reactor"
              }
            }
          }
        }
      }
    }
  }
  
```
5. **Ubicacion**

```java
{
    "$jsonSchema": {
      "bsonType": "object",
      "required": [
        "_id",
        "ubicacion"
      ],
      "properties": {
        "_id": {
          "bsonType": "objectId",
          "description": "Identificador único para el documento"
        },
        "ubicacion": {
          "bsonType": "array",
          "minItems": 1,
          "items": {
            "bsonType": "object",
            "required": [
              "id",
              "ciudad",
              "id_pais"
            ],
            "properties": {
              "id": {
                "bsonType": "int",
                "description": "ID de la ubicación"
              },
              "ciudad": {
                "bsonType": "string",
                "description": "Nombre de la ciudad"
              },
              "id_pais": {
                "bsonType": "int",
                "description": "ID del país"
              }
            }
          }
        }
      }
    }
  }
  
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
