from fileinput import filename
import glob
from msilib.schema import File                                             #Recorrer achivos
import pandas as pd                                     #Dataframes
import re                                               #Regular expressions
import os                                               #Llamados al sistema

l_extensiones = ['.csv', '.xlsx', '.xls', '.txt']       #Lista extensiones de archivos que se pueden buscar
l_searchWords = []                                      #Lista de palabras clave a buscar

#Función que busca en una dirección, en este caso './test_folder', los archivos con la extensión elegida
def file_mapping(ext, num, word):
    str1 = 'test_folder/*'
    str2 = str1 + ext
    print("\nArchivos que finalizan con la extensión \'{}\':".format(ext))
    for fileName in glob.glob(str2, recursive=True):
        print(' - {}'.format(fileName))
        if(num == 1):
            try:
                search_csv(fileName, word)
            except:
                print('\n[Error]: search_csv falló')
        elif(num == 2):
            try:
                search_excel(fileName, word)
            except:
                print('\n[Error]: search_excel falló')
        elif(num == 3):
            try:
                search_xls(fileName, word)
            except:
                print('\n[Error]: search_xls falló')
        elif(num == 4):
            try:
                search_txt(fileName, word)
            except:
                print('\n[Error]: search_txt falló')
        elif(num == 5):
            print('para todos')

def search_csv(csvName, word):
    df = pd.read_csv(csvName, sep=';')
    count = len(re.findall(word, df.to_string().upper()))
    if(count > 0):
        print(('    Veces que se repite \'{}\': {}'.format(word, count)))

def search_excel(excelName, word):
    df = pd.read_excel(excelName, sheet_name='Hoja1')
    count = len(re.findall(word, df.to_string().upper()))
    if(count > 0):
        print('    Veces que se repite \'{}\': {}'.format(word, count))

def search_xls(excelName, word):
    df = pd.read_excel(excelName, engine='xlrd')
    count = len(re.findall(word, df.to_string().upper()))
    if(count > 0):
        print('    Veces que se repite \'{}\': {}'.format(word, count))

def search_txt(txtName, word):
    txtFile = open(txtName)
    lines = txtFile.readlines()
    count = 0
    for line in lines:
        times = len(re.findall(word, line.upper()))
        if(times != 0):
            count += times
    if(count > 0):
        print('   Veces que se repite \'{}\': {}'.format(word, count))

def main():
    ext = 0
    while(ext < 1 or ext > 4):
        extension = input('\nIngrese el # del tipo de archivo que quiere buscar:\n(1) .csv\n(2) .xlsx\n(3) .xls\n(4) .txt\n(5) Todas las anteriores\n')
        try:
            ext = int(extension)
        except:
            print("\n[Error]: Ingrese un valor númerico")
            return
        search_word = input('\nIngrese la palabra que desea buscar: ')
        word_upper = search_word.upper()
        try:
            if ext == 1:
                file_mapping(l_extensiones[ext-1], ext, word_upper)
            elif ext == 2:
                file_mapping(l_extensiones[ext-1], ext, word_upper)
            elif ext == 3:
                file_mapping(l_extensiones[ext-1], ext, word_upper)
            elif ext == 4:
                file_mapping(l_extensiones[ext-1], ext, word_upper)
            elif ext == 5:
                it = 0
                for e in l_extensiones:
                    it += 1
                    file_mapping(e, it, word_upper)
            else:
                print("\n[Error]: Ingrese una opción valida")
        except:
            print('\n[Error]: file_mapping() falló')
    print('\nEND')
main()