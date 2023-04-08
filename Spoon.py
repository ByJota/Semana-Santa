#Programa Principal
"""
while True:
    try:
        out=1
        print("Programa de gerencia de Spoon.\n"+
            "---------------------------------------")
        while out==1:
            print("Ingrese un codigo de la lista otorgada por el administrados.\n")
            code=input('Codigo:')
            print("---------------------------------------")
            print(codigoSpoonAUX(code))
            print("---------------------------------------")
            print("¿Quieres ingresar otro codigo?\n"+
                  "1.Si\n"+
                  "0.No\n")
            out=int(input("R/"))
            print("---------------------------------------")
        break
    except:
        print('Error inesperado.')
"""
#librerias importadas
import re
#definicion de funciones
def codigoSpoonAUX(pcode):
    """
    Función: Validar el código
    Entradas:
    - pcode(str): Código del item
    Salidas:
    - Dirige el código a  la función correspondiente que lo decodifica
    """
    if not (len(pcode)>=4 and len(pcode)<=7):
        return"Ingrese un codigo de 4 a 7 letras"
    else:
        pcode = pcode.upper()
        if re.match('^RE',pcode):
            return determinarTipoRE(pcode)
        #determina si es una reposteria
        elif re.match('^QE',pcode):
            if re.match('[A-Z]',pcode):
                return determinarTipoQE(pcode)
            else:
                return "Los códigos de queques no llevan caracteres númericos."
        elif re.match('^TCAGR',pcode):
            result= "Usted solicita una torta chilena de tamaño Grande."
            return result
        else:
            return"El código ingresado no pertenece al de un producto.Ingrese un código valido."
            
def determinarTipoRE(pcode):
    """
    Función: Determina el sabor,tipo y tamaño de una repostería
    Entradas:
    - pcode(str): Código del item
    Salidas:
    - result(str): Cadena del item decodificada
    """
    result='Usted solicita una repostería de sabor  ' 
    if re.match('RE[DS]',pcode):
        if re.match('RED[13457]',pcode) and len(pcode)==4:
            result+='Dulce '
            type=pcode[3]
            if type=='1':
                result+='correspondiente a un: Nidito.'
            elif type=='3':
                result+='correspondiente a un: Orejita'
            elif type=='4':
                result+='correspondiente a un: Biscuit'
            elif type=='5':
                result+='correspondiente a un: Crocante'
            elif type=='7':
                result+='correspondiente a una: Empanada'
            else:
                result='El código ingresado no corresponde a una repostería valida'
        else:
            result+='Salada '
            type=pcode[3]
            if type=='1':
                result+='correspondiente a un: Nidito '
            elif type=='2':
                result+='correspondiente a un: Palito de queso.'
            elif type=='4':
                result+='correspondiente a un: Biscuit.'
            elif type=='6':
                result+='correspondiente a una: Enchilada '
            elif type=='7':
                result+='correspondiente a una: Empanada '
            else:
                result='El código ingresado no corresponde a una repostería valida'
            #determina el sabor
            if re.match('RES[167][12]',pcode):
                type=pcode[4]
                if type=='1':
                    result+='de pollo, '
                elif type=='2':
                    result+='de carne, '
                else:
                    result='El código ingresado no corresponde a un Sabor valido.'
            #determina el tamaño
            if re.match('RES[167][12]PQ',pcode):
                result+='de tamaño Pequeño.'
            elif re.match('RES[167][12]MD',pcode):
                result+='de tamaño Mediano.'
            elif re.match('RES[167][12]GD',pcode):
                result+='de tamaño Grande.'
            else:
                result='El código ingresado no concuerda con ningún item'
    return result

def determinarTipoQE (pcode):
    """
    Función: Determina el sabor y tamaño de un queque
    Entradas:
    - pcode(str): Código del item
    Salidas:
    - result(str): Cadena del item decodificada
    """
    result="Usted solicita un queque sabor de "
    if re.match("QE[A-Z]{2}FR",pcode):
        result+= "Fresa"
    elif re.match("QE[A-Z]{2}VN",pcode):
        result+= "Vainilla"
    elif re.match("QE[A-Z]{2}CM",pcode):
        result+= "Caramelo"
    elif re.match("QE[A-Z]{2}CE",pcode):
        result+= "Chocolate"
    else:
       result="El código de item no corresponde a sabor de queque"
    #determina el tamaño
    if re.match('QE[GR]',pcode):
        result+=', de tamaño Grande.'
    elif re.match('QE[PQ]',pcode):
        result+=', de tamaño Pequeño.'
    else:
        result="El código de item no corresponde a un tamaño de queque"   
    return result

#Programa Principal
while True:
    try:
        out=1
        print("Programa de gerencia de Spoon.\n"+
            "---------------------------------------")
        while out==1:
            print("Ingrese un codigo de la lista otorgada por el administrados.\n")
            code=input('Codigo:')
            print("---------------------------------------")
            print(codigoSpoonAUX(code))
            print("---------------------------------------")
            print("¿Quieres ingresar otro codigo?\n"+
                  "1.Si\n"+
                  "0.No\n")
            out=int(input("R/"))
            print("---------------------------------------")
        break
    except:
        print('Error inesperado.')
