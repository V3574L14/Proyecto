import requests

url_departamentos = "https://collectionapi.metmuseum.org/public/collection/v1/departments"
url_obras = "https://collectionapi.metmuseum.org/public/collection/v1/objects/"

id_obra_solicitada = input("Ingrese el ID de la obra: ")

data_departments = requests.get(url_departamentos)
data_obras = requests.get(url_obras + id_obra_solicitada)

departments = data_departments.json()
obras = data_obras.json()

print(obras)