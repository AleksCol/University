import json
from util import *

def cargar_usuarios():
    usuarios = []

    archivo = open('usuarios.csv', 'r',encoding='utf-8')
    lineas = archivo.readlines()
    archivo.close()

    for i in range(1, len(lineas)):
        linea = lineas[i].strip()

        if linea == "":
            continue

        partes = linea.split(',')

        usuario = {
            'codigo': partes[0],
            'nombre': partes[1],
            'clave': partes[2],
            'rol': partes[3]
        }

        usuarios.append(usuario)

    return usuarios

def cargar_estaciones():
    estaciones = []
    archivo = open('estaciones.csv', 'r', encoding='utf-8')
    lineas = archivo.readlines()
    archivo.close()

    for i in range(1, len(lineas)):
        linea = lineas[i].strip()

        if linea == "":
            continue

        partes = linea.split(',')

        estacion = {
            'codigo': partes[0],
            'nombre': partes[1],
        }

        estaciones.append(estacion)

    return estaciones

def cargar_variables():
    archivo = open('variables.json', 'r', encoding='utf-8')
    datos = json.load(archivo)
    archivo.close()
    return datos['variables']


def cargar_registros():
    archivo = open('registros.json', 'r', encoding='utf-8')
    datos = json.load(archivo)
    archivo.close()
    return datos['registros']

def guardar_usuarios(usuarios):
    archivo = open('usuarios.csv', 'w', encoding ='utf-8')
    archivo.write('codigo,nombre,clave,rol\n')
    for usuario in usuarios:
        linea = usuario['codigo'] + ',' + usuario['nombre'] + ',' + usuario['clave'] + ',' + usuario['rol'] + '\n'
        archivo.write(linea)
    archivo.close()
    
def guardar_estaciones(estaciones):
    archivo = open('estaciones.csv', 'w', encoding='utf-8')
    archivo.write('codigo,nombre\n')
    for e in estaciones:
        linea = e['codigo'] + ',' + e['nombre'] + '\n'
        archivo.write(linea)
    archivo.close()
    
def guardar_registros(registros):
    archivo = open('registros.json', 'w', encoding='utf-8')
    datos = {
        'registros': registros
    }
    json.dump(datos, archivo, indent=4)
    archivo.close()

def buscar_usuario(usuarios, codigo):
    for i in range(len(usuarios)):
        if usuarios[i]['codigo'] == codigo:
            return i
    return -1

def autenticar(usuarios, codigo, clave):
    pos = buscar_usuario(usuarios,codigo)
    if pos == -1:
        return None
    if usuarios [pos]['clave'] == clave:
        return usuarios[pos]
    return None

