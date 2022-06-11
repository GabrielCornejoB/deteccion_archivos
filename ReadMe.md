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

Una vez ejecutamos esto podemos ver el puerto que está utilizando el servidor y la dirección IPv4 privada del mismo, esta la necesitaremos para un paso más adelante.

Luego en otro dispositivo (o incluso en el mismo es posible) se ejecuta **client.py**, para poder ejecutarlo debemos de colocar la dirección IP privada del dispositivo que hará de server. 

Para conocer la dirección IP, abrimos el **Simbolo del Sistema** en el dispositivo que hará de server y ejecutamos el comando

    ipconfig /all

Bajamos a las ultimas líneas y copiamos la dirección IP donde dice **"Dirección IPv4"**

Ahora si, para ejecutar **client.py**, debemos de digitar el siguiente comando:

    py client.py (dirección IP server)

Una vez logrado eso, se establecerá la conexión entre los dos dispositivos
