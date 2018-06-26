'''Proyecto DECODIFICADOR
        CABEZERA'''

print("**********************************")
print("*        DECODIFICADOR           *")
print("**********************************\n")

opc = 1
while opc != 0:
    print("1.- CODIFICAR")
    print("2.- DECODIFICAR")
    print("0.- SALIR")
    opc = int(input("INGRESA LA OPCION QUE QUIERES REALIZAR: "))
    if opc == 1:
        print("\n")
        print("codificando")
    elif opc ==2:
        print("\n")
        print("decodificando")
    elif opc == 0:
        #exit()
        print("\n")
        print("Saliendo")
    else:
        print("\n")
        print("Ingresa un numero valido")