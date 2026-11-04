import csv
import json
#propósito fundamental en el framework es la parametrización impulsada por datos (Data-Driven Testing).
# Esto permite separar por completo el código de los tests de las credenciales o datos fijos, leyendo todo directamente desde la carpeta data/.

#creo una funcion que será el lector del CSV
def read_users_csv():
    with open("data/users.csv",newline="") as file:
#aca lo convierto cada fila del CSV en una lista de diccionarios para ver lo que esta adentro
        reader = csv.DictReader(file)
#Transforma el lector en una lista real de diccionarios de Python y la devuelve
        return list(reader)
#Aca creo una funcion que será el lector del Json
def read_productos_json():
#Abre el archivo de formato estructurado JSON.        
        with open("data/products.json") as file:
#El módulo json analiza el archivo de texto y lo convierte directamente en la estructura nativa de datos correspondiente en Python             
            return json.load(file)
data = read_productos_json()
print(data)
        