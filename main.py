print("Estructura del proyecto Final Parte 2 Análisis")

#Importar el csv
import csv

with open('synergy_logistics_database.csv','r') as archivo_csv:
    lector = csv.reader(archivo_csv)

    for linea in lector:
        print(linea[2])