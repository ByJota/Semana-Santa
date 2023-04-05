#librerias importadas
from funciones import *

def validarPositivo(pnum):
    if pnum<=0:
        print('El numero ingresado debe ser mayor a 0')
        return menu()
    else:
        return

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
    print('')

    opcion = int (input ("Escoja una opción: "))
    if opcion >=0 and opcion <=9: 
        if opcion == 1:
            print("\n-----------------------------\n")
            print ("Analizar Texto")
            print("Ingrese un texto:")
            texto=input()
            AnalizarCadena(texto)
        elif opcion == 2 :
            print("\n-----------------------------\n")
            print ("El Gordito Navideño")
            print('')
        elif opcion == 3:
            print("\n-----------------------------\n")
            print ("Indicando la paridad")
            print("Ingrese un numero mayor a cero:")
            num=int(input())
            validarPositivo(num)
            indicarParidad(num)
        elif opcion == 4:
            print("\n-----------------------------\n")
            print("Convirtiendo en listas")
            print('')
        elif opcion == 5:
            print("\n-----------------------------\n")
            print ("Notas imaginarias")
            notasImaginarias()
        elif opcion == 6: 
            print("\n-----------------------------\n")  
            print ("Lista de palíndromos.")
            print('')
        elif opcion == 7: 
            print("\n-----------------------------\n") 
            print ("Clasificando edades.") 
            print('')
        elif opcion == 8:
            print("\n-----------------------------\n")
            print ("Las edades de mis conocidos.")
            veces=int(input("Digite la cantidad de edades que desea ingresar:"))
            validarPositivo(veces)
            lasEdadesDeMisConocidos(veces)
        elif opcion == 9:
            print ("Producto Cartesiano")
            print("\n-----------------------------\n")
            print('')
        else:
            return
    else:
        print ("Opción inválida, indique una opción según las opciones indicadas.")
    menu()

menu()