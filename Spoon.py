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
    if not (len(pcode)>=4 and len(pcode)<=7):
        return"Ingrese un codigo de 4 a 7 letras"
    else:
        if re.match('RE\w',pcode):
            return codigoSpoon(pcode)
        elif re.match('QE\w',pcode):
            for i in pcode:
                if i.isdigit():
                    return"Los codigos de los queque no llevan numeros."
            return codigoSpoon(pcode)
        elif re.match('TCAGR',pcode):
            return codigoSpoon(pcode)
        else:
            return"Codigo ingresado invalido"
            
def codigoSpoon(code):
    result='Ha solicitado '
    
    if re.match('RE[DS]',code):
        if re.match('RED[13457]',code) and len(code)==4:
            result+='una reposteria dulce. '
            type=code[3]
            if type=='1':
                result+='Correspode a un: Nidito.'
            elif type=='3':
                result+='Correspode a un: Orejita'
            elif type=='4':
                result+='Correspode a un: Biscuit'
            elif type=='5':
                result+='Correspode a un: Crocante'
            elif type=='7':
                result+='Correspode a una: Empanada'
            else:
                result='Error en el codigo ingresado'
        else:
            result+='una reposteria Salada. '
            type=code[3]
            if type=='1':
                result+='Correspode a un: Nidito '
            elif type=='2':
                result+='Correspode a un: Palito de queso.'
            elif type=='4':
                result+='Correspode a un: Biscuit.'
            elif type=='6':
                result+='Correspode a una: Enchilada '
            elif type=='7':
                result+='Correspode a una: Empanada '
            else:
                result='Error en el codigo ingresado'
        
            if re.match('RES[167][12]',code):
                type=code[4]
                if type=='1':
                    result+='de pollo. '
                elif type=='2':
                    result+='de carne. '
                else:
                    result='Error en el codigo ingresado.'
            
            if re.match('RES[167][12]PQ',code):
                result+='Tamaño pequeño.'
            elif re.match('RES[167][12]MD',code):
                result+='Tamaño mediano.'
            elif re.match('RES[167][12]GD',code):
                result+='Tamaño grande.'
            else:
                result='Error en el codigo ingresado.'
    
    if re.match('TCAGR',code):
        result+='una torta chilena, tamaño grande.'
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
