import glob                                                     #Recorrer achivos
import pandas as pd                                             #Dataframes
import re                                                       #Regular expressions
import warnings                                                 #Ignorar warnings de excels con reglas de formato

l_exts = ['.csv','.xlsx','.xls','.txt']                         #Lista con las extensiones de los archivos a buscar
l_searchWords = []                                              #Lista de palabras clave a buscar
l_sumFiles = []                                                 #Lista de todos los archivos para el resumen
# Lista donde se adicionaran las distintas cadenas, esta luego será retornada
l_return = []

warnings.filterwarnings('ignore', category=UserWarning, module='openpyxl')

def search_words(path, word):
    files = []
    for e in l_exts:
        tmp_path =  path + '/**/*' + e
        files.extend(glob.glob(tmp_path, recursive=True))
    l_return.append("La palabra " + word.upper() + " se encuentra en los siguientes archivos:")
        
    for filename in files:
        if(filename.lower().endswith(".csv")):
            search = search_csv(filename, word.upper())
            if(search > 0):
                l_return.append(' - ' + filename)
        elif(filename.lower().endswith(".xlsx")):
            search = search_xlsx(filename, word.upper())
            if(search > 0):
                l_return.append(' - ' + filename)
        elif(filename.lower().endswith(".xls")):
            search = search_xls(filename, word.upper())
            if(search > 0):
                l_return.append(' - ' + filename)
        elif(filename.lower().endswith(".txt")):
            search = search_txt(filename, word.upper())
            if(search > 0):
                l_return.append(' - ' + filename)

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

def start_search(word, path):  
    l_return.clear()
    # Indica en el output, la busqueda que se realizó para recibir ese resultado
    l_return.append("BUSQUEDA: Ruta: " + path + " Palabra: " + word)
    # Busca según la ruta y la palabra entregada, en proceso la busqueda de varias palabras
    search_words(path, word)
    # Junta los elementos de la lista en un string
    l_return_str = "\n".join([str(elem) for elem in l_return])
    # Retorna la string con el output del programa
    return l_return_str