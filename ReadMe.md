# **Programa de detección de palabras en archivos**
El siguiente programa esta realizado con el fin de encontrar una o más palabras en archivos de tipo:

- Excel (.xlsx y .xls)
- CSVs (.csv)
- Archivos de texto (.txt)

## **Preparación previa**

### **Palabras clave** (o palabras a buscar)
En el archivo llamado *'search_words.txt'* se deben de colocar las palabras que desea buscar el usuario, colocando una palabra por línea (se pueden buscar frases pero deben estar también en la misma línea).

Despues de haber colocado la palabra o palabras clave a buscar, se puede proceder a ejecutar el programa.

### **Recursos necesarios**
Para poder ejecutar el programa debemos primero que todo estar en un entorno Windows, tener una versión de Python 3, tener pip instalado (lo cual por lo general viene cuando instalamos Python) y por ultimo debemos descargar las librerías/paquetes que son necesarias para el funcionamiento del programa, son las siguientes:

 - pandas
 - openpyxl
 - xlrd

Para instalarlas, entramos a la terminal del sistema y escribimos el siguiente comando:

    pip install (nombre librería)


## **Cómo usar el programa**
Una vez cumplidos todos los requisitos previos podemos ejecutar el programa, nos ubicamos en la ruta donde tengamos el proyecto y en la terminal ejecutamos el comando:

    py main.py

Una vez ejecutado entraremos en dos etapas que tiene el programa, en la primera elegiremos que tipo de archivos queremos buscar (mencionados arriba), debemos de colocar el número correspondiente a la opción de nuestra preferencia. Luego saldrán otras opciones donde podremos elegir en que carpeta (tambien llamado directorio) deseamos buscar el tipo de archivos elegido previamente, podemos elegir una ruta en específica o las que esta ya predefinidas.

Una vez elegidas estas dos opciones, el programa comenzará a ejecutarse y buscar entre todos los archivos las palabras del archivo de texto que ya tuvimos que haber colocado en un paso anterior, al finalizar si no hubo ningún error, el programa creará dos archivos, uno con la salida (*output*) del programa y otro con un resumen (*summary*) en el que se podrá visualizar de una manera más sencilla la salida del programa. Cada uno de estos archivos tiene en su nombre la fecha y hora en la que fue ejecutado cada comando.
