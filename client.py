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

l_sw = []

while(True):
    msg = s.recv(1024).decode()
    print("from server: " + msg)
    if(msg.lower().startswith('search')):
        tokens = msg.split()
        if(len(tokens) != 2):
            print("El comando \'search\' solo lleva un argumento")
        else:
            print("Realizando busqueda")
            try:
                ans = search.start_search(l_sw, tokens[1])
                print("Busqueda finalizada")
            except Exception as e:
                ans = "No se pudo realizar la consulta." + e
    elif(msg.lower().startswith('add')):
        tokens = msg.split()
        for t in tokens[1:]:
            l_sw.append(t)
        


s.close()

