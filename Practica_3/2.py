'''2- Realizar una función que pida por pantalla un número del 1 al 10 y muestre
por pantalla el número escrito en letras.'''
r = None #es lo mismo que nada
c = int(input("Digite un numero del 1 al 10: "))
def numero():
   if c <= 10:
      if c == 1:
        r = "Uno"
      if c == 2:
        r = "Dos"
      if c == 3:
        r = "Tres"  
      if c == 4:
        r = "Cuatro"
      if c == 5:
        r = "Cinco"
      if c == 6:
        r = "Seis"
      if c == 7:
        r = "Siete"
      if c == 8:
        r = "Ocho"
      if c == 9:
        r = "Nueve" 
      if c == 10:
        r = "Diez" 
      print(r)        
   else:   
    print ("Usted no digito un numero del 1 al 10 :)")

numero()