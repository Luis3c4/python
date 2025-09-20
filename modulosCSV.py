import csv

with open("usuarios.csv", "r") as archivo_csv:
    lector = csv.reader(archivo_csv)
    for fila in lector:
        print(fila)

datos= [["nombre", "edad"],
        ["Ana", 25]]

with open("nuevo.csv", "w", newline='') as nuevo_csv:
    escritor = csv.writer(nuevo_csv)
    escritor.writerows(datos)

nueva_fila = ["Luis", "35"]
archivo_csv= "usuarios.csv"
contenido_existente = []
with open(archivo_csv, "r") as archivo:
    lector = csv.reader(archivo)
    contenido_existente = list(lector)

contenido_existente.append(nueva_fila)
with open(archivo_csv, "w", newline='') as archivo:
    escritor = csv.writer(archivo)
    escritor.writerows(contenido_existente)