import socket
import threading
from datetime import datetime

# Creación socket
s = socket.socket()
print("Socket creado exitosamente por servidor")

# Puerto reservado
port = 12345

# Vinculación del puerto con el socket
s.bind(('', port))
print('Socket asociado al puerto ' + str(port))

# Socket escucha hasta 5 peticiones
s.listen(5)
print("Socket está escuchando peticiones")

l_cons = []

end = False

def thread_recv(con,addr):
    try:
        while True:
            try:
                msg = con.recv(1024).decode()     
            except Exception as e:
                print("[Error]: No se pudo recibir el mensaje: " + e)   
                l_cons.remove(con) 
            if(msg.startswith('[error]')):
                pass
            else:
                if(msg.startswith('[START]')):
                    now = datetime.now()
                    day_timef = now.strftime("%d-%m-%Y_%H.%M.%S")
                    output_name = 'outputs/output-'+day_timef+'.txt'
                    output = open(output_name, "w", encoding='utf-8')
                    print("Creando output...")              
                elif(msg.startswith('[END]')):     
                    output.close()
                    print("Output creado exitosamente")
                else:
                    output.write(msg + '\n')
            if end is True:
                break
    except:
        print("Hilo \'recv()\' finalizó")

# Creo que no hace falta un hilo pq solo quiero que sea una conexión
def thread_accept():
    try:
        while True:
            con, address = s.accept()                          
            print("Conexión establecida con: " + str(address))
            l_cons.append(con)
            thread_r = threading.Thread(target=thread_recv, args=(con,address))
            thread_r.daemon = True
            thread_r.start()
            if end is True:
                break
    except:
        print("Hilo \'accept()\' finalizó")

thread_a = threading.Thread(target=thread_accept)
thread_a.daemon = True
thread_a.start()

while True:
    msg = input()
    if(msg.lower() == 'exit'):
        end = True
        break
    if(len(l_cons) > 0):
        for c in l_cons:
            c.send(msg.encode())
    else:
        print("No hay conexiones activas")
    
for con in l_cons:
    con.close()
s.close()