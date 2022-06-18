import socket
import threading
import sys
import main as search

# Variable de salida para los hilos
end = False

# Creación socket
s = socket.socket()
print("Socket creado exitosamente por cliente")

# Vinculación del socket
port = 12345
s.bind(('',12345))
print('Socket asociado al puerto ' + str(port))

hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)
print("IP del cliente: " + str(ip))

# Escucha 1 petición de conexión (la del server)
s.listen(1)
print("Cliente esperando a server")

con, address = s.accept()

print("conectó")

# Thread_recv()
