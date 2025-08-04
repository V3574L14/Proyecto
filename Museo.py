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
        url_obras = "https://collectionapi.metmuseum.org/public/collection/v1/objects/"

        id_obra_solicitada = input("Ingrese el ID de la obra: ")

        data_departmentos = requests.get(url_departamentos)
        data_obras = requests.get(url_obras + id_obra_solicitada)

        db_departmentos = data_departmentos.json()
        db_obras = data_obras.json()



        departamentos_dic = self.db_departamentos["departments"]

        self.departamentos = []
        self.obras = []

        for dpto in departamentos_dic: 
            self.departamentos.append(Departamento(dpto["id"], dpto["nombre"]))
        
        
