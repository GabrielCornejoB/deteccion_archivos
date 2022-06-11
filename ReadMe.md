# **Programa de detección de palabras en archivos**
El siguiente programa tiene el fin de encontrar palabras clave en archivos de un dispositivo, inicialmente estuvo pensado para ser usado localmente pero en la versión actual está implementado como un cliente-servidor.

En esta versión, el cliente se conecta al servidor, una vez se establece la conexión, el servidor manda las consultas al cliente, el cliente realiza el procesamiento del algoritmo que encuentra las palabras y envía el resultado al servidor, luego el servidor genera un archivo de salida con el resultado de la busqueda.

Para utilizar el programa primero se tiene que ejecutar **server.py**, que se ejecuta con el siguiente comando:

    py server.py

Luego en otro dispositivo (o incluso en el mismo es posible) se ejecuta **client.py**, para poder ejecutarlo debemos de colocar la dirección IP privada del dispositivo que hará de server. 

Para conocer la dirección IP, abrimos el **Simbolo del Sistema** en el dispositivo que hará de server y ejecutamos el comando

    ipconfig /all

Bajamos a las ultimas líneas y copiamos la dirección IP donde dice **"Dirección IPv4"**

Ahora si, para ejecutar **client.py**, debemos de digitar el siguiente comando:

    py client.py (dirección IP server)

Una vez logrado eso, se establecerá la conexión entre los dos dispositivos
