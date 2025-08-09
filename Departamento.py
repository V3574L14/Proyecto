class Departamento: 
    
    def __init__(self, id, nombre): 
        """
        Definir atributos de la clase. 

        Args:
            id (int): Identificación del departamento. 
            nombre (str): Nombre del departamento. 

        """
        self.id = id
        self.nombre = nombre

    def show(self):
        """
        Mostrar ID del departamento y el nombre respectivo. 

        """ 
        print(f"ID: {self.id} - {self.nombre}")