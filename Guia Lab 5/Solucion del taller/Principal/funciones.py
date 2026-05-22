def cargar_usuarios():
    usuarios = []

    archivo = open('usuarios.csv', 'r')
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