

# Proyecto FastAPI con PostgreSQL

Este es un proyecto desarrollado en **FastAPI** que utiliza **PostgreSQL** como base de datos y está configurado para utilizar **`asyncpg`** como controlador asíncrono para las operaciones de base de datos. Este README contiene los pasos para configurar y ejecutar el proyecto de manera local.

## Pre-requisitos

Antes de comenzar, asegúrate de tener instaladas las siguientes herramientas en tu entorno:

- **Python 3.8 o superior**: Para ejecutar FastAPI y todas las dependencias del proyecto.
- **PostgreSQL**: La base de datos que se usará para este proyecto.
- **Git**: Para clonar el repositorio si lo deseas.
- **Virtualenv**: (Opcional) Si no lo tienes instalado, puedes usar `pip` para instalarlo:

```bash
pip install virtualenv
```

## Instalación y configuración del entorno

Sigue estos pasos para configurar y ejecutar el proyecto:

### 1. Clonar el repositorio (opcional)

Si estás trabajando con un repositorio Git, puedes clonarlo con el siguiente comando:

```bash
git clone <url-del-repositorio>
```

### 2. Crear y activar el entorno virtual

Es recomendable usar un entorno virtual para aislar las dependencias del proyecto. Para crear y activar el entorno virtual, sigue estos pasos:

#### En sistemas basados en Unix (Linux y macOS):

```bash
# Crear el entorno virtual
python3 -m venv venv

# Activar el entorno virtual
source venv/bin/activate
```

#### En Windows:

```bash
# Crear el entorno virtual
python -m venv venv

# Activar el entorno virtual
.\venv\Scripts\activate
```

### 3. Instalar dependencias

Una vez que el entorno virtual esté activo, instala las dependencias que el proyecto necesita ejecutando el siguiente comando:

```bash
pip install -r requirements.txt
```

### 4. Configurar PostgreSQL

El proyecto está configurado para usar una base de datos **PostgreSQL** local. Debes asegurarte de que tienes PostgreSQL instalado y ejecutándose en tu máquina.

#### Crear la base de datos

1. Accede a tu consola de PostgreSQL y crea una base de datos llamada `postgres` (o usa una existente). Asegúrate de que los valores coincidan con los que se indican en el archivo `.env`.

2. Asegúrate de tener las siguientes credenciales configuradas en tu base de datos local (o ajusta según sea necesario):

   - **Usuario**: `postgres`
   - **Contraseña**: `12345678`
   - **Host**: `localhost`
   - **Puerto**: `5432`
   - **Nombre de la base de datos**: `postgres`

#### Modificar la URL de conexión en el archivo `.env`

En el archivo **`.env`**, ajusta la variable `DATABASE_URL` para que coincida con la configuración de tu PostgreSQL local. Debería verse algo como esto:

```
DATABASE_URL="postgresql+asyncpg://postgres:12345678@localhost:5432/postgres"
```

- **postgresql+asyncpg**: Este esquema indica que estamos usando el controlador **`asyncpg`**, que es una biblioteca asíncrona de alto rendimiento para PostgreSQL. **`asyncpg`** es ideal para usar en proyectos asíncronos como FastAPI, ya que permite manejar múltiples solicitudes concurrentes de manera eficiente.
  
- **postgres**: Es el usuario de PostgreSQL.
- **12345678**: Es la contraseña del usuario.
- **localhost**: Indica que estás conectando a una instancia local de PostgreSQL.
- **5432**: Es el puerto por defecto de PostgreSQL.
- **postgres**: Es el nombre de la base de datos.

Si tus credenciales o configuración de PostgreSQL son diferentes, ajusta esta URL de conexión según sea necesario.

### 5. Ejecutar la aplicación

Con el entorno virtual activado y PostgreSQL configurado, puedes ejecutar la aplicación con **Uvicorn**, que es el servidor ASGI utilizado para ejecutar aplicaciones FastAPI.

Ejecuta el siguiente comando para iniciar el servidor:

```bash
uvicorn app.main:app --reload --port 8000
```

- **`app.main:app`**: Indica el archivo `main.py` dentro de la carpeta `app` y la instancia de la aplicación `app`.
- **`--reload`**: Habilita el modo de recarga automática, lo que significa que el servidor se recargará automáticamente si haces cambios en el código.
- **`--port 8000`**: Especifica el puerto en el que se ejecutará la aplicación. Puedes cambiar este puerto si es necesario.

Una vez que el servidor esté corriendo, puedes acceder a la API desde tu navegador o herramientas como Postman en la siguiente URL:

```
http://localhost:8000
```

### 6. Endpoints disponibles

Una vez que la aplicación esté en ejecución, puedes interactuar con la API. FastAPI genera automáticamente una documentación interactiva de la API, la cual puedes ver accediendo a:

```
http://localhost:8000/docs
```

Esta documentación te permitirá probar los endpoints directamente desde el navegador.

### Especificación del esquema en las tablas

En este proyecto, he especificado el esquema en el que se encuentra la tabla **`users`** dentro de la base de datos. Esto se hace a través de la propiedad **`__table_args__`** en el modelo de SQLAlchemy.

### Ejemplo del modelo `User` con esquema especificado:

```python
from sqlalchemy import Column, Integer, String
from app.core.database import Base

class User(Base):
    __tablename__ = 'users'
    __table_args__ = {'schema': 'schemaflask1'}  # Esquema especificado

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False)
```

### Explicación:

- **`__tablename__`**: Define el nombre de la tabla, en este caso **`users`**.
- **`__table_args__ = {'schema': 'schemaflask1'}`**: Aquí se especifica el esquema **`schemaflask1`** en el que la tabla **`users`** reside. Esto indica que SQLAlchemy buscará la tabla **`users`** dentro del esquema **`schemaflask1`** en PostgreSQL.

### Creación manual del esquema y la tabla en PostgreSQL

Las tablas no se crearán automáticamente, ya que estamos utilizando un esquema específico. Si la tabla no existe, los usuarios deben crearla manualmente en PostgreSQL.

#### Comando SQL para crear el esquema:

```sql
CREATE SCHEMA IF NOT EXISTS schemaflask1;
```

#### Comando SQL para crear la tabla:

```sql
CREATE TABLE schemaflask1.users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL
);
```

### Nota:

- **Esquemas en PostgreSQL**: Un esquema es una forma de agrupar objetos como tablas, vistas, etc., dentro de una base de datos. Es útil para organizar y segmentar los datos de una manera lógica.
- **Las tablas no se crean automáticamente**: En este proyecto, SQLAlchemy no crea automáticamente las tablas en la base de datos. Por lo tanto, asegúrate de crear tanto el esquema como las tablas antes de ejecutar la aplicación.

### Notas finales

- **`asyncpg`** es un controlador asíncrono para PostgreSQL que permite manejar múltiples conexiones simultáneas de manera eficiente. Esto es crucial en aplicaciones como FastAPI, que son asíncronas por diseño, ya que mejora el rendimiento al permitir que múltiples solicitudes se manejen sin bloquear el servidor.


