'''5- Cree una clase Carro, con un campo llamado _cantidadCombustible y un
método que se llame Encender el cual en base a la gasolina disponible
mostrara si el carro pudo o no avanzar. Cada vez que el método se ejecute,
deberá restarse 1 a la gasolina disponible. La cantidad de gasolina debe
establecerse al momento de instanciar un objeto de del tipo de la clase.'''

class carro:
    def __init__(self,galones,):
        self.marca = "Toyota"
        self.tipo_combustible = "gasolina"
        self.galones_combustible = 5

    def encender(self):
        if self.galones_combustible > 0:
            self.galones_combustible -= 1
            print("El carro enciende")
        else:
            print("el carro no enciende")


c1 = carro (5)
c1.encender()

