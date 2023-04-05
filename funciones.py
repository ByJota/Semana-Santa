#Librerias importadas
import re
import random

#Funciones
#Reto 1
def AnalizarCadena(texto):
    """ Funcionalidad: Analiza una cadena en str 
    y te retorna la cantidad de vocales, consonantes,
    simbolos, numeros y de espacios."""
    if texto=="":
        print("Debe ingresar una cadena valida")
        return""
    vocales=0
    consonantes=0
    espacios=0
    numeros=0
    simbolos=0

    for i in texto:
        caracter=i.lower()
        if re.match('\s',caracter):
            espacios+=1
        if caracter.isalpha():
            if caracter in 'aeiou':
                vocales+=1 
            else:
                consonantes+=1
        if caracter.isdigit():
            numeros+=1
        if re.match("[-+_*''""%$#@.,;:¿?¡!]",caracter):#Esta expresion regula lo que hace es analizar si el caracter es un simbolo
            simbolos+=1
    #Si encuentras la forma de meter esto en una lista, especificando cada una de las cosas
    print('-----------------------------')
    print("Texto Original: "+ texto +"\n"+"-----------------------------")
    print(f"Vocales: "+str(vocales)+"\n" +
          "Consonantes: "+str(consonantes)+"\n" +
          "Espacios: "+str(espacios)+"\n" +
          "Numeros: "+str(numeros)+"\n" +
          "Simbolos: "+str(simbolos))
    print('-----------------------------')

    return

#reto 2 Gordo Navideño
def obtenerLista(pnum):
    """
    Funcion: Obtiene una lista de numeros random
    Entradas:
    - pnum(int): cantidad de numeros que quiere el usuario
    Salidas:
    - listaPares(list): lista de numeros pares
    """
    listaPares=[]
    while len(listaPares) < pnum:
        numRandom = random.randint(0,99)
        if EsPar(numRandom) == False:
            pass
        else:
            listaPares.append(numRandom)
    return listaPares

#Reto 3
def EsPar(num):

    if num%2==0:
        return True
    else:
        return False
    
def indicarParidad(pveces):
    i=1
    lista=[]
    listaPares=[]
    while i<=pveces:
        numero=random.randint(0,99)
        lista.append(numero)
        if EsPar(numero):
            listaPares.append(0)
        else:
            listaPares.append(1)
        i+=1
    
    print(f"Lista de numeros Random\n"+
          str(lista))
    print('')
    print(f"Lista si es par o no es par\n"+
          "0 es par\n"+
          '1 es impar\n'
          +str(listaPares))
    return
#reto 4 Conviertiendo listas
def clasificarGen (lista):
    """
    Funcion: Clasificar los carnet segun su año
    Entradas:
    - lista(list): lista de carnets
    Salidas:
    - Cuenta de carnets segun la generacion a la que pertenecen
    """
    i = 0
    c2018= 0
    c2019= 0
    c2020= 0
    c2021= 0
    c2022= 0
    c2023= 0
    listaStr= []
    for x in lista:
        listaStr.append(str(x))
    while i in range (len(listaStr)):
        carnet = listaStr[i]
        anno = int(carnet[:4])
        if anno == 2018:
            c2018 +=1
        elif anno == 2019:
            c2019 +=1
        elif anno == 2020:
            c2020 +=1
        elif anno == 2021:
            c2021 +=1
        elif anno == 2022:
            c2022 +=1
        else:
             c2023 +=1
        i+=1
    print('-----------------------------------------')
    print("Las generaciones de la clase son:")
    print("Del 2018:",c2018,
          "\nDel 2019:",c2019,
          "\nDel 2020:",c2020,
          "\nDel 2021:",c2021,
          "\nDel 2022:",c2022,
          "\nDel 2023:",c2023)
