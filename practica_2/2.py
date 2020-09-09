'''Realizar un programa que presente un menu con las siguientes opciones: 
1- Convertir grados a Celsius a F hrenheit
2- Convertir dolar a pesos
3- Convertir metros a pies
4- salir
Cada vez que finalice una de estas acciones deberegresar al menu.
El programa solo finalizara cuando el usuario elija la opcion salir.'''
import os
os.system("cls")
#Funcion que limpia la pantalla y muestra nuevamente el menu
def menu():
  print("elija una opcion del 1 al 4 ")
  print("1- Convertir grados a Celsius a Fhrenheit")
  print("2- Convertir dolar a pesos ")
  print("3- Convertir metros a pies ")
  print("4- Salir")


while True:
  menu()
  n = int(input())
  if n == 1:
    c = int(input("digite los Celsius: "))
    f = c * 9/5 + 32
    print(f)
  elif n == 2:
    d = int(input("digite dolares: "))
    p = d * 58.45
    print (p)
  elif n == 3:
    m = int(input("digite los metros: "))
    pie = m * 3.28084
    print (pie)
  elif n == 4:
    break
