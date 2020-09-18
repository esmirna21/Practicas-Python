'''3- Hacer una clase llamada Aritmética, que contenga métodos para cada una de
las operaciones aritméticas básicas.'''

class arimetmetica:
    def __init__ (self,a,b):
        self.suma = a + b
        self.resta = a - b
        self.multiplicacion = a * b
        self.division = a / b
        self.potencia = a**a
    def display(self):
        print(f"suma:  {self.suma} resta:  {self.resta} multiplicacion:  {self.multiplicacion} division: {self.division} potencia: {self.potencia}")


math = arimetmetica(5,2)
math.display()