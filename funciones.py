#Librerias importadas
import re
import random
from datetime import datetime

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