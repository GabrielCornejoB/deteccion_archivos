import socket
import threading
from datetime import datetime
import sys

l_ips = []

def format_ip(l_ip):
    if(len(l_ip) != 4):
        print("Sintaxis de IP invalida")
        return -1
    for i in l_ip:
        if(int(i) > 255):
            print("Sintaxis de IP invalida, no debe superar 255")
            return -1

def validate_ips():
    if(len(sys.argv) != 2):
        print("Sintaxis no valida")
        return -1
    else:
        if(',' in sys.argv[1]):     #IPs no consecutivas
            tmp = sys.argv[1].split(',')
            for i in tmp:
                if(format_ip(i.split('.')) == -1):
                    return -1
            l_ips.extend(tmp)
        elif(':' in sys.argv[1]):   #Rango de IPs consecutivas
            l_tmp = sys.argv[1].split(':')        
            l_min = l_tmp[0].split('.')
            l_max = l_tmp[1].split('.')
            if(format_ip(l_min) == -1 or format_ip(l_max) == -1):
                return -1
            for i in range(0,2):
                if(l_min[i] != l_max[i]):
                    print("IPs de rango no coincide")
                    return -1
            if(l_min[3] < l_max[3]):
                for i in range(int(l_min[3]), int(l_max[3])+1):
                    tmp_arr = [l_min[0], l_min[1], l_min[2], str(i)]
                    tmp_str = '.'.join([item for item in tmp_arr])
                    l_ips.append(tmp_str)
            else:
                print("Segunda IP es menor a primera IP")
                return -1
        else:                       # Solo una dirección
            if(format_ip(sys.argv[1].split('.')) == -1):
                return -1
            l_ips.append(sys.argv[1])

l_sockets = []
l_sw = []

def thread_recv(ip):
    try:
        s = socket.socket()
        s.connect((ip,12345))
        l_sockets.append(s)
    except Exception as e:
        print("No se pudo conectar con: " + ip + "\n"+ str(e))
    else:
        print("Conexión con " + ip + " exitosa")

def main():
    end = False
    if(validate_ips() == -1):
        end = True
    print(l_ips)
    for ip in l_ips:
        thread_ip = threading.Thread(target=thread_recv, args=(ip,))
        thread_ip.start()

    while(True):
        msg = input()
        if(msg.lower() == 'exit'):
            end = True
            break
        # elif(msg.lower().startswith("add")):
        #     tokens = msg.split()
        #     if(len(tokens) > 1):
        #         for t in tokens[1:]:
        #             l_sw.append(t)
        #     print("Search words: " + str(l_sw))
        # elif(msg.lower().startswith('clear')):
        #     l_sw.clear()
        #     print("Se borraron las palabras de busqueda")
        # elif(msg.lower().startswith('search')):
        #     if(len(l_sw) == 0):
        #         print("Debe definir las palabras de busqueda antes de realizar la consulta.")
        #     elif(len(l_sockets) == 0):
        #         print("El servidor no se encuentra conectado a ningún cliente")
        #     else:
        #         tokens = msg.split()
        #         if(len(tokens) != 2):
        #             print("El comando \'search\' solo lleva un argumento")
        #             break
        elif(msg.lower().startswith("add") or msg.lower().startswith('clear') or msg.lower().startswith('search')):
            for s in l_sockets:
                s.send(msg.encode())
        else:
            print("Comando invalido")
    if(end is True):
        print("EXIT")
        return

main()
# s.close()