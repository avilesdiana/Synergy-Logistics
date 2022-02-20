print("Estructura del proyecto Final Parte 2 Análisis")

import matplotlib.pyplot as plt 
#Importar el csv
import csv
#Importar Pandas
import pandas as pd

with open('synergy_logistics_database.csv','r') as archivo_csv:
    lector = csv.reader(archivo_csv)

    for linea in lector:
        print(linea[2])

        