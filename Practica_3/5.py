'''5- Un número palindrómico se lee igual en ambos sentidos. El palíndromo más
grande hecho del producto de dos números de 2 dígitos es 9009 = 91 × 99.
Cree una función que encuentre el palíndromo más grande hecho del
producto de dos números de 3 dígitos.'''

def palidromico(numero):
    if str(numero)==str(numero)[::-1]:
        return True
    else:
        return False

maximo_de_p=1
for n1 in range(100,999):
    for n2 in range(100,999):
        r=n1*n2  
        if palidromico(r):
            if r > maximo_de_p:
                maximo_de_p = r
print (maximo_de_p)

 
   