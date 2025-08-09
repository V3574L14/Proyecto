from Departamento import Departamento
from Obra import Obra
from PIL import Image
from imagen import guardar_imagen_desde_url
from validacion_lista_nacionalidades import lista
import requests

class Museo: 
    def __init__(self):
        """
        Definir atributos de la clase. 

        """ 
        self.departamentos = []
        self.obras = []


    def start(self):
        """
        Iniciar el programa. 

        """ 
        while True: 
            menu = input("\n__________________________________________________________________________________\n\n\t\t\t\t  ~ METROART MUSEUM ~\n\n¡Bienvenido al catálogo en línea de la colección del Museo Metropolitano de Arte!\n\nVer listado de obras por:\n\t1. Departamento\n\t2. Nacionalidad del autor\n\t3. Nombre del autor\n\t4. Salir\n---> ")

            if menu == "1": 
                print()
                self.busqueda_por_departamento()
                self.mostrar_detalles_obra()
            
            elif menu == "2": 
                print()
                self.busqueda_por_nacionalidad()
                self.mostrar_detalles_obra()

            elif menu == "3": 
                print()
                self.busqueda_por_autor()
                self.mostrar_detalles_obra()
            
            elif menu == "4": 
                break

            else:
                print("\n~ Ingreso inválido. Debe ingresar un número (1, 2, 3, 4).") 


    def mostrar_detalles_obra(self):
        """
        Mostrar los detalles de la obra seleccionada según el filtro elegido en el menú. 

        """ 
        seguir = True
        while seguir: 
            try: 
                id_seleccionado = int(input("\n---> Ingrese el ID de la obra seleccionada de la lista: "))
                for obra in self.obras:
                    if id_seleccionado == obra.id:
                        seguir = False
                        break
            except ValueError:
                print("~ Ingreso inválido. Debe escribir el ID de una de las obras mostradas.\n")

        print("\n__________________________________________________________________________________\n\n\t\t\t\t~ DETALLES DE LA OBRA ~") 
        for obra in self.obras:                                                     
            if obra.id == id_seleccionado:
                print()
                obra.detalles_obra()
                ver_imagen = input("\n\t¿Desea ver la imagen de la obra en otra ventana?\n\t(Ingrese (s) de ser afirmativa su respuesta, de lo contrario ingrese cualquier otro caracter)\n---> ")
                if ver_imagen == "s": 
                    if obra.imagen == "":
                        print("~ Imagen no disponible.")
                    else: 
                        api_url = obra.imagen
                        nombre_archivo_destino = "imagen_obra"                 
                        nombre_archivo_destino = guardar_imagen_desde_url(api_url, nombre_archivo_destino) 
                        img = Image.open(nombre_archivo_destino) 
                        img.show()


    def busqueda_por_autor(self):
        """
        Filtrar la lista de obras según el autor indicado por el usuario. 

        """  
        while True: 
            try:
                autor_seleccionado = str(input("\tEscriba el nombre del autor:\n\t(Asegúrese de escribirlo correctamente)\n---> "))
                break
            except ValueError:
                print("~ Ingreso inválido.\n")
        
        url_autores = "https://collectionapi.metmuseum.org/public/collection/v1/search"
        data_autor = requests.get(url_autores, params={"artistOrCulture": "true", "q": autor_seleccionado})
        db_autor = data_autor.json()
        self.obtener_obras(db_autor["objectIDs"])


    def busqueda_por_nacionalidad(self):
        """
        Mostrar lista de nacionalidades. 
        Filtrar la lista de obras según la nacionalidad del autor indicada por el usuario.  

        """  
        archivo = open("CH_Nationality_List_20171130_v1.csv")
        print(archivo.read())
        
        seguir = True
        while seguir: 
            try:
                nac_seleccionada = str(input("\tEscriba la nacionalidad del autor:\n\t(Asegúrese de escribirlo tal como aparece en el listado)\n---> "))
                for i in lista: 
                    if nac_seleccionada == i: 
                        seguir = False
                        break
            except ValueError:
                print("~ Ingreso inválido.\n")
        
        url_nacionalidades = "https://collectionapi.metmuseum.org/public/collection/v1/search"
        data_nacionalidad = requests.get(url_nacionalidades, params={"artistOrCulture": "true", "q": nac_seleccionada})
        db_nacionalidad = data_nacionalidad.json()
        self.obtener_obras(db_nacionalidad["objectIDs"])
        

    def busqueda_por_departamento(self): 
        """
        Crear clase Departamentos. 
        Mostrar Departamentos. 
        Filtrar la lista de obras según el departamento del autor indicado por el usuario.  

        """ 
        url_departamentos = "https://collectionapi.metmuseum.org/public/collection/v1/departments"
        data_departamentos = requests.get(url_departamentos)
        db_departamentos = data_departamentos.json()

        for dpto in db_departamentos["departments"]: 
            self.departamentos.append(Departamento(dpto["departmentId"], dpto["displayName"]))
        
        for departamento in self.departamentos:
            departamento.show()
            print()
        
        while True: 
            try:
                eleccion = int(input("\n---> Ingrese el ID del departamento seleccionado: "))
                if eleccion == 0 or eleccion == 2 or eleccion == 20 or eleccion > 21: 
                    print("~ Ingreso inválido. Debe ingresar el número de ID de uno de los Departamentos mostrados.\n")
                    continue 
                break
            except ValueError:
                print("~ Ingreso inválido. Debe ingresar el número de ID de uno de los Departamentos mostrados.\n")

        print()
        url_obras = "https://collectionapi.metmuseum.org/public/collection/v1/objects"
        data_obras_id = requests.get(url_obras, params={"departmentIds": eleccion, "limit":10})
        db_obras = data_obras_id.json()
        self.obtener_obras(db_obras['objectIDs'])
    

    def obtener_obras(self, db_obras_id):
        """
        Crear clase Obras. 
        Mostrar de 20 en 20 obras del conjunto de obras obtenidas según la selección del usuario. 

        Args: 
            db_obras_id (list): Lista de id's que coinciden con la elección del usuario.

        """ 
        url_obras = "https://collectionapi.metmuseum.org/public/collection/v1/objects"
        obras = []
        indice_actual = 0 
        elementos = 20
        total_obras = len(db_obras_id)
        print(f"\nTotal de obras encontradas: {total_obras}")
        print("Buscando obras...")
        print()

        while indice_actual < total_obras:
            ids_actuales = db_obras_id[indice_actual:indice_actual + elementos]
                   
            for id in ids_actuales:
                try:
                    url = url_obras + "/" + str(id)
                    data_obras = requests.get(url)
                    db_obra = data_obras.json()
                    obra = Obra(db_obra['objectID'], db_obra['title'], db_obra['artistDisplayName'], db_obra['artistNationality'], db_obra['artistBeginDate'], db_obra['artistEndDate'], db_obra["classification"], db_obra["objectDate"], db_obra["primaryImage"]) 
                    obras.append(obra)

                except Exception as e:
                    print(f'Error con {id}, respuesta api: {data_obras}, data: {db_obra}, url: {url}, error: {e}')
                    break        
                
            for obra in obras:
                obra.show()
                print()
            
            indice_actual += elementos

            if total_obras > 20:
                if indice_actual < total_obras:
                    respuesta = input("\t¿Desea ver 20 obras más?\n\t(Ingrese s de ser afirmativa su respuesta, de lo contrario ingrese cualquier otro caracter)\n---> ")
                    respuesta = respuesta.lower()
                if respuesta != "s":
                    print("\nFin de la búsqueda.")
                    break
                else:
                    print("\nBuscando más obras...")

        self.obras = obras 