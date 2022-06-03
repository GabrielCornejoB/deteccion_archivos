import glob                                                     #Recorrer achivos
import pandas as pd                                             #Dataframes
import re                                                       #Regular expressions
import os                                                       #Llamados al sistema
import warnings                                                 #Ignorar warnings de excels con reglas de formato
from datetime import datetime                                   #Para nombre archivo

l_exts = ['.csv','.xlsx','.xls','.txt','Todas las anteriores']  #Lista con las extensiones de los archivos a buscar
l_searchWords = []                                              #Lista de palabras clave a buscar
l_sumFiles = []                                                 #Lista de todos los archivos para el resumen

now = datetime.now()
day_timef = now.strftime("%d-%m-%Y_%H.%M.%S")

warnings.filterwarnings('ignore', category=UserWarning, module='openpyxl')

def file_mapping(ext, path, output, summary):
    l_path = ['C:/Users/', os.getlogin(),'/']
    user_path = ''.join([str(elem) for elem in l_path])
    folder_path = ['Downloads/**/*', 'Desktop/**/*', 'Documents/**/*', '.','C:/**/*']
    str_ext = l_exts[ext-1]
    if(path < 6):
        full_path = user_path + folder_path[path-1] + str_ext
    elif(path == 6):
        custom_path = input('\nIngrese la ruta del directorio en el que desea buscar (debe terminar en \'/\' y no debe llevar \'\\\'): ')
        output.write("Busqueda en ruta: " + custom_path + "\n")
        summary.write("Busqueda en ruta: " + custom_path + "\n")
        full_path = custom_path + '**/*' + str_ext

    # Busqueda cuando no es la opción 4 (buscar en Documentos, Descargas y Escritorio)
    if(path != 4):
        try:
            search = glob.glob(full_path, recursive=True)
        except Exception as e:
            print('[ERROR]: Ruta no valida. ' + e)

        output.write('-'*100)
        output.write('\n' + len(search) + 'archivos encontrados con extensión \'' + str_ext + '\'\n\n')
        for file_name in search:
            if('search_words.txt' in file_name):
                continue
            output.write('- ' + file_name + '\n')    
            try:
                if(ext == 1 or ext == 5):
                    for w in l_searchWords:
                        search_ext = search_csv(file_name, w.upper())
                        if(search_ext > 0):
                            break
                        output.write('    Veces que se repite \'' + w + '\': ' + search_ext + '\n')
                    output.write("\n\n\n")
                if(ext == 2 or ext == 5):
                    for w in l_searchWords:
                        search_ext = search_excel(file_name, w.upper())
                        if(search_ext > 0):
                            break
                        output.write('    Veces que se repite \'' + w + '\': ' + search_ext + '\n')
                    output.write("\n\n\n")
                if(ext == 3 or ext == 5):
                    for w in l_searchWords:
                        search_ext = search_xls(file_name, w.upper())
                        if(search_ext > 0):
                            break
                        output.write('    Veces que se repite \'' + w + '\': ' + search_ext + '\n')   
                    output.write("\n\n\n") 
                if(ext == 4 or ext == 5):
                    for w in l_searchWords:
                        search_ext = search_txt(file_name, w.upper())
                        if(search_ext > 0):
                            break
                        output.write('    Veces que se repite \'' + w + '\': ' + search_ext + '\n') 
                    output.write("\n\n\n")
            except Exception as e:
                print('\nNo fue posible leer el archivo: ' + file_name + 'Error: ' + e)
        l_sumFiles.extend(search)
    # else:
    #     try:
    #         print('a')
    #         # for i in range(3):            
    #     except Exception as e:
    #         print('[ERROR]: Ruta no valida. ' + e)   
    

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
def search_excel(excelName, word, out):
    try:
        df = pd.read_excel(excelName)
    except Exception:
        return -1   
    count = len(re.findall(word, df.to_string().upper()))
    if(count > 0 and out == 1):
        output.write('    Veces que se repite \'{}\': {}\n'.format(word, count))
    return count
def search_xls(excelName, word, out):
    try:
        df = pd.read_excel(excelName, engine='xlrd')
    except Exception:
        return -1
    count = len(re.findall(word, df.to_string().upper()))
    if(count > 0 and out == 1):
        output.write('    Veces que se repite \'{}\': {}\n'.format(word, count))
    return count
def search_txt(txtName, word, out):
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
    if(count > 0 and out == 1):
        output.write('   Veces que se repite \'{}\': {}\n'.format(word, count))
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
        print('\n[ERROR]: No hay palabras de busqueda en el archivo de texto')
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
    output_name = 'output-'+day_timef+'.txt'
    output = open(output_name, "w", encoding='utf-8')
    summary_name = "summary-"+day_timef+".txt"
    summary = open(summary_name, "w", encoding='utf-8')

    # 5. El programa escribe en el output la información sobre la busqueda
    l_paths = ["Descargas", "Escritorio", "Documentos", "Descargas, Escritorio y Documentos", "Disco C:", "Ruta personalizada"]
    output.write("[BUSQUEDA] Ext: "+l_exts[ext-1]+", Ruta: "+l_paths[path-1]+"\n")

    # 6. 
    try:
        print("\nEn proceso... espere por favor")
        if(location > 0 and location < 7 and location != 4):
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
    
    try:
        create_summary()
    except Exception as e:
        print('\n[ERROR]: create_summary() falló. {}'.format(e))
    output.close()
    summary.close()
main()
print('FIN DEL PROGRAMA')