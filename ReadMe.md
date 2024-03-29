# **Programa de detección de palabras en archivos**
El siguiente programa tiene el fin de encontrar palabras clave en los encabezados de archivos (excel, csv y txt) de un dispositivo, se puede usar tanto de manera local como una aplicación tipo cliente-servidor dentro de una misma red.

**NOTA: La aplicación estuvo un tiempo para modo cliente-servidor pero a la final quedó solamente para uso LOCAL.**

Los siguientes vinculos te desplazaran hasta la sección correspondiente:

[Requisitos previos](#requisitos-prevíos)

[Flujo programa cliente-servidor](#flujo-del-programa-en-modo-cliente-servidor)

[Cómo usar (en modo cliente-servidor)](#como-usar-el-programa-en-modo-cliente-servidor)

[Cómo usar (en modo local)](#como-usar-el-programa-en-modo-local)

---

## **Requisitos prevíos**

Para poder utilizar el programa se debe tener:
* Versión de Python 3
* Librería Pandas
* Librería openpyxl
* Librería xlrd

Para instalar las librerías debemos tener pip y en la consola realizar el siguiente comando:

    pip install nombre_librería

---

## **Flujo del programa en modo cliente-servidor**
El paso a paso del programa sería algo así:

1. Se inicia el servidor
2. Se inicia el cliente, conectandose al servidor
3. El servidor envía consultas hacia el cliente
4. El cliente procesa la consulta y devuelve el resultado al servidor
5. El servidor genera un archivo de texto con el resultado de la consulta

---

## **Como usar el programa en modo cliente-servidor**

Para utilizar el programa primero se tiene que ejecutar **server.py** en el dispositivo que hará de controlador/servidor, para ejecutar este script realizamos el siguiente comando:

    py .\server.py

Una vez ejecutamos esto podemos ver el puerto que está utilizando el servidor y la dirección IPv4 privada del mismo, esta la necesitaremos más adelante.

Lo siguiente sería cambiarnos al dispositivo donde deseamos buscar los archivos, este es el agente/cliente. En este dispositivo debemos ejecutar la clase **client.py**, y el comando para ejecutarla es el siguiente:

    py .\client.py dirección_IP_del_server

---

Si realizamos bien lo anterior, el cliente se conectará al servidor y se confirmará en ambas partes que se estableció conexión.

Una vez iniciado el programa, tendremos que específicar que palabras deseamos buscar en los archivos, esto lo hacemos con el comando "add", con este comando podemos adicionar unicamente 1 palabra a la vez, y se hace con el siguiente comando:

    add palabra

Si queremos agregar más palabras volvemos a usar el comando pero con la neuva palabra y esta se agregará a la lista de palabras de busqueda.

---

Lo siguiente sería realizar las consultas desde el dispositivo que hace de servidor, el comando actualmente es el siguiente:

    search ruta donde buscar

NOTA: La ruta debe ser separada por '\' y no debe terminar en backslash, lo ideal es que sea copiada y pegada del explorador de archivos. Ej: C:\Users\usuario\Documents

Despues de realizar esta consulta el cliente la procesará, despues de un momento mandará un mensaje de que ya finalizó y el servidor generará un archivo de texto con el resultado de la consulta. En esta se ve en que archivos se encuentra la palabra buscada.

---

Luego en el servidor si deseamos salir del prograa podemos escribir el comando:

    exit

Para cerrar ambos, tanto el cliente como el servidor, en caso tal de que no cierre correctamente se puede forzar la ejecución de un programa con 

    ctrl + C

---

## **Como usar el programa en modo local**
Para poder utilizar el programa de manera local para realizar las busquedas en nuestro dispositivo lo primero que debemos hacer es abrir una terminal en la dirección donde está ubicado el programa.

Luego podemos ejecutarlo según dos escenarios distintos:

1. Queremos buscar solo una palabra en una ruta en específico
2. Queremos buscar multiples palabras en una ruta en específico

Si queremos buscar solo una palabra, el comando para ejecutar el programa sería el siguiente:

    py .\main.py palabra ruta

Por otro lado, si queremos buscar varias palabras, sería de la siguiente manera:

    py .\main.py palabra1 palabra2 palabra3 ruta

### Aclaracines palabras
* El programa no está limitado solo a 3 palabras, se pueden buscar más, pero tener en cuenta que mientras más palabras, más largo será el tiempo de ejecución del programa
* Si se desea buscar una palabra compuesta por dos palabras (Ej: tipo id), se deben colocar las palabras con comilla simple, de la siguiente manera: 'tipo id', asi el programa la reconocerá como una sola palabra de busqueda

### Aclaraciones ruta
* La ruta debe de estar separada por backslash y no por slash sencillo, si queremos copiarla de una manera más sencilla, en el explorador de archivos nos ubicamos en la ruta donde deseamos buscar y copiamos y pegamos la ruta que aparece arriba.
* La ruta no debe finalizar en backslash sino en el nombre de la carpeta donde buscaremos.
* Si la ruta que deseamos buscar tiene espacios, debemos aplicar lo mismo del punto anterior, la ruta debemos de colocarla con comilla simple
* Ej 1: C:\Users\usuario\Desktop
* Ej 2: 'D:\carpeta\subcarpeta\mi carpeta'
