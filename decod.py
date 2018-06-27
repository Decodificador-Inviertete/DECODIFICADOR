#Funciones
def codificar(f):
    letras = {'s':'a','u':'b','i':'c','l':'i'}
    frasec = ''
    l = len(f)
    for j in range(0,l):
        for letra in letras:
            if f[j] == letra:
                frasec += letras[letra]
    print("LA FRASE CODIFICADA ES: ",frasec,"\n")
        
'''def codificar(f):
    letras = {'s':'a','u':'b','i':'c','l':'i'}
    frasec = ''
    l = len(f)
    for j in range(0,l):
        for letra in letras:
            if f[j] == letra:
                frasec += letras[letra]
    print("LA FRASE CODIFICADA ES: ",frasec,"\n")
    '''
#MENU
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
        f = input("\n Ingresa una frase: ")
        codificar(f)
    elif opc ==2:
        f = input("\n Ingresa una frase: ")
        print("DECODIFICADO")
        decodificar(f)
    elif opc == 0:
        exit()
    else:
        print("\n")
        print("Ingresa una opción valida")