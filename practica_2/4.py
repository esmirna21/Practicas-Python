"""4- Realizar un programa que reciba
por teclado el sueldo de un empleado y 
le aplique los cálculos de ISR (ver tabla DGII), 
ARS, y AFP (investigar porcentajes)"""
sueldo = input("sueldo: ")
afp = sueldo * 0.0287
print(afp)
"""Siguiendo el ejemplo si tu salario es de RD$21.000,
 lo único que debes hacer es multiplicar por 2.87% o lo que es igual, por 0.0287:
RD$21.000 x 0.0287 = RD$602,70"""