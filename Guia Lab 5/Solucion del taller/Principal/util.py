def validarnombre(nombre):
    '''
    Valida nombre válido (solo letras y espacios)
    Argumentos:
        nombre: String a validar
    return -> Boolean (True or False) si es valido o no
    '''
    if len(nombre) == 0:
        return False
    letras = 'abcdefghijklmnñopqrstuvwxyzáéíóúüABCDEFGHIJKLMNÑOPQRSTUVWXYZÁÉÍÓÚÜ '
    for letra in nombre:
        if not letra in letras or letra in ' ':
            return False
    return True
pass
        
def validar_documento(documento):
    '''
    Valida un número de documento. Debe contener 10 caracteres, todos numéricos.
    
    Argumentos:
        documento: string a validar
    return -> Boolean (True or False) si es valido o no
    '''
    if len(documento) !=10:
        return False
    caracteres = '0123456789'
    for caracter in documento:
        if not caracter in caracteres:
            return False
        return True
    pass

def validar_fecha(fecha):
    '''
    Valida que un string corresponda a una fecha válida (con formato yyyy-mm-dd).
    
    Argumentos:
        fecha -> string a validar
    return -> Boolean (True or False) si es valido o no
    '''
    if len(fecha) != 10:
        return False
    if fecha[4] != '-' or fecha[7] != '-':
        return False
    anio = fecha[0:4]
    mes = fecha[5:7]
    dia = fecha[8:10]
    caracteres = '0123456789'
    for caracter in anio:
        if not caracter in caracteres:
            return False
    for caracter in mes:
        if not caracter in caracteres:
            return False
    for caracter in dia:
        if not caracter in caracteres:
         return False 
    anio = int(anio)
    mes = int(mes)
    dia = int(dia)
    if mes < 1 or mes > 12:
        return False
    dia_por_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    es_bisiesto = False
    if anio % 4 == 0 and anio % 100 != 0:
        es_bisiesto = True
    if anio % 400 == 0:
        es_bisiesto = True
    if es_bisiesto:
        dia_por_mes[1]= 29
    if dia < 1 or dia > dia_por_mes[mes-1]:

        return False
    return True

pass

def dividir_fila(ancho,sep='-'):
        '''
        ancho: Lista con el tamaño de cada columna
        se: Caracter con el que se van a formar las líneas que 
            separan las filas
        '''
        linea = ''
        for i in range(len(ancho)):
            linea += ('+'+sep*(ancho[i]-1))
        linea = linea[:-1]+'+'
        print(linea)

def imprimir_celda(texto, impresos, relleno):
        '''
        texto: Texto que se va a colocar en la celda
        impresos: cantidad de caracteres ya impresos del texto
        relleno: cantidad de caracteres que se agregan automáticamente,
            para separar los textos del borde de las celda.
        '''        
        # Imprimir celda
        if type(texto) == type(0.0):
            #print(texto)
            texto = '{:^7.2f}'.format(texto)
            #print(type(texto), texto)
        else:
            texto = str(texto)
        texto = texto.replace('\n',' ').replace('\t',' ')
        if impresos+relleno < len(texto):
            print(texto[impresos:impresos+relleno],end='')
            impresos+=relleno
        elif impresos >= len(texto):
            print(' '*(relleno),end='')
        else:
            print(texto[impresos:], end='')
            print(' '*(relleno-(len(texto) - impresos)),end='')
            impresos = len(texto)
        return impresos
    
def limpiar_pantalla():
    '''
    Imprime varias líneas en blanco, para dar la ilusión 
    de limpiar la pantalla
    '''
    print('\n'*20)
    
def imprimir_tabla(tabla, ancho, encabezado=None):  
    ''' 
    Imprime en pantalla un tabla con los datos pasados, ajustado a los tamaños deseados.
    
    Argumentos:
        tabla: Lista que representa la tabla. Cada elemento es una fila
        ancho: Lista con el tamaño deseado para cada columna. Si se especifica
            un entero, todas las columnas quedan de ese tamaño
        encabezado: Lista con el encabezado de la tabla
    '''
    if type(ancho) == type(0):
        ancho = [ancho]*len(tabla[0])
    if encabezado != None:
        if type(ancho) == type(0):
            ancho = [ancho]*len(encabezado)
        assert len(ancho) == len(encabezado), 'La cantidad de columnas no coincide con los tamaños dados'
        

