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
Para poder ejecutar el programa debemos primero que todo estar en un entorno Windows, tener una versión de Python 3, tener pip instalado (lo cual por lo general viene cuando instalamos Python) y por ultimo descargar la librería 'virtualenv', para descargar esta simplemente debemos de ejecutar en nuestra terminal el comando:

    pip install virtualenv

### **Entorno virtual** (virtualenv)
Un entorno virtual es una entorno de Python parcialmente aislado donde podemos instalar paquetes o librerías específicos para un proyecto sin instalarlos para todo el sistema, como este programa requiere de librerías diferentes a las que trae Python por defecto, utilizaré un entorno virtual para facilitar el "port" a otros dispositivos.

En este repo la carpeta *'virtualenv'* contiene todo lo del entorno virtual, para poder activar el entorno virtual y ejecutar el programa debemos de activarlo, esto se realiza abriendo nuestra terminal cmd de Windows y ejecutar el siguiente comando (el comando a continuación no funciona con PowerShell ni otras terminales, solo con la terminal CMD Simbolo del Sistema, en otras terminales el comando es distinto)

    .\virtualenv\Scripts\activate

Si no lo activamos no podremos ejecutar el programa ya que no tendremos las librerías necesarias.

Si luego queremos desactivarlo para quedar en nuestro entorno normal por defecto, escribimos en la terminal el comando

    deactivate

## **Cómo usar el programa**
