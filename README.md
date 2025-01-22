# Proyecto Urban Grocers 

## _Proyecto para TripleTen QA Sprint 7_

En este proyecto haremos una lista de comprobación para la aplicación de prueba "Urban Grocers", específicamente el módulo de creación de kits

Se utilizó lo aprendido en el modulo actual con algo de conocimiento de lo visto en el curso de Data Scientist y leyendo la documentación de https://cnt-00325675-2c3c-4aef-b3b7-805610c2765a.containerhub.tripleten-services.com/docs para realizar las pruebas.

Se utilizó el siguiente IDE para realizar el proyecto y correr las pruebas:
- PyCharm 2024.3.1.1 (Community Edition)
- Build #PC-243.22562.220, built on December 18, 2024
- Runtime version: 21.0.5+8-b631.28 amd64 (JCEF 122.1.9)
- VM: OpenJDK 64-Bit Server VM by JetBrains s.r.o.
- Toolkit: sun.awt.windows.WToolkit
- Windows 10.0
- GC: G1 Young Generation, G1 Concurrent GC, G1 Old Generation
- Memory: 1500M
- Cores: 8
- Registry:
  - ide.experimental.ui=true
  - llm.show.ai.promotion.window.on.start=false
- Non-Bundled Plugins:
  - com.intellij.plugins.vscodekeymap (243.21565.122)

Instrucciones para ejecutar las pruebas
- Tener instalado Python. Al tiempo de creación del proyecto se utilizó la versión 3.12
- Un entorno base funciona, de preferencia es mejor tener uno exclusivo para el proyecto con conda. Para más información revise la siguiente dirección: https://www.campusmvp.es/recursos/post/como-gestionar-diferentes-entornos-para-python-con-conda.aspx  
- Instalar las dependencias, para mayor orden se localizan en el archivo requirements.txt. Utilizar el siguiente comando desde la raíz del proyecto: *pip install -r requirements*
- Instalar pytest: *pip install pytest*
- En el archivo *configuration.py* cambiar la variable URL_SERVICE por la de la API actual y activa de Urban Grocers
- Ejecutar desde consola, donde "root" es la carpeta base donde se encuentra el proyecto: *pytest root/create_kit_name_kit_test.py*

Estructura del proyecto:
- root
  - .gitignore: archivos a ignorar en repositorio git
  - configuration-py: variables de URL para la dirección del servidor de Urban Grocers y las funciones de la API
  - create_kit_name_kit_test.py: archivo principal de las pruebas 
  - data.py: archivo con las estructuras de datos para los cuerpos de los mensajes POST de la API y sus respuestas. 
  - README.md: este archivo
  - requirements.txt: archivo con las dependencias del proyecto
  - sender_stand_request.py: archivo con las llamadas a la API de Urban Grocers
  