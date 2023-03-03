def separar_cadena(cadena, separador):
    partes = cadena.split(separador)
    tabla = []
    for i in range(len(partes)):
        tabla.append((i+1, partes[i].strip()))
    return tabla
