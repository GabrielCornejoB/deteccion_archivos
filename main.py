import glob
from numpy import full                                                     #Recorrer achivos
import pandas as pd                                             #Dataframes
import re                                                       #Regular expressions
import os                                                       #Llamados al sistema
import warnings                                                 #Ignorar warnings de excels con reglas de formato
from datetime import datetime                                   #Para nombre archivo

l_exts = ['.csv','.xlsx','.xls','.txt','Todas las anteriores']  #Lista con las extensiones de los archivos a buscar
l_searchWords = []                                              #Lista de palabras clave a buscar
l_sumFiles = []                                                 #Lista de todos los archivos para el resumen

warnings.filterwarnings('ignore', category=UserWarning, module='openpyxl')

def file_mapping(ext, path, output):
    l_path = ['C:/Users/', os.getlogin(),'/']
    user_path = ''.join([str(elem) for elem in l_path])
    folder_path = ['Downloads/**/*', 'Desktop/**/*', 'Documents/**/*', '.','C:/**/*']
    paths = []
    if(ext == 5):
        if(path != 4):
            for i in range(4):
                tmp_path = user_path + folder_path[path-1] + l_exts[i]
                paths.append(tmp_path)
        else:
            for i in range(4):
                for j in range(3):
                    tmp_path = user_path + folder_path[j] + l_exts[i]
                    paths.append(tmp_path)  
    str_ext = l_exts[ext-1]
    if(path < 6 and path != 4):
        full_path = user_path + folder_path[path-1] + str_ext
        paths.append(full_path)
    elif(path == 6):
        custom_path = input('\nIngrese la ruta del directorio en el que desea buscar (debe terminar en \'/\' y no debe llevar \'\\\'): ')
        output.write("Busqueda en ruta: " + custom_path + "\n")
        # summary.write("Busqueda en ruta: " + custom_path + "\n")
        full_path = custom_path + '**/*' + str_ext
        paths.append(full_path)
  
    for p in paths:
        try:
            search = glob.glob(p, recursive=True)
        except Exception as e:
            print('[ERROR]: Ruta no valida. ' + e)
        output.write('\n\n' + ('-'*100) + '\n\n\n')
        # output.write('\n' + str(len(search)) + ' archivos encontrados con extensión \'' + str_ext + '\'\n\n')
        for file_name in search:
            if('search_words.txt' in file_name):
                continue
            output.write('- ' + file_name + '\n')    
            try:
                if(file_name.endswith('.csv')):
                    for w in l_searchWords:
                        search_ext = search_csv(file_name, w.upper())
                        if(search_ext < 0):
                            break
                        elif(search_ext > 0):
                            output.write('    Veces que se repite \'' + w + '\': ' + str(search_ext) + '\n')
                    output.write('\n')
                if(file_name.endswith('.xlsx')):
                    for w in l_searchWords:
                        search_ext = search_excel(file_name, w.upper())
                        if(search_ext < 0):
                            break
                        elif(search_ext > 0):
                            output.write('    Veces que se repite \'' + w + '\': ' + str(search_ext) + '\n')
                    output.write('\n')
                if(file_name.endswith('.xls')):
                    for w in l_searchWords:
                        search_ext = search_xls(file_name, w.upper())
                        if(search_ext < 0):
                            break
                        elif(search_ext > 0):
                            output.write('    Veces que se repite \'' + w + '\': ' + str(search_ext) + '\n') 
                    output.write('\n')
                if(file_name.endswith('.txt') or file_name.endswith('.TXT')):
                    for w in l_searchWords:
                        search_ext = search_txt(file_name, w.upper())
                        if(search_ext < 0):
                            break
                        elif(search_ext > 0):
                            output.write('    Veces que se repite \'' + w + '\': ' + str(search_ext) + '\n') 
                    output.write('\n')
            except Exception as e:
                print('\nNo fue posible leer el archivo: ' + file_name + 'Error: ' + e)
        l_sumFiles.extend(search)
    

