import glob                                                     #Recorrer achivos
import pandas as pd                                             #Dataframes
import re                                                       #Regular expressions
import warnings                                                 #Ignorar warnings de excels con reglas de formato

l_exts = ['.csv','.xlsx','.xls','.txt']                         #Lista con las extensiones de los archivos a buscar
l_searchWords = []                                              #Lista de palabras clave a buscar
l_sumFiles = []                                                 #Lista de todos los archivos para el resumen

warnings.filterwarnings('ignore', category=UserWarning, module='openpyxl')

def search_words(path, word, l_s):
    files = []
    for e in l_exts:
        tmp_path =  path + '/**/*' + e
        files.extend(glob.glob(tmp_path, recursive=True))

    l_s.append("La palabra " + word.upper() + " se encuentra en los siguientes archivos:")
        
    for filename in files:
        if(filename.lower().endswith(".csv")):
            search = search_csv(filename, word.upper())
            if(search > 0):
                l_s.append(' - ' + filename)
        elif(filename.lower().endswith(".xlsx")):
            search = search_xlsx(filename, word.upper())
            if(search > 0):
                l_s.append(' - ' + filename)
        elif(filename.lower().endswith(".xls")):
            search = search_xls(filename, word.upper())
            if(search > 0):
                l_s.append(' - ' + filename)
        elif(filename.lower().endswith(".txt")):
            search = search_txt(filename, word.upper())
            if(search > 0):
                l_s.append(' - ' + filename)
    return l_s

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
    # Lista donde se adicionaran las distintas cadenas, esta luego será retornada
    l_return_str = []
        
    # # Revisa si si se pasaron los argumentos necesarios para poder ejecutar el programa
    # if(len(sys.argv) != 3):
    #     print('\n[Error]: No se ingresaron los parametros previos en el llamado de la función. La función se debe llamar así: \'py main.py (palabra) (ruta)\'')
    #     return

    # Se comienza a realizar el resultado de la busqueda
    l_return_str.append('[START]')
    l_return_str.append("BUSQUEDA: Ruta: " + path + " Palabra: " + word + '\n')
    search_words(path, word, l_return_str)
    l_return_str.append('[END]')
    return l_return_str