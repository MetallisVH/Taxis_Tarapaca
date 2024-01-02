
# Taxis Aeropuerto Tarapaca
En este proyecto nos enfocaremos en implementar un sistema de gestión para una empresa de taxis, centrado en el funcionamiento interno de la empresa, sin dejar de lado a nuestros clientes.

## Tecnologías Utilizadas
Las tecnologías que utilizaremos en la creación del sistema.

#### Python
#### Framework Django
#### PostgreSQL (propio servidor)
### Instalación
Proporciona instrucciones claras sobre cómo instalar y configurar el entorno de desarrollo necesario para el proyecto. Puedes dividir esto en secciones para cada tecnología o herramienta si es necesario. Aquí hay un ejemplo genérico:

### (Opcional) Crea un entorno virtual
Abre la Terminal (o línea de comandos):

En Windows, puedes usar el cmd o PowerShell.
En Linux/macOS, usa la terminal.
Navega al Directorio de tu Proyecto:

```
cd ruta/del/proyecto
```
Crea un Entorno Virtual:

```
python -m venv venv
```

Este comando creará un directorio llamado venv que contendrá el entorno virtual.

Activa el Entorno Virtual:

En Windows (PowerShell):

```
.\venv\Scripts\Activate
```
En Linux/macOS:

```
source venv/bin/activate
```

## Python
Pasos para instalar
Windows:

Descargar Python:

Visita el sitio oficial de Python: Python Downloads.
- [Python](https://www.python.org/downloads/)
Haz clic en el botón "Downloads".
Selecciona la versión más reciente de Python para Windows.
Instalar Python:

Ejecuta el archivo descargado.
Asegúrate de marcar la casilla "Add Python x.x to PATH" durante la instalación.
Sigue las instrucciones en pantalla.
Verificar la Instalación:

Abre la línea de comandos (cmd) y ejecuta:
```
python --version
```
Linux (Ubuntu/Debian):

Verificar Python Preinstalado:

Muchas distribuciones de Linux ya incluyen Python. Verifica la versión instalada ejecutando:
```
python3 --version
```
Instalar Python:

Si no tienes Python instalado, ejecuta:
```
sudo apt update
sudo apt install python3
```
Verificar la Instalación:

Ejecuta:
```
python3 --version
```
macOS:

Instalar Homebrew (opcional pero recomendado):

Si no tienes Homebrew instalado, sigue las instrucciones en Homebrew para instalarlo.
Instalar Python con Homebrew:

Abre la terminal y ejecuta:
```
brew install python
```
Verificar la Instalación:

Ejecuta:
```
python3 --version
```
## Dependencias
Navega al Directorio del Proyecto:

Abre la terminal o línea de comandos.
Navega al directorio donde se encuentra tu archivo requirements.txt.

Instala las Dependencias:

Ejecuta el siguiente comando para instalar todas las dependencias listadas en requirements.txt:

```
pip install -r requirements.txt
```
Asegúrate de que tu entorno virtual esté activado antes de ejecutar este comando.

Verifica la Instalación:

Puedes verificar que las dependencias se hayan instalado correctamente ejecutando:

```
pip list
```
Esto mostrará todas las bibliotecas instaladas junto con sus versiones.

Uso
Primero migra los modelos con los comandos:

```
python manage.py makemigrations
python manage.py migrate
```
Luego corre el servidor:

```
python manage.py runserver
```
Asegúrate de que funcione correctamente.

## APIs Utilizadas
En esta sección, puedes listar y describir las APIs que tu proyecto utiliza. Incluye información relevante sobre cómo acceder a estas APIs, cómo autenticarse (si es necesario) y cómo utilizarlas en tu proyecto.

### Google Maps API

Descripción: [Descripción de la API]
Documentación: [Enlace a la documentación]

### API 2

Descripción: [Descripción de la API]
Documentación: [Enlace a la documentación]

## Licencia
Este proyecto está bajo la GNU General Public License v3.0. Puedes encontrar más detalles en el archivo LICENSE.
 - [GNU General Public License v3.0](https://github.com/fbrzzhormazabal/TaxisTarapca/blob/main/LICENSE)

## Contacto
Si tienes preguntas o necesitas ponerse en contacto contigo, proporciona la información de contacto, como tu dirección de correo electrónico o tu perfil de redes sociales.

## Autores del Proyecto

- [@MetallisVH](https://github.com/MetallisVH)
- [@fbrzzhormazabal](https://github.com/fbrzzhormazabal)
