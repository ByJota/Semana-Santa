#librerias importadas
from funciones import *

def validarPositivo(pnum):
    if pnum<=0:
        print('El numero ingresado debe ser mayor a 0')
        return menu()
    else:
        indicarParidad(pnum)

def menu():

    """
    Funcionamiento: De manera repetitiva, muestra el menú al usuario. 
    Entradas: NA
    Salidas: Resultado según lo solicitado
    """

    print ("\n-----------------------------\n")
    print ("Menu de Funciones")
    print ("\n-----------------------------\n")
    print ("1. Analizar Texto")
    print ("2. El Gordito Navideño")
    print ("3. Indicando la paridad")
    print ("4. Convirtiendo en listas")
    print ("5. Notas imaginarias")
    print ("6. Lista de palíndromos.")
    print ("7. Clasificando edades.")
    print ("8. Las edades de mis conocidos.")
    print ("9. Producto Cartesiano")
    print ("0. Salir del menu")

    opcion = int (input ("Escoja una opción: "))
    if opcion >=0 and opcion <=9: 
        if opcion == 1:
            print("Ingrese un texto:")
            texto=input()
            AnalizarCadena(texto)
        elif opcion == 2 :
            print("Ingrese un numero mayor a cero:")
            num=int(input())
            validarPositivo(num)
        elif opcion == 3:
            print('')
        elif opcion == 4:
            print('')
        elif opcion == 5:
            print('')
        elif opcion == 6:   
            print('')
        elif opcion == 7:   
            print('')
        elif opcion == 8:
            print('')
        elif opcion == 9:
            print('')
        else:
            return
    else:
        print ("Opción inválida, indique una opción según las opciones indicadas.")
    menu()

menu()