import requests

data_departments = requests.get("https://collectionapi.metmuseum.org/public/collection/v1/departments")
data_obras = requests.get("https://collectionapi.metmuseum.org/public/collection/v1/objects")

departments = data_departments.json()
obras = data_obras.json()

print(departments)