'''6- Hacer una función que reciba una cedula como argumento y diga si la
cedula es válida o no.''' #11 digitos
cedula = ""
def validar(cedula):
    cedula = input("introduzca su cedula: ")
    if(len(cedula)==11):
        print("tu cedula  es valida")
    else:
        print("no es valida")


validar(cedula)