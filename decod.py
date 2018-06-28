#Funciones
def codificar(f):
    letras = {'s':'a','u':'b','i':'c','l':'i'}
    frasec = ''
    for l in f:
        if l == ' ':
            frasec += ' '
        else:
            for letra in letras:
                if l == letra:
                    frasec += letras[letra]
    print("LA FRASE CODIFICADA ES:",frasec,"\n")
        
def decodificar(f):
    letras = {'s':'a','u':'b','i':'c','l':'i'}
    frasec = ''
    for l in f:
        if l == ' ':
            frasec += ' '
        else:
            for letra in letras:
                if l == letra:
                    frasec += letras[letra]
    print("LA FRASE CODIFICADA ES:",frasec,"\n")

#MENU
     
print("**********************************")
print("*        DECODIFICADOR           *")
print("**********************************\n")

opc = 1
while opc != 0:
    print("1.- CODIFICAR")
    print("2.- DECODIFICAR")
    print("0.- SALIR")
    opc = input("INGRESA LA OPCION QUE QUIERES REALIZAR: ")
    if opc == '1':
        fr = input("\n Ingresa una frase: ")
        codificar(fr)
    elif opc =='2':
        fr = input("\n Ingresa una frase: ")
        decodificar(fr)
    elif opc == '0':
        exit()
    else:
        print("\n")
        print("Ingresa una opción valida")