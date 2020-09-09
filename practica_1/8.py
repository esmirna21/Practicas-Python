'''Almacene monto, cantidad de cuotas,
porcentaje de interes anual de un prestamo y 
calcule la cuota mensual. (Amortizar mediante el sistema frances)'''
monto = 100000.00
cant_cuotas = 12
pia = 30 
r = pia * monto /100
e = (monto - r )/ 12
print(float(e))
