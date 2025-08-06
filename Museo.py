from Departamento import Departamento
from Obra import Obra
from PIL import Image
from imagen import guardar_imagen_desde_url
import pandas as pd
import requests

class Museo: 
    def __init__(self):
        self.departamentos = []
        self.obras = []

    def start(self): 

        while True: 
            menu = input("\n\n\t\t***** METROART MUSEUM *****\n\t\t---------------------------\n¡Bienvenido al catálogo en linea de la colección del Museo Metropolitano de Arte!\n\nVer lista de obras por:\n\t1. Departamento\n\t2. Nacionalidad del autor\n\t3. Nombre del autor\n\t4. Salir\n---> ")

            if menu == "1": 
                print()
                self.busqueda_por_departamento()
                print()
                self.mostrar_detalles_obra()
            
            elif menu == "2": 
                print()
                self.busqueda_por_nacionalidad()
                print()
                self.mostrar_detalles_obra()

            elif menu == "3": 
                print()
                self.busqueda_por_autor()
                print()
                self.mostrar_detalles_obra()
            
            elif menu == "4": 
                break

            else:
                print("Ingreso invalido. ") 


    def mostrar_detalles_obra(self): 
        id_seleccionado = int(input("---> Ingrese el ID de la obra seleccionada: "))
        print("\n\t\t~ DETALLES DE LA OBRA ~") 
        for obra in self.obras:
            if obra.id == id_seleccionado:
                print()
                obra.detalles_obra()
                
                api_url = obra.imagen #hay obras que no tienen un link para la imagen. Indicar que no se encuentra disponible
                nombre_archivo_destino = "logo_aleatorio"                 
                nombre_archivo_destino = guardar_imagen_desde_url(api_url, nombre_archivo_destino) 
                img = Image.open(nombre_archivo_destino) 
                img.show() 

    def busqueda_por_autor(self): 
        autor_seleccionado = input("---> Ingrese el nombre del autor: ")
        for obra in self.obras: 
            if obra.autor == autor_seleccionado:
                obra.show() #el objeto esta creado en otra funcion
                print()

    def busqueda_por_nacionalidad(self): 
        df = pd.read_csv("CH_Nationality_List_20171130_v1.csv")
        for index, row in df.iterrows():
            print(f"{index + 1}. {row['Nationality']}")
        
        print()
        nac_seleccionada = input("---> Escriba la nacionalidad del autor: ")
        for obra in self.obras: 
            if obra.nacionalidad == nac_seleccionada: 
                obra.show() #el objeto esta creado en otra funcion
                print()
    
    def busqueda_por_departamento(self): 
        url_departamentos = "https://collectionapi.metmuseum.org/public/collection/v1/departments"
        data_departamentos = requests.get(url_departamentos)
        db_departamentos = data_departamentos.json()

        for dpto in db_departamentos["departments"]: 
            self.departamentos.append(Departamento(dpto["departmentId"], dpto["displayName"]))
        
        for departamento in self.departamentos:
            departamento.show()
            print()
        
        eleccion = int(input("---> Ingrese el ID del departamento seleccionado: "))
        print()

        url_obras_id = "https://collectionapi.metmuseum.org/public/collection/v1/objects"
        data_obras_id = requests.get(url_obras_id, params={"departmentIds": eleccion, "limit":10})
        db_obras = data_obras_id.json()

        db_obras_id = db_obras['objectIDs']

        url_obras = "https://collectionapi.metmuseum.org/public/collection/v1/objects/"
        indice_actual = 0 
        elementos = 20
        total_obras = len(db_obras_id)

        while indice_actual < total_obras:
            ids_actuales = db_obras_id[indice_actual:indice_actual + elementos]
            self.obras = []
                   
            for id in ids_actuales:
                try:
                    url = url_obras + str(id)
                    data_obras = requests.get(url)
                    db_obra = data_obras.json()

                    obra = Obra(db_obra['objectID'], db_obra['title'], db_obra['artistDisplayName'], db_obra['artistNationality'], db_obra['artistBeginDate'], db_obra['artistEndDate'], db_obra["classification"], db_obra["objectDate"], db_obra["primaryImage"]) 
                    self.obras.append(obra)

                except Exception as e:
                    print(f'Error con {id}, respuesta api: {data_obras}, data: {db_obra}, url: {url}, error: {e}')
                    break
                
            for obra in self.obras:
                obra.show()
                print()
            
            indice_actual += elementos

            if indice_actual < total_obras:
                respuesta = input("---> ¿Desea ver 20 obras más? (s/n): ")
                respuesta = respuesta.lower()
            
            if respuesta != "s":
                print("Fin de la búsqueda.")
                break
            
            else:
                print("No hay más obras por mostrar.")
            
            break