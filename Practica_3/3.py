'''3- Hacer una función que reciba un año como argumento y retorne
verdadero si es bisiesto.'''

a = int(input("Su año :"))
def bisiesto (año):
    if a % 4 == 0:
        print("es bisiesto")
        if a % 100 == 0:
          print("es bisiesto")
          if a % 400 == 0:
           print("es bisiesto")    
        return True
    else:
        print("no es bisiesto")
        return False


bisiesto(a)