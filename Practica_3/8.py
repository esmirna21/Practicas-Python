'''8- Hacer una función que reciba un valor iniciar y uno final, y muestre en
pantalla las tablas de multiplicar de los números múltiplos de 6 que hay
entre el valor inicial y el valor final.'''


c = int(input())
a = int(input())
def multiple(valor, multiple):
    resto = valor % multiple
    if resto == 0:
        return True
    else:
        return False
 

multiples_6=[]
 
for i in range(c,a):
    if multiple(i,6):
        multiples_6.append(i)
 
print ("Los multiples de 6 son:", multiples_6)
    

         

    






