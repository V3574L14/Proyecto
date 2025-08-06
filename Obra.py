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
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
    
    def detalles_obra(self): 
        print(f"Titulo: {self.titulo}")
        print("Información del artista:")
        print(f"\tNombre: {self.autor}")
        print(f"\tNacionalidad: {self.nacionalidad}")
        print(f"\tFecha de nacimiento: {self.fecha_nacimiento}")
        print(f"\tFecha de muerte: {self.fecha_muerte}")
        print(f"Tipo: {self.tipo}")
        print(f"Año de creacion: {self.año_creacion}")
    
    # hay varias obras con informacion vacia. reemplazar por "Desconocido". 