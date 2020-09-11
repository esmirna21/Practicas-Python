"""5-Cree una aplicación de cajero automático para el banco ABC. El cajero tendrá un
límite de billetes descrito a continuación: 9 de 1000, 19 de 500, 99 de 100
El cajero debe solicitar Banco y monto a retirar. Si el banco es ABC el limite de
retiro son 10,000 y 2000 pesos por transacción en caso contrario.
El cajero debe informar si el monto solicitado no puede ser dispensado o si
excede el límite de transacción. Y debe hacer la distribución de los billetes de
acuerdo al monto. Por ejemplo, si el usuario solicita 3,900 y hay disponibilidad en
todos los billetes, el cajero debe dispensar 3 billetes de mil, 1 de quinientos y 4 de
cien."""
bill1000 = 9
bill500 = 19
bill100 = 99
 
def billetes(cantidad):
  global bill1000, bill500, bill100
  if cantidad <= 1000 * bill1000 + 500 * bill500 + 100 * bill100: 

    de1000 = int(cantidad / 1000)
    cantidad = cantidad % 1000
    if de1000 >= bill1000: # Si hay suficientes billetes de 1000
      cantidad = cantidad + (de1000 - bill1000) * 1000
      de1000 = bill1000
 
    de500 = int(cantidad / 500)
    cantidad = cantidad % 500
    if de500 >= bill500: # y hay suficientes billetes de 500
      cantidad = cantidad + (de500 - bill500) * 500
      de500 = bill500
 
    de100 = int(cantidad / 100)
    cantidad = cantidad % 100
    if de100 >= bill100: # y hay suficientes billetes de 100
      cantidad = cantidad + (de100 - bill100) * 100
      de100 = bill100
 
    # Si todo ha ido bien, la cantidad que resta por entregar es nula:
    if cantidad == 0:
      # Así que hacemos efectiva la extracción
      bill1000 = bill1000 - de1000
      bill500 = bill500 - de500
      bill100 = bill100 - de100
      return [de1000, de500, de100]
    else: # Y si no, devolvemos la lista con tres ceros:
      return [0, 0, 0]
  else:
    return [-1, -1, -1]




print("Seleccione el banco : ")
print("1- Banco ABC.")
print("2- Banco Ernesto.")
n = int(input())
if n == 1:
  print("Banco ABC")
  o = int(input("Cuanto desea retirar?" ))
  if o < 10000:
    r = billetes(o)
    if r == [0,0,0]:
      print("no se puede distingir los billetes para su importe")
    elif r ==[-1,-1,-1]:
      print ("No hay suficientes billetes")
    else:
      print("billetes de 1000", r[0])
      print("billetes de 500", r[1])
      print("billetes de 100", r[2])
  else:
    print("El monto solicitado excede el limite (10,000)")
if n == 2: 
  print("Banco Ernesto") 
  o = int(input("Cuanto desea retirar?" ))
  if o < 2000:
    r = billetes(o)
    if r == [0,0,0]:
      print("no se puede distingir los billetes para su importe")
    elif r ==[-1,-1,-1]:
      print ("No hay suficientes billetes")
    else:
      print("billetes de 1000", r[0])
      print("billetes de 500", r[1])
      print("billetes de 100",r[2])
  else: 
    print("El monto solicitado excede el limite (2,000)")







    

