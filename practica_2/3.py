"""3- Hacer un programa que genere las tablas de 
multiplicar de los numeros multiplos de 5 que hay entre 1 y 1000"""

def multiple(valor, multiple):
    """
    Funcion para calcular si el numero es multiplo
    utilizando el modulo de la division
    """
    resto = valor % multiple
    if resto == 0:
        return True
    else:
        return False
 


multiples_5 =[]
 
for i in range(1,1001):
    if multiple(i,5):
        multiples_5.append(i)
 
print ("Los multiples de 5 son:", multiples_5)