#Librerias
import re

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

AnalizarCadena('') 
AnalizarCadena('Murcielago!') 
AnalizarCadena('Hola, buenos dias a todos') 
AnalizarCadena('La prueba tiene una duracion de 110 minutos') 
AnalizarCadena('Luis: Como te fue?') 
AnalizarCadena('12345 .,;!?: abcde') 