class Obra: 
    
    def __init__(self, id, titulo, autor, nacionalidad, fecha_nacimiento, fecha_muerte, tipo, año_creacion, imagen):
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
        print(f"* ID: {self.id}")
        print(f"* Título: {self.titulo}")
        print(f"* Autor: {"Desconocido" if self.autor == "" else self.autor}")
    
    def detalles_obra(self): 
        print(f"TITULO: {self.titulo}")
        print("INFORMACION DEL ARTISTA")
        print(f"\tNOMBRE: {"Desconocido" if self.autor == "" else self.autor}")
        print(f"\tNACIONALIDAD: {"-" if self.nacionalidad == "" else self.nacionalidad}")
        print(f"\tFECHA DE NACIMIENTO: {"-" if self.fecha_nacimiento == "" else self.fecha_nacimiento}")
        print(f"\tFECHA DE MUERTE: {"-" if self.fecha_muerte == "" else self.fecha_muerte}")
        print(f"TIPO: {self.tipo}")
        print(f"AÑO DE CREACION: {self.año_creacion}")