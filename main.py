import glob
from tkinter import END                         #Recorrer achivos
import pandas as pd                 #Dataframes
import re                           #Regular expressions
import os                           #Llamados al sistema

l_extensiones = ['.csv', '.xlsx', '.xls', '.txt']

def main(): 
    ext = 0
    while(ext < 1 or ext > 4):
        extension = input('\nIngrese el # del tipo de archivo que quiere buscar:\n(1) .csv\n(2) .xlsx\n(3) .xls\n(4) .txt\n') 
        try:
            ext = int(extension)
            if ext == 1:
                print('csv')
            elif ext == 2:
                print('excel')
            elif ext == 3:
                print('excel viejitos')
            elif ext == 4:
                print('txt')
            else:
                print("\n[Error]: Ingrese una opción valida")
        except:
            print("\n[Error]: Ingrese un valor númerico")
    print('\nEND')

main()