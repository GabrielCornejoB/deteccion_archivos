# **Programa de detección de palabras en archivos**
El siguiente programa tiene el fin de encontrar palabras clave en archivos (excel, csv y txt) de un dispositivo, inicialmente estuvo pensado para ser usado localmente pero en la versión actual está implementado como un cliente-servidor.

El paso a paso del programa sería algo así:

1. Se inicia el servidor
2. Se inicia el cliente, conectandose al servidor
3. El servidor envía consultas hacia el cliente
4. El cliente procesa la consulta y devuelve el resultado al servidor
5. El servidor genera un archivo de texto con el resultado de la consulta

## **Requisitos prevíos**

Para poder utilizar el programa se debe tener:
* Versión de Python 3
* Librería Pandas
* Librería openpyxl
* Librería xlrd

Para instalar las librerías debemos tener pip y en la consola realizar el siguiente comando:

    pip install (nombre librería)

## **Como usar el programa**

Para utilizar el programa primero se tiene que ejecutar **server.py** en el dispositivo que hará de controlador/servidor, para ejecutar este script realizamos el siguiente comando:

    py server.py

Una vez ejecutamos esto podemos ver el puerto que está utilizando el servidor y la dirección IPv4 privada del mismo, esta la necesitaremos más adelante.

Lo siguiente sería cambiarnos al dispositivo donde deseamos buscar los archivos, este es el agente/cliente. En este dispositivo debemos ejecutar la clase **client.py**, y el comando para ejecutarla es el siguiente:

    py client.py (dirección IP del server)

Si realizamos bien lo anterior, el cliente se conectará al servidor y se confirmará en ambas partes que se estableció conexión.

Lo siguiente sería realizar las consultas desde el dispositivo que hace de servidor, el comando actualmente es el siguiente:

    search (palabra a buscar) (ruta donde buscar)

De momento está funcionando solo con una palabra pero ya está en proceso la opción de leer por archivo de texto.

Despues de realizar esta consulta el cliente la procesará, despues de un momento mandará un mensaje de que ya finalizó y el servidor generará un archivo de texto con el resultado de la consulta. En esta se ve en que archivos se encuentra la palabra buscada.

Luego en el servidor podemos escribir el comando:

    exit

Para cerrar ambos, tanto el cliente como el servidor, en caso tal de que no cierre correctamente se puede forzar la ejecución de un programa con 

    ctrl + C