'''1- Modele tres entidades del mundo real, colocar por lo menos 3
características distintivas.'''

class persona:
    def __init__ (self,nombre,apellido,edad):
        self.nombre = "maria"
        self.apellido = "fernandez"
        self.edad = 20

    def display(self):
      print(f"nombre :  {self.nombre}  apelldo : {self.apellido} edad {self.edad}")   
    

class casa:
    def __init__ (self,tamaño,baños,habitaciones):
        self.tamaño = "37 metros cuadrados"
        self.baños = 1
        self.habitaciones = 1

    def display(self):
        print(f"Tamaño :   {self.tamaño}  Baños : {self.baños}  habitaciones {self.habitaciones}")

class carro:
    def __init__ (self,marca,color,asientos):
        self.marca = "toyota"
        self.color = "azul"
        self.asientos = 4
        
    def display (self):
        print(f"Marca :  {self.marca}  color: {self.color}  asientos {self.asientos}")


persona1 = persona ("maria","fernandez",20)
persona1.display()

