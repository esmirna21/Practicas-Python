'''4- Cree una clase llamada Personaje con los métodos de instancia MoverArriba,
MoverAbajo, MoverDerecha y MoverIzquierda. Cree una clase llamada Mario y
otra clase llamada Koopa que herede las funcionalidades de la clase Personaje.'''
class personaje:
  def __init__ (self,moverarriba,moverabajo,moverderecha,moverizquierda):
    self.moverarriba = "moverse hacia arriba"
    self.moverabajo = "moverse hacia abajo"
    self.moverderecha = "moverse hacia la derecha"
    self.moverizquierda = "moverse hacia la izquierda"
  def display(self):
     print( f'personaje puede:{self.moverarriba},{self.moverabajo}, {self.moverderecha },{self.moverizquierda}')

class mario (personaje):
  def __init__(self,flordefuego,mapache):
    self.flordefuego = "modo flor de fuego"
    self.mapache = "modo mapache"
  def display(self):
     print(f'Mario puede: {self.flordefuego},{self.mapache}')

class koopa (personaje):
  def __init__ (self,escupirfuego):
    self.escupirfuego = "escupir fuego"
  def display(self):
    print(f'koopa puede:{self.escupirfuego}')  

personaje1= personaje(True,True,True,True)
mario1 = mario(True,True)
personaje1.display()
mario1.display()
koopa1 = koopa(True)
koopa1.display()
