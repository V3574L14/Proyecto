from Departamento import Departamento
from Obra import Obra
import requests

class Museo: 

    def start(self): 
        self.iniciar_objetos()

        while True: 
            menu = input("\n***** METROART *****\n\nBienvenido al catálogo en linea de la colección de arte del Museo Metropolitano de Arte\n\nSeleccione una opcion:\n\t1. Busqueda de obras\n\t2.Mostrar detalles de la obra\n\t3. Salir\n---> ")

            if menu == "1": 
                busqueda = input("\n\tBUSQUEDA DE OBRAS\n\nVer listas de obras por:\n\ta. Departamento\n\tb. Nacionalidad del autor\n\tc. Nombre del autor\n---> ")
                if busqueda == "a": 
                    self.busqueda_por_departamento()
                elif busqueda == "b": 
                    pass
                elif busqueda == "c": 
                    pass
            
            elif menu == "2": 
                pass

            elif menu == "3": 
                break

            else:
                print("Ingreso invalido. ") 


    def mostrar_detalles_obra(self): 
        pass
    
    def busqueda_por_autor(self): ###
        pass

    def busqueda_por_nacionalidad(self): ###
        pass

    def busqueda_por_departamento(self): 
        for dpto in self.departamentos: 
            dpto.show()
            print()


    def iniciar_objetos(self): 

        url_departamentos = "https://collectionapi.metmuseum.org/public/collection/v1/departments"
        url_obras_id = "https://collectionapi.metmuseum.org/public/collection/v1/objects"
        url_obras = "https://collectionapi.metmuseum.org/public/collection/v1/objects/"

        data_departamentos = requests.get(url_departamentos)
        data_obras_id = requests.get(url_obras_id)
        # id_obra_solicitada = input("Ingrese el ID de la obra: ")
        # data_obras = requests.get(url_obras + id_obra_solicitada)

        db_departamentos = data_departamentos.json()
        db_obras_id = data_obras_id.json()
        # db_obras = data_obras.json()



        departamentos_dic = self.db_departamentos["departments"]
        obras_dic = {}

        self.departamentos = []
        self.obras = []

        for dpto in departamentos_dic: 
            self.departamentos.append(Departamento(dpto["departmentId"], dpto["displayName"]))

        for id in db_obras_id["objectIDs"]: 
            url = url_obras + str(id)
            obras = requests.get(url)
            db_obra = obras.json() 
            todas_obras = []
            todas_obras.append(db_obra)
            obras_dic["obras"] = todas_obras

        for obra in obras_dic: 
            self.obras.append(Obra(obra["objectID"], obra["title"], obra["artistDisplayName"], obra["artistNationality"], obra["artistBeginDate"], obra["artistEndDate"], obra["classification"], obra["objectDate"], obra["primaryImage"]))


        
        
