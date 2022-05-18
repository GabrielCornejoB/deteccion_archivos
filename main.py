from fileinput import filename
import glob                                             #Recorrer achivos
import pandas as pd                                     #Dataframes
import re                                               #Regular expressions
import os                                               #Llamados al sistema

l_extensiones = ['.csv', '.xlsx', '.xls', '.txt']       #Lista extensiones de archivos que se pueden buscar

#Función que busca en una dirección, en este caso './test_folder', los archivos con la extensión elegida
def file_mapping(ext, num, word):
    str1 = 'test_folder/*'
    str2 = str1 + ext
    print("\nArchivos que finalizan con la extensión \'{}\':".format(ext))
    for fileName in glob.glob(str2, recursive=True):
        print(' - {}'.format(fileName))
        if(num == 1):
            search_csv(fileName, word)
        elif(num == 2):
            try:
                search_excel(fileName, word)
            except:
                print('\n[Error]: search_excel falló')
        elif(num == 3):
            search_excel(fileName, word)
        else:
            search_txt(fileName, word)

def search_csv(csvName, word):
    df = pd.read_csv(csvName, sep=';')
    print(('    Veces que se repite: {}'.format(len(re.findall(word, df.to_string())))))

def search_excel(excelName, word):
    df = pd.read_excel(excelName, sheet_name='Hoja1')
    print('    Veces que se repite: {}'.format(len(re.findall(word, df.to_string()))))

def search_xls(excelName, word):
    # df = pd.read_excel(excelName)
    # print('    Veces que se repite: {}'.format(len(re.findall(word, df.to_string()))))
    print('En proceso')

def search_txt(txtName, word):
    txtFile = open(txtName)
    lines = txtFile.readlines()
    count = 0
    for line in lines:
        times = len(re.findall(word, line))
        if(times != 0):
            count += times
    print('   Veces que se repite: {}'.format(count))

def main():
    ext = 0
    while(ext < 1 or ext > 4):
        extension = input('\nIngrese el # del tipo de archivo que quiere buscar:\n(1) .csv\n(2) .xlsx\n(3) .xls\n(4) .txt\n')
        try:
            ext = int(extension)
        except:
            print("\n[Error]: Ingrese un valor númerico")
        search_word = input('\nIngrese la palabra que desea buscar: ')
        try:
            if ext == 1:
                file_mapping(l_extensiones[ext-1], ext, search_word)
            elif ext == 2:
                file_mapping(l_extensiones[ext-1], ext, search_word)
            elif ext == 3:
                file_mapping(l_extensiones[ext-1], ext, search_word)
            elif ext == 4:
                file_mapping(l_extensiones[ext-1], ext, search_word)
            else:
                print("\n[Error]: Ingrese una opción valida")
        except:
            print('\n[Error]: file_mapping() falló')
    print('\nEND')
main()