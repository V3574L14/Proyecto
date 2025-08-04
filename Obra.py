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
        print(f"ID: {self.id}")
        print(f"Titulo: {self.titulo}")
        print(f"Autor: {self.autor}")
    
    def detalles_obra(self): 
        print(f"Titulo: {self.titulo}")
        print(f"Nombre del artista: {self.autor}")
        print(f"Nacionalidad del artista: {self.nacionalidad}")
        print(f"Fecha de nacimiento: {self.fecha_nacimiento}")
        print(f"Fecha de muerte: {self.fecha_muerte}")
        print(f"Tipo: {self.tipo}")
        print(f"Año de creacion: {self.año_creacion}")
        print(f"Imagen: {self.imagen}")