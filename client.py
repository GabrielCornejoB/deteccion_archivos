import socket
import threading
import sys
import main as search

# Variable de salida para los hilos
end = False

# Validaciones previas para la conexión con el servidor
s = socket.socket()
if(len(sys.argv) == 2):
    try:
        s.connect((sys.argv[1], 12345))
        print("Conexión con server exitosa")
    except:
        print("No se pudo realizar la conexión")
        end = True
else:
    end = True
    print("Debe ingresar la dirección IP del server")

# sw = open("search_words.txt", "w", encoding="utf-8")
# sw.close()
sw = []

# Hilo que recibe los mensajes del servidor
def thread_recv():
    try:
        while True:
            ans = s.recv(1024).decode()
            print("from server: " + ans)   
            if(ans.lower().startswith("search")):
                tokens = ans.split()
                if(len(tokens) == 2):
                    print("Realizando consulta...")
                    output_msg = search.start_search(sw, tokens[1])
                    s.send(output_msg.encode())
                    print("Consulta finalizada y enviada al servidor")
                else:
                    s.send("[error] Función incompleta. Debe escribirse así: \'search (palabra) (ruta)\'".encode())
            elif(ans.lower().startswith("add")):
                tokens = ans.split()
                if(len(tokens) > 1):
                    for t in tokens[1:]:
                        sw.append(t)
                    print("Search words: \n{}".format(sw))
                else:
                    s.send("[error] Función incompleta. Debe agregar al menos 1 argumento".encode())
    except:
        print("Finalizó la conexión con el server")
        s.close()
        
def main():
    thread_r = threading.Thread(target=thread_recv)
    thread_r.daemon = True
    thread_r.start()
    while thread_r.is_alive():
        pass

if(end is False):
    main()