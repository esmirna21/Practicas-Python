'''2- Crear una clase llamada Estudiante con un campo llamado promedio, el cual
solo podrá ser accedido mediante un metodo. El valor del promedio no puede
estar por encima de 100 que es la nota máxima.'''

class estudiante:
    def __init__ (self,matematica,español,ingles,ciencias):
      self.matematica = 140
      self.español = 80
      self.ingles = 70
      self.ciencias = 80

    def display (self):
        print(f"matematica = {self.matematica}, español = {self.español} , ingles = {self.ingles} , ciencias = {self.ciencias}")
    
    def promedio (self):
        promedio = (self.matematica + self.español + self.ingles + self.ciencias )/ 4
        if promedio < 60 :
            print("no paso el promedio")
        else:
            print(promedio)

    def ingresar (self):
        c = int(input("ingrese 5 para ingresar al promedio: "))
        if c == 5:
            estudiante.promedio(self)
           
            


estudiante1 = estudiante(60,70,80,60)
estudiante1.display()
estudiante1.ingresar()


