#librerias importadas
from funciones import *

def validarPositivo(pnum):
    if pnum<=0:
        print('El numero ingresado debe ser mayor a 0')
        return menu()
    else:
        return
        
def obtenerGordoAUX (pnum):
    if pnum <= 0:
        print('El numero ingresado debe ser mayor a 0')
        return menu()
    else:
        obtenerGordo(pnum)
        
def obtenerGordo(pnum):
    print('El gordo navideño se viene par!:',obtenerLista(pnum))
    return ''

def convertirListaAUX (carnets):
    lista = carnets.split(', ')
    i = 0
    while i in range (len(lista)):
        if re.match("^\d{10}$",lista[i]):
            print("Canet valido")
        else:
            print("Carnet Invalido. Porfavor digite un carnet de 10 digitos numericos")
        i+=1
    return clasificarGen(lista)

def ESproductoCartesiano():
    print("El producto cartesiano de:",
        "\n[1,2],['x','y','z']", "es:")
    print(obtenerProductoCartesiano([[1,2],['x','y','z']]))
    print("-------------------------------------")
    print("El producto cartesiano de:",
        "\n[1,2,3,4],['a','b']", "es:")
    print(obtenerProductoCartesiano([[1,2,3,4],['a','b']]))
    return ''

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
            print("Ingrese un numero:")
            num = int(input())
            obtenerGordoAUX(num)
        elif opcion == 3:
            num=int(input('Ingrese la cantidad de numeros aleatorios que quieres analizar:'))
            validarPositivo(num)
            indicarParidad(num)
        elif opcion == 4:
            print('Ingrese el numero de carnets, separados por "," :')
            carnets = "2018012345, 2021019876, 2021021234, 2019012345, 2018025678, 2022012345"
            convertirListaAUX (carnets)
        elif opcion == 5:
            num=int(input("Indique la cantidad de numeros aleatorios que quieres analizar:"))
            validarPositivo(num)
            notasImaginarias(num)
        elif opcion == 6:   
            print('Ingrese una lista de palabras:')
            print('Entrada:',['ana','comida','somos','hola'])
            print('Salida:',encontrarPalindromo(['ana','comida','somos','hola']))
            print('')
            print('Entrada:',['ana','comida','somos','hola','radar','oro','mundo'])
            print('Salida:',encontrarPalindromo(['ana','comida','somos','hola','radar','oro','mundo']))
        elif opcion == 7:
            num = int(input('Digite la cantidad de edades que desea clasificar:'))
            print('---------------------------')   
            print(obtenerEdades(num))
        elif opcion == 8:
            num=int(input("Indique la edades que quieres ingresar:"))
            validarPositivo(num)
            lasEdadesDeMisConocidos(num)
        elif opcion == 9:
            print(ESproductoCartesiano())
        else:
            return
    else:
        print ("Opción inválida, indique una opción según las opciones indicadas.")
    menu()

menu()