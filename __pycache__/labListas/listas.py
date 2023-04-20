#Elaborado por
# Fecha de creacion
# Ultima modificacion
# version 3.10.6
#importar librerias
import re
#definicion de funciones
def validarCodigo(codigo):
    if re.match('^\d{4}-\d{3}-[i|d]\d{4}$','codigo'):
        print('Codigo Registrado')
        return codigo
    else:
        print('Debe un codigo en formato tipo y area-piso y pasillo-(direccion)fila y columna')
   
#programa principal
