"""4- Realizar un programa que reciba
por teclado el sueldo de un empleado y 
le aplique los cálculos de ISR (ver tabla DGII), 
ARS, y AFP (investigar porcentajes)"""
top1 = 416220.00
top2 = 624329.00
top3 = 867123.00
sueldo = (float(input("ingrese su sueldo: ")))
salario_anual = sueldo * 12
isr = 0;
 
if salario_anual <= top1:
    print("excenta")  
elif salario_anual <= top2:
    excedente = salario_anual - top1
    isr = excedente * 0.15
elif salario_anual <= top3:
    excedente = salario_anual - top2
    isr = 31216.00 + (excedente * 0.20)
else:
    excedente = salario_anual - top3
isr = 79776.00 + excedente * 0.25
print("irs valor anual: " ,isr)
print ("irs valor mensual: " , isr / 12)
afp = sueldo * 0.0287
print("AFP: ", afp )
ars = sueldo * 0.304
print ("ARS: ", ars)