# def create_summary():
#     summary.write("RESUMEN BUSQUEDA: ")
#     for w in l_searchWords:
#         summary.write("\n\nLa palabra " + w.upper() + " se encuentra en los siguientes archivos:\n")
#         for fileName in l_sumFiles:
#             if(fileName == 'search_words.txt'):
#                 continue
#             if fileName.endswith('.csv'):
#                 try:
#                     search = search_csv(fileName, w.upper(), 0)
#                     if(search > 0):
#                         summary.write(' - ' + fileName + '\n')
#                 except Exception as e:
#                     print('\n[Error]: search_csv falló. ' + e)
#             elif fileName.endswith('.xlsx'):
#                 try:
#                     search = search_excel(fileName, w.upper(), 0)
#                     if(search > 0):
#                         summary.write(' - ' + fileName + '\n')
#                 except Exception as e:
#                     print('\n[Error]: search_xlsx falló. ' + e)
#             elif fileName.endswith('.xls'):
#                 try:
#                     search = search_xls(fileName, w.upper(), 0)
#                     if(search > 0):
#                         summary.write(' - ' + fileName + '\n')
#                 except Exception as e:
#                     print('\n[Error]: search_xls falló. ' + e)
#             elif fileName.endswith('.txt'):
#                 try:
#                     search = search_txt(fileName, w.upper(), 0)
#                     if(search > 0):
#                         summary.write(' - ' + fileName + '\n')
#                 except Exception as e:
#                     print('\n[Error]: search_txt falló. ' + e)

def search_csv(csvName, word):
    try:
        df = pd.read_csv(csvName, sep=';')
    except Exception:
        return -1
    count = len(re.findall(word, df.to_string().upper()))
    return count
def search_excel(excelName, word):
    try:
        df = pd.read_excel(excelName)
    except Exception:
        return -1   
    count = len(re.findall(word, df.to_string().upper()))
    return count
def search_xls(excelName, word):
    try:
        df = pd.read_excel(excelName, engine='xlrd')
    except Exception:
        return -1
    count = len(re.findall(word, df.to_string().upper()))
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

def load_words():
    txtWords = open('search_words.txt')
    lines = txtWords.readlines()
    print(len(lines))
    if(len(lines) == 0):
        return -1
    for line in lines:
        l_searchWords.append(line.strip())

def main():
    # 1. Revisa si el archivo de texto con las palabras de busqueda está vacío
    if(load_words() == -1):
        print('\n[Error]: No hay palabras de busqueda en el archivo de texto')
        return
   
    # 2. El programa pide al usuario que extensiones desea buscar
    ext = 0
    while(ext < 1 or ext > 5):
        input_ext = input('\nIngrese el # del tipo de archivo que quiere buscar:\n(1) .csv\n(2) .xlsx\n(3) .xls\n(4) .txt\n(5) Todas las anteriores\n')       
        try:
            ext = int(input_ext)          
        except:
            print("\n[Error]: Ingrese un valor númerico")
            continue 
        if(ext < 1 or ext > 5):
            print("\n[Error]: Ingrese un valor valido")

    # 3. El programa pide al usuario que ingrese la dirección donde desea buscar       
    path = 0
    while(path < 1 or path > 6):
        input_path = input('\nIngrese el # correspondiente a la carpeta donde desea buscar:\n(1) Descargas\n(2) Escritorio\n(3) Documentos\n(4) Todas las anteriores\n(5) Todo el disco C:\n(6) Escribir ruta manualmente\n')    
        try:
            path = int(input_path)
        except:
            print("\n[Error]: Ingrese un valor númerico")
        if(path < 1 or path > 6):
            print("\n[Error]: Ingrese un valor valido")
            continue

    # 4. Se crean los archivos de salida (output) y resumen (summary)
    now = datetime.now()
    day_timef = now.strftime("%d-%m-%Y_%H.%M.%S")
    output_name = 'outputs/output-'+day_timef+'.txt'
    output = open(output_name, "w", encoding='utf-8')
    # summary_name = "summary-"+day_timef+".txt"
    # summary = open(summary_name, "w", encoding='utf-8')

    # 5. El programa escribe en el output la información sobre la busqueda
    l_paths = ["Descargas", "Escritorio", "Documentos", "Descargas, Escritorio y Documentos", "Disco C:", "Ruta personalizada"]
    output.write("[BUSQUEDA] Ext: "+l_exts[ext-1]+", Ruta: "+l_paths[path-1]+"\n")

    # 6. Inicia la busqueda de las palabras en los archivos
    try:
        print("\nPrograma en ejecución, espere un momento por favor...\n")
        file_mapping(ext, path, output)       
    except Exception as e:
        print('\n[Error]: file_mapping() falló. {}'.format(e))
    
    # try:
    #     create_summary()
    # except Exception as e:
    #     print('\n[ERROR]: create_summary() falló. {}'.format(e))
    output.close()
    # summary.close()
main()
print('FIN DEL PROGRAMA')