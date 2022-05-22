import glob                                             #Recorrer achivos
import pandas as pd                                     #Dataframes
import re                                               #Regular expressions
import os                                               #Llamados al sistema
import warnings

l_extensiones = ['.csv', '.xlsx', '.xls', '.txt']       #Lista extensiones de archivos que se pueden buscar
l_searchWords = []                                      #Lista de palabras clave a buscar

warnings.filterwarnings('ignore', category=UserWarning, module='openpyxl')

#Función que encuentra que archivos tienen la extensión elegida
def file_mapping(ext, num, loc):
    l_path = ['C:/Users/', os.getlogin(),'/']
    str1 = ''.join([str(elem) for elem in l_path])
    if(loc == 1):
        str2 = 'Downloads/**/*'
    elif(loc == 2):
        str2 = 'Desktop/**/*'
    elif(loc == 3):
        str2 = 'Documents/**/*'
    str3 = str1 + str2 + ext
    if(loc == 5):
        str3 = 'C:/**/*'
    search = glob.glob(str3, recursive=True)
    print("\n\n")
    print('-'*75)
    print("{} archivos encontrados con extensión \'{}\'\n".format(len(search), ext))
    for fileName in search:
        if(fileName == 'search_words.txt'):
            continue
        print('- {}'.format(fileName))      
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

# Buscan de forma distinta para cada tipo de archivo
def search_csv(csvName, word):
    try:
        df = pd.read_csv(csvName, sep=';')
    except Exception as e:
        # print('\n[ERROR]: read_csv falló {}'.format(e))
        return -1
    count = len(re.findall(word, df.to_string().upper()))
    if(count > 0):
        print(('    Veces que se repite \'{}\': {}'.format(word, count)))
def search_excel(excelName, word):
    try:
        df = pd.read_excel(excelName)
    except Exception as e:
        # print('\n[ERROR]: read_excel falló {}'.format(e))
        return -1   
    count = len(re.findall(word, df.to_string().upper()))
    if(count > 0):
        print('    Veces que se repite \'{}\': {}'.format(word, count))
def search_xls(excelName, word):
    try:
        df = pd.read_excel(excelName, engine='xlrd')
    except Exception as e:
        # print('\n[ERROR]: read_excel (xls) falló {}'.format(e))
        return -1
    count = len(re.findall(word, df.to_string().upper()))
    if(count > 0):
        print('    Veces que se repite \'{}\': {}'.format(word, count))
def search_txt(txtName, word):
    try:
        txtFile = open(txtName)
        lines = txtFile.readlines()
    except Exception as e:
        print('\n[ERROR]: archivo no valido'.format())
        return -1
    count = 0
    for line in lines:
        times = len(re.findall(word, line.upper()))
        if(times != 0):
            count += times
    if(count > 0):
        print('   Veces que se repite \'{}\': {}'.format(word, count))

# Carga palabras clave del archivo de texto
def load_words():
    txtWords = open('search_words.txt')
    lines = txtWords.readlines()
    for line in lines:
        l_searchWords.append(line.strip())

def main():
    ext = 0
    load_words()
    while(ext < 1 or ext > 5):
        extension = input('\nIngrese el # del tipo de archivo que quiere buscar (o \'0\' para salir):\n(1) .csv\n(2) .xlsx\n(3) .xls\n(4) .txt\n(5) Todas las anteriores\n')
        try:
            ext = int(extension)
            if(ext == 0):
                print('\n[EXIT]')
                return
            if(ext < 1 or ext > 5):
                print("\n[Error]: Ingrese un valor valido")
                continue          
        except:
            print("\n[Error]: Ingrese un valor númerico")
            continue 
    location = 0
    while(location < 1 or location > 5):
        location = input('\nIngrese el # correspondiente a la carpeta donde desea buscar (o \'0\' para salir):\n(1) Descargas\n(2) Escritorio\n(3) Documentos\n(4) Todas las anteriores\n(5) Todo el disco C:\n')   
        try:
            location = int(location)
            if(ext == 0):
                print('\n[EXIT]')
                return
            if(location < 1 or location > 5):
                print("\n[Error]: Ingrese un valor valido")
                continue
        except:
            print("\n[Error]: Ingrese un valor númerico")
            continue
    try:
        if(location > 0 and location < 6):
            if (ext > 0 and ext < 5):
                file_mapping(l_extensiones[ext-1], ext, location)
            elif ext == 5:
                it = 0
                for e in l_extensiones:
                    it += 1
                    file_mapping(e, it, location)
        elif location == 4:
            l_l = ['DOWNLOADS', 'DESKTOP', 'DOCUMENTS']
            for l in range(3):
                print('\n\n\t\t\t\t[{}]\n'.format(l_l[l]))
                if (ext > 0 and ext < 5):
                    file_mapping(l_extensiones[ext-1], ext, l+1)
                elif ext == 5:
                    it = 0
                    for e in l_extensiones:
                        it += 1
                        file_mapping(e, it, l+1)
    except Exception as e:
        print('\n[Error]: file_mapping() falló. {}'.format(e))
    print('\nEND')
main()