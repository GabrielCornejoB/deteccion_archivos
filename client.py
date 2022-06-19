from http.server import ThreadingHTTPServer
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

def thread_recv():
    while(True):
        msg = con.recv(1024).decode()
        print("from server: " + msg)
        if(msg.lower().startswith('search')):
            if(len(l_sw) == 0):
                con.send("[error] No hay palabras de busqueda.".encode())
            else:
                if(len(msg) <= 7):
                    con.send("[error] Comando \'search\' incompleto.".encode())
                else:
                    path_n = msg[7:]
                    print("Realizando busqueda")
                    try:
                        ans = search.start_search(l_sw, path_n)
                        print("Busqueda finalizada")
                    except Exception as e:
                        ans = "No se pudo realizar la consulta." + e
                    con.send(ans.encode())
        elif(msg.lower().startswith('add')):
            if(len(msg) > 4):
                word = msg[4:]
                l_sw.append(word)
                con.send(("[sw] Search words: {}".format(l_sw)).encode())
            else:
                con.send("[error] Comando \'add\' incompleto.".encode())
        elif(msg.lower().startswith('clear')):
            l_sw.clear()
            con.send("[cl] Se borraron las palabras de busqueda exitosamente.".encode())
        elif(msg.lower().startswith('exit')):
            con.send('[exit]'.encode())
            break

def main():
    thread_r = threading.Thread(target=thread_recv)
    thread_r.start()
    while(thread_r.is_alive()):
        pass

main()     
s.close()

