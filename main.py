import glob                                                     #Recorrer achivos
import pandas as pd                                             #Dataframes
import re                                                       #Regular expressions
import warnings                                                 #Ignorar warnings de excels con reglas de formato
import sys
from datetime import datetime
import time

l_exts = ['.csv','.xlsx','.xls','.txt']                         #Lista con las extensiones de los archivos a buscar
l_searchWords = []                                              #Lista de palabras clave a buscar
l_sumFiles = []                                                 #Lista de todos los archivos para el resumen

warnings.filterwarnings('ignore', category=UserWarning, module='openpyxl')
# warnings.filterwarnings('ignore', category=DTypeWarning, module='pandas')

now = datetime.now()
day_timef = now.strftime("%d-%m-%Y_%H.%M.%S")
output_name = 'outputs/output(local)-' + day_timef+ '.txt'   
output = open(output_name, "w", encoding='utf-8')
start_time = time.time()

def search_words(path, words):
    files = []
    print("Realizando la busqueda de los archivos en \'" + path + "\'");
    for e in l_exts:
        tmp_path =  path + '/**/*' + e
        files.extend(glob.glob(tmp_path, recursive=True))
    print("Archivos detectados, iniciando la busqueda de las palabras...");

    for word in words:
        print("Buscando la palabra \'" + word + "\'...")
        output.write("\n\nLa palabra " + word.upper() + " se encuentra en los siguientes archivos:")
        for filename in files:
            if(filename.lower().endswith(".csv")):
                search = search_csv(filename, word.upper())
                if(search > 0):
                    output.write('\n - ' + filename)
            elif(filename.lower().endswith(".xlsx")):
                search = search_xlsx(filename, word.upper())
                if(search > 0):
                    output.write('\n - ' + filename)
            elif(filename.lower().endswith(".xls")):
                search = search_xls(filename, word.upper())
                if(search > 0):
                    output.write('\n - ' + filename)
            elif(filename.lower().endswith(".txt")):
                search = search_txt(filename, word.upper())
                if(search > 0):
                    output.write('\n - ' + filename)

def search_csv(csvName, word):
    try:
        df = pd.read_csv(csvName, sep=';', encoding='utf-8')
    except Exception:
        return -1
    columns = list(df.columns.values)
    l = [c for c in columns if word in str(c).upper()]
    count = len(l)
    return count
def search_xlsx(excelName, word):
    try:
        df = pd.read_excel(excelName, engine='openpyxl')
    except Exception:
        return -1   
    columns = list(df.columns.values)
    l = [c for c in columns if word in str(c).upper()]
    count = len(l)
    return count
def search_xls(excelName, word):
    try:
        df = pd.read_excel(excelName, engine='xlrd')
    except Exception:
        return -1
    columns = list(df.columns.values)
    l = [c for c in columns if word in str(c).upper()]
    count = len(l)
    return count
def search_txt(txtName, word):
    try:
        txtFile = open(txtName)
        lines = txtFile.readlines()
    except Exception:
        return -1
    count = 0
    for line in lines:
        times = len(re.findall(word, line.upper()))
        if(times != 0):
            count += times
    return count

def start_search(words, path):  
    output.write("[BUSQUEDA]: Ruta: " + path + " Palabra(s): " + str(words))
    search_words(path, words)

if(len(sys.argv) >= 3):
    tmp_l = []
    for i in range(1, len(sys.argv)-1):
        tmp_l.append(sys.argv[i])
    
    print("Busqueda en proceso...")
    start_search(tmp_l, sys.argv[-1])
    print("Busqueda finalizada. Tiempo de ejecuci??n: {0:5f} segundos".format((time.time()-start_time)))
    output.close()