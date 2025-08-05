import requests

url_departamentos = "https://collectionapi.metmuseum.org/public/collection/v1/departments"
url_obras = "https://collectionapi.metmuseum.org/public/collection/v1/objects"

id_obra_solicitada = input("Ingrese el ID de la obra: ")

data_departments = requests.get(url_departamentos)
data_obras = requests.get(url_obras + id_obra_solicitada)

if data_departments.status_code and data_obras.status_code == 200:
    print("\n** Carga de datos completada con exito.\n")
else: 
    print("\n** Error. Carga de datos fallida.\n")

departments = data_departments.json()
obras = data_obras.json()

print(departments)
print()
print(obras)