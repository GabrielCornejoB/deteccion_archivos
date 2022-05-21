from fileinput import filename
import glob
from msilib.schema import File                                             #Recorrer achivos
import pandas as pd                                     #Dataframes
import re                                               #Regular expressions
import os                                               #Llamados al sistema

l_extensiones = ['.csv', '.xlsx', '.xls', '.txt']       #Lista extensiones de archivos que se pueden buscar
l_searchWords = []                                      #Lista de palabras clave a buscar

def file_mapping(ext, num):
    str1 = 'test_folder/*'
    str2 = str1 + ext
    for fileName in glob.glob(str2, recursive=True):
        print('- {}'.format(fileName))
        if(num == 1):
            try:
                for w in  l_searchWords:
                    search_csv(fileName, w.upper())
            except:
                print('\n[Error]: search_csv falló')
        elif(num == 2):
            try:
                for w in  l_searchWords:
                    search_excel(fileName, w.upper())
            except:
                print('\n[Error]: search_excel falló')
        elif(num == 3):
            try:
                for w in  l_searchWords:
                    search_xls(fileName, w.upper())
            except:
                print('\n[Error]: search_xls falló')
        elif(num == 4):
            try:
                for w in  l_searchWords:
                    search_txt(fileName, w.upper())
            except:
                print('\n[Error]: search_txt falló')  


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

def load_words():
    txtWords = open('search_words.txt')
    lines = txtWords.readlines()
    for line in lines:
        l_searchWords.append(line.strip())
    print(l_searchWords)

def main():
    ext = 0
    load_words()
    while(ext < 1 or ext > 5):
        valid = 1
        extension = input('\nIngrese el # del tipo de archivo que quiere buscar (o \'0\' para salir):\n(1) .csv\n(2) .xlsx\n(3) .xls\n(4) .txt\n(5) Todas las anteriores\n')
        try:
            ext = int(extension)
            if(ext == 0):
                print('\n[EXIT]')
                break
            if(ext < 1 or ext > 5):
                print("\n[Error]: Ingrese un valor valido")
                valid = -1
        except:
            print("\n[Error]: Ingrese un valor númerico")
            valid = -1
        if(valid == 1):   
            try:
                if (ext > 0 and ext < 5):
                    file_mapping(l_extensiones[ext-1], ext)
                elif ext == 5:
                    it = 0
                    for e in l_extensiones:
                        it += 1
                        file_mapping(e, it)
                else:
                    print("\n[Error]: Ingrese una opción valida")
            except:
                print('\n[Error]: file_mapping() falló')
    print('\nEND')
main()