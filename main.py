import glob                                             #Recorrer achivos
import pandas as pd                                     #Dataframes
import re                                               #Regular expressions
import os                                               #Llamados al sistema
import warnings                                         #Ignorar warnings de excels con reglas de formato
from datetime import datetime                           #Para nombre archivo

l_extensiones = ['.csv', '.xlsx', '.xls', '.txt']       #Lista extensiones de archivos que se pueden buscar
l_searchWords = []                                      #Lista de palabras clave a buscar

now = datetime.now()
day_timef = now.strftime("%d-%m-%Y_%H.%M.%S")
output_name = 'output-'+day_timef+'.txt'
output = open(output_name, "w", encoding='utf-8')

warnings.filterwarnings('ignore', category=UserWarning, module='openpyxl')

def file_mapping(ext, num, loc):
    l_path = ['C:/Users/', os.getlogin(),'/']
    str1 = ''.join([str(elem) for elem in l_path])
    if(loc == 1):
        str2 = 'Downloads/**/*'
        str2 = str1 + str2 + ext
    elif(loc == 2):
        str2 = 'Desktop/**/*'
        str2 = str1 + str2 + ext
    elif(loc == 3):
        str2 = 'Documents/**/*'
        str2 = str1 + str2 + ext
    elif(loc == 5):
        str2 = 'C:/**/*' + ext
    elif(loc == 6):
        custom_path = input('\nIngrese la ruta del directorio en el que desea buscar (debe terminar en \'/\' y no debe llevar \'\\\'): ')
        output.write("Busqueda en ruta: " + custom_path + "\n")
        str2 = custom_path + '**/*' + ext
    try:
        search = glob.glob(str2, recursive=True)
    except Exception as e:
        print('[ERROR]: Ruta no valida. {}'.format(e))
    output.write('-'*100)
    output.write('\n')
    output.write("{} archivos encontrados con extensión \'{}\'\n\n".format(len(search), ext))
    for fileName in search:
        if(fileName == 'search_words.txt'):
            continue
        output.write('- {}\n'.format(fileName))
        if(num == 1):
            try:
                for w in  l_searchWords:
                    if(search_csv(fileName, w.upper()) == -1):
                        break
            except Exception as e:
                print('\n[Error]: search_csv falló {}'.format(e))
        elif(num == 2):
            try:
                for w in  l_searchWords:
                    if(search_excel(fileName, w.upper()) == -1):
                        break
            except Exception as e:
                print('\n[Error]: search_excel falló {}'.format(e))
        elif(num == 3):
            try:
                for w in  l_searchWords:
                    if(search_xls(fileName, w.upper()) == -1):
                        break
            except Exception as e:
                print('\n[Error]: search_xls falló {}'.format(e))
        elif(num == 4):
            try:
                for w in  l_searchWords:
                    if(search_txt(fileName, w.upper()) == -1):
                        break
            except Exception as e:
                print('\n[Error]: search_txt falló {}'.format(e))  
    output.write("\n\n\n")

def search_csv(csvName, word):
    try:
        df = pd.read_csv(csvName, sep=';')
    except Exception as e:
        return -1
    count = len(re.findall(word, df.to_string().upper()))
    if(count > 0):
        output.write(('    Veces que se repite \'{}\': {}\n'.format(word, count)))
def search_excel(excelName, word):
    try:
        df = pd.read_excel(excelName)
    except Exception as e:
        return -1   
    count = len(re.findall(word, df.to_string().upper()))
    if(count > 0):
        output.write('    Veces que se repite \'{}\': {}\n'.format(word, count))
def search_xls(excelName, word):
    try:
        df = pd.read_excel(excelName, engine='xlrd')
    except Exception as e:
        return -1
    count = len(re.findall(word, df.to_string().upper()))
    if(count > 0):
        output.write('    Veces que se repite \'{}\': {}\n'.format(word, count))
def search_txt(txtName, word):
    try:
        txtFile = open(txtName)
        lines = txtFile.readlines()
    except Exception as e:
        return -1
    count = 0
    for line in lines:
        times = len(re.findall(word, line.upper()))
        if(times != 0):
            count += times
    if(count > 0):
        output.write('   Veces que se repite \'{}\': {}\n'.format(word, count))

def load_words():
    txtWords = open('search_words.txt')
    lines = txtWords.readlines()
    print(len(lines))
    if(len(lines) == 0):
        return -1
    for line in lines:
        l_searchWords.append(line.strip())

def main():
    num = 0
    if(load_words() == -1):
        print('\n[ERROR]: No hay palabras de busqueda en el archivo de texto')
        output.close()
        os.remove(output_name)
        return
    while(num < 1 or num > 5):
        extension = input('\nIngrese el # del tipo de archivo que quiere buscar (o \'0\' para salir):\n(1) .csv\n(2) .xlsx\n(3) .xls\n(4) .txt\n(5) Todas las anteriores\n')
        l_e = ['.csv','.xlsx','.xls','.txt','Todas las extensiones']
        try:
            num = int(extension)
            if(num == 0):
                print('\n[EXIT]')
                output.close()
                os.remove(output_name)
                return
            if(num < 1 or num > 5):
                print("\n[Error]: Ingrese un valor valido")
                continue          
        except:
            print("\n[Error]: Ingrese un valor númerico")
            continue 
    location = 0
    while(location < 1 or location > 6):
        locationI = input('\nIngrese el # correspondiente a la carpeta donde desea buscar (o \'0\' para salir):\n(1) Descargas\n(2) Escritorio\n(3) Documentos\n(4) Todas las anteriores\n(5) Todo el disco C:\n(6) Escribir ruta manualmente\n')   
        l_p = ["Descargas", "Escritorio", "Documentos", "Descargas, Escritorio y Documentos", "Disco C:", "Ruta personalizada"]
        try:
            location = int(locationI)
            if(num == 0):
                print('\n[EXIT]')
                output.close()
                os.remove(output_name)
                return
            if(location < 1 or location > 6):
                print("\n[Error]: Ingrese un valor valido")
                continue
        except:
            print("\n[Error]: Ingrese un valor númerico")
            continue
    output.write("[BUSQUEDA] Ext: "+l_e[num-1]+", Ruta: "+l_p[location-1]+"\n")
    try:
        print("\nEn proceso... espere por favor")
        if(location > 0 and location < 7 and location != 4):
            if (num > 0 and num < 5):
                file_mapping(l_extensiones[num-1], num, location)
            elif num == 5:
                it = 0
                for e in l_extensiones:
                    it += 1
                    file_mapping(e, it, location)
        elif location == 4:
            l_l = ['DOWNLOADS', 'DESKTOP', 'DOCUMENTS']
            for l in range(3):
                output.write('\n\n[{}]\n'.format(l_l[l]))
                if (num > 0 and num < 5):
                    file_mapping(l_extensiones[num-1], num, l+1)
                elif num == 5:
                    it = 0
                    for e in l_extensiones:
                        it += 1
                        file_mapping(e, it, l+1)        
    except Exception as e:
        print('\n[Error]: file_mapping() falló. {}'.format(e))
    output.close()
    print('\nFIN')
main()