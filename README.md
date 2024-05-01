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
- **.env**: Archivo que contiene variables de entorno para la configuración local del proyecto, como claves secretas, configuraciones de la base de datos, etc.

## Datos
1. **Crear Uuarios**
  ![alt text](Usuarios.png)

2. **Crear la Base de datos y a su vez las colecciones**
  ![alt text](Colleciones_en_mongodb.png)


# Pasos para la Ejecución

Tener en cuenta la instalación de python y sus complementos

1. Crear el entorno virtual:
- instalar pipenv: pip install pipenv
- python -m pipenv shell o pipenv shell

2. Importar las siguientes librerías en el entorno virtual:
  - pip install fastapi uvicorn sqlalchemy pydantic psycopg2
  
3. Ejecutar la app:
  - python -m uvicorn project.app.controllers.reactor_controller:app --port 1234
  ![alt text](image.png)

  - Entrar en la dirección (local host) y agregar la extensión /docs
  ![alt text](image-1.png)

  ![alt text](image-2.png)

# Resultados
Se deja el archivo de word "Evidencias de los resultados.docx" el cual se puedes descargar y evidenciar capturas de los resultados



