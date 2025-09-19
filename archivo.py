import modulos 

res_sum = modulos.suma(5, 3)
print("La suma es:", res_sum)

numero = int (4)
print(type(numero))

nota_examen = float (7.5)
nota_minima = 12
if nota_examen >= nota_minima:
    print("Aprobado")
else:
    print("Reprobado")

contador = 0
while contador < 5 :
    print("el contador es:", contador)
    contador +=1

frutas = ["manzana", "banana", "cereza"]
for fruta in frutas:
    print("Me gusta la", fruta)

def ensender(estado):
    if estado== 1 :
        print("La luz esta encendida")
    else:
        print("la luz esta apgada")

mi_lista = [1, 2, 3, 4, 5]
mi_tupla = (6, 7, 8, 9, 10)

def coordenadas():
    x= 10
    y= 20
    return x, y

resultado = coordenadas()
print(resultado)
print("juan" in mi_tupla)

diccionario = {"nombre": "Juan", "edad": 30, "ciudad": "Madrid"}
print(diccionario["nombre"])

diccionario["edad"] = 31
diccionario["profesion"] = "Ingeniero"
del diccionario["ciudad"]
if "edad" in diccionario:
    print("La clave 'edad' existe en el diccionario")
else:
    print("La clave 'edad' no existe en el diccionario")
for clave, valir in diccionario.items():
    print(clave, ":", valir)

#colecciones
conjunto = {1, 2, 3, 4, 5}
conjunto.add(6)
conjunto.remove(3)
conjunto2= {4,5,6,7,8}
if 3 in conjunto:
    print("El numero 3 esta en el conjunto")
else:
    print("El numero 3 no esta en el conjunto")
union = conjunto | conjunto2
interseccion = conjunto & conjunto2
diferencia = conjunto - conjunto2
print("Union:", union)
print("Interseccion:", interseccion)
print("Diferencia:", diferencia)

archivo = open("archivo.txt", "r")
contenido = archivo.read()
archivo.close()

archivo = open("archivo.txt", "a")
archivo.write("\nEsta es una nueva linea.")
archivo.close()

with open("archivo.txt", "r") as archivo:
    contenido = archivo.read()
    print(contenido)