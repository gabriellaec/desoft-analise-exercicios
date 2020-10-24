def separa_trios (lista):
    grupos = []
    i = 0
    while i<len(lista):
        grupos.append(lista[i:i+3])
        i+=3
        return grupos
    