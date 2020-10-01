import sqlite3
conn = sqlite3.connect("agendatelefonica.db")
cursor = conn.cursor()


def creartabla():
  cursor.execute("CREATE TABLE contactos (ID integer primary key autoincrement, nombre varchar(15), apellido varchar (25), numero text )")
  conn.commit()

def insertar ():
  cursor = conn.cursor()
  cursor.execute( "INSERT INTO contactos (nombre,apellido,numero) VALUES (?,?,?)",(nombre,apellido,numero))
  conn.commit()

def listar():
  query1 = "SELECT * FROM contactos "
  cursor = conn.cursor()
  cursor.execute(query1)
  rows = cursor.fetchall()
  for row in rows:
    print(row)


def listarID():
  cursor = conn.cursor()
  cursor.execute("SELECT * FROM contactos where ID  = (?)",(d))
  rows = cursor.fetchone()
  for row in rows:
    print(row)
    row = cursor.fetchone()

def eliminar ():
  cursor = conn.cursor()
  cursor.execute("DELETE FROM contactos where ID = ?",(d))
  conn.commit()

def buscarnombre():
  cursor.execute("SELECT * FROM contactos where nombre like  ? ",('%'+nombre+'%'))
  rows = cursor.fetchone()
  for row in rows:
    print(row)
    row = cursor.fetchone()

def buscartelefono():
  cursor.execute("SELECT * FROM contactos where numero like  ?",(numero))
  rows = cursor.fetchone()
  for row in rows:
    print(row)
    row = cursor.fetchone()

def modificarnombre():
  cursor = conn.cursor()
  cursor.execute( "UPDATE contactos SET  nombre = ? where ID = ? ",(n,d))
  conn.commit()

def modificarapellido():
  cursor = conn.cursor()
  cursor.execute( "UPDATE contactos SET  apellido = ? where ID = ? ",(ap,d))
  conn.commit()

def modificarnumero():
  cursor = conn.cursor()
  cursor.execute( "UPDATE contactos SET  numero = ? where ID = ? ",(num,d))
  conn.commit()

def menu():
  print("Agenda Telefonica :3")
  print("Seleccione una opcion :3")
  print("1- Agregar un nuevo contacto")
  print("2- Ver todos los contactos ")
  print("3- Seleccionar contactos")
  print("4- Eliminar un contactos")
  print("5- Modificar contactos")
  print("6- buscar contactos")
  print("7- Salir")

while True:
  menu()
  c = int(input("Digite su opcion: "))
  if c == 1:
    nombre = input("nombre : ")
    apellido = input("Nombre del Apellido : ")
    numero = input("Numero del contacto: ")
    insertar()
    t = input("volver al menu: ")
  if c == 2:
    listar()
    t = input("volver al menu: ")
  if c == 3:
    d = input("Digite ID que desea ver: ")
    listarID()
    t = input("volver al menu: ")
  if c == 4:
    d = input("Digite ID o campo a eliminar: ")
    eliminar()
    t = input("volver al menu: ")
  if c == 5:
    print("1- Modificar nombre")
    print("2- Modificar apellido")
    print("2- Modificar numero")
    m = int(input("Digite una opcion:"))
    if m == 1:
      listar()
      n = input("Nombre a modificar: ")
      d = int(input("ID del campo a modificar: "))
      modificarnombre()
      t = input("volver al menu: ")
    if m ==2 :
      listar()
      ap = input("apellido a modificar: ")
      d = input("ID del campo a modificar: ")
      modificarapellido()
      t = input("volver al menu: ")
    if m == 3:
      listar()
      num = input("numero a modificar: ")
      d = int("ID del campo a modificar: ")
      modificarnumero()
      t = input("volver al menu: ")
  if c == 6:
    print("1- Buscar nombre")
    print("2- Buscar numero")
    b = int(input("Digite una opcion: "))
    if b == 1:
      nombre = input("buscar nombre: ")
      buscarnombre()
      t = input("volver al menu: ")
    if b ==2:
      numero = int(input("buscar numero: "))
      buscartelefono()
      t = input("volver al menu: ")
  if c == 7 :
    break




conn.close()