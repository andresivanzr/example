
def programa(opcion):
    if opcion == '1':
        print(cadena[0:2])
    elif opcion == '2':
       print(cadena[0:3])
    elif opcion == '3':
       print(cadena[-2:])
    elif opcion == '4':
       print(cadena[-1:])
    else:
        print('error')




if __name__ == "__main__":
    cadena = input('Ingrese un texto: ')
    print('Elija una opcion')
    print('1 Mostrar sus dos primeras letras.')
    print('2 Mostrar sus tres primeras letras.')
    print('3 Mostrar sus dos últimas letras.')
    print('4 Mostrar su última letra.')
    opcion = input('Opción: ')
    programa(opcion)