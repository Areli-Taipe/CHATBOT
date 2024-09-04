# chatbot
1. Primero, crear una carpeta para el proyecto.
   Ruta: C:\xampp\htdocs\webFlask
   
3. Segundo, abrir Visual Studio Code y crear el entorno virtual, para ello abrimos la terminal.

   -Instalamos el entorno         : pip install virtualenv
   
   -Crear el entorno virtual      : virtualenv -p python3 env
   
   -Activar el entorno virtual    : .\env\Scripts\activate
   
   -Instalar Flask                : pip install flask
   
   -Para ver librerias instaladas : pip list
   
5. Tercero, crear un archivo main.py donde se encuentra la aplicacion del chatbot creada en colab y adaptada para verlo en el archivo de python. Tambien creamos una carpeta "templates" donde se encuentra el index.html, style.css y script.js; ademas otra carpeta "static" donde se encuentra una carpeta img con las imagenes necesarias para la aplicacion.

6. Buscar en la web https://www.pythonanywhere.com/, crear una cuenta gratuita.

7. Dentro de pythonanywhere, nos dirigimos a Web y presionamos "Add a new web app".  Seleccionamos el tipo de framework para la aplicacion, en este caso elegimos Flask y la version de python.

8. Nos dirigimos a Code y seleccionamos "Source code" en Go to directory.

9. Cambiamos el nombre del archivo principal como flask_app.py, en el directorio subir el archivo que cambiamos el nombre.

10. Crear el directorio templates y subir el archivo index.html.

11. Tambien creamos otro directorio static donde crearemos otra carpeta llamada img donde se encontrara las imagenes del proyecto que necesitamos.

12. Volver a la seccion Web y actualizamos la pagina presionando Reload Areli123.pythonanywhere.com. Despues de hacer esto podemos ver la aplicacion creada y podemos interactuar con el chatbot.
