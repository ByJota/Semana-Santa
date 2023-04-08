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
#Reto 5
def notasImaginarias():
    i=1
    aprobados=0
    reposicion=0
    reprobados=0
    total=0
    notas=[]
    while i<=10:
        nota=random.randint(1,100)
        if nota>=70:
            aprobados+=1
        elif nota>=60:
            reposicion+=1
        else:
            reprobados+=1
        total+=nota
        i+=1
        notas.append(nota)
    print(f'-------------------------------------\n'+'Lista de notas:',notas)
    print('-------------------------------------')
    print(f'Aprovados:',aprobados)
    print(f'Reposicion:',reposicion)
    print(f'Reprobados:',reprobados)
    print(f'Promedio:',(total/10))
    return

#reto6 Lista palindromos
def espalindromo(ppalabra):
    """
    Funcion: Determinar si una palabra es palindroma
    Entradas:
    - ppalabra(str): palabra
    Salidas:
    - True
    - False
    """
    i =- 1
    i2 = 0
    contador = 0
    while i2 < len(ppalabra):
        inicio= ppalabra[i2]
        fin = ppalabra[i]
        i-= 1
        i2+= 1
        if inicio == fin:
            contador += 1
    return contador == len(ppalabra)

def encontrarPalindromo(lista):
    """
    Funcion: Añadir palabras palindromas a una lista
    Entradas:
    - lista(list): lista de palabras
    Salidas:
    - listaPalin(list): lista con palabras únicamente palindromas
    """
    listaPalin = []
    for i in range (len(lista)):
        if espalindromo(lista[i]):
            listaPalin.append(lista[i])
    return listaPalin

#reto7 clasificar edades
def obtenerEdades (pnum):
    """
    Funcion: Obtener pnum cantidad de edades aleatorias
    Entradas:
    - pnum(int): número de edades
    Salidas:
    - listaEdades(list): lista con las edades 
    """
    listaEdades=[]
    while len(listaEdades) < pnum:
        numRandom = random.randint(1,99)
        listaEdades.append(numRandom)
    return clasificarEdades(listaEdades)

def clasificarEdades(listaEdades):
    """
    Funcion: Clasificar la edad
    Entradas:
    - listaEdades(list): lista con las edades
    Salidas:
    - contador con la cantidad de edades dependiendo de la etapa de la vida en la que este 
    """
    list
    bebe = 0
    ninno= 0
    adolescente= 0
    adultoJoven= 0
    adultoMayor= 0
    for i in range (len(listaEdades)):
        edad = listaEdades[i]
        if edad <= 3:
            bebe+=1
        elif edad <= 12:
            ninno+=1
        elif edad <= 21:
            adolescente+=1
        elif edad <=60:
            adultoJoven+=1
        else:
            adultoMayor+=1
    print('Edades generadas:', listaEdades,
          "\nBebé:",bebe,
          "\nNiño:",ninno,
          "\nAdolescente:",adolescente,
          "\nAdulto joven:",adultoJoven,
          "\nAdulto mayor:",adultoMayor)
    return ''

#Reto 8
def annoBisiesto(edad,anno):
    if (anno-edad)%4==0:
        return True
    else:
        return False

def lasEdadesDeMisConocidos(pveces): 
    anno=datetime.now().year
    i=1
    mayor=0
    menor=150
    lista=[]

    while i<=pveces:
        edad=int(input(f"Indique la edad "+str(i)+":"))
        lista.append(edad)
        if edad>mayor:
            mayor=edad
        if edad<menor:
            menor=edad  
        i+=1
    diferencia=(anno-menor)-(anno-mayor)
    lista.remove(mayor)
    lista.remove(menor)
    i=1
    print('------------------------------------------------------------')
    if annoBisiesto(mayor,anno):
        print(F"\nEl mayor nacio en el año "+str(anno-mayor)+'. Esta persona nacio en un año bisiesto')
    else:
        print(F"\nEl mayor nacio en el año "+str(anno-mayor)+'.')
    if annoBisiesto(menor,anno):
        print(F"\nEl menor nacio en el año "+str(anno-menor)+'. Esta persona nacio en un año bisiesto')
    else:
        print(F"\nEl menor nacio en el año "+str(anno-menor)+'.')
    
    print(F"Hay",diferencia,"entre el mayor y el menor. En ese rango se encuentran las edades:")
    
    for n in lista:
        print("Edad "+str(i)+":",n)
    return 

#reto 9 Producto Cartesiano
"""
    Funcion: Crear un producto cartesiano
    Entradas:
    - lista(list): lista con una lista A y una lista B
    Salidas:
    - productoCartesiano(list): arreglo de listas con todos los productos
    """
def obtenerProductoCartesiano(lista):
    i = 0
    x = 1
    contador = 0
    productoCartesiano = []
    while i < len(lista[0]): 
        indiceA = lista[0]
        elementoA= indiceA[i]
        while contador in range (len(lista[x])):
            indiceB= lista[x]
            elementoB= indiceB[contador]
            productoCartesiano.append([elementoA,elementoB])
            contador+=1 
        i += 1
        contador = 0
    return productoCartesiano