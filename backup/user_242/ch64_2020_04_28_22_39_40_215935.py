def acha_bigramas(string):
    lista_bigramas = []
    i=0
    brigrama = string[i] + string[i+1]
    for brigrama in string:
        if bigrama in lista_bigramas:
            continue
        if bigrama not in lista_bigramas:
            lista_bigramas.append(bigrama)
    return lista_bigramas
        