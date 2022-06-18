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
    print(l_ips)

def thread_recv():
    print('a')

def thread_ip(ip):
    try:
        s = socket.socket()
        s.connect((ip,12345))
    except Exception as e:
        print("No se pudo conectar con: " + ip + "\n"+ str(e))
    else:
        print("Conexión con " + ip + " exitosa")
        # Input
        # thread_recv

def main():
    end = False
    if(validate_ips() == -1):
        end = True
    print(l_ips)
    for ip in l_ips:
        thread_i = threading.Thread(target=thread_ip, args=(ip,))
        thread_i.start()
    # 1. Verifica el argv
    # 2. Crea hilo por c/ip
    # 3. El hilo intenta conectarse al cliente de su ip, si falla muere hilo
    # 4. Si no falla, crea otro hilo pa recibir y utiliza ese mismo para input
    print('a')
    if(end is True):
        print("EXIT")
        return

main()
# s.close()