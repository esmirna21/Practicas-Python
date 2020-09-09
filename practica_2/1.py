'''Realizar un programa que solicite al
usuario un numero indeterminado de numeros
(mientras se tecleen nunmeros que no sean cero).
Al salir el programa debe dar en pantalla el total
de numeros dados y la suma de ellos.'''


print("no digite el cero ")
lasuma = 0 
while True:
   n = int(input("digite un numero: "))
   if n > 0:
     lasuma = lasuma + n
     print(lasuma)
   else:
    break

