class Obra: 
    
    def __init__(self, id, titulo, autor, nacionalidad, fecha_nacimiento, fecha_muerte, tipo, año_creacion, imagen):
        """
        Definir atributos de la clase. 

        Args:
            id (int): Número de identificación de la obra. 
            titulo (str): Nombre de la obra. 
            autor (str): Nombre del artista de la obra. 
            nacionalidad (str): Nacionalidad del artista. 
            fecha_nacimiento (str): Fecha de nacimiento del artista. 
            fecha_muerte (str): Fecha de muerte del artista. 
            tipo (str): Tipo de objeto al que se refiere la obra. 
            año_creacion (str): Epoca en la que se creó. 
            imagen (str): URL de la imagen de la obra. 

        """
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.nacionalidad = nacionalidad
        self.fecha_nacimiento = fecha_nacimiento
        self.fecha_muerte = fecha_muerte
        self.tipo = tipo
        self.año_creacion = año_creacion
        self.imagen = imagen

    def show(self):
        """
        Mostrar datos básicos de la obra por resultado de búsqueda. 

        """ 
        print(f"* ID: {self.id}")
        print(f"* Título: {self.titulo}")
        print(f"* Autor: {"Desconocido" if self.autor == "" else self.autor}")
    
    def detalles_obra(self): 
        """
        Mostrar detalles de la obra. 

        """
        print(f"TITULO: {self.titulo}")
        print("INFORMACION DEL ARTISTA")
        print(f"\tNOMBRE: {"Desconocido" if self.autor == "" else self.autor}")
        print(f"\tNACIONALIDAD: {"-" if self.nacionalidad == "" else self.nacionalidad}")
        print(f"\tFECHA DE NACIMIENTO: {"-" if self.fecha_nacimiento == "" else self.fecha_nacimiento}")
        print(f"\tFECHA DE MUERTE: {"-" if self.fecha_muerte == "" else self.fecha_muerte}")
        print(f"TIPO: {"-" if self.tipo == "" else self.tipo}")
        print(f"AÑO DE CREACION: {"-" if self.año_creacion == "" else self.año_creacion}")